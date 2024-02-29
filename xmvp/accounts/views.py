from rest_framework import viewsets
from .serializers import CustomUserRegistrationSerializer, User


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserRegistrationSerializer
