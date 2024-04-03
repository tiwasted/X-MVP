from django.urls import path
from .views.employer_views import EmployerRegistrationView
from .views.order_views import OrderEmployerView
from .views.order_views import OrderEmployerDetailView


urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='employer_registration'),

    path('orders/', OrderEmployerView.as_view(), name='order-list'),
    path('orders/detail/', OrderEmployerDetailView.as_view(), name='order-detail'),
]
