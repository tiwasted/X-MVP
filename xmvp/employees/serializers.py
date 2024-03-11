from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('phone', 'password')

    def create(self, validated_data):
        return User.objects.create_user(phone=validated_data['phone'], password=validated_data['password'], email=None)


# Авторизация и валидация пользователя Employee
