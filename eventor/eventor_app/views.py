from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def home_page_view(request):
    events = models.Events.objects.all()
    context = {'events':events}
    return render (request, 'index.html', context)

def event_page_view(request):
    context = {}
    return render(request, 'event_page.html', context)

def search_event_page(request):
    context = {'f'}
    return render(request, 'search_event_page.html', context)

def my_events_page_view(request):
    currentUser = request.user
    bookedEvents = models.BookedEvent.objects.filter(user=currentUser)
    createdEvents = models.Events.objects.filter(organizer=currentUser)
    createEventForm = forms.CreateEventForm
            
    context = {'bookedEvents':bookedEvents, 'createdEvents':createdEvents, 'ccreateEventForm':createEventForm}
    return render(request, 'my_events_page.html', context)

def create_event_page_view(request):
    context = {}
    return render (request, 'create_event_page.html', context)

def edit_event_page_view(request):
    context = {}
    return render (request, 'edit_event_page.html', context)