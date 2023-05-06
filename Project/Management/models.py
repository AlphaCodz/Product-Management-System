from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User

# Create your models here.
class PrimaryUser(User):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    gender = models.CharField(max_length=6, choices=GENDER, null=True)
    
    def __str__(self):
        return self.first_name
    
class Category(models.Model):
    CATEGORY = (
        ("New Arrival", "New Arrival"),
        ("Most Popular", "Most Popular"),
        ("Trending", "Trending")
    )
    name = models.CharField(max_length=200, choices=CATEGORY)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    units_in_stock=models.IntegerField()
    units_sold = models.IntegerField(null=True)
    image = models.ImageField(upload_to="media/product_images")
    
    def __str__(self):
        return self.name
    
    
    