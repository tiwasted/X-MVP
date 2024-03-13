from rest_framework import serializers
from rest_framework.generics import ListAPIView

from .models import Service, SubService


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ['sub_service_name', 'price', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    subservices = SubServiceSerializer(many=True, required=False)

    class Meta:
        model = Service
        fields = ['service_name', 'subservices']

    def create(self, validated_data):
        subservices_data = validated_data.pop('subservices', None)
        service = Service.objects.create(**validated_data)
        if subservices_data:
            for subservice_data in subservices_data:
                SubService.objects.create(service=service, **subservice_data)
        return service


# Чтение услуг по выпадающему списку
class ServiceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name']


class SubServiceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ['id', 'sub_service_name']
