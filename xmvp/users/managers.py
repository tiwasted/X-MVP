from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email=None, phone=None, password=None, **extra_fields):
        if not email and not phone:
            raise ValueError('У пользователей должен быть адрес электронной почты или номер телефона.')

        if email:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
        else:
            user = self.model(phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not email:
            raise ValueError('У суперпользователей должен быть адрес электронной почты.')

        return self.create_user(email, password=password, **extra_fields)
