from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.service_serializers import ServiceSerializer
# from ..serializers.service_serializers import SubserviceSerializer
# from ..models import Service, Subservice


class ServiceCreateView(APIView):
    def post(self, requset):
        serializer = ServiceSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ServiceListView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, reguest):
#         services = Service.objects.all()
#         serializer = ServiceSerializer(services, many=True)
#         return Response(serializer.data)
#
#
# class SubserviceListView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, service_id):
#         subservices = Subservice.objects.filter(service_id=service_id)
#         serializer = SubserviceSerializer(subservices, many=True)
#         return Response(serializer.data)
