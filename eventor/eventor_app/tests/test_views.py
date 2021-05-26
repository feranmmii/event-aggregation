from django.test import TestCase, Client
from django.urls import  reverse
from ..models import Events
from django.contrib.auth.models import User
import datetime


class Test_views(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Frank', 'frank@email.com', 'randpass')
        self.test_obj = Events.objects.create(
            organizer=self.user,
            eventName='Paul',
            startDate=datetime.date.today(),
            startTime='12:00',
            endDate=datetime.date.today(),
            address='Just a rand address',
            eventDescription='well this shuld be some long description buh aint got time'

        )


    def test_get_homepage_view(self):
        res = self.client.get(reverse('home'))
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'index.html')


    def test_check_home_view_content(self):
        res = self.client.get(reverse('home'))
        print (self.test_obj.eventName)
        self.assertIn(bytes(self.test_obj.eventName, 'utf-8'), res.content)
        self.assertIn(bytes(self.test_obj.eventDescription[0:20], 'utf-8'), res.content)


    def test_event_details_view_for_signedout_user(self):
        res = self.client.get(reverse('event_detail', args='1'))
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'event_details.html')

        self.assertIn(bytes(self.test_obj.eventName, 'utf-8'), res.content)
        self.assertIn(bytes(self.test_obj.address, 'utf-8'), res.content)
        self.assertIn(bytes(self.test_obj.eventDescription, 'utf-8'), res.content)




