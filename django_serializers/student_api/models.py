from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name