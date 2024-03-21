from rest_framework import serializers

from ..models import Service
from ..models import Subservice


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']


class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        fields = ['id', 'service', 'name']
