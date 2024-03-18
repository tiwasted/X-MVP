from django.db import models
from employers.models import Employer


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EmployerService(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.employer.name}"
