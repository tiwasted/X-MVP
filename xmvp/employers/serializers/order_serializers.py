from rest_framework import serializers
from orders.models import Order


class OrderEmployer(serializers.ModelSerializer):
    offer_title = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'address', 'service_date', 'service_time', 'offer_title']

    def get_offer_title(self, obj):
        return obj.offer.title if obj.offer else None


class OrderEmployerDetail(serializers.ModelSerializer):
    service_name = serializers.CharField(source='offer.subservice.service.name', read_only=True)
    subservice_name = serializers.CharField(source='offer.subservice.name', read_only=True)
    offer_title = serializers.CharField(source='offer.title', read_only=True)
    offer_price = serializers.IntegerField(source='offer.price', read_only=True)

    class Meta:
        model = Order
        fields = [
            'offer_title',
            'service_name',
            'subservice_name',
            'offer_price',
            'service_date',
            'service_time',
            'address',
            'square_meters',
            'status'
        ]
