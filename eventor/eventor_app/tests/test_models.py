from django.test import TestCase, Client
from django.urls import  reverse
from ..models import Events, BookedEvent
from django.contrib.auth.models import User
import datetime


class Test_views(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Frank', 'frank@email.com', 'randpass')
        self.eventData = Events.objects.create(
            organizer=self.user,
            eventName='Paul',
            startDate=datetime.date.today(),
            startTime='12:00',
            endDate=datetime.date.today(),
            address='Just a rand address',
            eventDescription='Here are the most interesting short stories. There are various animal-characters and human characters in these short stories. WE should learn the most wanted lessons from these characters of these short stories. Both the fables and the parables have interesting twists which make these short stories quite interesting in all possible manners. Fables are animal-based short stories. Parables are human-based short stories. '
        )


    def test_events(self):

        reducedText = self.eventData.eventDescription[0:104]

        self.assertEquals(self.eventData.isBooked, False)
        self.assertEquals(self.eventData.imageUrl, '')
        self.assertEquals(self.eventData.getSummary, f'{reducedText}...')
        self.assertEquals(self.eventData.__str__(), self.eventData.eventName)


    def test_bookedEvent(self):
        bookedEventData = BookedEvent.objects.create(
            self.user,
            self.eventData
        )

        self.assertEquals(bookedEventData.userEmail, self.user.email)
