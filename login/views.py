from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, authenticate, login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .forms import UserLoginForm, Password_resetform
from django.urls import reverse
from django.http import HttpResponseRedirect
from homepage.models import User_Detail, User_product
from django.contrib.auth import get_user_model
from django.forms import ValidationError


User=get_user_model()

def login_user(request): 
    form =   UserLoginForm(request.POST or None)
    nextt = request.GET.get('next')
    
    if form.is_valid():
       email=form.cleaned_data.get('email')
       password= form.cleaned_data.get('password')
       user=authenticate(request, username=email, password=password)
       login(request, user)
       if nextt:
           return redirect(nextt)
       return redirect("/")             
    context={"form":form}
    return render(request,'login.html',context)
  
def password_reset(request):
    form2 =  Password_resetform(request.POST or None)
        
    if form2.is_valid():
        email = form2.cleaned_data.get('email_address')
        password2 = form2.cleaned_data.get('confirm_password')
        
        user = User.objects.get(email=email)
        user.password = make_password(password2)
        user.save()
        return redirect("login") 
    
    context = {"form2":form2} 
    return render(request,'password.html',context)       

def logout_user(request):
    logout(request)
    return redirect('/login/')


# @receiver(user_logged_in)
# def is_online(sender, user, request,**kwargs):
#      my_user = User.objects.get(email = user)
#      if User_Detail.objects.filter(user=my_user).exists():
#          my_user =  User_Detail.objects.get(user=my_user)
#          my_user.online=True
#          my_user.save()
#          product = User_product.objects.filter(user=my_user)
#          for i in product:
#              i.online = True
#              i.save()
         
# @receiver(user_logged_out)
# def is_offline(sender, user, request,**kwargs):
    
#      my_user= User.objects.get(email = user)
#      if User_Detail.objects.filter(user=my_user).exists():
#          my_user =  User_Detail.objects.get(user=my_user)
#          my_user.online=False
#          my_user.save()
#          product = User_product.objects.filter(user=my_user)
#          for i in product:
#              i.online = False
#              i.save()

