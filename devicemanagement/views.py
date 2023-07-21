from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .models import Device
from .serializers import DeviceSerializer

class DeviceListView(ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
      
    def list(self, request, *args, **kwargs):
        devices = self.get_queryset()
        serializer = self.get_serializer(devices, many=True)
        return render(request, 'index.html', {'devices': serializer.data})