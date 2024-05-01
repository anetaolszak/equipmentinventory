from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('admindashboard/', views.admindashboard),
    path('equipment/<str:id>', views.equipment, name = "equipmentpage"),
    path('createitem/', views.createItem, name = "appone_createitem"),
    path('updateitem/<str:id>', views.updateitem, name = "appone_updateitem"),
    path('deleteitem/<int:id>', views.deleteItem, name = "appone_deleteitem"),
    path('reserve/', views.reserve_item, name='reserve_item'), #rayan - url pattern
    path('current-bookings/', views.current_bookings, name='current_bookings'), #rayan
    path('historical-bookings/', views.historical_bookings, name='historical_bookings'), #rayan
    path('rebook-booking/<int:booking_id>/', views.rebook_booking, name='rebook_booking'), #rayan
    path('booking/success/', views.booking_success, name='booking_success'), #rayan
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'), #rayan
    path('reports/inventorystatus/', views.inventory_report, name="inventory_status"),
    path('reports/usage/', views.equipment_usage_history, name='usage_history'),
    path('reports/warranty/', views.warranty_report, name="warranty_report"),
    path('reports/overdue/', views.overdue_equipment_report, name="overdue_equipment"),
    path('inventory/overduecount/', views.overdue_equipment_count_view, name='overdue_count'),
    path('inventory/countbydevicetype/', views.inventory_count_by_device_type_view, name='count_by_device_type'),




]