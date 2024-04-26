from django.db import models
from accounts.models import CustomUser
from services.models import Offer
from employees.models import Employee


class Order(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'В ожидании'),
        ('processing', 'В обработке'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=100)
    square_meters = models.DecimalField(max_digits=6, decimal_places=2)
    service_date = models.DateField()
    service_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='в ожидании')

    approved_time = models.DateTimeField(null=True, blank=True)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_orders')

    def __str__(self):
        return f"Order {self.id} - {self.offer.title} by {self.user.username}"


class Task(models.Model):
    order = models.ForeignKey(Order, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description
