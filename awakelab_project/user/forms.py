from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    group = Group.objects.all()
    class Meta: 
        model = User
        fields = ['username','email','password1','password2','group']