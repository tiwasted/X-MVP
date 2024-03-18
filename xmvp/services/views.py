from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

from .serializers import CategorySerializer
from .serializers import ServiceSerializer
from .serializers import EmployerServiceSerializer

from .models import Category, Service, EmployerService

User = get_user_model()


class CategoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reguest):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ServiceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id=None):
        services = Service.objects.filter(category_id=category_id) if category_id else Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class CreateEmployerService(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Проверка, является ли аутентифицированный пользователь работодателем
        print("Текущая роль пользователя:", request.user.role)
        if request.user.role != User.EMPLOYER:
            return Response({"Ошибка": "Только работодатели могут создавать услуги."}, status=status.HTTP_403_FORBIDDEN)

        employer = getattr(request.user, 'employer_profile', None)
        if not employer:
            return Response({"error": "Профиль Employer не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployerServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=employer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
