from django import forms
from .models import Equipment
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
