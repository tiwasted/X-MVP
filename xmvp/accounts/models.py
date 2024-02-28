from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission


class CustomUserManager(BaseUserManager):
    def create_user(self, login=None, phone_number=None, password=None, **extra_fileds):
        if not login and not phone_number:
            raise ValueError('Необходимо указать логин или номер телефона')

        if login:
            user = self.model(login=login, **extra_fileds)
        elif phone_number:
            user = self.model(phone_number=phone_number, **extra_fileds)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password, **extra_fileds):
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)

        if not login:
            raise ValueError('У суперпользователя должен быть логин')
        return self.create_user(login=login, password=password, **extra_fileds)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Добавляем related_name для каждого поля
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="customuser",
    )

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.login or self.phone_number


# Модель для Работодателя (используется login)
class Employer(CustomUser):
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'


# Модель для Работника (используется phone_number)
class Employee(CustomUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Client(CustomUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
