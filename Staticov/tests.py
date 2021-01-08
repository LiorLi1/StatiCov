from django import urls
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from Staticov.views import *
from Staticov.models import *



class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('home')
        url1 = reverse('login')
        url2= reverse('AdminDash')
        url3 = reverse('MainDashBoard')
        print(resolve(url))
        print(resolve(url1))
        print(resolve(url2))
        print(resolve(url3))

class workerstest(TestCase):

    def test_workers(self):
       item=WorkersModel()
       item.ID=1
       item.name='jean'
       item.taz='123456789'
       item.password='123456'
       item.Type='admin'
       item.save()
       record= WorkersModel.objects.get()
       print("HERRE")
       self.assertEqual(record,item)

class registertest(TestCase):

    def test_register(self):
       item=RegisterFormModel()
       item.ID=1
       item.name='jean'
       item.taz='123456789'
       item.password='123456'
       item.Type='civilian'
       item.civiliantype='student'
       item.save()
       record= RegisterFormModel.objects.get()
       print("HERRE")
       self.assertEqual(record,item)

class Patient(TestCase):

    def test_Patient(self):
       item=Patientworker()
       item.id=3
       item.workerid=12
       item.taz='111111111'
       item.telephone="0512233445"
       item.save()
       record= Patientworker.objects.get()
       print("HERRE")
       self.assertEqual(record,item)

# Create your tests here.
