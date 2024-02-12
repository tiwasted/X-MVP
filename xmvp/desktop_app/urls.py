from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import ServiceListAPIView, ServiceDetailAPIView
from .views import EmployeeCreateAPIView

from . import views

urlpatterns = [
    path('', views.index),
    path('company/', views.company),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/services/create', ServiceListAPIView.as_view(), name='service-list'),
    path('api/services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    path('api/employees/create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
]
