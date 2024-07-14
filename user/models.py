import uuid
from django.db import models
from VesselAPIs.models import Voyage
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Parcel(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='parcels')
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)


    def __str__(self):
        return f'{self.user.username} Profile'
