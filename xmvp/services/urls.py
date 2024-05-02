from django.urls import path

from .views.service_views import ServiceCreateView

# from .views.service_views import SubserviceListView

# from .views.employer_views import EmployerServiceCreator

# from .views.client_views import OfferListView
# from .views.client_views import OfferDetailView


urlpatterns = [
    path('create/', ServiceCreateView.as_view(), name='service-create'),  # Создание независимой услуги для пользователей программы (POST)

    # path('<int:service_id>/subservices/', SubserviceListView.as_view(), name='subservice-list'),  # Эндпоинт чтения под-услуг для Работодателя/Клиента
    # path('subservices/<int:subservice_id>/offers/', OfferListView.as_view(), name='offer-list'),  # Эндпоинт чтения предложений для клиентов
    # path('offers/<int:offer_id>/', OfferDetailView.as_view(), name='offer-detail'),

    # path('create/', EmployerServiceCreator.as_view(), name='offer-list-for-create'),  # Эндпоинт создание услуги для Работодателя
]
