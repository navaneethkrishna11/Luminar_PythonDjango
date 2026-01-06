from django.shortcuts import render
from .models import Recipe,Review
from .serializer import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework import generics,viewsets,status
from django.db.models import Q
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeSearch(APIView):
    def get(self,request):
        s=self.request.query_params.get('search')
        if s:
            r=Recipe.objects.filter(Q(recipe_name__icontains=s)|
                                    Q(mealtype__icontains=s)|
                                    Q(cusine__icontains=s))
            if not r.exists():
                return Response({'msg':'not found'},status=status.HTTP_404_NOT_FOUND)
            serial=RecipeSerializer(r,many=True)
            return Response(serial.data,status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Successfully logged out'},status=status.HTTP_200_OK)

class AddReview(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from django.http import HttpResponse,Http404
class AllReviews(APIView):
    def get(self,request,pk):
        try:
            r=Recipe.objects.get(id=pk)
        except:
            raise Http404

        rev= Review.objects.filter(recipe=r)
        reviews= ReviewSerializer(rev,many=True)

        return Response(reviews.data,status=status.HTTP_200_OK)


