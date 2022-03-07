from django.contrib import admin
from django.urls import path,include
from .views import  StudentCurd
urlpatterns = [
    path('students', StudentCurd, name="students_list_or_create"),
    path('students/<int:pk>/', StudentCurd, name="students_get_or_update"),
]