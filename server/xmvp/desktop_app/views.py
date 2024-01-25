from django.shortcuts import render
from django.http import HttpResponse

from .models import Employer
from .serializers import EmployerSerializer
from .serializers import EmployerLoginSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions


from django.contrib.auth import authenticate


def index(request):
    return HttpResponse("Главная страница")


def company(request):
    return HttpResponse("Страница для Компаний")


class EmployerAPIView(generics.ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmployerSerializer


class EmployerTokenRefreshView(TokenRefreshView):
    pass


class EmployerLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = EmployerLoginSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            password = serializer.validated_data['password']
            employer = authenticate(request, login=login, password=password)
            if employer is not None:
                refresh = RefreshToken.for_user(employer)
                return Response({
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
