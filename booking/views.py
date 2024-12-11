from django.shortcuts import render,HttpResponseRedirect
from .forms import BookingForm
from .models import Booking
import uuid
from packages.models import Package
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from joyjourney.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def booknow(request,packageId):
    if request.method=='GET':
        form=BookingForm()
        return render(request, "booknow.html", {"form":form})
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            booking=Booking.objects.create(booking_id=uuid.uuid4().hex,
                                   user=request.user,
                                   package=Package.objects.get(id=packageId),
                                #    booking_date=form.cleaned_data["booking_date"],
                                   number_of_people=form.cleaned_data["number_of_people"],
                                   arrival_date=form.cleaned_data["arrival_date"],
                                   leaving_date=form.cleaned_data["leaving_date"],
                                   phone_number=form.cleaned_data["phone_number"],
                                   total_price=Package.objects.get(id=packageId).package_price*form.cleaned_data["number_of_people"]
        
                                   )
            return HttpResponseRedirect("/packages/booking/payment/"+str(booking.booking_id))

def payment(request,booking_id):
    booking=Booking.objects.get(booking_id=booking_id)
    client=razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3","LVkt6Cs9VskcAarHG1ryJNdr"))
    data = { "amount": int(booking.total_price*100), "currency": "INR", "receipt": booking_id }
    payment = client.order.create(data=data)
    return render(request, "payment.html",{"payment":payment,"booking":booking})

@csrf_exempt
def paymentSuccess(request,booking_id):
    razorpay_response={
        "razorpay_payment_id":request.POST.get("razorpay_payment_id"),
        "razorpay_order_id":request.POST.get("razorpay_order_id"),
        "razorpay_signature":request.POST.get("razorpay_signature")

    }
    client=razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3","LVkt6Cs9VskcAarHG1ryJNdr"))
    payment_check=client.utility.verify_payment_signature(razorpay_response)
    if payment_check:
        booking=Booking.objects.get(booking_id=booking_id)
        booking.paid=True
        booking.save()
        send_mail(f"[{Booking.booking_id} placed]",
                  "Booking Done SuccessFully...",
                  EMAIL_HOST_USER,
                  ["soulehashaikh39@gmail.com"],
                  fail_silently=False)

    return render(request, "success.html",{"booking":booking})