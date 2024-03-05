from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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


# Авторизация и валидация пользователя Employee
class EmployeeTokenObtainPairSerializer(TokenObtainPairSerializer):
    phone = serializers.CharField(required=False)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        phone = attrs.get('phone', None)
        password = attrs['password']

        # Аутентификация пользователя
        user = None
        if phone:
            user = authenticate(phone=phone, password=password)

        if user is None:
            raise serializers.ValidationError("Неверные учетные данные.")

        # Проверка роли пользователя
        allowed_roles = ['employee']  # Список разрешённых ролей
        print(f"User role: {user.role}, Allowed roles: {allowed_roles}")
        if user.role not in allowed_roles:
            raise serializers.ValidationError("Доступ разрешен только для сотрудников.")

        data = super().validate(attrs)
        data['role'] = user.role

        return data
