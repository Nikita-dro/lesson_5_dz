from django.db import models


# Create your models here.
class Groups(models.Model):
    name_group = models.CharField(max_length=200)
    number_group = models.IntegerField()
    count_students = models.IntegerField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return (f"Name - {self.name_group}, number group- {self.number_group}, number of students - {self.count_students}, "
                f"subject - {self.subject}")