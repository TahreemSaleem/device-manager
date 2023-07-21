from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewset with it.
urlpatterns = [
    
#   """User Registeration [GET]
    path('',views.DeviceListView.as_view()), 

#   """" User Login [GET]"""
    path('add/',views.DeviceFormView.as_view()),

#   """" User Login [GET]"""
    path('add/device/',views.DeviceCreateView.as_view()),

]