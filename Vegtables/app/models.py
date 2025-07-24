from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import uuid

# class Register(models.MOdel):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.models.CharField(unique=True, max_length=50)


class Post(models.Model):
    name = models.CharField(max_length=60)
    content = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    MFD = models.DateField()


    def __str__(self):
        return self.name





class CustomerOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    total_amount = models.FloatField(default=0)

    def __str__(self):
        return self.customer_name

class VegetableItem(models.Model):
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='vegetables')
    veg_name = models.CharField(max_length=100)
    veg_price = models.FloatField()
    veg_kg = models.FloatField()
    amount = models.FloatField()

    def save(self, *args, **kwargs):
        self.amount = self.veg_price * self.veg_kg
        super().save(*args, **kwargs)
    

class Dash(models.Model):
    Cus_name = models.CharField(max_length=100, null=True)
    Number = models.CharField(max_length=15)
    Address = models.CharField(max_length=100)
    def __str__(self):
        return self.Cus_name




