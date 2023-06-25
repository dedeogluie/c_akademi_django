from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .seralizers import TodoSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todo = Todo.objects.filter(is_done = False)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id = id)
    if request.method == 'GET':
        # todo = Todo.objects.get(id = id)
        # todo = get_object_or_404(Todo, id = id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # todo = get_object_or_404(Todo, id = id)
        serializer = TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # todo = get_object_or_404(Todo, id =id)
        todo.delete()
        message = {
            "message": "Todo deleted succesfully"
        }
        return Response(message)
    

class Todos(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'


class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
