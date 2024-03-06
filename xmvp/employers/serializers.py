from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import Employer

User = get_user_model()


class EmployerRegistrationSerializer(serializers.ModelSerializer):
    # Поля для пользователя
    email = serializers.EmailField(required=False, allow_blank=True)
    # phone = serializers.CharField(max_length=11, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Подтвердите пароль")

    # Поля для Employer
    company_name = serializers.CharField(required=True)
    company_description = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'company_name', 'company_description']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return data

    def validate_email(self, value):
        # Проверка Email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользотель с таким email уже существует")
        return value

    def create(self, validated_data):
        # Удаление данных, не относящихся к пользователю
        email = validated_data.pop('email')
        validated_data.pop('password2')
        password = validated_data.pop('password')
        company_name = validated_data.pop('company_name')
        company_description = validated_data.pop('company_description')

        # Создание пользователя
        user = User(email=email)
        user.set_password(password)
        user.save()

        # Создание профиля Employer
        Employer.objects.create(user=user, company_name=company_name, company_description=company_description)

        return user


# Авторизация и валидация пользователя Employer
class EmployerTokenObtainPairSerializer(TokenObtainPairSerializer):
    # username_field = User.USERNAME_FIELD
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get('request'), username=email, password=password)

        if not user:
            raise serializers.ValidationError('Невозможно аутентифицировать с указанными учетными данными.')

        if user.role != 'employer':
            raise serializers.ValidationError('Доступ разрешен только для работодателей.')

        data = super().validate(attrs)

        data['role'] = user.role

        return data
