# from rest_framework import permissions
#
#
# class IsEmployee(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'employee'
#
#
# class IsEmployer(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'employer'
