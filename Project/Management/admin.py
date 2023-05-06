from django.contrib import admin
from .models import PrimaryUser, Category, Product, Order
# Register your models here.

admin.site.register(PrimaryUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)