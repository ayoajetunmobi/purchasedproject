from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.core import serializers
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.urls import reverse
import json
from django.core.mail import send_mail
from .models import  User_Detail , User_product , Product_image ,  Customer_care, Searchdata , Contacted, Reviews
from django.contrib.auth import get_user_model
from .forms import (RegistrationForm , UserDetailForm) 
from pygments.formatters import img
from numpy import random
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from webpush import send_user_notification


from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator 


User=get_user_model()
page_num = 1

@require_GET
def index(request):
    context={}
    loged_in_user = request.user
    product = User_product.objects.filter(
                                          Q(searchTag__contains = "avila")      |
                                          Q(description__contains = "soap")     |
                                          Q(searchTag__contains = "box")        |
                                           Q(description__contains = "henna")   |
                                          Q(searchTag__contains = "henna" )     |
                                           Q(description__contains = "jalab")   |
                                        Q(searchTag__contains = "jalab" )       |
                                        Q(description__contains = "jog")        |
                                           Q(searchTag__contains = "cosmetic")  | 
                                            Q(searchTag__contains = "earring" ) |
                                        Q(description__contains = "earring")|
                                         Q(searchTag__contains = "bag" ) |
                                        Q(description__contains = "bag")  
                                           ).order_by("-id")[:18]
    
    picarray = []
    for i in product:
        picarray.append(Product_image.objects.filter(product=i)[0])
    context['product'] = product
    context['picture'] = picarray
    
    if loged_in_user.is_authenticated:
        user = User_Detail.objects.get(user=loged_in_user)
        user_pic = []
        user_product = User_product.objects.filter(user=user).order_by('-id')
        for i in user_product:
            user_pic.append(Product_image.objects.filter(product=i)[0])
            
        review = Reviews.objects.filter(user = user).order_by('-id')
        context['userProduct'] = user_product
        context['userProductPic'] = user_pic
        context['review'] = review
        context['userDetail'] = user

    return render(request,'practise.html', context)

def register(request):
    context={}
    form1 = RegistrationForm(request.POST or None)
    form2 = UserDetailForm(request.POST or request.FILES or None)
    
    context["form1"]=form1
    context["form2"]=form2
    Images = request.FILES.get('profileimages')
    img = str(Images)
    if img[-4:] == '.png' or img[-4:] == '.PNG' or img[-4:] == '.jpg' or img[-4:] == '.jpeg' or img[-4:] == '.JPG' or img[-4:] == '.JPEG':
        if form1.is_valid() and form2.is_valid() and Images:
            email = form1.save(commit=False)
            email.active = False
            email.save()
            profile = form2.save(commit=False)
            profile.user = email
            profile.profilepic = Images
            profile.save()
            
            
            uidb64   = urlsafe_base64_encode(force_bytes(email.pk))
            domain   = get_current_site(request).domain
            link     = reverse('activate',kwargs={'uidb64':uidb64, 'token':token_generator.make_token(email)})
            activate_url  = 'http://'+domain+link
            sub_ject = 'activate your account'
            message  = 'Hi '+profile.username + " " + \
                'click on the link below to activate your account\n' + activate_url
            send_mail(
                  sub_ject,
                  message,
                  'noreply@shopatpurchased.com',
                  [email.email,],
            )
            return HttpResponseRedirect('/login/')
    return render(request, 'register.html',context)

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
          id  = force_str(urlsafe_base64_decode(uidb64))
          user  = User.objects.get(pk=id)
          
          if user.is_active:
             return redirect('login')
          user.active = True
          user.save()
        except Exception as ex:
            pass
        return redirect('login')
   
def bagsPage(request):
    context={}
    
    productList = User_product.objects.filter( Q(description__contains = "bag") |
                                              Q(searchTag__contains = "bag") 
                                           ).order_by("-id")
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(description__contains = "wig")  |
                                              Q(searchTag__contains = "wig") 
                                           ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter( Q(description__contains = "bag") | 
                                          Q(searchTag__contains = "bag")    
                                        
                                           ).order_by("-id").order_by('id')[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request ,'bags.html', context)
           
