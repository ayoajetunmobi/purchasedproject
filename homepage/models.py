from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import django
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# import strip,replace


class UserManager(BaseUserManager):
    def create_user (self, email, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError ('user must have a mail')
        if not password:
            raise ValueError('user must insert password')
        user_obj = self.model(
            email= self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff  = is_staff
        user_obj.superuser = is_superuser
        user_obj.save(using=self.db)
        
    def  create_staffuser(self,email,password=None):
         user=self.create_user(email,password=password,is_staff=True)
         return user
        
    def  create_superuser (self, email, password=None):
        user=self.create_user(email,password=password,is_staff=True ,is_superuser=True)
        return user
        
        
class CustomUser(AbstractBaseUser):
    email              = models.EmailField(verbose_name="email", max_length=254 , unique=True)
    password           = models.CharField(max_length = 150)
    active             = models.BooleanField(default=True)
    staff              = models.BooleanField(default= False)
    superuser          = models.BooleanField(default=False)
   
    USERNAME_FIELD= 'email'
    REQUIRED_FIELD =[]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
        
    def get_username(self):
        return self.email
    
    
    def has_perm(self,perm ,obj=None):
        return True
        
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff
    
    @property   
    def is_superuser(self):
        return self.superuser
  
        
class User_Detail(models.Model):
    campus = (('ojo', 'OJO'),('epe', 'EPE'),('lasuth', 'LASUTH'),)
    gender = (('male', 'male'),('female', 'female'),)
    
    
    active            = models.BooleanField(default=False)
    username          = models.CharField(max_length = 150 ,blank=False ,unique=True)
    firstname         = models.CharField(max_length = 150 ,blank=False)
    lastname          = models.CharField(max_length = 150,blank=False)
    gender            = models.CharField(max_length = 50,choices=gender)
    contact           = models.CharField( max_length = 150, unique = True)
    about             = models.TextField( max_length =150)
    quote             = models.TextField(max_length = 500, blank=False, null=False)
    university        = models.CharField(max_length=100, default="LASU") 
    campus            = models.CharField(max_length=100, choices= campus) 
    profilepic        = models.ImageField(upload_to = 'profilepic', blank=True,null= True) 
    online            = models.BooleanField(default=False)
    user              = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        
    def __str__(self):
        return (self.username).replace(" ","")
    
    def save(self,*args, **kwargs):
        #open uploaded image
        img =  Image.open(self.profilepic)
        if img.height > 200 or img.width > 200:
            output_size = (100,100)
            
            img.thumbnail(output_size)
            
            
            img= img.convert('RGB')            
            output = BytesIO()
             
            img.save(output, format ='JPEG', optimize = True , quality = 20)
            output.seek(0)  
                  
            
            #change the imageField value to the newly modified image field value
            self.image = InMemoryUploadedFile(output,'ImageField',"%s.jpg"%self.profilepic.name.split(".")[0],
                                              'image/jpeg', sys.getsizeof(output),None)
      
            super(User_Detail,self).save(*args, **kwargs)
    
    
class User_product(models.Model):
    category = (('pef', 'PERFUME'),('lasureg', 'LASU REGISTRATIONS,FEES AND FORMS'),
       ('shoe', 'SHOE'),('sneak', 'SNEAKERS'),('trouser', 'TROUSER'),('electronics', 'ELECTRONICS'),
       ('shirt', 'SHIRT'),('bag', 'BAG'),('bedsheet', 'BEDSHEET'),('health', 'HEALTH'),
       ('wig', 'WIG'),('graphics', 'GRAPHICS'),('phones', ''), ('furniture', 'HOME | FURNITURE | APPLIANCES') , 
       ('laptop', 'LAPTOPS'),('engineer', 'ENGINEERING'),('property', 'HOUSE TO LET | HOUSE TO BUY'),('cosmetics', ' BEUTY | COSMETICS'), 
       ('meal', 'FAST MEALS'),('food', 'FOOD STUFF'),('gadgets', 'POWER BANK | CHARGER CORD | MUSIC BOX | EAR PIECE |  PS4'),('snack', 'SNACKS & PASTERIES'),('necklace', 'CUBBAN | JEWELRIES| EARRINGS | BRACELET | BEADS'), ('sport', ' SPORT | JERSY | FOOTBALL'),
       ('drinks', 'DRINKS'),  ('webapp', 'SOFTWARE ENGINEER'), ('cloth', 'FEMALE CLOTHING'), ('services', 'OFFER SERVICE'), ('gown', 'GOWN AND DRESS'),
      ('maleCLTH', 'MALE CLOTHING'),('repairs', 'PLUMBER | CARPENTER | ELECTRICIAN'),('others', 'OTHERS'),
                )
    
    id              = models.AutoField(primary_key=True)
    price           = models.IntegerField( blank=False,null=False)
    description     = models.TextField(max_length=150,blank=False,null=False) 
    searchTag       = models.CharField(max_length = 150, default="none")
    category        = models.CharField(max_length=100 , choices= category, default= "others")
    date_time       = models.DateField( default=django.utils.timezone.now)
    contact         = models.CharField(max_length=150, blank=True,null= True,default= "0902nite")
    campus            = models.CharField(max_length=100)
    user            = models.ForeignKey(User_Detail, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.description)
    
 
class Product_image(models.Model):
     id                = models.AutoField(primary_key=True)
     product           = models.ForeignKey(User_product, on_delete=models.CASCADE) 
     product_img       = models.ImageField(upload_to = "media") 
     
     def __str__(self):
        return str(self.product)
    
    
     def save(self,*args, **kwargs):
            #open uploaded image
        img =  Image.open(self.product_img)
        if img.height > 200 or img.width > 200:
            output_size = (100,100)
            
            img.thumbnail(output_size)
            
            
            img= img.convert('RGB')            
            output = BytesIO()
             
            img.save(output, format ='JPEG', optimize = True , quality = 20)
            output.seek(0)  
                  
            
            #change the imageField value to the newly modified image field value
            self.image = InMemoryUploadedFile(output,'ImageField',"%s.jpg"%self.product_img.name.split(".")[0],
                                              'image/jpeg', sys.getsizeof(output),None)
            
            
      
            super(Product_image,self).save(*args, **kwargs)
        
       
        
        #after modifications , save it to the output
        
    
class Searchdata(models.Model):
    word= models.CharField(max_length= 150,blank=True,null=True)
    def __str__(self):
        return self.word
    
    
class Customer_care(models.Model):
    reportbug =models.TextField(max_length = 150 ,blank=True,null=True)
    suggestionbox =models.TextField(max_length= 150,blank=True,null=True)
    deactivate_account =models.TextField(max_length= 150,blank=True,null=True)  
    # reportuser is what the user has done and user is the user who has been reported
    reportuser =models.TextField(max_length= 150,blank=True,null=True)
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE)
    

class Contacted(models.Model):
    username = models.CharField(max_length=100)#user contacted
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE)#user who made contact
    
    
class Reviews(models.Model):
    review = models.TextField(max_length=150, default= "no review yet")
    userReviewing = models.CharField(max_length=150, default= "no review yet")
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE)

    
##python manage.py migrate admin zero  for cosnstraint foreign key error involving admin logtable