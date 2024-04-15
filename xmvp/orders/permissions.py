from rest_framework import permissions


class IsOrderProcessor(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки, моогут ли Компании и сотрудники обрабатывать заказы
    """

    def has_permission(self, request, view):
        # Проверяем, имеет ли пользователь нужную роль
        return request.user.is_authenticated and (request.user.role == 'employer' or request.user.role == 'employee')