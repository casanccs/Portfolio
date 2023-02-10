from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(productPhoto)
admin.site.register(productReview)
admin.site.register(Order)