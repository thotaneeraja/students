from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import testSerializer
from .models import test
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(generics.ListCreateAPIView):
    queryset = test.objects.all()
    serializer_class = testSerializer
    permission_classes = [permissions.AllowAny]


class StudentCurd(generics.RetrieveUpdateDestroyAPIView):
    queryset = test.objects.all()
    serializer_class = testSerializer
    permission_classes = [permissions.AllowAny]

# Create your views here.
