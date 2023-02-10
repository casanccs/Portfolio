from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    phone = models.CharField(max_length=13, blank=True) # Validation
    address = models.CharField(max_length=40) # Validation
    type = models.CharField(
         max_length = 20, default="Customer",
         choices=[
            ("Customer", "Customer"), ("Vendor", "Vendor"), ("Transit", "Transit")
         ]
        )
    orders = models.ManyToManyField('Order', blank=True)
    wishlist = models.ManyToManyField('Product', related_name="wishlist", blank=True)
    cart = models.ManyToManyField('Product', related_name="cart", blank=True)


class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=40)
    desc = models.TextField(max_length=500)
    #reviews
    #photos


class productPhoto(models.Model):
    photo = models.ImageField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class productReview(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    desc = models.CharField(max_length=500)
    score = models.IntegerField(blank=True) #Must validate this to be between 0-5


class Order(models.Model):
    #buyer is referenced from Profile class
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #so seller can be referenced with other info
    status = models.CharField(
         max_length = 20, default="Problem With Transit",
         choices=[
            ("Shipping","Shipping"), ("On Delivery","On Delivery"), ("Delivered","Delivered"), ("Probelm with Transit","Probelm with Transit")
         ]
        )
    date_placed = models.DateField(auto_now=True)
    date_delivered = models.DateField(blank=True, null=True)