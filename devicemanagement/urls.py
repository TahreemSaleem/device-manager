from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    
#   """Device list [GET]
    path('',views.DeviceListView.as_view()), 

#   """" Add device [GET]"""
    path('add/',views.DeviceFormView.as_view()),

#   """" Add device [POST]"""
    path('add/device/',views.DeviceCreateView.as_view()),

]