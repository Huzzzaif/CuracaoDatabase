from rest_framework import generics
from curacao_devices_db.models import Device
from curacao_devices_db.serializer import DeviceSerializer
class DevicesView(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()