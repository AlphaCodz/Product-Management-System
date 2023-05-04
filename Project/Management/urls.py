from django.urls import path, re_path
from . import views

app_name="Management"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product, name="products"),
    re_path("add_product/", views.add_product, name="add_product")
]
