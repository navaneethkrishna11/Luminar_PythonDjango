from django.shortcuts import render
from rest_framework import mixins,generics,viewsets
from books.models import Book
from books.serializer import BookSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# class Booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class BookDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#        return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

# ---------------------------------------------------------------------------------------------
#  GENERICS BASED VIEW
# ---------------------------------------------------------------------------------------------
# class Booklist(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# ---------------------------------------------------------------------------------------------
#  VIEWSET BASED VIEW
# ---------------------------------------------------------------------------------------------
class BookView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchView(APIView):
    def get(self,request):
        s=self.request.query_params.get('search')
        if s:
            b=Book.objects.filter(Q(name__icontains=s)|
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

