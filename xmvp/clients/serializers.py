from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from .models import Client

User = get_user_model()


class ClientRegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    first_name = serializers.CharField(max_length=30, required=True, allow_blank=True)
    last_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    address = serializers.CharField(max_length=60, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'first_name', 'last_name', 'address')

    def validate_phone(self, value):
        # Проверка Phone
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Пользотель с таким phone уже существует")
        return value

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                phone=validated_data['phone'],
                password=validated_data['password'],
                email=None  # Указано явно, если email не используется или необязателен
            )
            user.role = 'client'
            user.save()

            # Создание профиля клиента
            Client.objects.create(
                user=user,
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                address=validated_data.get('address', '')
            )

            return user
