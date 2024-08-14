from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework import filters

class VesselList(ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'naccs_code', 'owner_id']

class VesselDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class VoyagelList(ListCreateAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'vessel', 'start_location', 'end_location', 'start_time', 'end_time']

class VoyageDetail(RetrieveUpdateDestroyAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer

class ParcelList(ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['voyage', 'description', 'user', 'received']

class ParcelDetail(RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
