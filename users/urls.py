from users.apps import UsersConfig
from rest_framework import routers
from .views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name

routers = routers.DefaultRouter()
routers.register(r"user", UserViewSet, basename="user")
routers.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = routers.urls
