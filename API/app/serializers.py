from rest_framework.serializers import ModelSerializer
from . import models


class SerializedCustomer(ModelSerializer):
    class Meta:
        model = models.Customer
        fields = "__all__"


class SerializedDeliveryCrew(ModelSerializer):
    class Meta:
        model = models.DeliveryCrew
        fields = "__all__"


class SerializedOrder(ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class SerializedMenuItem(ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = "__all__"


class SerializedCart(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = "__all__"
