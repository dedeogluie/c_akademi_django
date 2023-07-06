from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True, required = True)
    first_name = serializers.CharField(required = True)


    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password", "password2")

    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {
                    'password': 'password fileds didn\'t match.'
                }
            )
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)# username = valideted_data['username]
        user.set_password(password)
        user.save()
        return user