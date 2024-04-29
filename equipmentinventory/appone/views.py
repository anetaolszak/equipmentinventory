from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipment, DeviceWarranty, UsageHistory
from .forms import CreateItemForm, ItemForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def is_admin(user):
    return user.is_superuser


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

@login_required
@user_passes_test(is_admin)
def createItem(request):
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():                 # validate data
                form = form.save()          # save to database
                return redirect("homepage")
    else:
            form = CreateItemForm()
    return render(request, 'appone/createitem.html', {"form": form})

@login_required
@user_passes_test(is_admin)
def inventory_report(request):
    # Query all equipment and their statuses
    inventory = Equipment.objects.select_related('status').all()
    return render(request, 'appone/inventory_report.html', {'inventory': inventory})

@login_required
@user_passes_test(is_admin)
def equipment_usage_history(request):
    # To track usage history
    usage_history = UsageHistory.objects.all()
    return render(request, 'appone/usage_history.html', {'usage_history': usage_history})

@login_required
@user_passes_test(is_admin)
def warranty_report(request):
    # This will fetch all Equipment objects and their related DeviceWarranty objects
    inventory = Equipment.objects.all().select_related('devicewarranty')
    return render(request, 'appone/warranty_report.html', {'inventory': inventory})

@login_required
@user_passes_test(is_admin)
def overdue_equipment_report(request):
    # To determine if equipment is overdue
    overdue_equipment = Equipment.objects.filter(due_date__lt=timezone.now()).all()
    return render(request, 'appone/overdue_report.html', {'overdue_equipment': overdue_equipment})

@login_required
@user_passes_test(is_admin)
def updateitem(request, id):
    item = get_object_or_404(Equipment, id=id)  # Get the item or return 404 error if not found

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()  # Save the changes to the item
            # Redirect to the updated item's page to see the changes
            #return redirect('appone_updateitem', id=item.id)
            return redirect("homepage")
    else:
        form = ItemForm(instance=item)

    context = {'form': form}
    return render(request, 'appone/update_equipment_details.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def deleteItem(request, id):
    item = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        print(request.POST)  # This will print the POST data in the console
        item.delete()
        return redirect("homepage")
    return render(request, 'appone/delete.html', {"item" : item})
