from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Dash


class CustomerUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class DashForm(forms.ModelForm):
    class Meta:
        model = Dash
        fields ='__all__'