from django.urls import path
from .views import DepartmanListCreate, PersonelListCreate, PersonelUpdateDelete, DepartmanPersonelView, DepartmanPersonelViewLOOKUPFİELD

urlpatterns = [
    path('departman/', DepartmanListCreate.as_view()),
    path('personel/', PersonelListCreate.as_view()),
    path('personel/<int:pk>/', PersonelUpdateDelete.as_view()),
    # path('departman/<str:departman>/', DepartmanPersonelView.as_view()),
    path('departman/<str:name>/', DepartmanPersonelViewLOOKUPFİELD.as_view()),
]
