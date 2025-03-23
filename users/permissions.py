from rest_framework.permissions import BasePermission

class IsModeratorOrReadOnly(BasePermission):
    """Разрешение для модераторов (только просмотр и изменение)."""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:  # Разрешаем просмотр всем
            return True
        return request.user.groups.filter(name="Модераторы").exists() and request.method in ["PUT", "PATCH"]
