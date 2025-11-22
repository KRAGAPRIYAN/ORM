from django.db import models

from django.contrib import admin
class Product(models.Model):
    ProductID=models.CharField(primary_key=True,max_length=7)
    Name=models.CharField(max_length=30)
    SellerID=models.CharField(max_length=7)
    Price=models.FloatField()
    WarrantyMonths=models.IntegerField()
    Ratings=models.FloatField()
    DeliveryDate=models.DateField()

class ProductAdmin(admin.ModelAdmin):
    list_display=["ProductID","Name","SellerID","Price","WarrantyMonths","Ratings","DeliveryDate"]
    