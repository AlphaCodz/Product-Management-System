from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
from .models import PrimaryUser, Product, Category, Order
from django.views.generic import ListView, DetailView
from datetime import timedelta, datetime

# Create your views here.
def index(request):
    user = request.user
    # Get the datetime for 2 hours ago
    two_hrs_ago = datetime.now() - timedelta(hours=2)
    # Get List of Products
    new_products = Product.objects.filter(created_at__gte=two_hrs_ago)
    # Get all orders
    orders = Order.objects.all()
    # Get new orders
    new_orders = Order.objects.filter(created_at__gte=two_hrs_ago)
    context = {
        "user":user,
        "orders":orders,
        "new_products": new_products,
        "new_orders": new_orders
    }
    return render(request, "index.html", context)

class ProductList(ListView):
    model = Product
    template_name= 'product_list.html'
    context_object_name = "products"
    
    def get_category(self, *args, **kwargs):
        categories = Category.objects.all()
        return categories
    
    def post(self, request, *args, **kwargs):
        # Get the list of IDs of selected items to delete
        selected_items = request.POST.getlist('selected_items')
        
        if selected_items:
            Product.objects.filter(id__in=selected_items).delete()
        return redirect('Management:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_category() 
        return context
    
class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = "product"

def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        category_id = request.POST.get("category")
        unit_sold = request.POST["units_sold"]
        # make category instance
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, "Category does not exist")
            return redirect("Management:add_product")
        
        expire_date = request.POST["expire_date"]
        
        try:
            expire_date_str = datetime.strptime(expire_date, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid Expiry Date. Please use YYYY-MM-DD.")
            return redirect("Management:add_product")
        
        units_in_stock = request.POST["units_in_stock"]
        product_image = request.FILES["product_image"]
        
        product = Product.objects.create(name=name, 
                                        description=description,
                                        category=category,
                                        expiry_date=expire_date_str,
                                        units_in_stock=units_in_stock,
                                        image=product_image,
                                        units_sold=unit_sold
                                        )
        product.save()
        messages.success(request, "Product Added Successfully")
        return redirect("Management:products")
    
    # GET PRODUCT CATEGORY
        # get all categories
    category = Category.objects.all()
    context = {
        "category":category
    }
    
    return render(request, "add-product.html", context)


def account(request):
    user = request.user
    context = {
        "user":user
    }
    return render(request, "accounts.html", context)

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = PrimaryUser.objects.filter(email=email).first()
        if not user:
            messages.error(request, "Invalid Email")
            return redirect("Management:login")
        # check_password
        if not check_password(password, user.password):
            messages.error(request, "Invalid Password")
            return redirect("Management:login")
        
        # login user
        auth.login(request, user)
        print("Login Successful")
        messages.success(request, "Logged in successfully")
        return redirect("Management:index")
    return render(request, "login.html")
            
        

def register(request):
    if request.method == "POST":
        # get form values
        first_name = request.POST['firstname']
        # middle_name = request.POST["middlename"]
        username=request.POST["username"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        phone_no = request.POST["phone_no"]
        profile_img = request.FILES["image"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        
        # validate
        if password == password2:
            # check username
            if PrimaryUser.objects.filter(username=username).exists():
                messages.error(request, "Sorry that username is taken")
                return redirect("Management:register")
            else:
                if PrimaryUser.objects.filter(email=email).exists():
                    messages.error(request, "Sorry that email is being used")
                    return redirect("Management:register")
                else:
                    user = PrimaryUser.objects.create(username=username,
                                                      email=email, 
                                                      first_name=first_name, 
                                                      last_name=last_name,
                                                      phone_no=phone_no,
                                                      image=profile_img)
                                                      
                    user.set_password(raw_password=password)
                    # login user directly
                    # auth.login(request, user)
                    # messages.success(request, "Registration Successful")
                    # return redirect("/")
                    user.save()
                    messages.success(request, "Registration Successful")
                    return redirect("Management:login")
        else:
            messages.error(request, 'Passwords do not match')
            return redirect("Management:register")
    else:
        return render(request, "register.html")
