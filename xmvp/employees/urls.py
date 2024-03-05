from django.urls import path
from .views import EmployeeCreateAPIView, EmployeeTokenObtainPairView
# from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
     path('create/', EmployeeCreateAPIView.as_view(), name='employee_create'),

     path('token/', EmployeeTokenObtainPairView.as_view(), name='token_obtain_pair'),
     # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
