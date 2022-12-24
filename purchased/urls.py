"""purchased URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from homepage.models import  User_Detail , User_product , Product_image ,  Customer_care , Searchdata , Contacted, Reviews
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdminSite(name='OTPAdmin')
admin_site.register(User)
admin_site.register(User_Detail)
admin_site.register( User_product)
admin_site.register(Product_image)
admin_site.register(Customer_care)
admin_site.register(Searchdata)
admin_site.register(Contacted)
admin_site.register(Reviews)

admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    path('',include('homepage.urls')),
    path('post-product/', admin_site.urls), 
    path('login/',include('login.urls')),
    path('blog/',include('blog.urls')),
    path('tinymce/', include('tinymce.urls')) 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)