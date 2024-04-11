from rest_framework import generics
from curacao_devices_db.models import Location
from curacao_devices_db.serializer import LocationSerializer

class LocationsView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()