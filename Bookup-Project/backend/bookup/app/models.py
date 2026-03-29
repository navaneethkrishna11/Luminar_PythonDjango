from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('service_provider', 'Service Provider'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    place = models.CharField(max_length=100)
    pincode = models.CharField(max_length=12)

    def __str__(self):
        return self.username


class Slot(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        limit_choices_to={'role': 'service_provider'}
    )
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slots/')
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    PAYMENT_METHODS = (
        ('online', 'Online'),
        ('cod', 'Cash on Delivery'),
    )

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )

    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="bookings")
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'customer'}
    )
    seat_count = models.IntegerField(default=1)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='pending')

    def save(self, *args, **kwargs):
        if self.pk is None:
            # New booking
            if self.slot.available_slots >= self.seat_count:
                self.slot.available_slots -= self.seat_count
                self.slot.save()
            else:
                raise ValueError("Not enough available slots")
        else:
            # Updating existing booking
            old = Booking.objects.get(pk=self.pk)
            difference = self.seat_count - old.seat_count
            self.slot.available_slots -= difference
            self.slot.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Add seats back to slot
        self.slot.available_slots += self.seat_count
        self.slot.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.username} - {self.slot.name}"