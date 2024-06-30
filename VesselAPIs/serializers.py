from rest_framework import serializers
from .models import *

class VesselSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Vessel

class VoyageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Voyage

class ParcelSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Parcel

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Notification