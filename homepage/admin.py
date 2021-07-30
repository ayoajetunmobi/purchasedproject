from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import  User_Detail , User_product , Product_image ,  Customer_care , Advertisment, Messages , Searchdata , Contacted, Reviews

User = get_user_model()
# adding a search box in the admin field
""" class UserAdmin(admin.ModelAdmin):
   search_fields= ['email']
   class Meta:
       model=User
admin.site.register(User,UserAdmin) """


   
admin.site.register(User)
admin.site.register(User_Detail)
admin.site.register( User_product)
admin.site.register(Product_image)
admin.site.register(Customer_care)
admin.site.register(Advertisment)
admin.site.register(Searchdata)
admin.site.register(Messages)
admin.site.register(Contacted)
admin.site.register(Reviews)

