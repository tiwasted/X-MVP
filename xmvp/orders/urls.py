from django.urls import path
from .views import OrderListAPIView


urlpatterns = [
    path('create/', OrderListAPIView.as_view(), name='order-list'),
]
