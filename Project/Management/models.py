from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    