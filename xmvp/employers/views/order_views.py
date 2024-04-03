from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from orders.models import Order
from ..serializers.order_serializers import OrderEmployer
from ..serializers.order_serializers import OrderEmployerDetail


class OrderEmployerView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderEmployer


class OrderEmployerDetailView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderEmployerDetail
