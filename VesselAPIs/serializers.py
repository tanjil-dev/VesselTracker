from rest_framework import serializers
from .models import Vessel, Voyage

class VesselSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Vessel

class VoyageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'vessel', 'transit_time_in_hour')
        model = Voyage