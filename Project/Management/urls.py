from django.urls import path, re_path
from . import views

app_name="Management"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product, name="products"),
    re_path("add_product/", views.add_product, name="add_product"),
    re_path("edit_product/", views.edit_product, name="edit_product"),
    path("account", views.account, name="account"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register")
]
