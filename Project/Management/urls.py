from django.urls import path, re_path
from . import views
from .views import ProductList, ProductDetail
from django.conf import settings
from django.conf.urls.static import static

app_name="Management"

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^products/$', ProductList.as_view(), name='products'), 
    re_path("add_product/", views.add_product, name="add_product"),
    re_path(r'^products/(?P<pk>[0-9]+)/\Z', ProductDetail.as_view(), name='product_details'),
    path("account", views.account, name="account"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
