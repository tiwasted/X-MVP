from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('company/', include('employers.urls')),
    path('services/', include('services.urls')),
    path('employees/', include('employees.urls')),
    path('orders/', include('orders.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
