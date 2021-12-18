from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


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
    username          = models.CharField(max_length = 255 ,blank=False ,unique=True)
    firstname         = models.CharField(max_length = 150 ,blank=False)
    lastname          = models.CharField(max_length = 150,blank=False)
    gender            = models.CharField(max_length = 50,choices=gender)
    contact           = models.CharField( max_length = 255, unique = True)
    about             = models.CharField( max_length =500)
    quote             = models.CharField(max_length = 500, blank=False, null=False)
    university        = models.CharField(max_length=100, default="LASU") 
    campus            = models.CharField(max_length=100, choices= campus) 
    matricNo          = models.CharField(max_length=100,blank=True,null=True) 
    profilepic        = models.ImageField(upload_to = 'profilepic', blank=True,null= True) 
    securityQusetion  = models.CharField(max_length=100, blank=True, null=True)
    answer            = models.CharField(max_length=100, blank=True, null=True)
    matricverified    = models.BooleanField(default=False)
    topuser           = models.BooleanField(default=False)
    online            = models.BooleanField(default=False)
    user              = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    
    def save(self,*args, **kwargs):
        #open uploaded image
        img =  Image.open(self.profilepic)
        if img.height > 400 or img.width > 400:
            output_size = (150,150)
            
            img.thumbnail(output_size)
            
            
            img= img.convert('RGB')            
            output = BytesIO()
             
            img.save(output, format ='JPEG', optimize = True , quality = 70)
            output.seek(0)  
                  
            
            #change the imageField value to the newly modified image field value
            self.image = InMemoryUploadedFile(output,'ImageField',"%s.jpg"%self.profilepic.name.split(".")[0],
                                              'image/jpeg', sys.getsizeof(output),None)
      
            super(User_Detail,self).save(*args, **kwargs)
    
    
class User_product(models.Model):
    id              = models.AutoField(primary_key=True)
    price           = models.IntegerField( blank=False,null=False)
    description     = models.CharField(max_length=4000,blank=False,null=False) 
    searchTag       = models.CharField(max_length=30,blank=False,null=False)
    profile_pic     = models.ImageField(upload_to='profilepic' ,blank=True)
    date_time       = models.DateField( default=timezone.now())
    username        = models.CharField(max_length=255)
    campus            = models.CharField(max_length=100)
    online          = models.BooleanField(default=False)
    matricverified    = models.BooleanField(default=False)
    topuser           = models.BooleanField(default=False)
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
        if img.height > 400 or img.width > 400:
            output_size = (150,150)
            
            img.thumbnail(output_size)
            
            
            img= img.convert('RGB')            
            output = BytesIO()
             
            img.save(output, format ='JPEG', optimize = True , quality = 70)
            output.seek(0)  
                  
            
            #change the imageField value to the newly modified image field value
            self.image = InMemoryUploadedFile(output,'ImageField',"%s.jpg"%self.product_img.name.split(".")[0],
                                              'image/jpeg', sys.getsizeof(output),None)
            
            
      
            super(Product_image,self).save(*args, **kwargs)
        
       
        
        #after modifications , save it to the output
        
    
class Messages(models.Model):
    message= models.CharField(max_length= 1000,blank=True,null=True)
    read =models.BooleanField(default=False)
    contacted =models.BooleanField(default=False)# would be sent to review table
    user_to_review = models.CharField(max_length= 100,blank=True,null=True)# would be sent to review table too
    my_messages = models.ForeignKey(User_Detail,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message
    
   
class Searchdata(models.Model):
    word= models.CharField(max_length= 1000,blank=True,null=True)
    timesSearched = models.IntegerField()
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE) 
    def __str__(self):
        return self.word
    
    
class Customer_care(models.Model):
    reportbug = models.CharField(max_length = 600 ,blank=True,null=True)
    suggestionbox = models.CharField(max_length= 600,blank=True,null=True)
    deactivate_account = models.CharField(max_length= 700,blank=True,null=True)  
    # reportuser is what the user has done and user is the user who has been reported
    reportuser = models.CharField(max_length= 700,blank=True,null=True)
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE)
    

class Contacted(models.Model):
    username = models.CharField(max_length=100)#user contacted
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE)#user who made contact
    
class Reviews(models.Model):
    review = models.CharField(max_length=500)
    as_buyer = models.BooleanField(default=False) #if contacted == True then user is seller
    username = models.CharField(max_length=100) #request.user
    user = models.ForeignKey(User_Detail,on_delete=models.CASCADE)# user to be reviewed gotten from msg table
    
##python manage.py migrate admin zero  for cosnstraint foreign key error involving admin logtable