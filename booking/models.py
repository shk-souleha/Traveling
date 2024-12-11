from django.db import models
from django.contrib.auth.models import User
from packages.models import Package

# Create your models here.
class Booking(models.Model):
    booking_id=models.CharField(primary_key=True,max_length=50)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    package=models.ForeignKey(Package,on_delete=models.PROTECT)
    booking_date=models.DateField(auto_now_add=True)
    number_of_people=models.PositiveIntegerField(null=False)
    arrival_date=models.DateField(null=False)
    leaving_date=models.DateField(null=False)
    phone_number=models.BigIntegerField(null=False)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    paid=models.BooleanField(default=False)

    def number_of_days(self):
        if self.arrival_date and self.leaving_date:
            return (self.leaving_date - self.arrival_date).days
        return 0  # Return 0 if dates are invalid

    def __str__(self):
        return f"{self.booking_id} {self.user.username} {self.package.package_name}"
