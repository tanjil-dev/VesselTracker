import uuid
from django.db import models
from django.contrib.auth.models import User

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

class Parcel(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='parcels')
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id

class Notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    read_unread = models.BooleanField(default=False)