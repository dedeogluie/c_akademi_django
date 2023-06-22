from django.db import models

# Create your models here.

class Path(models.Model):
    path_name = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.path_name}"
    
class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name
    

    '''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
'''