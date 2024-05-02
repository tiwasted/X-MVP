# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth import get_user_model
#
# from ..serializers.employer_serializers import EmployerServiceSerializer
#
# User = get_user_model()
#
#
# class EmployerServiceCreator(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, *args, **kwargs):
#         # Проверка, является ли аутентифицированный пользователь работодателем
#         print("Текущая роль пользователя:", request.user.role)
#         if request.user.role != User.EMPLOYER:
#             return Response({"Ошибка": "Только работодатели могут создавать услуги."}, status=status.HTTP_403_FORBIDDEN)
#
#         employer = getattr(request.user, 'employer_profile', None)
#         if not employer:
#             return Response({"error": "Профиль Employer не найден."}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = EmployerServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(employer=employer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
