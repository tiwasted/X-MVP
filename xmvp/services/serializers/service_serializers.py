from rest_framework import serializers

from ..models import Service, Subservice


class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        fields = ['id', 'name']


class ServiceSerializer(serializers.ModelSerializer):
    subservices = SubserviceSerializer(many=True, required=False)
    class Meta:
        model = Service
        fields = ['id', 'name', 'subservices']

    def create(self, validated_data):
        subservices_data = validated_data.pop('subservices', [])
        service = Service.objects.create(**validated_data)
        for subservice_data in subservices_data:
            Subservice.objects.create(service=service, **subservice_data)
        return service
