from django import forms
from django.core.exceptions import ValidationError
from .models import  User_Detail , User_product , Product_image
from django.contrib.auth import get_user_model


User=get_user_model()

class RegistrationForm(forms.ModelForm):
    email= forms.EmailField(required=True , label="EMAIL ADDRESS", widget=forms.TextInput(attrs={
        "class":"inputs","placeholder":"Enter email",
    }))
    password1= forms.CharField(label= "PASSWORD", widget= forms.PasswordInput(
      attrs={
          "name":"Password", "placeholder":"Enter password","class":"inputs"
      }
    ))
    password2= forms.CharField(label= "CONFIRM PASSWORD" , widget= forms.PasswordInput(
      attrs={
          "name":"Confirm password", "placeholder":"Confirm password","class":"inputs"
      }
    ))
    
    class Meta:
        model = User
        fields = ('email',)
        
    
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2") 
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('passwords don"t match')
        return password2
    
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        err= User.objects.filter(email=email).exists()
        if err:
            raise ValidationError('User account already exist')
        return email
    
    
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.active=True
        if commit:
            user.save()
        return user
    
    
    
User=get_user_model()

class UserDetailForm (forms.ModelForm): 
    username          = forms.CharField(max_length = 150 , label = "USERNAME", widget=forms.TextInput(
        attrs={
            "placeholder":"Enter username","class":"inputs"
        }))
    firstname          = forms.CharField(max_length = 150 , label = "FIRST NAME", widget=forms.TextInput(
        attrs={
            "placeholder":"Enter firstname","class":"inputs"
        }))
    lastname           = forms.CharField(max_length = 150, label = "LAST NAME",widget=forms.TextInput(
        attrs={
            "placeholder":"Enter lastname","class":"inputs"
        }))

    gender             = forms.SelectDateWidget(attrs={
       "class":"inputs"
    })
    contact            = forms.IntegerField( label = "CONTACT", widget=forms.TextInput(
        attrs={
            "placeholder":"Enter contact no.","class":"inputs", "maxlength":"15"
        }))
    about             = forms.CharField( label = "ABOUT YOURSELF", max_length=500,widget=forms.TextInput(
        attrs={
            "placeholder":"About user(max_length:500 words)" , "maxlength":"500","class":"inputs"
        }))
    quote             = forms.CharField( label = "A QUOTE YOU CANNOT FORGET", max_length = 500, required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"Favorite Quote(max_length:500 words)","maxlength":"500","class":"inputs"
        }))
    matricNo         = forms.CharField( label = "MATRIC NO", max_length = 60,required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"matric number(optional)","maxlength":"60","class":"inputs"
        }))
    campus   = forms.SelectDateWidget( attrs={
       "class":"inputs"
    })
    
    
    class Meta:
        model= User_Detail
        fields=('username','firstname','lastname',
            'gender','contact','about','quote','matricNo','campus')
        
        
    def clean_username(self):
        model=User_Detail
        username= self.cleaned_data.get('username')
        if  model.objects.filter(username=username).exists():
            raise ValidationError('this user is already taken')
        return username


