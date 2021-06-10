from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    balance = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'email','phone_no','password1', 'password2', 'balance']
