import os
import pandas as pd
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework.response import Response

class VesselList(ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'naccs_code', 'owner_id']
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data})

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

def data_upload(request):
    vessels = []
    directory_path = os.getenv('STATIC_ROOT') + '/senpaku_n.xlsx'
    all_sheets_df = pd.read_excel(directory_path, sheet_name=None, engine='openpyxl')
    df = pd.concat(all_sheets_df[frame] for frame in all_sheets_df.keys())
    text_to_remove1 = "※船舶コードは誤って登録されている場合があるため、入出港届等照会（IVS）業務において、税関確認状況等をご確認ください。"
    df = df[~df.apply(lambda row: row.astype(str).str.contains(text_to_remove1).any(), axis=1)]
    text_to_remove2 = "船舶コード"
    df = df[~df.apply(lambda row: row.astype(str).str.contains(text_to_remove2).any(), axis=1)]
    df = df.drop_duplicates(subset=[df.columns[2]], keep='first')
    for d in df.values:
        vessel = Vessel(name=d[1], owner_id=d[3], naccs_code=d[2])
        vessels.append(vessel)
    try:
        Vessel.objects.bulk_create(vessels)
    except:
        return HttpResponse('Excel data upload unsuccessful!')
    return HttpResponse('Excel data uploaded Successfully!')