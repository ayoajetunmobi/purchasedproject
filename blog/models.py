from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from tinymce.models import HTMLField 
import django
import sys


class Post(models.Model):
    id              = models.AutoField(primary_key=True)
    title           = models.CharField(max_length=100)
    overview        = models.CharField(max_length=500)
    content         = HTMLField ()
    dateupdated     = models.DateField( default=django.utils.timezone.now)
    
    
    def __str__(self):
        return (self.title)
    
class Post_Pic(models.Model):
     id                = models.AutoField(primary_key=True)
     post              = models.ForeignKey(Post, on_delete=models.CASCADE) 
     blogImg           = models.ImageField(upload_to = "media") 
     
     def __str__(self):
        return str(self.post)
    
    
     def save(self,*args, **kwargs):
            #open uploaded image
        img =  Image.open(self.blogImg)
        if img.height > 200 or img.width > 200:
            output_size = (100,100)
            
            img.thumbnail(output_size)
            
            
            img= img.convert('RGB')            
            output = BytesIO()
             
            img.save(output, format ='JPEG', optimize = True , quality = 20)
            output.seek(0)  
                  
            
            #change the imageField value to the newly modified image field value
            self.image = InMemoryUploadedFile(output,'ImageField',"%s.jpg"%self.blogImg.name.split(".")[0],
                                              'image/jpeg', sys.getsizeof(output),None)
            
            
      
            super(Post_Pic,self).save(*args, **kwargs)

        
        