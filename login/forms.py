from django import forms 
from django.contrib.auth import authenticate
from homepage.models import User_Detail
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User= get_user_model()
class UserLoginForm (forms.Form):
    email= forms.EmailField(widget=forms.TextInput(attrs={  
        "placeholder":"Enter email" , "class":"inputs"
    }))
    password= forms.CharField(widget = forms.PasswordInput(
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
    email= forms.EmailField(widget=forms.TextInput(attrs={  
        "placeholder":"Enter email" , "class":"inputs"
    }))
    username= forms.CharField(widget=forms.TextInput(attrs={  
        "placeholder":"Enter username" , "class":"inputs"
    }))
    password_reset_key= forms.CharField(widget = forms.PasswordInput(
        attrs={
          "placeholder":"Enter password reset key" ,"class":"inputs"
        } 
    ))    
    password= forms.CharField(widget = forms.PasswordInput(
        attrs={
          "placeholder":"Enter password" ,"class":"inputs"
        }  
    ))
    confirm_password = forms.CharField(widget = forms.PasswordInput(
        attrs={
          "placeholder":"Confirm password" , "class":"inputs"
        }  
    ))
  
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        err= User.objects.filter(email=email).exists()
        if not err:
            raise forms.ValidationError('check credentials/password reset key and try again')
        return email
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        
        err= User.objects.get(email=email)
        user= User_Detail.objects.get(user=err)
        
        if user.username != username:
            raise forms.ValidationError('username is incorrect')
        else:
            return username
            
            
    def clean_password_reset_key(self):
        password_reset_key = self.cleaned_data.get('password_reset_key')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        err  = User.objects.get(email=email)
        user = User_Detail.objects.get(user=err)
        
        
        if user.password_reset_key != password_reset_key:
            raise forms.ValidationError('password reset key is incorrect')
        else:
            return password_reset_key
            
    def clean_confirm_password(self):
        pass1 = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        print(pass1,confirm_password)
        if pass1 == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("passwword do not match")
        
        
    
        