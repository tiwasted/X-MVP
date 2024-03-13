from django.urls import path
from .views import ClientRegistrationView

urlpatterns = [
    path('register/', ClientRegistrationView.as_view(), name='client_registration'),
]
