from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q #rayan
from django.contrib.auth import get_user #rayan
from .models import Booking #rayan
from .forms import ReservationForm #rayan - import reservation form
from django.contrib import messages #rayan
from .models import Equipment, DeviceWarranty, UsageHistory
from .forms import CreateItemForm, ItemForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count


# Create your views here.

def is_admin(user):
    return user.is_superuser


def home(request):
    item = Equipment.objects.all
    context = {'item': item}
    return render(request, 'appone/home.html', context)

def admindashboard(request):
        # Get necessary data from the database
    equipment_count = Equipment.objects.count()

    context = {
        'equipment_count': equipment_count,
    }
    return render(request, 'appone/admindashboard.html', context)


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

<<<<<<< HEAD
def reserve_item(request): #rayan
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            equipment = booking.equipment
            if not equipment.is_available():
                messages.error(request, "This item is currently unavailable.")
            elif equipment.is_booked(booking.start_date, booking.end_date):
                messages.error(request, "This item is already booked for the selected dates.")
            else:    
                user = get_user(request)
                booking.user = user
                booking.start_date = timezone.now()
                booking.save()
                return redirect('booking_success')
    else:
        form = ReservationForm()
    return render(request, 'appone/reservation_form.html', {'form':form})

def booking_success(request): #rayan
    return render(request, 'appone/booking_success.html')
    

def current_bookings(request): #rayan
    current_bookings = Booking.objects.filter(user=request.user, is_current=True)
    return render(request, 'appone/current_bookings.html', {'current_bookings': current_bookings})

def historical_bookings(request): #rayan
    historical_bookings = Booking.objects.filter(Q(user=request.user) & Q(is_current=False))
    return render(request, 'appone/historical_bookings.html', {'historical_bookings': historical_bookings})

def rebook_booking(request, booking_id): #rayan
    booking = get_object_or_404(Booking, id=booking_id)
    new_booking = Booking.objects.create(
        equipment=booking.equipment,
        user=request.user,
        start_date=timezone.now().date(),
        end_date=booking.end_date,
        is_current=True
    )

    booking.is_current = False #rayan
    booking.save()
    return redirect('current_bookings')

def cancel_booking(request, booking_id): #rayan
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user == booking.user:
        booking.is_current = False
        booking.save()
        return redirect('current_bookings')
    else:
        return HttpResponse("You cannot cancel this booking.")   
=======
@login_required
@user_passes_test(is_admin)
def overdue_equipment_count_view(request):
    # Queryset of overdue equipment
    overdue_equipment = Equipment.objects.filter(due_date__lt=timezone.now().date())
    overdue_count = overdue_equipment.count()  # Count of overdue equipment

    # Pass the queryset and count to the context
    context = {
        'overdue_equipment': overdue_equipment,
        'overdue_count': overdue_count,
    }

    return render(request, 'appone/overdue_count.html', context)


@login_required
@user_passes_test(is_admin)
def inventory_count_by_device_type_view(request):
    # Count of equipment by device type
    count_by_device_type = Equipment.objects.values('devicetype__type').annotate(count=Count('id')).order_by('devicetype__type')
    
    # Pass the counts to the context
    context = {
        'count_by_device_type': count_by_device_type,
    }

    return render(request, 'appone/count_by_device_type.html', context)
>>>>>>> 3e78b2890d26c5d4679768a63b26f2026219b30d
