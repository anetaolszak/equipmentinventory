from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class DeviceType(models.Model):
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type

class DeviceWarranty(models.Model):
    WARRANTY_CHOICES = (
        (24, '24 months warranty provided'),
        (12, '12 months warranty provided'),
        (6, '6 months warranty provided'),
    )
    
    warranty_period = models.IntegerField(choices=WARRANTY_CHOICES)
    expiration_date = models.DateField(default=timezone.now, null=True)

    def __str__(self):
        return f"{self.get_warranty_period_display()} (Expires on: {self.expiration_date})"

class Location(models.Model):
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location

class Status(models.Model):
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.status


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    devicetype = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)
    devicewarranty = models.ForeignKey(DeviceWarranty, on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)  #field for device serial
    cpu = models.CharField(max_length=255, null=True, blank=True)  #field for CPU
    gpu = models.CharField(max_length=255, null=True, blank=True)  #field for GPU
    ram = models.CharField(max_length=255, null=True, blank=True)  #field for RAM
    quantity = models.PositiveIntegerField()
    audit_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    comments = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    due_date = models.DateField(null=True, blank=True)  # field to track due dates

    
    def __str__(self): 
        return self.name

    def is_available(self): #rayan
        return self.status.status == 'Available'

    def is_booked(self, start_date, end_date): #rayan
        return self.booking_set.filter(
            start_date__lte=end_date,
            end_date__gte=start_date,
            is_current=True
        ).exists()    

class Booking(models.Model): #rayan - booking model
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.equipment.name} - {self.user.username}"
class UsageHistory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_used = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.equipment.name} used on {self.date_used} by {self.user.username if self.user else "Unknown"}'

    def is_available(self): #rayan
        return self.status.status == 'Available'

    def is_booked(self, start_date, end_date): #rayan
        return self.booking_set.filter(
            start_date__lte=end_date,
            end_date__gte=start_date,
            is_current=True
        ).exists()    

class Booking(models.Model): #rayan - booking model
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.equipment.name} - {self.user.username}"