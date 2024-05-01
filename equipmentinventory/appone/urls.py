from . import views
from django.urls import path
from .views import register #maryam
from django.contrib.auth import views as log_views #maryam
from .views import privacypolicy #maryam
from .views import termsofuse #maryam


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
    path('register/', register, name = 'register'), #path created by maryam
    path('login/', log_views.LoginView.as_view(template_name='appone/login.html'), name='login'), #maryam
    path('logout/', log_views.LogoutView.as_view(template_name='appone/logout.html'), name='logout'), #maryam
    path('privacypolicy/', privacypolicy, name = "privacypolicy"), #maryam
    path('termsofuse/', termsofuse, name = "termsofuse"), #maryam




]