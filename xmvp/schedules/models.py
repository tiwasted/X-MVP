# from django.db import models
# from employees.models import Employee
# from orders.models import Order
#
#
# class Schedule(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     scheduled_time = models.DateTimeField()
#     client_address = models.CharField(max_length=50)
#     client_phone = models.CharField(max_length=15)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
