from django.db import models

from desktop_app.models import Employer


class Service(models.Model):
    name = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='services')


class SubService(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    # employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='subservices', on_delete=models.CASCADE)
