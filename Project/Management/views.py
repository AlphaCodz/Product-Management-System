from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def product(request):
    return render(request, "products.html")

def add_product(request):
    return render(request, "add-product.html")

def edit_product(request):
    return render(request, "edit_product.html")
