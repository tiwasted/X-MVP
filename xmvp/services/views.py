from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer


# API для создания услуги
class ServiceListAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Получаем работодателя, создавшего услугу
        employer = self.request.user
        # Устанавливаем employer_id перед сохранением услуги
        serializer.save(employer=employer)


class ServiceDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
