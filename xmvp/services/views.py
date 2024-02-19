from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer


# API для создания услуги
class ServiceListAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


class ServiceDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
