# Generated by Django 3.2.15 on 2024-07-12 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VesselAPIs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('received', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcels', to='VesselAPIs.voyage')),
            ],
        ),
    ]
