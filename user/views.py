from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm, PasswordResetForm
from django.urls import reverse_lazy
# Create your views here.

class UserRegistrationViews(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class UserLoginViews(generic.FormView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")

class UserLogoutViews(generic.FormView):
    success_url = reverse_lazy("home")
    