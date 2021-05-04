from django.test import SimpleTestCase
from django.urls import  resolve, reverse
from ..views import *


class Test_urls(SimpleTestCase):
    def test_homepage_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_page_view)

    def test_user_events_url_resolves(self):
        url = reverse('user_events')
        self.assertEquals(resolve(url).func, created_event_page_view)

    def test_booked_events_url_resolves(self):
        url = reverse('booked_events')
        self.assertEquals(resolve(url).func, booked_event_page_view)

    def test_create_event_url_resolves(self):
        url = reverse('create_event')
        self.assertEquals(resolve(url).func, create_event_page_view)


    # def test_event_details_view_url_resolves(self):
    #     url = reverse('event_detail')
    #     self.assertEquals(resolve(url).func, event_details_view)

    def test_book_event_view_url_resolves(self):
        url = reverse('book_event_view')
        self.assertEquals(resolve(url).func, book_event_view)

    def test_search_events_url_resolves(self):
        url = reverse('search_events')
        self.assertEquals(resolve(url).func, search_event_page_view)

    def test_create_event_url_resolves(self):
        url = reverse('update_events')
        self.assertEquals(resolve(url).func, update_event_page_view)

    def test_create_event_url_resolves(self):
        url = reverse('delete_event')
        self.assertEquals(resolve(url).func, delete_event_view)

