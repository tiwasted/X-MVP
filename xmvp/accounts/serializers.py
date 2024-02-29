from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': False},  # Указываем, что поля не обязательны
            'phone': {'required': False},
        }

    def validate(self, data):
        """
        Проверяем, что хотя бы одно из полей email или phone заполнено.
        """
        email = data.get('email')
        phone = data.get('phone')
        if not email and not phone:
            raise ValidationError("Необходимо указать либо email, либо номер телефона.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
