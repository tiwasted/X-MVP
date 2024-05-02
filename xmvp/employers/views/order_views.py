from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone

from employees.models import Employee
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
    permission_classes = [IsAuthenticated]
    def update(self, request, order_id=None):
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Заказ не найден"}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status')
        new_service_date = request.data.get('service_date')
        new_service_time = request.data.get('service_time')
        new_assigned_employee_id = request.data.get('assigned_employee_id')

        if new_status:
            order.status = new_status
        if new_service_date:
            order.service_date = new_service_date
        if new_service_time:
            order.service_time = new_service_time
        if new_assigned_employee_id:
            try:
                assigned_employee = Employee.objects.get(pk=new_assigned_employee_id)
                order.assigned_employee = assigned_employee
            except Employee.DoesNotExist:
                return Response({"error": "Сотрудник не найден"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderProcessingSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save(created_at=timezone.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
