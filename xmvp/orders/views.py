from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)