def sneakers(request):
    context={}
    
    productList =  User_product.objects.filter( Q(description__contains = "sneak") | 
                                          Q(searchTag__contains = "sneak")     |
                                          Q(description__contains = "shoe") | 
                                          Q(searchTag__contains = "shoe")    
                                           ).order_by("-id")
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList 
    context['pictures'] = pictures 
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(searchTag__contains = "trouser")  |
                                              Q(description__contains = "trouser")  |
                                              Q(searchTag__contains = "trouser")  |
                                              Q(description__contains = "trouser")  
                                           ).order_by("-id")[:10]
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest =  User_product.objects.filter( Q(description__contains = "shoe") | 
                                          Q(searchTag__contains = "shoe")  )[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'sneakers.html',context)
                   
def jewelries(request):
    context={}
    
    productList =  User_product.objects.filter( 
                                          Q(description__contains = "necklace") | 
                                          Q(searchTag__contains = "necklace")  |
                                          Q(description__contains = "earrin") | 
                                          Q(searchTag__contains = "earrin")   |
                                           Q(description__contains = "chain") | 
                                          Q(searchTag__contains = "chain")  
                                           ).order_by("-id")
    
    pictures = []
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(searchTag__contains = "cloth")  |
                                              Q(description__contains = "palazzo")  |
                                              Q(searchTag__contains = "trouser")  |
                                              Q(description__contains = "trouser")  
                                           ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest =User_product.objects.filter( Q(description__contains = "chain") | 
                                          Q(searchTag__contains = "chain")    
                                           ).order_by("-id").order_by('id')[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'jewelries.html',context)
               
def gown(request):
    context={}
    productList = productList = User_product.objects.filter( 
                                              Q(description__contains = "gown") |
                                              Q(searchTag__contains = "gown") 
                                           ).order_by("-id")
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(searchTag__contains = "sneak")  |
                                              Q(description__contains = "sneak")  |
                                              Q(searchTag__contains = "shoe")  |
                                              Q(description__contains = "shoe")  
                                           ).order_by("-id")[:10]
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "gown") | 
                                          Q(searchTag__contains = "gown")   
                                       
                                           )[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'gown.html',context)
           
def ladies_outfit(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "ladie")   | 
                                          Q(searchTag__contains = "ladie")    |
                                          Q(description__contains = "wea")    | 
                                          Q(searchTag__contains = "wea")      
                                           )
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                             Q(searchTag__contains = "scarf")   |
                                             Q(description__contains = "scarf") |
                                             Q(searchTag__contains = "bag")   |
                                             Q(description__contains = "bag")
                                           ).order_by("-id")[:10]
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "henn") | 
                                          Q(searchTag__contains = "henn")   |
                                          Q(description__contains = "neck")   | 
                                          Q(searchTag__contains = "neck")      
                                           )[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'ladies.html',context)
                          
def bedsheet(request):
    context={}
    productList = User_product.objects.filter(
                                          Q(description__contains = "bed") | 
                                          Q(searchTag__contains = "bed")       
                                           ).order_by('-id')
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(searchTag__contains = "senator")  |
                                              Q(description__contains = "senator")  |
                                              Q(searchTag__contains = "zara")  |
                                              Q(description__contains = "zara")  
                                           ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "bed") | 
                                          Q(searchTag__contains = "bed")       
                                           ).order_by('id')[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest'] = suggest
    context['suggestPic'] = suggestPic
    
    return render(request,'bedsheet.html',context)
                                                    
def clothing(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "croc") | 
                                          Q(searchTag__contains = "croc")  |
                                          Q(description__contains = "shir") | 
                                          Q(searchTag__contains = "shir")   |
                                           Q(description__contains = "wea") | 
                                          Q(searchTag__contains = "wea") |
                                            Q(description__contains = "material") | 
                                          Q(searchTag__contains = "material")
                                           ).order_by('-id')
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(searchTag__contains = "sneak")  |
                                              Q(description__contains = "sneak")  |
                                              Q(searchTag__contains = "shoe")  |
                                              Q(description__contains = "shoe")  
                                           ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest =User_product.objects.filter(
                                          Q(description__contains = "trouser") | 
                                          Q(searchTag__contains = "trouser")   
                                           )[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'clothing.html',context)
  
def cookedfood(request):
    context={}
    
    productList = User_product.objects.filter( Q(description__contains = "beef")      | 
                                               Q(searchTag__contains = "food")        |
                                               Q(description__contains = "moi moi")   |
                                               Q(description__contains = "egg")         
                                           ).order_by("-id")
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
                                              Q(searchTag__contains = "corn")     |
                                              Q(description__contains = "paint")  |
                                              Q(searchTag__contains = "milk")   
                                           ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "food") | 
                                          Q(searchTag__contains = "food")  
                                           ).order_by('-id')[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'cookedfood.html',context)
  
