from django import forms
from .models import Equipment
from .models import Booking #rayan - import booking form
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

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['equipment', 'start_date', 'end_date', 'is_current']
        widgets = {
            'is_current': forms.HiddenInput()
        }
class DeviceWarrantyForm(forms.ModelForm):
    class Meta:
        model = DeviceWarranty
        fields = ['warranty_period', 'expiration_date']
        widgets = {
            'warranty_period': forms.Select(choices=DeviceWarranty.WARRANTY_CHOICES),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
