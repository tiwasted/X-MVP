from django.urls import path
from .views import EmployeeCreateAPIView
from .views import EmployeeTokenObtainPairView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
     path('create/', EmployeeCreateAPIView.as_view(), name='employee_create'),

     path('token/', EmployeeTokenObtainPairView.as_view(), name='employee_token_obtain_pair'),
]
