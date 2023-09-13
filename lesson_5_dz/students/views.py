from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from faker import Faker
from .models import Students


# Create your views here.
def generate_student(request):
    fake = Faker()
    student = Students.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                      age=fake.random_int(min=0, max=100))
    return render(request, 'student.html', {"student": student})


def generate_students(request):
    fake = Faker()
    try:
        count = int(request.GET.get('count', 1))
        if 0 < count <= 100:
            list_students = []
            for i in range(count):
                first_name = fake.first_name()
                last_name = fake.last_name()
                age = fake.random_int(min=0, max=100)
                student = Students.objects.create(first_name=first_name, last_name=last_name, age=age)
                list_students.append({'id': student.id, 'first_name': first_name, 'last_name': last_name, 'age': age})
            return JsonResponse(list_students, safe=False)
        else:
            return HttpResponse('Error. count must be from 0 to 100')
    except ValueError:
        return HttpResponse('Count must be int')
