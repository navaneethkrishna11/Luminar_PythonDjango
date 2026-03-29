from rest_framework import serializers
from .models import Slot,Booking, User

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slot
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields = ['username', 'password', 'email', 'first_name', 'last_name','role']

    def create(self,validate_data):
        user=User.objects.create_user(**validate_data) #here all the data fields area valdiated
        return user

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"