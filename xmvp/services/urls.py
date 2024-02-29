from django.urls import path
from .views import ServiceListAPIView, ServiceDetailAPIView, ServiceNameListAPIView, SubServiceListAPIView


urlpatterns = [
    path('create/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    path('service-names/', ServiceNameListAPIView.as_view(), name='service-names'), # эндпоинт для чтения всех услуг
    path('<int:service_id>/subservices/', SubServiceListAPIView.as_view(), name='subservice-list'), # эндпоинт для чтения всех подуслуг
]
