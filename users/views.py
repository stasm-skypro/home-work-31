from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Класс для представления пользователей в API."""

    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """Класс для представления оплат в API."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Фильтрация, поиск и сортировка
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Фильтрация по конкретным полям
    filterset_fields = ["user", "course", "lesson", "payment_method"]

    # Поля, по которым можно выполнять поиск (по частичному совпадению)
    search_fields = ["user__email", "course__name", "lesson__name"]

    # Поля, по которым можно сортировать (`ordering=-date` для сортировки по убыванию)
    ordering_fields = ["date", "amount"]
