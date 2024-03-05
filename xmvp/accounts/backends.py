from .models import CustomUser
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
           return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
           return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )
            if user and user.check_password(password) and self.user_can_authenticate(user):
                return user
        except CustomUser.DoesNotExist:
            # Возвращаем None, если пользователь не найден
            return None

    def user_can_authenticate(self, user):
        """
        Проверяет, разрешена ли аутентификация для данного пользователя.
        Вы можете использовать этот метод для учета флага `is_active` или других
        условий аутентификации.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None
