from django.urls import path
from .views import OrderCreateView
from .views import OrderProcessView


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('process/<int:pk>/', OrderProcessView.as_view(), name='order-process'),
]
