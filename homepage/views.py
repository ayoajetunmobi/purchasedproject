from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.core import serializers
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import json
from django.core.mail import send_mail
from .models import   User_Detail , User_product , Product_image ,  Customer_care, Searchdata , Contacted, Reviews
from django.contrib.auth import get_user_model
from .forms import (RegistrationForm, UserDetailForm) 
from pygments.formatters import img
from numpy import random
from django.views.decorators.csrf import csrf_exempt



User=get_user_model()
page_num = 1

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
            
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     contextual={}
        
    #     productlist = []
    #     productlistImg = []
     
     
    #     product =User_product.objects.filter(
    #             Q(description__contains = "sho") |
    #             Q(searchTag__contains = "sho" )  |
    #                  Q(description__contains = "jog")   |
    #                  Q(description__contains = "dlg") |
    #                   Q(searchTag__contains = "wea" ) 
    #             ).order_by("-id")
    #     for i in product:
    #         productlistImg.append(Product_image.objects.filter(product=i).values()[0])
            
    #     product2 =User_product.objects.filter(
    #             Q(description__contains = "henna") |
    #             Q(searchTag__contains = "henna" ) |
    #             Q(description__contains = "jalab") |
    #             Q(searchTag__contains = "jalab" ) 
    #             ).order_by("-id")
    #     for i in product2:
    #         productlistImg.append(Product_image.objects.filter(product=i).values()[0])
        
    
    #     contextual['products']= list((product).values())
    #     contextual['products2']= list((product2).values())
    #     contextual['productlistImg']= list(productlistImg)
         
    #     return JsonResponse(contextual, safe=False)

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
            email= form1.save(commit=False)
            email.active = True
            email.save()
            profile= form2.save(commit=False)
            profile.user=email
            profile.profilepic = Images
            profile.save()
            
            return HttpResponseRedirect('/login/')
    return render(request, 'register.html',context)
   
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
                    for img in Images:
                        jim =str(img)
                        if jim[-4:] == '.png' or jim[-4:] == '.PNG' or jim[-4:] == '.jpg' or jim[-4:] == '.jpeg' or jim[-4:] == '.JPG' or jim[-4:] == '.JPEG':
                            product= User_product(user=data,price=price,description=str(desc),campus=data.campus,category =categories,searchTag =categories)
                            product.save()
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
    
    # if request.user.is_authenticated:
    #     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #         response = json.load(request)['post_data']
    
    #         user = User_Detail.objects.get(id=response['target'])

    #         context['profileupdate']= True
    #         context['userdetail'] = {
    #             "username":user.username,"about":user.about,
    #             "gender":user.gender,"matricverified":user.matricverified, "topuser":user.topuser,
    #             "online":user.online , "propic":str(user.profilepic),"contact":user.contact
    #         }
            
    #         if User_product.objects.filter(user=user).exists(): 
    #             imagefill=[]           
    #             data1  = User_product.objects.filter(user=user).order_by('-id')
    #             context['data1']= list(User_product.objects.filter(user=user).order_by('-id').values())
    #             for i in data1:
    #                 imagefill.append(Product_image.objects.filter(product = i).values()[0])
    #                 context['images'] = list(imagefill)
    #         else:
    #             context['images'] = [{"product_img":""}] 
    #             context['data1']  =  [{"searchTag":"no product yet"}] 
                
                 
    #         if Reviews.objects.filter(user=user).exists(): 
    #             context['reviews']= list(Reviews.objects.filter(user=user).order_by('-id').values())
    #         else:
    #             context['reviews']= [{"review":"no reviews yet","username":"no reviews yet","as_buyer":"no reviews yet"}]
 

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
# def get_profile(request):
#     context={}
    # if request.user.is_authenticated:
    #     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                
    #         user = User_Detail.objects.get(user = request.user)
            
    #         context['userdetail'] = {
    #           "username":user.username,"about":user.about,
    #             "gender":user.gender,"matricverified":user.matricverified, "topuser":user.topuser,
    #             "online":user.online , "propic":str(user.profilepic), "contact":user.contact
    #         }
            
    #         if User_product.objects.filter(user=user).exists(): 
    #             imagefill = [] 
                
    #             data1  = User_product.objects.filter(user=user).order_by('-id')
    #             context['data1'] = list(User_product.objects.filter(user=user).order_by('-id').values())
                
    #             for i in data1:
    #                 imagefill.append(Product_image.objects.filter(product = i).values()[0])
    #                 context['images'] = list(imagefill)

    #         else:
    #             context['images'] = [{"product_img":""}] 
    #             context['data1']  =  [{"description":"no product yet"}] 
                  
    #         if Reviews.objects.filter(user=user).exists(): 
    #             context['reviews']= list(Reviews.objects.filter(user=user).order_by('-id').values())
    #         else:
    #             context['reviews']= [{"review":"no reviews yet","username":"no reviews yet","as_buyer":"no reviews yet"}]
    # return JsonResponse(context , safe=False)

# def pagination_page(request):
#     context={}
#     picture=[]
    
#     global page_num
    
#     listt= User_product.objects.all().order_by("-id")
    
#     page = request.GET.get('page', page_num)
    
#     paginator = Paginator(listt, 4)
    
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
        
#     for i in users.object_list:
#         picture.append(list((Product_image.objects.filter(product=i.id)).values())[0])
    
#     if users.has_next() == True:
#         page_num = users.next_page_number()
#         context["pictures"] = picture
#         context["data"]= list((users.object_list).values())
        
#     if users.has_next() == False:
#        context["pictures"] = picture
#        context["data"]= list((users.object_list).values())
#        page_num = 1
       
#     return JsonResponse( context, safe=False)

@csrf_exempt 
def search(request):
    context = {}
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        images = []
        response = json.load(request)['post_data'] 
        target = response['target']
        res = str(response['target2']).strip()
        response = str(response['target2']).lower()
        response = response.strip()
        if int(target) == 1:
            if User_Detail.objects.filter(username = res).exists():
                data = User_Detail.objects.get(username = res)
                data2 = User_product.objects.filter(user=data)[0]
                context["username"] =[str(data.username),str(data.profilepic),str(data2.id)]    
            elif User_product.objects.filter(Q(description__contains = response)|Q(searchTag__contains = response)).exists(): 
                data2 =  User_product.objects.filter(
                Q(description__contains = response) | Q(searchTag__contains = response)).order_by("-id")[:20]
                context["product"] = list((data2).values())
                for i in data2:
                    images.append(Product_image.objects.filter(product = i).values()[0])
                    context['images'] = list(images)
                context["yes"] = True 
                Searchdata.objects.create(word=response)
            else:
                context['noData'] =  str("No MATCH FOR SEARCH")     
                     
            # if int(target) == 2:
            #     if request.user.is_authenticated:
            #         user = User_Detail.objects.get(user= request.user)
            #         data2 =  User_product.objects.filter(
            #         Q(description__contains = 'shoe') | Q(description__contains = 'bag') | Q(description__contains = 'wear') | Q(searchTag__contains = 'wear') | Q(description__contains = 'sneaker')  | Q(searchTag__contains = 'material') | Q(description__contains = 'cloth')
            #         | Q(description__contains = 'dress') | Q(searchTag__contains = 'jewel') | Q(description__contains = 'wig') | Q(description__contains = 'suit')  | Q(description__contains = 'women')  | Q(searchTag__contains = 'ladies') & Q(campus__contains = user.campus)
            #         ).order_by("-id")[:20]
            #         context["product"] = list((data2).values())
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["yes"] = True 
            #         Searchdata.objects.create(word=response,timesSearched =0,user=user)
            #     else:
            #         data2 =  User_product.objects.filter(
            #         Q(description__contains = 'shoes') | Q(description__contains = 'bag') | Q(searchTag__contains = 'wear') | Q(description__contains = 'sneaker') | Q(description__contains = 'material') | Q(description__contains = 'cloth')
            #         | Q(description__contains = 'dress') | Q(searchTag__contains = 'jewel') | Q(description__contains = 'wig') | Q(description__contains = 'suit')  | Q(description__contains = 'ladies')
            #         ).order_by("-id")[:20]
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["product"] = list((data2).values())
            #         context["yes"] = True
                    
            # if int(target) == 3:
            #     if request.user.is_authenticated:
            #         user = User_Detail.objects.get(user = request.user)
            #         data2 =  User_product.objects.filter(
            #         Q(description__contains = 'food') | Q(searchTag__contains = 'rice') | Q(description__contains = 'asun') | Q(searchTag__contains = 'ofada') | Q(searchTag__contains = 'spag')
            #         | Q(searchTag__contains = 'food') | Q(searchTag__contains = 'soup') | Q(description__contains = 'turkey') & Q(campus__contains = user.campus)
            #          ).order_by("-id")[:20]
            #         context["product"] = list((data2).values())
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["yes"] = True 
            #         Searchdata.objects.create(word=response,timesSearched =0, user=user)
            #     else:
            #         data2 =  User_product.objects.filter(
            #         Q(description__contains = 'food') | Q(searchTag__contains = 'rice') | Q(description__contains = 'asun') | Q(searchTag__contains = 'ofada') | Q(searchTag__contains = 'spag') 
            #         | Q(searchTag__contains = 'food') | Q(searchTag__contains = 'soup') | Q(description__contains = 'turkey')
            #          ).order_by("-id")[:20]
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["product"] = list((data2).values())
            #         context["yes"] = True
                    
                    
            # if int(target) == 4:
            #     if request.user.is_authenticated:
            #         user = User_Detail.objects.get(user= request.user)
            #         data2 =  User_product.objects.filter(
            #          Q(searchTag__contains = 'milk') | Q(searchTag__contains = 'flake') | Q(searchTag__contains = 'morn')
            #         | Q(description__contains = 'cereals')  & Q(campus__contains = user.campus)
            #         ).order_by("-id")[:20]
            #         context["product"] = list((data2).values())
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #             context["yes"] = True 
            #         Searchdata.objects.create(word=response,timesSearched =0,user=user)
            #     else:
            #         data2 =  User_product.objects.filter(
            #         Q(searchTag__contains = 'milk') | Q(searchTag__contains = 'flakes') | Q(searchTag__contains = 'morn')
            #         | Q(description__contains = 'cereals') 
            #         ).order_by("-id")[:20]
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["product"] = list((data2).values())
            #         context["yes"] = True
                    
            # if int(target) == 5:
            #     if request.user.is_authenticated:
            #         user = User_Detail.objects.get(user= request.user)
            #         data2 =  User_product.objects.filter(
            #         Q(description__contains = 'phone') | Q(searchTag__contains = 'laptop') | Q(description__contains = 'gadget') & Q(campus__contains = user.campus)
            #         ).order_by("-id")[:20]
            #         context["product"] = list((data2).values())
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["yes"] = True 
            #         Searchdata.objects.create(word=response,timesSearched =0,user=user)
            #     else:
            #         data2 =  User_product.objects.filter(
            #             Q(description__contains = 'phone') | Q(searchTag__contains = 'laptop') | Q(description__contains = 'gadget') 
            #         ).order_by("-id")[:20]
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["product"] = list((data2).values())
            #         context["yes"] = True
                    
            # if int(target) == 6:
            #     if request.user.is_authenticated:
            #         user = User_Detail.objects.get(user= request.user)
            #         data2 =  User_product.objects.filter(
            #         Q(description__contains = 'graphic') |  Q(searchTag__contains = 'graphic') & Q(campus__contains = user.campus)
            #         ).order_by("-id")[:20]
            #         context["product"] = list((data2).values())
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["yes"] = True 
            #         Searchdata.objects.create(word=response,timesSearched =0,user=user)
            #     else:
            #         data2 =  User_product.objects.filter(
            #          Q(description__contains = 'graphics') |  Q(searchTag__contains = 'graphic')
            #         ).order_by("-id")[:20]
            #         for i in data2:
            #             images.append(Product_image.objects.filter(product = i).values()[0])
            #             context['images'] = list(images)
            #         context["product"] = list((data2).values())
            #         context["yes"] = True
                
            return JsonResponse(context , safe=False)

def Product_spec(request ,id = id):
        context={}
        # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        #     response = json.load(request)['post_data']
        #     response = response['data']
        #  # this part gets the product id and displays other pictures and full product description
        #     data1  = User_product.objects.get(id=response)
        #     context['data1'] = {
        #         "price":data1.price, "description":data1.description,"searchTag":data1.searchTag, 
        #         "propic":str(data1.profile_pic), "username":data1.username, "online":data1.online, "id":data1.user_id
        #     }
        #     imagefill = list(Product_image.objects.filter(product = data1).values())
        #     context['images'] = imagefill

        #     userContact = data1.user.contact
        #     context['contact'] = str(userContact)
                                     
            
        #     # suggested products
         
        #     Simagefill = []               
        #     Sproduct  = User_product.objects.all().order_by('-id')[:5]
        #     context['Sproduct'] = list(User_product.objects.all().order_by('-id').values())[:5]
        #     for i in Sproduct:
        #         Simagefill.append(Product_image.objects.filter(product = i).values()[0])
        #         context['Simages'] = list(Simagefill)
                
        #     context['userthatwascontacted'] = str(data1.user.username)
             
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
            
# def whencontacted(request):
#     context={}
#     if request.user.is_authenticated:
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             response = json.load(request)['post_data']
#             response = response['seler']
                 
#             seler = User_Detail.objects.get(username=response)
#             buyer = User_Detail.objects.get(user = request.user)
#             if str(buyer.username) == str(seler.username):
#                  return JsonResponse(context , safe=False)
#             else:     
#                   #message to person who contacted/buyer
#                       Messages.objects.create(message = "Hi "+buyer.username+" you contacted "+seler.username+" please leave a review on that user after business meeting",
#                                    user_to_review= seler.username, my_messages = buyer) 
            
#                  #  Message to person contacted/seler
#                       Messages.objects.create(message = "Hi "+seler.username+" your contact was requested by "+buyer.username+" please leave a review on that user after business meeting",
#                          contacted = True, user_to_review= buyer.username, my_messages = seler)
            
#                       Contacted.objects.create(username = seler.username, user =buyer)
                           
#     return JsonResponse(context , safe=False)
 

# def msgDisplay(request):
#     context={}
#     if request.user.is_authenticated:
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                
#             user = User_Detail.objects.get(user = request.user)
#             if Messages.objects.filter(my_messages = user).exists:
#                 message = list( Messages.objects.filter(my_messages =user).order_by('-id').values())
                
#                 context['message'] = message
#     return JsonResponse(context , safe=False)   



# def suggestproduct(request):
#     context={}
#     products = User_product.objects.all()[30:40]
#     suggestions  = []
#     suggestions1 = User_product.objects.filter(Q(searchTag__contains = 'food') | Q(description__contains = 'rice')).order_by("-id")[:1]
#     suggestions2 = User_product.objects.filter(Q(searchTag__contains = 'laptop') | Q(description__contains = 'laptop') | Q(description__contains = 'phone')).order_by("-id")[:1]
#     suggestions3 = User_product.objects.filter(Q(searchTag__contains = 'wear') | Q(description__contains = 'wear')).order_by("-id")[:1]
#     suggestions4 =  User_product.objects.filter(Q(searchTag__contains = 'hp') | Q(description__contains = 'games')).order_by("-id")[:1]
    
#     suggestions = [suggestions1,suggestions2,suggestions3,suggestions4]
#     suggestionImg = []
#     for i in suggestions:
#         suggestionImg.append(Product_image.objects.filter(product = i).values()[0])
        
        
#     productsrotateImg =[]
#     for i in products:
#          productsrotateImg.append(Product_image.objects.filter(product = i).values()[0])
         
#     context['products'] =  list(User_product.objects.all().values()[30:40])
#     context['productsrotateImg'] = list(productsrotateImg)
        
#     context['suggestion1'] = list((suggestions1).values())
#     context['suggestion2'] = list((suggestions2).values())
#     context['suggestion3'] = list((suggestions3).values())
#     context['suggestion4'] = list((suggestions4).values())
        
#     context['suggestionImg'] = list(suggestionImg)
    
#     return JsonResponse(context , safe=False)

