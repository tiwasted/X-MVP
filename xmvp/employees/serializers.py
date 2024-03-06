from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

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
    username_field = 'phone'

    def __init__(self, *args, **kwargs):
        # Переопределите поля, которые будут использоваться для аутентификации
        super(EmployeeTokenObtainPairSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = serializers.CharField(write_only=True)

    def validate(self, attrs):
        # Возьмите учетные данные пользователя из атрибутов
        username = attrs.get(self.username_field)
        password = attrs.get("password")

        # Аутентифицируйте пользователя с помощью переданных учетных данных
        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Невозможно аутентифицировать с указанными учетными данными.')

        # Проверьте, что аутентифицированный пользователь имеет роль 'employee'
        if user.role != 'employee':
            raise serializers.ValidationError('Доступ разрешен только для сотрудников.')

        # Если пользователь успешно прошел проверку, используйте метод базового класса для генерации токена
        data = super().validate(attrs)

        # Добавьте дополнительную информацию в ответ, если это необходимо
        data['role'] = user.role

        return data
