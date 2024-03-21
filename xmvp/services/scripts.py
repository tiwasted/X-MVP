"""
from services.models import Service, Subservice


def create_data():
    # Создаем объекты моделей
    service1 = Service.objects.create(name='Бытовой ремонт')
    service2 = Service.objects.create(name='Строительство и отделка')
    service3 = Service.objects.create(name='Уборка и санитария')

    subservice1 = Subservice.objects.create(service=service1, name='Услуги уборки и клининга')
    subservice2 = Subservice.objects.create(service=service1, name='Услуги химчитски')
    subservice3 = Subservice.objects.create(service=service1, name='Санитарно-эпидемиологические услуги')

    subservice1.save()
"""
