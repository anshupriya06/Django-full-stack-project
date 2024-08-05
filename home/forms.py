from django import forms
from .models import home

class homeform(forms.ModelForm):
    class Meta:
        model = home
        fields =  ['text', 'photo']
        

