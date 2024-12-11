from django.urls import path
from . import views

urlpatterns = [
    path('booknow/<int:packageId>/',views.booknow,name="booknow"),
    path('payment/<str:booking_id>/',views.payment,name="payment"),
    path('success/<str:booking_id>/',views.paymentSuccess,name="success")
]
