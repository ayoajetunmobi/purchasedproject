from django import forms 
from django.contrib.auth import authenticate
from homepage.models import User_Detail
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User= get_user_model()
class UserLoginForm (forms.Form):
    email= forms.EmailField( label= "EMAIL" ,widget=forms.TextInput(attrs={  
        "placeholder":"Enter email" , "class":"inputs"
    }))
    password= forms.CharField( label= "PASSWORD" ,widget = forms.PasswordInput(
        attrs={
          "placeholder":"Enter password" ,"class":"inputs"
        }
    ))
    
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            if authenticate(username =email, password=password):
                 return super(UserLoginForm,self).clean(*args, **kwargs)
            else:
                raise forms.ValidationError('check credentials and try again')

                   
class Password_resetform (forms.Form):
    email_address = forms.EmailField(widget=forms.TextInput(attrs={  
        "placeholder":"Enter email" , "class":"inputs"
    }))
    favourite_quote = forms.CharField(widget=forms.TextInput(attrs={  
        "placeholder":"favorite quote in need" , "class":"inputs"
    }))
    new_password = forms.CharField(widget = forms.PasswordInput(
        attrs={
          "placeholder":"Enter password" ,"class":"inputs"
        }  
    ))
    confirm_password = forms.CharField(widget = forms.PasswordInput(
        attrs={
          "placeholder":"Confirm password" , "class":"inputs"
        }  
    ))
  
    
    def clean_email_address(self):
        email = self.cleaned_data.get('email_address')
        
        err= User.objects.filter(email=email).exists()
        print(err)
        if not err:
            raise forms.ValidationError('check credentials and try again')
        return email
    
    
    def clean_favourite_quote(self):
        favourite_quote = self.cleaned_data.get('favourite_quote')
        email = self.cleaned_data.get('email_address')
        
        err= User.objects.get(email=email)
        quote= User_Detail.objects.get(user=err).quote 
        
       
        if str(quote).lower() != str(favourite_quote).lower():
            raise forms.ValidationError('favorite quote did not match contact support 09079681347')
        else:
            return favourite_quote
            
            
            
    def clean_confirm_password(self):
        pass1 = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if pass1 == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("passwword do not match")
        
        
    
        