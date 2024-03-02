from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee

User = get_user_model()


class EmployeeSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['phone', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        phone = validated_data['phone']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create_user(phone=phone, password=password)
        employee = Employee.objects.create(user=user, first_name=first_name, last_name=last_name,
                                           employer=self.context['request'].user.employer_profile)
        return employee
