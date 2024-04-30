from django.contrib import admin
from .models import Equipment, DeviceType, DeviceWarranty, Location, Status 


# Register your models here.

admin.site.register(Equipment)
admin.site.register(DeviceType)
admin.site.register(DeviceWarranty)
admin.site.register(Location)
admin.site.register(Status)
