from django.shortcuts import render

from rest_framework.decorators import api_view,APIView
from rest_framework import status
from rest_framework.response import Response
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from django.http import Http404

@api_view(['GET','POST'])
def employeelist(request):
    if (request.method=='GET'):
        e=Employee.objects.all()
        emp=EmployeeSerializer(e,many=True)
        return Response(emp.data, status=status.HTTP_200_OK)

    if(request.method=='POST'):
        e=EmployeeSerializer(data=request.data)
        if e.is_valid():
            e.save()
            return Response(e.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def employeedetail(request, pk):
    try:
        e = Employee.objects.get(pk=pk)
    except:
        return Response({"message": "employee not exist"}, status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        emp=EmployeeSerializer(e)
        return Response(emp.data, status=status.HTTP_200_OK)
    if (request.method=='PUT'):
        emp = EmployeeSerializer(e,data=request.data)
        if emp.is_valid():
            emp.save()
            return Response(emp.data, status=status.HTTP_201_CREATED)
    if (request.method=='DELETE'):
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------
# CLASS BASED VIEW
# ----------------------------------------------------------------------------------------------------------------------
# class Employeelist(APIView):
#     def get(self,request):
#             e = Employee.objects.all()
#             emp = EmployeeSerializer(e, many=True)
#             return Response(emp.data, status=status.HTTP_200_OK)
#     def post(self,request):
#         e = EmployeeSerializer(data=request.data)
#         if e.is_valid():
#             e.save()
#             return Response(e.data, status=status.HTTP_201_CREATED)
#
#
# class EmployeeetDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self,request,pk):
#         e=self.get_object(pk)
#         emp=EmployeeSerializer(e)
#         return Response(emp.data,status=status.HTTP_200_OK)
#
#     def put(self,request,pk):
#         e=self.get_object(pk)
#         emp=EmployeeSerializer(e,data=request.data)
#         if emp.is_valid():
#             emp.save()
#             return Response(emp.data, status=status.HTTP_201_CREATED)
#
#     def delete(self,request,pk):
#         e=self.get_object(pk)
#         e.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
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
# class BookView(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# ----------------------------------------------------------------------------------------------------------------------
# MIXIN BASED VIEW
# ----------------------------------------------------------------------------------------------------------------------
from rest_framework import mixins,generics

class Employeelist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
       return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)