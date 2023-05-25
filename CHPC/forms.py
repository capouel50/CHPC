from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(label='Mot de passe', max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'}))