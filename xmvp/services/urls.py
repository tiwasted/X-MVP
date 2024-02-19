from django.urls import path
from .views import ServiceListAPIView, ServiceDetailAPIView


urlpatterns = [
    path('create/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),
]
