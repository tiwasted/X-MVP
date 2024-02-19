from rest_framework import serializers
from .models import Service, SubService


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ['name', 'price', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    subservices = SubServiceSerializer(many=True, required=False)

    class Meta:
        model = Service
        fields = ['name', 'subservices']

    def create(self, validated_data):
        subservices_data = validated_data.pop('subservices', [])
        service = Service.objects.create(**validated_data)
        for subservice_data in subservices_data:
            SubService.objects.create(service=service, **subservice_data)
        return service
