from django.db import models
from employers.models import Employer


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='services')


class SubService(models.Model):
    sub_service_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    service = models.ForeignKey(Service, related_name='subservices', on_delete=models.CASCADE)
