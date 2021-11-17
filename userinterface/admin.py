from django.contrib import admin
from .models import Product, Orders, OrderUpdates

# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdates)
# admin.site.register(Category)
