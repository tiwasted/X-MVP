from django.contrib import admin
from django.urls import path, include
from desktop_app.views import EmployerAPIView
from desktop_app.views import EmployerLoginView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('desktop_app.urls')),
    path('api/v1/employerlist', EmployerAPIView.as_view()),
    path('api/login/', EmployerLoginView.as_view(), name='user-login'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
