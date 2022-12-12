from django import forms 
from django.contrib.auth import authenticate
from homepage.models import User_Detail
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()
class UserLoginForm (forms.Form):
    email= forms.EmailField( label= "" ,widget=forms.TextInput(attrs={  
        "placeholder":"Enter email" , "class":"inputs"
    }))
    password= forms.CharField( label= "" ,widget = forms.PasswordInput(
        attrs={
          "placeholder":"Enter password" ,"class":"inputs"
        }
    ))
    
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = User.objects.get(email=email)
        if email and password:
            if authenticate(username =email, password=password):
                 return super(UserLoginForm,self).clean(*args, **kwargs)
            elif user.is_active == False:
               raise forms.ValidationError('check your mail to activate account') 
            else:
                raise forms.ValidationError('check credentials and try again')
            
    

                  
class Password_resetform (forms.Form):
    email_address = forms.EmailField(required=True ,label = "", widget=forms.TextInput(attrs={  
        "placeholder":"Enter email" , "class":"inputs"
    }))
    password2 = forms.CharField(required=True , label = "", widget= forms.PasswordInput(
      attrs={
          "name":"password", "placeholder":"New password","class":"inputs"
      }
    ))
    
    
    def clean_email_address(self):
        email = self.cleaned_data.get('email_address')
        
        err= User.objects.filter(email=email).exists()
        if not err:
            raise forms.ValidationError('This user does not exist')
        return email
    
   