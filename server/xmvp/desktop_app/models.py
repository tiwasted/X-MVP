from django.db import models


class Employer(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Service(models.Model):
    service_name = models.CharField(max_length=255)
    sub_service = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)
