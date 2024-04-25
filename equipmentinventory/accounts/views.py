from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def signupaccount(request):

    return render(request, 'signupaccount.html',

                  {'form':UserCreationForm})