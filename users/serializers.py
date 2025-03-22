from rest_framework import serializers
from .models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payment."""

    class Meta:
        """Класс Мета для сериализатора вывода модели 'Payment'."""
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    payments = PaymentSerializer(many=True, read_only=True).data

    class Meta:
        """Класс Мета для сериализатора вывода модели 'User'."""
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined", "payments",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор детализации для модели User."""

    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        """Класс Мета для сериализатора вывода детализации модели 'User'."""
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined", "payments"
        ]
