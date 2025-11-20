from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views, forms
from apps.users.forms import RegisterForm
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

class LoginView(views.LoginView):
    form_class = forms.AuthenticationForm
    template_name = "users/login.html"