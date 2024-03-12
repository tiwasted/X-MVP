from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

User = get_user_model()


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('phone', 'password')

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
                email=None
            )
            user.role = 'employee'
            user.save()
            return user
