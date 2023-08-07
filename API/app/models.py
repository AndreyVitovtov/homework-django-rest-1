from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100, default="No name")
    last_name = models.CharField(max_length=100, default="No name")
    email = models.EmailField(unique=True, default="user@email.com")
    phone_number = models.CharField(max_length=15, default="00000")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class DeliveryCrew(models.Model):
    first_name = models.CharField(max_length=100, default="No name")
    last_name = models.CharField(max_length=100, default="No name")
    phone_number = models.CharField(max_length=15, default="00000")


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    shipping_address = models.CharField(max_length=200, default="No address")
    order_date = models.DateField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=2)
    is_paid = models.BooleanField(default=False)


class MenuItem(models.Model):
    name = models.CharField(max_length=100, default="No name")
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=2)
    category = models.CharField(max_length=50, default="No category")


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=timezone.now)
