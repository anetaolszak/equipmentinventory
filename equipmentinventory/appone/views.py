from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q #rayan
from django.contrib.auth import get_user #rayan
from .models import Booking #rayan
from .models import Equipment
from .forms import CreateItemForm, ItemForm
from .forms import ReservationForm #rayan - import reservation form
from django.utils import timezone #rayan
from django.contrib import messages #rayan
from django.shortcuts import get_object_or_404

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