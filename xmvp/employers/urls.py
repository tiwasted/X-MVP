from django.urls import path
from .views import EmployerRegistrationView


urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='register_employer'),
]
