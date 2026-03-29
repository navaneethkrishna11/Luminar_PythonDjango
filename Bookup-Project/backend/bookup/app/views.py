from rest_framework import viewsets
from app.models import User,Slot,Booking
from app.serializers import UserSerializer,SlotSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SlotView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer



class BookView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SearchView(APIView):
    def get(self,request):
        s=self.request.query_params.get('search')
        if s:
            b=Slot.objects.filter(Q(name__icontains=s)|
                                  Q(author__icontains=s)|
                                  Q(language__icontains=s)|
                                  Q(price__icontains=s))
            if not b.exists():
                return Response({'msg': 'no result found'}, status=status.HTTP_404_NOT_FOUND)
            book=BookSerializer(b,many=True)
            return Response(book.data,status=status.HTTP_200_OK)
        else:
            return Response({'msg':'no result found'},status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Successfully logged out'},status=status.HTTP_200_OK)



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'role': user.role,
            'id': user.id,
            'name':user.username
        })

class MeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)