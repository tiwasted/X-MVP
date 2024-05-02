from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from employers.models import Employer

User = get_user_model()


class EmployerRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    company_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    company_description = serializers.CharField(max_length=255, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'company_name', 'company_description')

    def validate_email(self, value):
        # Проверка Email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользотель с таким email уже существует")
        return value

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                phone=None
            )
            user.role = 'employer'
            user.save()


            # Создание профиля для Employer
            Employer.objects.create(
                user=user,
                company_name=validated_data.get('company_name', ''),
                company_description=validated_data.get('company_description', '')
            )

            return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
