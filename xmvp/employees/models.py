from django.db import models

from employers.models import Employer


class Employee(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
