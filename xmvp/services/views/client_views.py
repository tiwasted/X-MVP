from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.client_serializers import OfferServiceSerializer
from ..serializers.client_serializers import OfferServiceDetailSerializer

from ..models import Offer


class OfferListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, subservice_id):
        offers = Offer.objects.filter(subservice_id=subservice_id)
        serializer = OfferServiceSerializer(offers, many=True)
        return Response(serializer.data)


class OfferDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, offer_id):
        try:
            offer_detail = Offer.objects.get(id=offer_id)
            serializer = OfferServiceDetailSerializer(offer_detail)
            return Response(serializer.data)
        except Offer.DoesNotExist:
            return Response({'Ошибка': 'Предложение не найдено'}, status=status.HTTP_404_NOT_FOUND)
