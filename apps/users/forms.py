from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # widgets = {
        #     "password": forms.PasswordInput(attrs={
        #         'placeholder': '密碼長度區間6-20個字元',
        #     }),
        # }