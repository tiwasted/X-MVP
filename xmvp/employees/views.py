from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeTokenObtainPairSerializer

# from accounts.permissions import IsEmployee


# API для создания работника
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user.employer_profile)


class EmployeeTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployeeTokenObtainPairSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)
