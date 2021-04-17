from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventsViewSet)
router.register(r'bookedEvent', views.BookedEventsViewSet)

urlpatterns = [
    path('', views.home_page_view, name = 'home'),
    path('user_event', views.my_events_page_view, name = 'user_event'),
    
    path('event/<id>', views.event_details_view, name = 'event_detail'),
    path('book_event_view', views.book_event_view, name = 'book_event_view'),

    path('', include((router.urls))),
    path('rest-api', include('rest_framework.urls', namespace='rest_framework')),
]