from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserProfileForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter username'})
        
        self.fields['email'].help_text = ''
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter email'})
        
        self.fields['password1'].help_text =''
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enter password'})
        
        self.fields['password2'].help_text=''
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'Confirm password'})
        
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        

class UserLoginForm(AuthenticationForm):    
    def __init__(self, *args, **kwargs):
        
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter username'})

        self.fields['password'].help_text = ''
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter username'})

 