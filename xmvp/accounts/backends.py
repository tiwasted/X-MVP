from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, request, username=None, password=None, **kwargs):
        # Поиск пользователя по email или phone
        user = User.objects.filter(
            Q(email=username) | Q(phone=username)
        ).first()

        # Проверка, что пользователь найден, пароль верный и пользователь активен
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def user_can_authenticate(self, user):
        """Проверяет, активен ли пользователь."""
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        """Получение экземпляра пользователя по ID."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
