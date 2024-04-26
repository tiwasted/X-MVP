from rest_framework import serializers
from employees.models import Employee
from orders.models import Order


# Сериализатор который отображает список заказов от Клиента
class OrderListEmployer(serializers.ModelSerializer):
    offer_title = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'address', 'service_date', 'service_time', 'offer_title']

    def get_offer_title(self, obj):
        return obj.offer.title if obj.offer else None


# Сериализатор который отображает полную информацию заказа от Клиента
class OrderDetailEmployer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='offer.subservice.service.name', read_only=True)
    subservice_name = serializers.CharField(source='offer.subservice.name', read_only=True)
    offer_title = serializers.CharField(source='offer.title', read_only=True)
    offer_price = serializers.IntegerField(source='offer.price', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


# Сериализатор обработки заказа для Работодателя (работодатель может изменить время, дату и назначить свободного сотрудника)
class OrderProcessingSerializer(serializers.ModelSerializer):
    assigned_employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=False)

    class Meta:
        model = Order
        fields = ['id', 'service_date', 'service_time', 'assigned_employee']
