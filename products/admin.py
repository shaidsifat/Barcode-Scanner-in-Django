from django.contrib import admin
from .models import Product, ProductDetails
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductDetails)