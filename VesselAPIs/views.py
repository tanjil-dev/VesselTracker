import os
import pandas as pd
from VesselTracker.settings import BASE_DIR
from django.http import HttpResponse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def data_upload(request):
    excel_dir = os.path.join(BASE_DIR,'Data/1.xlsx')
    all_sheets_df = pd.read_excel(excel_dir, sheet_name=None, engine='openpyxl')
    df = pd.concat(all_sheets_df[frame] for frame in all_sheets_df.keys())

    return  HttpResponse('Vessel Tracker')