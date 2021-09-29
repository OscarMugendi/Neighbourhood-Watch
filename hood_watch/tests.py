from django.test import TestCase
from .models import *

# Create your tests here.

class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.Nai = Neighbourhood.objects.create(name='Nai')

    def test_instance(self):
        self.Nai.save()
        self.assertTrue(isinstance(self.Nai, Neighbourhood))

    def test_get_hoods(self):
        self.Nai.save()
        hoods = Neighbourhood.get_hoods()
        self.assertTrue(len(hoods) > 0)


class BusinessTest(TestCase):
    def setUp(self):
        self.myBusiness= Business.objects.create(name='myBusiness', email='mybusiness@gmail.com')

    def test_instance(self):
        self.myBusiness.save()
        self.assertTrue(isinstance(self.myBusiness,Business))