from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def product(request):
    return render(request, "products.html")

def add_product(request):
    return render(request, "add-product.html")

def edit_product(request):
    return render(request, "edit-product.html")

def account(request):
    return render(request, "accounts.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")
