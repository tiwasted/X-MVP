from rest_framework import serializers

from services.models import Offer


class EmployerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['title', 'subservice', 'price', 'description']