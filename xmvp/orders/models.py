# from django.db import models
#
# from services.models import SubService
# from employers.models import Employer
#
#
# class Order(models.Model):
#     sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name='orders')
#     employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     date = models.DateField()
#     time = models.TimeField()
#     address = models.CharField(max_length=100)
#     square_meters = models.IntegerField()
#     phone_number = models.CharField(max_length=20)
