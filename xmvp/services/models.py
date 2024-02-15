from django.db import models

from desktop_app.models import Employer


class Service(models.Model):
    service_name = models.CharField(max_length=255)
    sub_service = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
