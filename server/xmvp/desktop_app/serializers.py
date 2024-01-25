from rest_framework import serializers
from .models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('login', 'password')


class EmployerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
