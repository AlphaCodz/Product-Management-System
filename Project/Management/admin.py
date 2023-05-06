from django.contrib import admin
from .models import PrimaryUser, Category, Product
# Register your models here.

admin.site.register(PrimaryUser)
admin.site.register(Category)
admin.site.register(Product)
