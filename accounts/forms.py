from django.contrib import auth
from django.contrib.auth.models import User
from .models import extendeduser
from django import forms 
from django.forms import ModelForm

class nameform(ModelForm):
    class Meta:
        model = extendeduser
        fields = ['uname','phone_num', 'age','email']