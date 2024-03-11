from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
# from .models import Employer

User = get_user_model()


class EmployerRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(email=validated_data['email'], password=validated_data['password'], phone=None)
