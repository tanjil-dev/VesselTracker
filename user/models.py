import uuid
from PIL import Image
from django.db import models
from VesselAPIs.models import Voyage
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

RECEIVE = (
    (1, 'SHIPPING INITIATED'),
    (2, 'ON THE WAY'),
    (3, 'READY TO RECEIVE'),
    (4, 'RECEIVED'),
)

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class Parcel(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)


    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if Image:
            image = Image.open(self.image.path)
            if image.height > 300 or image.width > 300:
                output_size = (300, 300)
                image.thumbnail(output_size)
                image.save(self.image.path)