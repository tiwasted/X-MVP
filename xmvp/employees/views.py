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
        serializer.save(employer=self.request.user.employer_profile)
