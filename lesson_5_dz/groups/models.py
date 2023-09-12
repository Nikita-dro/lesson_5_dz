from django.db import models


# Create your models here.
class Groups(models.Model):
    name_group = models.CharField(max_length=200)
    number_group = models.IntegerField()
    count_students = models.IntegerField()
    subject = models.CharField(max_length=200)