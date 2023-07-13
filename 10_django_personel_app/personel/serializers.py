from rest_framework import serializers

from .models import Departman, Personel

from django.utils.timezone import now

class DepartmanSerializer(serializers.ModelSerializer):

    personel_count = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = (
            'id',
            'name',
            "personel_count"
        )

    def get_personel_count(self, obj):
        return obj.personels.count()
    
class PersonelSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required = False)
    days_since_joind = serializers.SerializerMethodField()

    class Meta:
        model = Personel
        fields = (
            'id',
            'departman',
            "user_id",
            'user',
            'first_name',
            'last_name',
            "title",
            'gender',
            'salary',
            "start_date",
            'days_since_joind',
        )

    def create(self, validate_date):
        validate_date['user_id'] = self.context['request'].user.id
        instance = Personel.objects.create(**validate_date)
        return instance

    def get_days_since_joind(self, obj):
        return (now() - obj.start_date).days
    


class DepartmanPersonelSerializer(serializers.ModelSerializer):

    personels = PersonelSerializer(many = True, read_only = True)
    personel_count = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = (
            'id',
            'name',
            "personel_count",
            'personels',
        )

    def get_personel_count(self, obj):
        return obj.personels.count()