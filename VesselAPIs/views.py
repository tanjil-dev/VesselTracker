import os
import pandas as pd
from VesselTracker.settings import BASE_DIR
from django.http import HttpResponse
from rest_framework import generics
from .models import Vessel, Voyage
from .serializers import VesselSerializer, VoyageSerializer
from rest_framework import filters

class VesselList(generics.ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'naccs_code', 'owner', 'latest_update_user']

class VesselDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer

class VoyagelList(generics.ListCreateAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'vessel__name', 'transit_time_in_hour__estimate_time_in_hour']

class VoyageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer

def data_upload(request):
    vessels = []
    excel_dir = os.path.join(BASE_DIR,'Data/senpaku_n.xlsx')
    all_sheets_df = pd.read_excel(excel_dir, sheet_name=None, engine='openpyxl')
    df = pd.concat(all_sheets_df[frame] for frame in all_sheets_df.keys())
    for d in df.values:

        vessel = Vessel(name=d[1], owner_id=d[3], naccs_code=d[2], latest_update_user=d[4])
        vessels.append(vessel)
    Vessel.objects.bulk_create(vessels)
    return HttpResponse('Excel data uploaded Suceesfully!')
