from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio


class Adres(models.Model):
    name = models.CharField(max_length=40)
    adres = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Urun(models.Model):
    name = models.CharField(max_length=120)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
