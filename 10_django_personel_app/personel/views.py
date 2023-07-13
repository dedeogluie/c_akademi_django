from django.shortcuts import render

from .serializers import DepartmanSerializer, PersonelSerializer, DepartmanPersonelSerializer
from .models import Departman, Personel
from .permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DepartmanListCreate(generics.ListCreateAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class PersonelListCreate(generics.ListCreateAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]


class PersonelUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class DepartmanPersonelView(generics.ListAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanPersonelSerializer

    def get_queryset(self):
        name = self.kwargs['departman']
        return Departman.objects.filter(name__iexact = name)
    

class DepartmanPersonelViewLOOKUPFİELD(generics.RetrieveAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanPersonelSerializer
    lookup_field = 'name'
