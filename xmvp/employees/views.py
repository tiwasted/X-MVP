from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class EmployeeRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != User.EMPLOYER:
            return Response({"error": "Только Employer может создавать Employee."}, status=status.HTTP_403_FORBIDDEN)

        serializer = EmployeeRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
