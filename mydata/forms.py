from django import forms 
from .models import sfile

class BookForm(forms.ModelForm):
     class Meta:
         model= sfile
         fields=('tittle','pdf')