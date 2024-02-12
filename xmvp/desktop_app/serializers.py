from rest_framework import serializers
# from rest_framework.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from .models import Employer
from .models import Service
from .models import Employee


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('login',)


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         return data
#
#
# class CustomTokenRefreshSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         return data


# сериализатор для услуг Компаний
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'sub_service', 'price', 'description', 'employer_id']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone_number']

