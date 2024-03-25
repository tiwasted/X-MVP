from rest_framework import serializers

from ..models import Offer


class OfferServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'title', 'price']


class OfferServiceDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'price', 'company_name']

    def get_company_name(self, obj):
        return obj.employer.company_name
