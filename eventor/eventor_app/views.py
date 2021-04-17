from django.shortcuts import render
from rest_framework import viewsets
from.serializers import EventSerializers, BookedEventserializers
from . import models
from . import forms
import requests
from django.http import  JsonResponse
import json

# Create your views here.


class EventsViewSet(viewsets.ModelViewSet):
    queryset = models.Events.objects.all().order_by('startDate')
    serializer_class = EventSerializers

class BookedEventsViewSet(viewsets.ModelViewSet):
    queryset = models.BookedEvent.objects.all()
    serializer_class = BookedEventserializers


# def home_page_view(request):
#     events = requests.get('http://127.0.0.1:8000/events/').json()
#
#     for event in events:
#         if len(event['eventDescription']) > 104:
#             try:
#                 event['summary'] = f'{event["eventDescription"][0:104]}...'
#             except:
#                 pass
#         else:
#             event['summary'] = f'{event["eventDescription"]}...'
#
#         try:
#             imageUrl = f'static{event["eventImage"][21:]}'
#
#         except:
#             imageUrl = ''
#         event['imageUrl'] = imageUrl
#         print('image url',event['imageUrl'])
#
#     # if request.user.is_authenticated:
#     #     events = models.Events.objects.exclude(organizer=request.user)
#     # else:
#     #     events = models.Events.objects.all()
#     context = {'events':events}
#     return render (request, 'index.html', context)














def home_page_view(request):
    if request.user.is_authenticated:
        events = models.Events.objects.exclude(organizer=request.user)
    else:
        events = models.Events.objects.all()
    context = {'events':events}
    return render (request, 'index.html', context)


# def event_redirect_view(request):
#     id = json.loads(request)['eventId']
#     context = {'data':id}
#     print(context)
#     return  JsonResponse(context)
    #return redirect('event_page.html')


def event_details_view(request, id):
    context = {}
    context['event'] = models.Events.objects.get(id = id)
    return render(request, 'event_page.html', context)

def book_event_view(request):
    pass
    if request.user.is_authenticated:
        id = json.loads(request.body)
        models.BookedEvent(user = request.user, event = id['productId']).save()
        return JsonResponse('Event was booked successfully', safe=False)
    else:
        response = JsonResponse('You must be signed in before booking an Event')
        response.status_code = 403
        return response


def search_event_page(request):
    context = {'f'}
    return render(request, 'search_event_page.html', context)


def my_events_page_view(request):
    currentUser = request.user
    bookedEvents = models.BookedEvent.objects.filter(user=currentUser)
    createdEvents = models.Events.objects.filter(organizer=currentUser)
    
    if request.method == 'POST':
        createEventForm = forms.CreateEventForm(data = request.POST, files=request.FILES, initial={'organizer': currentUser})
        
        if createEventForm.is_valid():
            createEventForm.save()
    
    else:
        createEventForm = forms.CreateEventForm()
        
    context = {'bookedEvents':bookedEvents, 'createdEvents':createdEvents, 'createEventForm':createEventForm}
    return render(request, 'my_events_page.html', context)


def create_event_page_view(request):
    context = {}
    return render (request, 'create_event_page.html', context)


def edit_event_page_view(request):
    context = {}
    return render (request, 'edit_event_page.html', context)