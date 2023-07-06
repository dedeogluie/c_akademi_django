from rest_framework import serializers
from .models import Category, Blog

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class BlogSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'category',
            'category_id',
            'content',
            'status',
            'created_date'
        )