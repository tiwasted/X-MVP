"""
from services.models import Category, Service

category = Category.objects.get(id=1)

new_service = Service(category=category, name='Санитарно-эпидемиологические услуги')
new_service.save()
"""
