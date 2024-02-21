from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Service, SubService
from .serializers import ServiceSerializer, ServiceNameSerializer, SubServiceSerializer, SubServiceNameSerializer


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


class ServiceNameListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceNameSerializer(services, many=True)
        return Response(serializer.data)


class SubServiceListAPIView(ListAPIView):
    serializer_class = SubServiceNameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Этот метод переопределяется для фильтрации подуслуг по идентификатору услуги.
        """
        service_id = self.kwargs['service_id']
        return SubService.objects.filter(service__id=service_id)
