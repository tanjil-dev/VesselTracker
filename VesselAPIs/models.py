from django.db import models
from django.contrib.auth.models import User
class Vessel(models.Model):
    name = models.CharField(max_length=50)
    owner_id = models.CharField(max_length=20)
    naccs_code = models.CharField(max_length=20)
    latest_update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.naccs_code

class VoyagePort(models.Model):
    port_of_origin = models.CharField(max_length=20)
    port_of_destination = models.CharField(max_length=20)
    estimate_time_in_hour = models.CharField(max_length=10)

    def __str__(self):
         return self.estimate_time_in_hour

class Voyage(models.Model):
    name = models.CharField(max_length=20)
    vessel = models.ForeignKey(Vessel, on_delete=models.DO_NOTHING)
    transit_time_in_hour = models.ForeignKey(VoyagePort, on_delete=models.DO_NOTHING)

    def __str__(self):
         return self.name