from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Departman(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Personel(models.Model):
    TITLE = (
        ("Team Lead", "LEAD"),
        ("Mid Lead", "MID"),
        ("Junior", "JUN"),
    )
    GENDER = (
    ("Female", "F"),
    ("Male", "M"),
    ("Other", "O"),
    ("Prefer Not Say", "N"),
    )

    departman = models.ForeignKey(Departman, on_delete=models.SET_NULL, null=True, related_name='personels')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=15, choices=TITLE)
    gender = models.CharField(max_length=20, choices=GENDER)
    salary = models.PositiveIntegerField(default=30000)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.first_name} {self.last_name} - {self.departman.name}  "