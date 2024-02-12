from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Service
from .serializers import ServiceSerializer

from .models import Employee
from .serializers import EmployeeSerializer


def index(request):
    return HttpResponse("Главная страница")


def company(request):
    return HttpResponse("Страница для Компаний")


class TokenObtainAPIView(APIView):
    def post(self, request):
        # Получаем данные пользователя из запроса
        username = request.data.get('username')
        password = request.data.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)

        if user:
            # Если пользователь аутентифицирован успешно, создаем токен и возвращаем его
            token = user.auth_token.key
            return Response({'access': token}, status=status.HTTP_200_OK)
        else:
            # Если аутентификация не удалась, возвращаем сообщение об ошибке
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


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


# API для создания работника
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Получаем работодателя, создающего нового сотрудника
        employer = self.request.user
        # Устанавливаем поле employer перед сохранением сотрудника
        serializer.save(employer=employer)


class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
