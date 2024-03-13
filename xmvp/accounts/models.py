from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, null=True, blank=True)
#     phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
#     role = models.CharField(max_length=15, blank=True, null=True)
#
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']
#
#     objects = UserManager()  # Используйте UserManager
#
#     def __str__(self):
#         return self.username


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    EMPLOYER = 'employer'
    EMPLOYEE = 'employee'
    CLIENT = 'client'
    ROLE_CHOICES = [
        (EMPLOYER, 'Employer'),
        (EMPLOYEE, 'Employee'),
        (CLIENT, 'Client'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else self.phone
