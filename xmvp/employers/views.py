from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import EmployerRegistrationSerializer
from .serializers import EmployerTokenObtainPairSerializer


class EmployerRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Работодатель успешно зарегистрирован"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployerTokenObtainPairSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)
