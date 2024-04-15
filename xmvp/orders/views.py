from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Order
from .serializers import OrderCreateSerializer, OrderUpdateSerializer
from .permissions import IsOrderProcessor


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderProcessView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [IsAuthenticated, IsOrderProcessor]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return super().get_queryset()
        return Order.objects.filter(employee=user)
