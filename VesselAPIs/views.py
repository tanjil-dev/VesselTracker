from rest_framework import generics
from .models import Vessel, Voyage
from .serializers import VesselSerializer, VoyageSerializer
from rest_framework import filters

class VesselList(generics.ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'naccs_code', 'owner_id']

class VesselDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class VoyagelList(generics.ListCreateAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'vessel', 'start_location', 'end_location', 'start_time', 'end_time']

class VoyageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer