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
    phone = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        # Аутентификация пользователя
        user = authenticate(request=self.context.get('request'), phone=phone, password=password)

        if not user:
            raise serializers.ValidationError("Неверные учетные данные.")

        # Здесь предполагается, что у вас есть логика для определения, является ли пользователь сотрудником,
        # например, проверка наличия связанного объекта профиля или проверка поля role
        if not self.is_employee(user):
            raise serializers.ValidationError("Доступ разрешен только для сотрудников.")

        # Если проверка прошла успешно, вызываем родительский метод для генерации токенов
        data = super().validate(attrs)

        # Можно добавить дополнительные данные в ответ, если это необходимо
        # data['role'] = user.role

        return data

    def is_employee(self, user):
        # Пример функции для проверки, что пользователь имеет роль сотрудника
        # Адаптируйте этот метод под вашу логику определения ролей
        return user.role == 'employee'
