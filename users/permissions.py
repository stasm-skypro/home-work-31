from rest_framework.permissions import BasePermission

class IsModerator(BasePermission):
    """Проверяет зарегистрирован ли пользователь и входит ли он в группу 'Модераторы'"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Модераторы").exists()
        )


class DenyAll(BasePermission):
    """Полностью запрещает доступ"""
    def has_permission(self, request, view):
        return False
