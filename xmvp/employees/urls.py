from django.urls import path
from .views import EmployeeRegistrationView


urlpatterns = [
    path('register/', EmployeeRegistrationView.as_view(), name='register_employee'),
]
