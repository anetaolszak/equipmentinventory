from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('admindashboard/', views.admindashboard),
    path('equipment/<str:id>', views.equipment, name = "equipmentpage"),
    path('createitem/', views.createItem, name = "appone_createitem"),
    path('updateitem/<str:id>', views.updateitem, name = "appone_updateitem"),
    path('deleteitem/<int:id>', views.deleteItem, name = "appone_deleteitem"),
    path('reports/inventorystatus/', views.inventory_report, name="inventory_status"),
    path('reports/usage/', views.equipment_usage_history, name='usage_history'),
    path('reports/warranty/', views.warranty_report, name="warranty_report"),
    path('reports/overdue/', views.overdue_equipment_report, name="overdue_equipment"),




]