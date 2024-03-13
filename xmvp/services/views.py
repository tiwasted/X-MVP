from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Service, SubService
from .serializers import ServiceSerializer, ServiceNameSerializer, SubServiceSerializer, SubServiceNameSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class ServiceDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class CreateServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Проверка, является ли аутентифицированный пользователь работодателем
        print("Текущая роль пользователя:", request.user.role)
        if request.user.role != User.EMPLOYER:
            return Response({"Ошибка": "Только работодатели могут создавать услуги."}, status=status.HTTP_403_FORBIDDEN)

        employer = getattr(request.user, 'employer_profile', None)
        if not employer:
            return Response({"error": "Профиль Employer не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=employer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