def shoprandom(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "trouse") | 
                                          Q(searchTag__contains = "trouse")  |
                                          Q(description__contains = "ladi") | 
                                          Q(searchTag__contains = "ladi")   |
                                           Q(description__contains = "croc") | 
                                          Q(searchTag__contains = "croc")   |
                                           Q(description__contains = "dress") | 
                                          Q(searchTag__contains = "dress")    |
                                           Q(description__contains = "jala") | 
                                          Q(searchTag__contains = "jala")    
                                           ).order_by('-id')
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending = User_product.objects.all().order_by('-id')[95:105]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "neck") | 
                                          Q(searchTag__contains = "neck")  |
                                          Q(description__contains = "materia") | 
                                          Q(searchTag__contains = "materia")  
                                           ).order_by('-id')[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'shoprandom.html',context)
  
def food(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "food") | 
                                          Q(searchTag__contains = "food")  |
                                          Q(description__contains = "milk") | 
                                          Q(searchTag__contains = "milk")   |
                                           Q(description__contains = "corn") | 
                                          Q(searchTag__contains = "corn")   |
                                           Q(description__contains = "paint") | 
                                          Q(searchTag__contains = "paint")    
                                           ).order_by('-id')
    
    
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter( 
        Q(searchTag__contains = "food")  |
        Q(description__contains = "food")     
    ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
         Q(description__contains = "soup")  | 
         Q(searchTag__contains = "soup")).order_by('-id')[:10]
    
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'food.html',context)
                                                     
def fragrance(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "perfum") | 
                                          Q(searchTag__contains = "perfum")).order_by("-id")
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending = User_product.objects.filter( 
        Q(searchTag__contains = "chain")  |
        Q(description__contains = "chain")     
    ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "perfume") | 
                                          Q(searchTag__contains = "perfume")            
                                           ).order_by('-id')[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'fragrance.html',context)

def gadgets(request):
    context={}
    productList =User_product.objects.filter(
                                          Q(description__contains = "phone")  | 
                                          Q(searchTag__contains = "phone")    |
                                          Q(description__contains = "uk")     | 
                                          Q(searchTag__contains = "uk")       |
                                           Q(description__contains = "hp")    | 
                                          Q(searchTag__contains = "hp")       |
                                          Q(searchTag__contains = "bank")     
                                           ).order_by('-id')
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =User_product.objects.filter( 
        Q(description__contains = "hp")    | 
                                          Q(searchTag__contains = "hp")       |
                                           Q(description__contains = "bank")  | 
                                          Q(searchTag__contains = "bank")       
    ).order_by("-id")[:10]
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                          Q(description__contains = "crypt") | 
                                          Q(searchTag__contains = "crypt")  |
                                          Q(description__contains = "bit") | 
                                          Q(searchTag__contains = "bit")   
                                           )[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'gadgets.html',context)
                                                        
def graphics(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "graphic")
                                           ).order_by('-id')
    pictures = []
      
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter(
                Q(description__contains = "graphic")).order_by('-id')
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                         Q(description__contains = "uk") | 
                                          Q(searchTag__contains = "uk")  
                                           )[:10]
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'graphics.html',context)
                          
def postutme(request):
    context={}
    
    productList = User_product.objects.filter(
                                          Q(description__contains = "post")|
                                          Q(searchTag__contains = "utme")
                                           ).order_by('-id')
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter(
                                          Q(description__contains = "post")|
                                          Q(searchTag__contains = "utme")
                                           ).order_by('-id')
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                           Q(description__contains = "bank") | 
                                          Q(searchTag__contains = "bank")   |
                                          Q(description__contains = "phone") | 
                                          Q(searchTag__contains = "phone")
                                           )[:10]
        
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'postutme.html',context)
                          
def trousers(request):
    context={}
    
    productList =  User_product.objects.filter(
                                         Q(description__contains = "trouser") | 
                                          Q(searchTag__contains = "trouser")  |
                                           Q(description__contains = "jean")  | 
                                          Q(searchTag__contains = "jean")
                                          )
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter(
                                         Q(description__contains = "trouser") | 
                                          Q(searchTag__contains = "trouser")  |
                                           Q(description__contains = "jean")  | 
                                          Q(searchTag__contains = "jean") )    
        
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                         Q(description__contains = "jalab") |                                          Q(searchTag__contains = "jalab")   |
                                           Q(description__contains = "scarf") | 
                                          Q(searchTag__contains = "scarf")       
                                           )[:10]
        
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'trousers.html',context)
                                                  
