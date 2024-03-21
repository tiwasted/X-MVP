from django.db import models

from employers.models import Employer


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subservice(models.Model):
    service = models.ForeignKey(Service, related_name='subservices',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Offer(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    subservice = models.ForeignKey(Subservice, related_name='offers', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.employer.name}"
