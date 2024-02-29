from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email=None, phone=None, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с заданным адресом электронной почты и/или телефоном и паролем.
        """
        if not email and not phone:
            raise ValueError('Должен быть установлен адрес электронной почты/телефон')

        email = self.normalize_email(email) if email else None

        # Генерация username из email или phone, если он не был явно передан через extra_fields
        if 'username' not in extra_fields:
            extra_fields['username'] = email if email else phone

        username = extra_fields.pop('username')

        # Создание пользователя
        user = self.model(email=email, phone=phone, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email=email, phone=phone, password=password, **extra_fields)

    def create_superuser(self, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        # Убедитесь, что суперпользователь получает эти флаги
        if not extra_fields.get('is_superuser') or not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_superuser=True and is_staff=True.')

        return self._create_user(email=email, phone=phone, password=password, **extra_fields)
