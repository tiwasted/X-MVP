from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('desktop_app.urls')),
    path('services/', include('services.urls')),
    path('employees/', include('employees.urls')),
]
