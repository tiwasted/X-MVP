from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),

    path('employers/', include('employers.urls')),
    path('employees/', include('employees.urls')),
    path('clients/', include('clients.urls')),

    path('services/', include('services.urls')),
    path('orders/', include('orders.urls')),

]
