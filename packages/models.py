from django.db import models
from autoslug import AutoSlugField



#Create your models here

class Category(models.Model):
    category_name=models.CharField(max_length=100,null=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)

    def __str__(self):
        return self.category_name

class Package(models.Model):
    package_name=models.CharField(max_length=100,null=False)
    package_destination=models.CharField(max_length=200)
    package_description=models.TextField(default="Package Description")
    package_price=models.PositiveIntegerField(default=0)
    package_image=models.ImageField(upload_to="packages/")
    # price_per_day=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    def __str__(self):
        return self.package_destination

class Place(models.Model):
    place_name=models.CharField(max_length=100,null=False)
    place_destination=models.CharField(max_length=200)
    place_description=models.TextField(default="Package Description")
    place_attraction=models.TextField(default="Attraction")
    place_image=models.ImageField(upload_to="packages/")
    package=models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.place_destination
    

