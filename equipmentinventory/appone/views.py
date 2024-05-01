from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipment
from .forms import CreateItemForm, ItemForm
from django.shortcuts import get_object_or_404
#from django.contrib.auth.forms import UserCreationForm #maryam
from django.contrib import messages #maryam#
from .forms import UserRegisterForm

# Create your views here.

def home(request):
    item = Equipment.objects.all
    context = {'item': item}
    return render(request, 'appone/home.html', context)

def admindashboard(request):
    return render(request, 'appone/admindashboard.html')

def equipment(request, id):
    listitem = Equipment.objects.get(id=id) # 'READE' pull out all information out of our databasde on the homepage
    context = {'listitem': listitem}
    return render(request, 'appone/equipment.html', context)

def createItem(request):
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():                 # validate data
                form = form.save()          # save to database
                return redirect("homepage")
    else:
            form = CreateItemForm()
    return render(request, 'appone/createitem.html', {"form": form})


def updateitem(request, id):
    listitem = Equipment.objects.get(id=id) # 'READE' pull out all information out of our databasde on the homepage
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            #update the existing 'item' in the database
            listitem.save()
            # redirect to the equipment page
            # return redirect (appone_equipment, item.id)
            return redirect ('homepage')
    else:
            form = ItemForm(instance=listitem)
    context = {'listitem' :listitem, 'form': form}
    return render(request,'appone/equipment.html', context)


def deleteItem(request, id):
    item = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect("homepage")
    return render(request, 'appone/delete.html', {"item" : item})


#view created by maryam:
def register(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}!')
               return redirect('homepage')
          else:
           #    form = UserCreationForm()
               return render(request, "appone/register.html", {'form': form})
     else:
        # This branch handles GET requests by initializing a new, blank form
        form = UserRegisterForm()
        return render(request, "appone/register.html", {'form': form})                             
     
#maryam
def privacypolicy(request):
    return render(request, 'appone/privacypolicy.html')

#maryam
def termsofuse(request):
    return render(request, 'appone/termsofuse.html')