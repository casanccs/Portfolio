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
    wishlist = models.ManyToManyField('Product', related_name="wishlist", blank=True)
    cart = models.ManyToManyField('Product', related_name="cart", blank=True)

    def __str__(self):
        return f"{self.user.username}"


class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=40)
    desc = models.TextField(max_length=500)
    picture = models.ImageField(blank=True)
    unlisted = models.BooleanField(default=False)
    nReviews = models.IntegerField(default=0)
    averageScore = models.DecimalField(default=0, decimal_places=2, max_digits=40)

    #reviews
    #photos

    def __str__(self):
        return f"{self.seller.user.username}: {self.title}"

class productInCart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    totalCost = models.DecimalField(decimal_places=2, max_digits = 40, default=0)


class productPhoto(models.Model):
    photo = models.ImageField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

class productReview(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.CharField(max_length=500)
    score = models.IntegerField(blank=True) #Must validate this to be between 0-5


class Order(models.Model):
    buyer = models.ForeignKey("Profile", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #so seller can be referenced with other info
    status = models.CharField(
         max_length = 50, default="Waiting for payment confirmation",
         choices=[
            ("Waiting for payment confirmation","Waiting for payment confirmation"),("Shipping","Shipping"), ("On Delivery","On Delivery"), ("Delivered","Delivered"), ("Problem with Transit","Problem with Transit")
         ]
        )
    deliverer = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name="deliverer")
    date_placed = models.DateField(auto_now=True)
    date_delivered = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    totalCost = models.DecimalField(decimal_places=2, max_digits = 40, default=0)
    priority = models.IntegerField(default=0, blank=True, null=True)