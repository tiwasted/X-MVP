from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Service, SubService
from .serializers import ServiceSerializer, ServiceNameSerializer, SubServiceSerializer, SubServiceNameSerializer

from employers.models import Employer
# from accounts.permissions import IsEmployer


# API для создания услуги
# class ServiceListAPIView(generics.ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         employer = Employer.objects.get(user=self.request.user)
#         serializer.save(employer=employer)
#
#
class ServiceDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class CreateServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Проверка, является ли аутентифицированный пользователь работодателем
        print("Текущая роль пользователя:", request.user.role)
        if request.user.role != 'employer':
            return Response({"Ошибка": "Только работодатели могут создавать услуги."}, status=403)

        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
