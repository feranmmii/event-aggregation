from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name = 'home'),
    path('event', views.event_page_view, name  = 'event_details'),
    path('user_event', views.my_events_page_view, name = 'user_event'),
]