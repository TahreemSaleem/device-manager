
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .models import Device
from .serializers import DeviceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.models import APIKey
from rest_framework.decorators import permission_classes

class DeviceListView(APIView):
    """
    	GET: List all devices, fetches them from db
		
    """
    def get(self, request, *args, **kwargs):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return render(request, 'index.html', {'devices': serializer.data})


class DeviceCreateView(APIView):
    """
    	POST: Creates new device data, also validating request 
		
    """
    permission_classes = [HasAPIKey]
   
    def post(self, request, *args, **kwargs):
        serializer = DeviceSerializer(data=request.data)

        if not serializer.is_valid():	
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        task = serializer.save()

        if task:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"error": "An error occurred while saving the device."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class DeviceFormView(APIView):
    """
    	GET: Renders html page with add device form
		
    """
    # creates a static API key and sends it along the request
    api_key, key = APIKey.objects.create_key(name="global-key")
    def get(self, request, *args, **kwargs):
        
        return render(request, 'add.html',{'apiKey': self.key})
