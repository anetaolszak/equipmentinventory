from django import forms
from .models import Equipment
from .models import DeviceWarranty
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateItemForm(forms.ModelForm):


    class Meta:
        model = Equipment
        fields = '__all__'


class ItemForm(forms.ModelForm):


    class Meta:
        model = Equipment
        fields = '__all__'

class DeviceWarrantyForm(forms.ModelForm):
    class Meta:
        model = DeviceWarranty
        fields = ['warranty_period', 'expiration_date']
        widgets = {
            'warranty_period': forms.Select(choices=DeviceWarranty.WARRANTY_CHOICES),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
