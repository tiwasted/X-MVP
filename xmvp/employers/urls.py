from django.urls import path
from .views.employer_views import EmployerRegistrationView, ChangePasswordView
from .views.employee_views import EmployeeRegistrationView
from .views.service_views import EmployerServiceCreator
from .views.order_views import OrderEmployerView, OrderEmployerDetailView, OrderProcessingViewSet
from .views.schedule_views import ScheduleViewSet


# Создаем объект OrderProcessingViewSet и указываем поддерживаемые методы
order_processing_view = OrderProcessingViewSet.as_view({
    'put': 'update',  # указываем, что метод PUT обрабатывается методом update
})


urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='employer_registration'),  # Регистрация Работодателя (POST)
    path('employees/register/', EmployeeRegistrationView.as_view(), name='employee_registration'),  # Регистрация сотрудника от Работодателя (POST)

    path('change-password/', ChangePasswordView.as_view(), name='change_password'),  # Измение пароля (POST)

    path('service/create/', EmployerServiceCreator.as_view(), name='creat_service_from_employer'),  # Создание услуги от Работодателя (POST)

    path('orders/', OrderEmployerView.as_view(), name='order_list'),  # Список всех заказов (GET)
    path('orders/detail/', OrderEmployerDetailView.as_view(), name='order_detail'),  # Полная информация заказа (GET)
    path('orders/processing/<order_id>/', order_processing_view, name='order_processing'),  # (PUT)
    path('orders/schedule/', ScheduleViewSet.as_view({'get': 'list'}), name='order_schedule'),  # Расписание заказов для Работодателя (GET)
]
