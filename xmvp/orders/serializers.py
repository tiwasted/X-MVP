from rest_framework import serializers
from .models import Order, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description']


# Сериализатор создания заказа от Клиента
class OrderCreateSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'offer', 'address', 'square_meters', 'service_date', 'service_time', 'tasks']
        read_only_fields = ('id',)

    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks')
        order = Order.objects.create(**validated_data, user=self.context['request'].user)
        for task_data in tasks_data:
            Task.objects.create(order=order, **task_data)
        return order


# Сериализатор обработки заказа для Работодателя



class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status', 'employee']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['approved_time', 'assigned_employee']
