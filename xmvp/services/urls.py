from django.urls import path

from .views import CategoryList
from .views import ServiceList


urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),   # Эндпоинт для чтения категорий
    path('services/', ServiceList.as_view(), name='service-list'),   # Эндпоинт для чтения услуг
    path('services/<int:category_id>/', ServiceList.as_view(), name='service-list-by-category'),   # Эндпоинт для выбора услуг из категории
]
