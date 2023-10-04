from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_student, name='generate_student'),
    path('/', views.generate_students, name='generate_students')
]
