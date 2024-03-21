from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.service_serializers import ServiceSerializer
from ..serializers.service_serializers import SubserviceSerializer
from ..models import Service, Subservice


class ServiceListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reguest):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class SubserviceListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, service_id):
        subservices = Subservice.objects.filter(service_id=service_id)
        serializer = SubserviceSerializer(subservices, many=True)
        return Response(serializer.data)
