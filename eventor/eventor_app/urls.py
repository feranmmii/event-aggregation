from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventsViewSet)
router.register(r'bookedEvent', views.BookedEventsViewSet)

urlpatterns = [
    path('', views.home_page_view, name = 'home'),
    path('user_events', views.created_event_page_view, name = 'user_events'),
    path('booked_events', views.booked_event_page_view, name = 'booked_events'),
    path('create_event', views.create_event_page_view, name = 'create_event'),
    
    path('event/<id>', views.event_details_view, name = 'event_detail'),
    path('book_event_view', views.book_event_view, name = 'book_event_view'),
    path('search_events', views.search_event_page_view, name = 'search_events'),
    path('update_event/<id>', views.update_event_page_view, name = 'update_events'),
    path('delete_event', views.delete_event_view, name ='delete_event'),

    path('', include((router.urls))),
    path('rest-api', include('rest_framework.urls', namespace='rest_framework')),
]