from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import models
from . import serializers


# Create your views here.
@api_view(["GET", "POST", "PUT", "DELETE"])
def delivery_crew(request):
    delivery_crew = models.DeliveryCrew.objects.all()
    serialized_delivery_crew = serializers.SerializedDeliveryCrew(delivery_crew, many=True)
    data = serialized_delivery_crew.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT", "DELETE"])
def customer(request):
    customer = models.Customer.objects.all()
    serialized_customer = serializers.SerializedCustomer(customer, many=True)
    data = serialized_customer.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT", "DELETE"])
def order(request):
    order = models.Order.objects.all()
    serialized_order = serializers.SerializedOrder(order, many=True)
    data = serialized_order.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT", "DELETE"])
def menu_item(request):
    menu_item = models.MenuItem.objects.all()
    serialized_menu_item = serializers.SerializedMenuItem(menu_item, many=True)
    data = serialized_menu_item.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT", "DELETE"])
def cart(request):
    cart = models.Cart.objects.all()
    serialized_cart = serializers.SerializedCart(cart, many=True)
    data = serialized_cart.data
    return Response(data, status=status.HTTP_200_OK)
