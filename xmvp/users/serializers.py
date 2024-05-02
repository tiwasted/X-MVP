from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_phone = attrs.get('email_or_phone')
        password = attrs.get('password')

        # Обновление механизма аутентификации для использования кастомного бэкенда
        user = authenticate(request=self.context.get('request'), username=email_or_phone, password=password)

        if user:
            if not user.is_active:
                raise serializers.ValidationError(('Пользователь не активирован.'))

            data = {
                'refresh': str(RefreshToken.for_user(user)),
                'access': str(RefreshToken.for_user(user).access_token),
            }

            return data
        else:
            raise serializers.ValidationError(('Не удается войти в систему с предоставленными учетными данными.'))
