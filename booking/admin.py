from django.contrib import admin
from .models import Booking 

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display=['booking_id','user','package','number_of_people','arrival_date','leaving_date','phone_number','total_price']
admin.site.register(Booking,BookingAdmin)