from django.urls import path
from .views import EmployerRegistrationAPIView
from .views import EmployerTokenObtainPairView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', EmployerRegistrationAPIView.as_view(), name='employer_registration'),

    path('token/', EmployerTokenObtainPairView.as_view(), name='employer_token_obtain_pair'),
]
