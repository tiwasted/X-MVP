from django.urls import path
from .views.employer_views import EmployerRegistrationView
from .views.order_views import OrderEmployerView
from .views.order_views import OrderEmployerDetailView
from .views.order_views import OrderProcessingViewSet
from .views.schedule_views import ScheduleViewSet


# Создаем объект OrderProcessingViewSet и указываем поддерживаемые методы
order_processing_view = OrderProcessingViewSet.as_view({
    'put': 'update',  # указываем, что метод PUT обрабатывается методом update
})


urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='employer_registration'),

    path('orders/', OrderEmployerView.as_view(), name='order_list'),  # Список всех заказов
    path('orders/detail/', OrderEmployerDetailView.as_view(), name='order_detail'),  # Полная информация заказа

    path('orders/processing/<order_id>/', order_processing_view, name='order_processing'),

    path('orders/schedule/', ScheduleViewSet.as_view({'get': 'list'}), name='order_schedule'),
]
