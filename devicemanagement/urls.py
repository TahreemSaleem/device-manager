from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'', views.DeviceListView, basename='device_list')

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls