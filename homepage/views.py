from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import json
from .models import  User_Detail , User_product , Product_image , Advertisment,Messages,Contacted, Reviews,Searchdata
from django.contrib.auth import get_user_model
from .forms import ( RegistrationForm, UserDetailForm, Customer_care_form ) 
from pygments.formatters import img
from numpy import random



User=get_user_model()
page_num = 1

def formsdispaly(request):
    context={}
    form1 = RegistrationForm(request.POST or None)
    form2 = UserDetailForm(request.POST or request.FILES or None)
    loged_in_user= request.user
    
    if loged_in_user.is_authenticated:
        review = Reviews.objects.all()
        user_details = User_Detail.objects.get(user=loged_in_user)
        products = User_product.objects.filter(campus = user_details.campus).order_by('-id')[:6]
        context['products']= products
        images=[]
        for i in products:
            if Product_image.objects.filter(product=i)[0] != None:
                image = Product_image.objects.filter(product=i)[0]
                images.append(image)
            else:
                i.delete()
        context['images']= images
        context["usersDetails"] = user_details
        
        if len(review)>0 and len(review) > 15:
            review[:8].delete()
    else:
        images =[]
        products = User_product.objects.all().order_by('-id')[:6]
        context['products']= products
        for i in products:
            if  Product_image.objects.filter(product=i)[0] != None:
                image = Product_image.objects.filter(product=i)[0]
                images.append(image)
            else:
                i.delete()
        context['images']= images

           
    if form1.is_valid() and form2.is_valid():
        code =  str(random.random())[14:]
        email= form1.save(commit=False)
        email.active = True
        email.save()
        Images = request.FILES.get('eproimages')
        profile= form2.save(commit=False)
        profile.user=email
        profile.profilepic = Images
        profile.save()
        
        user = User_Detail.objects.get(user=email)
        user.answer = code
        user.save()
        
        mesageUser = Messages.objects.create(message=('hi '+user.username+' !!! welcome to purchased start exploring our online market place by searching for your desired product or services' ) , my_messages = user)
        return HttpResponseRedirect('/login/') 
       
       
    context["product"]=products
    context["form1"]=form1
    context["form2"]=form2
    
    
    return render(request,'purchased.html', context)
            
            
def getting_post(request):
    loged_in_user = request.user
    data= get_object_or_404(User_Detail,user=loged_in_user)
    price  = request.POST.get("price")
    searchTag   = str(request.POST.get("desc")).lower()
    desc   = str(request.POST.get("desc1")).lower()
    Images = request.FILES.getlist('images')
    if len(Images)>0 :
         product= User_product(user=data,price=price,description=str(desc),campus=data.campus, matricverified=data.matricverified, topuser=data.topuser, searchTag =searchTag, profile_pic=data.profilepic, username = data.username)
         product.save()
         for img in Images:
            fs= FileSystemStorage()
            file_path= fs.save(img.name,img)
            pimage = Product_image.objects.create(product=product, product_img=file_path)
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
     
     
def Prof_Update(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response = json.load(request)['post_data']
                
            user = User_Detail.objects.get(id=response['target'])
        

            context['profileupdate']= True
            context['userdetail'] = {
                "firstname":user.firstname,"lastname": user.lastname,"username":user.username,"about":user.about,
                "gender":user.gender,"matricverified":user.matricverified, "topuser":user.topuser,
                "online":user.online , "propic":str(user.profilepic),"contact":user.contact
            }
            
            if User_product.objects.filter(user=user).exists(): 
                imagefill=[]               
                data1  = User_product.objects.filter(user=user).order_by('-id')
                context['data1']= list(User_product.objects.filter(user=user).order_by('-id').values())
                for i in data1:
                    imagefill.append(Product_image.objects.filter(product = i).values()[0])
                    context['images'] = list(imagefill)
            else:
                context['images'] = [{"product_img":""}] 
                context['data1']  =  [{"searchTag":"no product yet"}] 
                
                  
            if Advertisment.objects.filter(id=1).exists(): 
               id_advert= random.randint(2,4)
               picture = Advertisment.objects.get(id=id_advert)
               context['advert'] = str(picture.picture)
            else:
                 context['advert'] = str("")
                 
                 
            if Reviews.objects.filter(user=user).exists(): 
                context['reviews']= list(Reviews.objects.filter(user=user).order_by('-id').values())
            else:
                context['reviews']= [{"review":"no reviews yet","username":"no reviews yet","as_buyer":"no reviews yet"}]
 
    return JsonResponse(context , safe=False)

def get_profile(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                
            user = User_Detail.objects.get(user = request.user)
            
            context['userdetail'] = {
                "firstname":user.firstname,"lastname": user.lastname,"username":user.username,"about":user.about,
                "gender":user.gender,"matricverified":user.matricverified, "topuser":user.topuser,
                "online":user.online , "propic":str(user.profilepic), "contact":user.contact
            }
            
            if User_product.objects.filter(user=user).exists(): 
                imagefill=[]               
                data1  = User_product.objects.filter(user=user).order_by('-id')
                context['data1']= list(User_product.objects.filter(user=user).order_by('-id').values())
                for i in data1:
                    imagefill.append(Product_image.objects.filter(product = i).values()[0])
                    context['images'] = list(imagefill)
            else:
                context['images'] = [{"product_img":""}] 
                context['data1']  =  [{"searchTag":"no product yet"}] 
                
                  
            if Advertisment.objects.filter(id=1).exists(): 
               id_advert=random.randint(2,4)
               picture = Advertisment.objects.get(id=id_advert)
               context['advert'] = str(picture.picture)
            else:
                 context['advert'] = str("")
                 
                 
            if Reviews.objects.filter(user=user).exists(): 
                context['reviews']= list(Reviews.objects.filter(user=user).order_by('-id').values())
            else:
                context['reviews']= [{"review":"no reviews yet","username":"no reviews yet","as_buyer":"no reviews yet"}]
    return JsonResponse(context , safe=False)

def pagination_page(request):
    context={}
    picture=[]
    
    global page_num
    
    listt= User_product.objects.all().order_by("-id")
    
    page = request.GET.get('page', page_num)
    
    paginator = Paginator(listt, 4)
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
        
    for i in users.object_list:
        picture.append(list((Product_image.objects.filter(product=i.id)).values())[0])
    
    if users.has_next() == True:
        page_num = users.next_page_number()
        context["pictures"] = picture
        context["data"]= list((users.object_list).values())
        
    if users.has_next() == False:
       context["pictures"] = picture
       context["data"]= list((users.object_list).values())
       page_num = 1
       
    return JsonResponse( context, safe=False)

def search(request):
    context = {}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            images = []
            response = json.load(request)['post_data'] 
            response = str(response['target']).lower()
            user = User_Detail.objects.get(user= request.user)
                      
            if User_Detail.objects.filter(username = response).exists():
                data = User_Detail.objects.get(username = response)
                context["username"] =[str(data.username),str(data.profilepic),str(data.id)]    
            elif User_product.objects.filter(Q(description__contains = response)|Q(searchTag__contains = response) & Q(campus__contains = user.campus)).exists():
                data2 =  User_product.objects.filter(
                    Q(description__contains = response) | Q(searchTag__contains = response) & Q(campus__contains = user.campus)
                )[:20]
                for i in data2:
                    images.append(Product_image.objects.filter(product = i).values()[0])
                    context['images'] = list(images)
                context["product"] = list((data2).values())
                context["yes"] = True
               
            else:
                context['noData']=  str("No MATCH FOR SEARCH")
                
            Searchdata.objects.create(word=response,timesSearched =0,user=user)
    return JsonResponse(context , safe=False)


def Product_spec(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response = json.load(request)['post_data']
            response = response['data']
         # this part gets the product id and displays other pictures and full product description
            data1  = User_product.objects.get(id=response)
            context['data1'] = {
                "price":data1.price, "description":data1.description,"searchTag":data1.searchTag, 
                "propic":str(data1.profile_pic), "username":data1.username, "online":data1.online, "id":data1.user_id
            }
            imagefill = list(Product_image.objects.filter(product = data1).values())
            context['images'] = imagefill

            userContact = data1.user.contact
            context['contact'] = str(userContact)
                                     
            
            # suggested products
         
            Simagefill = []               
            Sproduct  = User_product.objects.all().order_by('-id')[:5]
            context['Sproduct'] = list(User_product.objects.all().order_by('-id').values())[:5]
            for i in Sproduct:
                Simagefill.append(Product_image.objects.filter(product = i).values()[0])
                context['Simages'] = list(Simagefill)
                
            context['userthatwascontacted'] = str(data1.user.username)
             

    return JsonResponse(context , safe=False)          
            
def whencontacted(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response = json.load(request)['post_data']
            response = response['seler']
                 
            seler = User_Detail.objects.get(username=response)
            buyer = User_Detail.objects.get(user = request.user)
            if str(buyer.username) == str(seler.username):
                 return JsonResponse(context , safe=False)
            else:     
                  #message to person who contacted/buyer
                      Messages.objects.create(message = "Hi "+buyer.username+" you contacted "+seler.username+" please leave a review on that user after business meeting",
                                   user_to_review= seler.username, my_messages = buyer) 
            
                 #  Message to person contacted/seler
                      Messages.objects.create(message = "Hi "+seler.username+" your contact was requested by "+buyer.username+" please leave a review on that user after business meeting",
                         contacted = True, user_to_review= buyer.username, my_messages = seler)
            
                      Contacted.objects.create(username = seler.username, user =buyer)
                           
    return JsonResponse(context , safe=False)
    
def msgDisplay(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                
            user = User_Detail.objects.get(user = request.user)
            if Messages.objects.filter(my_messages = user).exists:
                message= list( Messages.objects.filter(my_messages =user).values())
                context['message'] = message
    return JsonResponse(context , safe=False)   


def Signals(request):
    context={}
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response = json.load(request)['post_data']
            response1= response['target']
            response2= response['contacted']
            response3= response['user_review']
            response4= response['reviewdata']
            response5= response['msgid']
            response5 = int(response5)
            
            if Messages.objects.filter(id = response5).exists:
                if str(response2) == 'true':
                    response2 = False
                else:
                     response2 = True  
            
                if int(response1) == 2:
                       Messages.objects.get(id =response5).delete()
                       userwhoreviewed = User_Detail.objects.get(user = request.user);
                       userreviewed = User_Detail.objects.get(username = response3);
                       Reviews.objects.create(review =response4, as_buyer =  response2, username = userwhoreviewed.username, user= userreviewed )
           
               
                 
           
                           
    return JsonResponse(context , safe=False)