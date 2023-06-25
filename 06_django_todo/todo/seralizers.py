from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Todo
        fields = ("id", "task", "description", "prioirity", "is_done", "updated_date" , "created_date")
