from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class DeviceType(models.Model):
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type

class DeviceWarranty(models.Model):
    warranty = models.CharField(max_length=200)
    
    def __str__(self):
        return self.warranty

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
    
    def __str__(self):
        return self.name
