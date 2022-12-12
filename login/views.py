from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, authenticate, login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .forms import UserLoginForm, Password_resetform
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import View
from django.http import HttpResponseRedirect
from homepage.models import User_Detail, User_product
from django.contrib.auth import get_user_model
from django.forms import ValidationError


from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator 


User=get_user_model()

def login_user(request): 
    form =   UserLoginForm(request.POST or None)
    nextt = request.GET.get('next')
    
    if form.is_valid():
       email = form.cleaned_data.get('email')
       password = form.cleaned_data.get('password')
       user = authenticate(request, username=email, password=password)
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
        password2 = form2.cleaned_data.get('password2')
        data_generate = str(str(email)+ " " + str(password2))
        user = User.objects.get(email=email)
        user = User_Detail.objects.get(user=user)
        uidb64   = urlsafe_base64_encode(force_bytes(data_generate))
        domain   = get_current_site(request).domain
        link     = reverse('activated',kwargs={'uidb64':uidb64, 'token':token_generator.make_token(email)})
        activate_url  = 'http://'+domain+link
        sub_ject = 'Reset your pasrd'
        message  = 'Hi '+ user.username + '  please click on link to reset your password' + \
            '' + activate_url
        send_mail(
                  sub_ject,
                  message,
                  'noreply@shopatpurchased.com',
                  [email,],
        )
    form2 =  Password_resetform()  
    context = {"form2":form2}
     
    return render(request,'password.html',context)       

class PassWordVerificationView(View):
    def get(self, request, uidb64, token):
      
          id  = force_str(urlsafe_base64_decode(uidb64)) 
          password = id.split(" ")[1:][0]
          email    = id.split(" ")[:1][0]
          user = User.objects.get(email=email)
          user.password = make_password(password)
          user.save()
          
          return redirect('login')

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

