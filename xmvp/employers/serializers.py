from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import Employer

User = get_user_model()


class EmployerRegistrationSerializer(serializers.ModelSerializer):
    # Поля для пользователя
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(max_length=11, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Confirm password")

    # Поля для Employer
    company_name = serializers.CharField(required=True)
    company_description = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'phone', 'password', 'password2', 'company_name', 'company_description']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Убедиться, что хотя бы одно из полей email или phone заполнено
        if not data.get('email') and not data.get('phone'):
            raise serializers.ValidationError("Должен быть указан хотя бы один из контактов: email или phone.")
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return data

    def validate_username(self, value):
        # Проверка Username
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Пользотель с таким username уже существует")
        return value

    def validate_phone(self, value):
        # Проверка Phone
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Пользотель с таким phone уже существует")
        return value

    def validate_email(self, value):
        # Проверка Email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользотель с таким email уже существует")
        return value

    def create(self, validated_data):
        # Удаление данных, не относящихся к пользователю
        validated_data.pop('password2', None)
        password = validated_data.pop('password')
        company_name = validated_data.pop('company_name', None)
        company_description = validated_data.pop('company_description', None)

        # Создание пользователя
        if validated_data.get('email'):
            username = validated_data.get('email')
        else:
            username = validated_data.get('phone')
        user = User(username=username, **validated_data)
        user.set_password(password)
        user.save()

        # Создание профиля Employer
        Employer.objects.create(user=user, company_name=company_name, company_description=company_description)

        return user


# Авторизация и валидация пользователя Employer
class EmployerAuthSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Неверные учетные данные.")
        if not hasattr(user, 'employer_profile'):
            raise serializers.ValidationError("Доступ разрешен только для работодателей.")
        return user
