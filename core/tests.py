import copy
from rest_framework.test import APIClient
from django.test import TestCase
import json
from .models import Raport

# Create your tests here.
class RaportTests(TestCase):
    mockRaport = {
        'id': None,
        'name': 'new raport',
        'formatR': 'xlsx',
        'email': 'test@email.mail',
        'scheduleType': 0,
        'scheduleTime': None,
        'scheduleDate': None,
        'scheduleDay': None
    }

    def testValidRaportPost(self):
        client = APIClient()
        response = client.post('/drfapi/post', self.mockRaport, format='json')
        self.assertTrue(json.loads(response.content))
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Raport.objects.exists())

    def testInvalidRaportPost(self):
        invalidRaport = copy.copy(self.mockRaport)
        invalidRaport['name']=None
        client = APIClient()
        response = client.post('/drfapi/post', invalidRaport, format='json')
        self.assertEquals(json.loads(response.content), None)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Raport.objects.exists())