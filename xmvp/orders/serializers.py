from rest_framework import serializers
from .models import Order
from services.models import SubService, Service  # Предполагая, что у вас есть такая модель


class OrderSerializer(serializers.ModelSerializer):
    sub_service_id = serializers.PrimaryKeyRelatedField(
        queryset=SubService.objects.all(),
        source='sub_service',
        write_only=True
    )
    # Предполагаем, что у SubService есть поле 'service' для обратной связи
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source='sub_service.service',
        write_only=True,
        required=False  # Делаем необязательным, если service можно вывести из sub_service
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'service_id',  # Добавляем service_id в выводимые поля, если это необходимо
            'sub_service_id',
            'price',
            'date',
            'time',
            'address',
            'square_meters',
            'phone_number'
        ]
