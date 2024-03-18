from rest_framework import serializers

from .models import Category
from .models import Service
from .models import EmployerService


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'category', 'name']


class EmployerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerService
        fields = ['service', 'title', 'description', 'price']
