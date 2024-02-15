from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager


class EmployerManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('The login field must be set')

        user = self.model(login=login, **extra_fields)

        if password:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, password, **extra_fields)


class Employer(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=150, unique=True)
    company_name = models.CharField(max_length=150, default='')
    description = models.TextField(blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = EmployerManager()

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login

