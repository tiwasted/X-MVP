from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(login=username) or CustomUser.objects.get(phone_number=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            # возвращается None, если пользователь не найден
            return None
