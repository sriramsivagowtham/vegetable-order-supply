from django import forms
from django.contrib.auth.models import User
from .models import Dash
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class CustomerUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email',
            'class': 'form-control'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username',
                'class': 'form-control'
            }),
        }


class DashForm(forms.ModelForm):
    class Meta:
        model = Dash
        fields ='__all__'