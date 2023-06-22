from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

