from django.urls import path

from .views.service_views import ServiceListView
from .views.service_views import SubserviceListView

from .views.employer_views import EmployerServiceCreator

from .views.client_views import OfferListView


urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),                                                  # Эндпоинт чтения услуг для Работодателя/Клиента
    path('services/<int:service_id>/subservices/', SubserviceListView.as_view(), name='subservice-list'),               # Эндпоинт чтения под-услуг для Работодателя/Клиента
    path('subservices/<int:subservice_id>/offers/', OfferListView.as_view(), name='offer-list'),                        # Эндпоинт чтения предложений для клиентов

    path('create/', EmployerServiceCreator.as_view(), name='offer-list-for-create'),                                    # Эндпоинт создание услуги для Работодателя
]
