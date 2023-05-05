from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == "POST":
        print("Login User")
        return redirect("Management:index")
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        # get form values
        first_name = request.POST['firstname']
        middle_name = request.POST["middlename"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        # validate
        if password == password2:
            # check username
            return
        else:
            messages.error(request, 'Passwords do not match')
            return redirect("Management:register")
    else:
        return render(request, "register.html")
