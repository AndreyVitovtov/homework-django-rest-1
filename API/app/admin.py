from django.contrib import admin

from .models import Customer, DeliveryCrew, Order, MenuItem, Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(DeliveryCrew)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Cart)
