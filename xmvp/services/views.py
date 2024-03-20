from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

from .serializers import CategorySerializer
from .serializers import ServiceSerializer

from .models import Category, Service

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
