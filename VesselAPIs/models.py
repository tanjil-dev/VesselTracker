from django.db import models

class Vessel(models.Model):
    name = models.CharField(max_length=50)
    owner_id = models.CharField(max_length=50)
    naccs_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
         return self.name

class Voyage(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete=models.DO_NOTHING)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
         return f"{self.vessel.name}: {self.start_location} to {self.end_location} from {self.start_time} to {self.end_time}"
