import uuid
from django.db import models
from VesselAPIs.models import Voyage
from django.contrib.auth.models import User

class Parcel(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='parcels')
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id
