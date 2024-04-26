from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from orders.models import Order
from ..serializers.order_serializers import OrderListEmployer, OrderDetailEmployer, OrderProcessingSerializer


# Представление списка заказов
class OrderEmployerView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderListEmployer


# Представление полной информации заказа
class OrderEmployerDetailView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderDetailEmployer


# Представление обработки заказа от Работодателя
class OrderProcessingViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderProcessingSerializer(order)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        # Получаем идентификатор сотрудника из данных запроса
        assigned_employee_id = request.data.get('assigned_employee')

        if assigned_employee_id:
            # Проверяем, существует ли сотрудник с указанным идентификатором
            try:
                employee = Employee.objects.get(pk=assigned_employee_id)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

            # Назначаем сотрудника на заказ
            order.assigned_employee = employee

        serializer = OrderProcessingSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
