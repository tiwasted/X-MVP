from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import EmployerRegistrationSerializer
from .serializers import EmployerAuthSerializer


class EmployerRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Работодатель успешно зарегистрирован"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerAuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = EmployerAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Теперь используем TokenObtainPairSerializer для генерации токена
        token_serializer = TokenObtainPairSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)

        return Response(token_serializer.validated_data, status=200)
