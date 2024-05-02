from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.models import Order
from ..serializers.order_serializers import OrderProcessingSerializer


class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Получить все заказы со статусом "В обработке"
        orders_in_processing = Order.objects.filter(status='in processing')
        serializer = OrderProcessingSerializer(orders_in_processing, many=True)
        return Response(serializer.data)
