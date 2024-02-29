from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    objects = UserManager()  # Используйте UserManager

    def __str__(self):
        return self.username
