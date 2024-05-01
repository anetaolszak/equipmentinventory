from django import forms
from .models import Equipment
from django.contrib.auth.forms import UserCreationForm #maryam
from django.contrib.auth.models import User


class CreateItemForm(forms.ModelForm):


    class Meta:
        model = Equipment
        fields = '__all__'


class ItemForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
class Meta:
    model = User
fields = ['username', 'email', 'password1', 'password2']