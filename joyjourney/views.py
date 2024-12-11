from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"index.html")

def user_login(request):
    if request.method=="GET":
        return render(request, "login.html")
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/packages")
        else:
            return render(request,"login.html",{"message":"Login Failed"})
    
    
            

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

def register(request):
    if request.method=="GET":
        form=CustomUserCreationForm()
        return render(request, "register.html", {"form":form})
    else:
        submittedform=CustomUserCreationForm(request.POST)
        if submittedform.is_valid():
            submittedform.save()
            return HttpResponseRedirect("/login")
        return render(request, "register.html",{"form":submittedform})
    

