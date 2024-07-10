from django.test import TestCase
from .models import *

class VesselModelTest(TestCase):
    def test_vessel_model_exists(self):
        vessel = Vessel.objects.count()
        self.assertEqual(vessel, 0)

# class BlogTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         testuser1 = User.objects.create_user(username='testuser1', password='bs4080')
#         testuser1.save()

#         test_vessel = Vessel.objects.create(name='ABC_Vessel', owner_id='XYZ', naccs_code='CODE_123', latest_update_user='UPDATE_abc123')
#         test_vessel.save()

#         test_voyage_port = VoyagePort.objects.create(port_of_origin='LA', port_of_destination='NYC', estimate_time_in_hour='3')
#         test_voyage_port.save()

#         test_voyage = Voyage.objects.create(name='V12', vessel_id='1', transit_time_in_hour_id='1')
#         test_voyage.save()

#     def test_vessel_content(self):
#         vessel = Vessel.objects.get(id=1)
#         name = f'{vessel.name}'
#         owner_id = f'{vessel.owner_id}'
#         naccs_code = f'{vessel.naccs_code}'
#         latest_update_user = f'{vessel.latest_update_user}'
#         self.assertEqual(name, 'ABC_Vessel')
#         self.assertEqual(owner_id, 'XYZ')
#         self.assertEqual(naccs_code, 'CODE_123')
#         self.assertEqual(latest_update_user, 'UPDATE_abc123')

#     def test_voyage_port_content(self):
#         voyage_port = VoyagePort.objects.get(id=1)
#         port_of_origin = f'{voyage_port.port_of_origin}'
#         port_of_destination = f'{voyage_port.port_of_destination}'
#         estimate_time_in_hour = f'{voyage_port.estimate_time_in_hour}'
#         self.assertEqual(port_of_origin, 'LA')
#         self.assertEqual(port_of_destination, 'NYC')
#         self.assertEqual(estimate_time_in_hour, '3')

#     def test_voyage_content(self):
#         voyage = Voyage.objects.get(id=1)
#         name = f'{voyage.name}'
#         vessel = f'{voyage.vessel_id}'
#         transit_time_in_hour = f'{voyage.transit_time_in_hour_id}'
#         self.assertEqual(name, 'V12')
#         self.assertEqual(vessel, '1')
#         self.assertEqual(transit_time_in_hour, '1')