def wig(request):
    context={}
    
    productList = User_product.objects.filter(searchTag = "wig")
    pictures = []
    
    for i in productList:
        pictures.append(Product_image.objects.filter(product=i)[0])
    context['products'] = productList
    context['pictures'] = pictures
    
    trendingPic = []
    trending =  User_product.objects.filter(
                                         Q(description__contains = "hair") | 
                                          Q(searchTag__contains = "hair")   |
                                         Q(description__contains = "wig") | 
                                          Q(searchTag__contains = "wig")  
                                           )[:10]
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    suggestPic = []
    suggest = User_product.objects.filter(
                                         Q(description__contains = "gown") | 
                                          Q(searchTag__contains = "gown")   |
                                         Q(description__contains = "suit") | 
                                          Q(searchTag__contains = "suit")   | 
                                          Q(description__contains = "bag") | 
                                          Q(searchTag__contains = "bag")     
                                           )[:10]
        
        
    for i in suggest:
      suggestPic.append(Product_image.objects.filter(product= i)[0])
      
    context['suggest']= suggest
    context['suggestPic']= suggestPic
    
    return render(request,'wig.html',context)
                                                                                             
def getting_post(request):
    context={}
    loged_in_user = request.user
    if  loged_in_user.is_authenticated:
            if request.method == 'POST':
                data = get_object_or_404(User_Detail,user=loged_in_user)
                price  = request.POST.get("price")
                categories   =  request.POST['categories']
                desc   = str(request.POST.get("desc1")).lower()
                Images = request.FILES.getlist('images')
                if len(Images)>0 :
                    product= User_product(user=data,price=price,description=str(desc),campus=data.campus,category =categories,searchTag =categories)
                    product.save()
                    for img in Images:
                        jim =str(img)
                        if jim[-4:] == '.png' or jim[-4:] == '.PNG' or jim[-4:] == '.jpg' or jim[-4:] == '.jpeg' or jim[-4:] == '.JPG' or jim[-4:] == '.JPEG':
                            fs= FileSystemStorage()
                            file_path= fs.save(img.name,img)
                            pimage = Product_image.objects.create(product=product, product_img=file_path)
    else:
        return  render(request,'postad.html',context)         
        
    return render(request,'postad.html',context)

def review(request):
    context={}
    user_pic=[]
    user2reviewID = int(request.POST.get("user2review"))
    productrec = User_product.objects.get(id= user2reviewID)
    user = productrec.user
    context["productrec"]=productrec
    context["user"]=user
    if user.user != request.user:
        if request.method == 'POST':
            if request.user.is_authenticated:
                getReview = request.POST.get("review")
                userReviewing = User_Detail.objects.get(user =request.user).username
                review = Reviews.objects.create(review = getReview, userReviewing = userReviewing, user = user)
                review.save()
    review = Reviews.objects.filter(user = user).order_by('-id')
    context["review"]=review
    user_product = User_product.objects.filter(user=user).order_by('-id')
    for i in user_product:
        user_pic.append(Product_image.objects.filter(product=i)[0])
    context['products'] = user_product
    context['userPic'] = user_pic
    return render(request,'profile.html',context)
         
def changedp(request):
    loged_in_user = request.user
    Images = request.FILES.getlist('imagesdp')[0]
    jim =str(Images)
    if jim[-4:] == '.png' or jim[-4:] == '.PNG' or jim[-4:] == '.jpg' or jim[-4:] == '.jpeg' or jim[-4:] == '.JPG' or jim[-4:] == '.JPEG':
        fs= FileSystemStorage()
        file_path= fs.save(Images.name,Images)
        user = User_Detail.objects.get(user=loged_in_user)
        user.profilepic = file_path
        user.save()
        return redirect('home')

def delete(request):
    context = {}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response = json.load(request)['post_data']
            response = response['target']
            idd = int(response)
            product = User_product.objects.get(id= idd)
            if product.user == User_Detail.objects.get(user=request.user):
                product.delete()
    return JsonResponse(context , safe=False)
       
def Prof_Update(request , id=id):
    context={}
    productrec = User_product.objects.get(id =id)
    products = User_product.objects.filter(user = productrec.user).order_by('-id')
    user = get_object_or_404(User_Detail,user=productrec.user.user)
    user_pic = []
    for i in products:
        user_pic.append(Product_image.objects.filter(product=i)[0])
            
    review = Reviews.objects.filter(user = user).order_by('-id')
    
    context['products'] = products
    context['user'] = user
    context['userPic']= user_pic
    context['review']= review
    context['productrec']= productrec
    
    return render(request,'profile.html',context)

