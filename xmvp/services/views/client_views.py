from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.client_serializers import OfferServiceSerializer

from ..models import Offer


class OfferListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, subservice_id):
        offers = Offer.objects.filter(subservice_id=subservice_id)
        serializer = OfferServiceSerializer(offers, many=True)
        return Response(serializer.data)
