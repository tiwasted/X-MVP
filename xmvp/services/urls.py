from django.urls import path

from .views import CreateEmployerService
from .views import CategoryList
from .views import ServiceList


urlpatterns = [
    path('create/', CreateEmployerService.as_view(), name='service-create'),  # эндпоинт для создания услуги от Работодателя

    path('categories/', CategoryList.as_view(), name='category-list'),
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:category_id>/', ServiceList.as_view(), name='service-list-by-category'),
]
