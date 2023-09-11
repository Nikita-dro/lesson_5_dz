from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from .models import Students


# Create your views here.
def generate_student(request):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = fake.random_int(min=0, max=100)
    student = Students.objects.create(first_name=first_name, last_name=last_name, age=age)
    return render(request, 'student.html', {"student": student})
