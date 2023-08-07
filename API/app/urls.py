from django.urls import path

from . import views

urlpatterns = [
    path("delivery-crew", views.delivery_crew),
    path("customer", views.customer),
    path("order", views.order),
    path("menu-item", views.menu_item),
    path("cart", views.cart),
]
