from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer  # Import only the necessary serializer

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer  # Fix: Use the correct serializer
