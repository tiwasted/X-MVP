from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('employers/', include('employers.urls')),
    path('employees/', include('employees.urls')),

    path('services/', include('services.urls')),
    path('orders/', include('orders.urls')),

]
