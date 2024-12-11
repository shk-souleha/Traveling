from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        exclude=['booking_id','user','package','total_price','paid']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'leaving_date': forms.DateInput(attrs={'type': 'date'})
            }
