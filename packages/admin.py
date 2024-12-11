from django.contrib import admin
from .models import Package,Place,Category
# from .models import Booking

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display=['id','package_name','package_destination','package_description','package_price','package_image']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']

class PlaceAdmin(admin.ModelAdmin):
    list_display=['id','place_name','place_destination','place_description','place_attraction','place_image','package','category']

# admin.site.register(Booking)
    

admin.site.register(Place,PlaceAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Category,CategoryAdmin)