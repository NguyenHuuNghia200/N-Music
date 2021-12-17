from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django import forms
from .models import Song
class registerview(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Password Confirmation')


    class Meta:
        model=User
        fields=('first_name','last_name','username','email',)
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','id':'username'}),
            'email': forms.TextInput(attrs={'class': 'form-control','id':'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','id':'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','id':'last_name'}),
            'password': forms.TextInput(attrs={'class': 'form-control','id':'email'}),
        }


class loginview(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username','placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'username','placeholder':'username'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)


class formsong(forms.ModelForm):
    class Meta:
        model=Song
        fields=('title','author','image','audio_link','category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),

        }