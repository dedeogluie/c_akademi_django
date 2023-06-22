from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework import generics 
from rest_framework.viewsets import ModelViewSet

from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

from django.shortcuts import render, HttpResponse, get_object_or_404


@api_view()
def home(request):
    return Response({
        "home":"burası home sayfasıdır"
    })

# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# - delete (dB de kayıt silme)
# - patch (kısmi update)

#!#################### FUNCTION BASED VIEWS ########################################
@api_view(['GET'])
def student_list(request):
    student = Student.objects.all()
    print(student)
    serializer = StudentSerializer(student, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message":"Öğrenci başarı bir şekilde kayıt edildi."
        }
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def stundent_detail(request, pk): 
    student = get_object_or_404(Student, id = pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['PUT'])
def stundet_update(request, pk):
   student = get_object_or_404(Student, id = pk)
   serializer = StudentSerializer(instance=student,data = request.data)
   if serializer.is_valid():
        serializer.save()
        message = {
            "message":"Öğrenci başarı bir şekilde değiştiril edildi."
        }
        return Response(message, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def stundet_patch(request, pk):
   student = get_object_or_404(Student, id = pk)
   serializer = StudentSerializer(instance=student,data = request.data, partial=True)
   if serializer.is_valid():
        serializer.save()
        message = {
            "message":"Öğrenci başarı bir şekilde değiştiril edildi."
        }
        return Response(message, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id = pk)
    student.delete()
    message = {
            "message":"Öğrenci başarı bir şekilde silindi."
        }
    return Response(message)


#!#################### CLASS BASED VIEWS ########################################
class StudentListCreate(APIView):

    def get(self, request):
        student = Student.objects.all()
        print(student)
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message":"Öğrenci başarı bir şekilde kayıt edildi."
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):

    def get(self, request, pk):
        student = get_object_or_404(Student, id = pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = get_object_or_404(Student, id = pk)
        serializer = StudentSerializer(instance=student,data = request.data)
        if serializer.is_valid():
                serializer.save()
                message = {
                    "message":"Öğrenci başarı bir şekilde değiştiril edildi."
                }
                return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = get_object_or_404(Student, id = pk)
        student.delete()
        message = {
                "message":"Öğrenci başarı bir şekilde silindi."
            }
        return Response(message)


#! GENERICAPIView and Mixins
"""
 #? GenericApıView
# One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

# GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

#? Mixins
# - ListModelMixin
#     - list method
# - CreateModelMixin
#     - create method
# - RetrieveModelMixin
#     - retrieve method
# - UpdateModelMixin
#     - update method
# - DestroyModelMixin
#     - destroy method """


class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)


class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve( request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update( request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy( request, *args, **kwargs)



#! Concrete Views

class StudentCV(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#! Model Views Set
class StundentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer