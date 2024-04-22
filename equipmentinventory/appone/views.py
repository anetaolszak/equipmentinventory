from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipment

# Create your views here.
'''testdata = [
    {'id':1, 'name': 'Item 1 of list'},
    {'id':2, 'name': 'Item 2 of list'},
    {'id':3, 'name': 'Item 3 of list'},
    {'id':4, 'name': 'Item 4 of list'},
    {'id':5, 'name': 'Item 5 of list'},
    {'id':6, 'name': 'Item 6 of list'},
    

    ]'''


def home(request):
    item = Equipment.objects.all
    context = {'item': item}
    return render(request, 'appone/home.html', context)

def admindashboard(request):
    return render(request, 'appone/admindashboard.html')

def equipment(request, id):
    listitem = Equipment.objects.get(id=id)
    context = {'listitem': listitem}
    return render(request, 'appone/equipment.html', context)

def navbar(request):
    return render(request, 'navbar.html')