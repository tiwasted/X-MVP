from rest_framework import serializers

from ..models import Offer


class OfferServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'title', 'price']
        # fields = ['id', 'title', 'description', 'price', 'employer_id']
