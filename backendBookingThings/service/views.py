from django.shortcuts import render

from rest_framework import viewsets
from .models import Service
from .serializer import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer