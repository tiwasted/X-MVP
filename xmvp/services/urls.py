from django.urls import path
from .views import (CreateServiceView,
                    ServiceDetailAPIView,
                    ServiceNameListAPIView,
                    SubServiceListAPIView)


urlpatterns = [
    path('create/', CreateServiceView.as_view(), name='service-create'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    path('service-names/', ServiceNameListAPIView.as_view(), name='service-names'),  # эндпоинт для чтения всех услуг
    path('<int:service_id>/subservices/', SubServiceListAPIView.as_view(), name='subservice-list'),  # эндпоинт для чтения всех подуслуг
]