def settingsfunctionality(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response = json.load(request)['post_data']
            sig = response['sig']
            target = response['target']
            target1 = response['target1']
            succmsg = "successful"
            succmsg2 = "not successful"
                            
            if target == "":
                context["data"] = succmsg2

            elif sig == 2:
                if target == target1:
                    data = User_Detail.objects.get(user = request.user)
                    user = data.user
                    user.password = make_password(target)
                    context['data'] = succmsg
                    user.save()
                else:
                     context['data'] = succmsg2
               
                      
            elif sig == 3:
                data = User_Detail.objects.get(user = request.user)
                data.about = str(target)
                context['data'] = succmsg
                data.save()
                   
            
            elif sig == 4:    
                data = User_Detail.objects.get(user = request.user)
                data.contact = int(target)
                data.save()
                context['data'] = succmsg
                    
            elif sig == 5:    
                data = User_Detail.objects.get(user = request.user)
                cus_care = Customer_care.objects.create(reportbug="",suggestionbox=str(target),deactivate_account='', reportuser= "", user = data)
                cus_care.save()
                context['data'] = succmsg
                
            elif sig == 6 and User_Detail.objects.filter(username = str(target)).exists():    
                data = User_Detail.objects.get(username = str(target))
                cus_care = Customer_care.objects.create(reportbug="", suggestionbox="", deactivate_account='', reportuser= str(target1), user = data)
                cus_care.save()
                context['data'] = succmsg

                
            elif sig == 9:    
                data = User_Detail.objects.get(user = request.user)
                cus_care = Customer_care.objects.create(reportbug="", suggestionbox="", deactivate_account=str(target), reportuser= "", user = data)
                cus_care.save()
                context['data'] = succmsg
                
            else:
                context['data'] = succmsg2
                      
    return JsonResponse(context,safe=False)

def search(request):
    context = {}
    searchdata = request.POST.get("searchinput")
    searchdata= str(searchdata)
    
    trendingPic = []
    trending =  User_product.objects.filter(
            Q(description__contains = searchdata) | 
            Q(searchTag__contains = searchdata))
    
    for i in trending:
        trendingPic.append(Product_image.objects.filter(product= i)[0])
            
    context['trending']= trending
    context['trendingPic']= trendingPic
        
    
    print(searchdata)
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     images = []
    #     response = json.load(request)['post_data'] 
    #     target = response['target']
    #     res = str(response['target2']).strip()
    #     response = str(response['target2']).lower()
    #     response = response.strip()
    #     if int(target) == 1:
    #         if User_Detail.objects.filter(username = res).exists():
    #             data = User_Detail.objects.get(username = res)
    #             data2 = User_product.objects.filter(user=data)[0]
    #             context["username"] =[str(data.username),str(data.profilepic),str(data2.id)]    
    #         elif User_product.objects.filter(Q(description__contains = response)|Q(searchTag__contains = response)).exists(): 
    #             data2 =  User_product.objects.filter(
    #             Q(description__contains = response) | Q(searchTag__contains = response)).order_by("-id")[:20]
    #             context["product"] = list((data2).values())
    #             for i in data2:
    #                 images.append(Product_image.objects.filter(product = i).values()[0])
    #                 context['images'] = list(images)
    #             context["yes"] = True 
    #             Searchdata.objects.create(word=response)
    #         else:
    #             context['noData'] =  str("No MATCH FOR SEARCH")     
                
    return render (request,'search.html',context)  

def Product_spec(request ,id = id):
        context={}
        product = get_object_or_404(User_product,id=id)
        pictures = Product_image.objects.filter(product=product)
        context['product']= product
        context['pictures']= pictures
        
        trendingPic = []
        trending = User_product.objects.all().order_by('-id')[:8]
        
        for i in trending:
             trendingPic.append(Product_image.objects.filter(product= i)[0])
            
        context['trending']= trending
        context['trendingPic']= trendingPic
        
        suggestPic = []
        suggest = User_product.objects.all().order_by('id')[:7]
        
        for i in suggest:
             suggestPic.append(Product_image.objects.filter(product= i)[0])
            
        context['suggest']= suggest
        context['suggestPic']= suggestPic
        
        
        return render(request,'products.html',context)          
