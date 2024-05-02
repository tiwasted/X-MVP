from rest_framework import permissions
from rest_framework.permissions import BasePermission


# class IsOrderProcessor(permissions.BasePermission):
#     """
#     Пользовательское разрешение для проверки, моогут ли Компании и сотрудники обрабатывать заказы
#     """
#
#     def has_permission(self, request, view):
#         # Проверяем, имеет ли пользователь нужную роль
#         return request.user.is_authenticated and (request.user.role == 'employer' or request.user.role == 'employee')


class IsManagerReadOnly(BasePermission):
    """
    Разрешение для проверки того, имеет ли пользователь право на редактирование заказа от клиента
    """

    def has_permission(self, request, view):
        # Разрешение только для менеджеров
        return request.user.is_manager

    def has_object_permission(self, request, view, obj):
        # Разрешение только для менеджеров и только для методов PATCH и PUT
        if request.method in ['PATCH', 'PUT']:
            return request.user.is_manager
        return True
