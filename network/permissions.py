from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Разрешение, которое позволяет доступ только активным сотрудникам.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован и является активным
        return request.user.is_authenticated and request.user.is_active
