from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


# API для создания работника
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Получаем работодателя, создающего нового сотрудника
        employer = self.request.user
        # Устанавливаем поле employer перед сохранением сотрудника
        serializer.save(employer=employer)


class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
