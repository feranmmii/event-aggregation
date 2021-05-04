from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import EventSerializers, BookedEventserializers
from . import models
from . import forms
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from .filters import EventFilter, BookedEventFilter


class EventsViewSet(viewsets.ModelViewSet):
    queryset = models.Events.objects.all().order_by('startDate')
    serializer_class = EventSerializers


class BookedEventsViewSet(viewsets.ModelViewSet):
    queryset = models.BookedEvent.objects.all()
    serializer_class = BookedEventserializers


def home_page_view(request):
    if request.user.is_authenticated:
        events = models.Events.objects.exclude(organizer=request.user)
    else:
        events = models.Events.objects.all()
    context = {'events': events}
    return render(request, 'index.html', context)


def event_details_view(request, id):
    context = {}
    context['event'] = models.Events.objects.get(id=id)
    return render(request, 'event_details.html', context)


def book_event_view(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        event = models.Events.objects.get(id=data['id'])
        isBooked = models.BookedEvent.objects.filter(event=event).exists()

        if data['action'] == 'make_booking' and isBooked == False:
            models.BookedEvent(user=request.user, event=event).save()
            return JsonResponse('Event was booked successfully', safe=False)
        elif data['action'] == 'cancel_booking' and isBooked == True:
            print('in delete')
            models.BookedEvent.objects.filter(event=event).delete()
            return JsonResponse('Event was removed successfully', safe=False)


    else:
        response = JsonResponse('You must be signed in before booking an Event')
        response.status_code = 403
        return response


def search_event_page_view(request):
    if request.method == 'POST':
        searched_term = request.POST.get('search')
        searched_events = forms.Events.objects.filter(eventName__contains=searched_term)
        print(searched_events)
        context = {'search_result': searched_term, 'events': searched_events}
        return render(request, 'search_page.html', context)
    else:
        context = {}
        return render(request, 'search_page.html', context)


def update_event_page_view(request, id):
    event = models.Events.objects.get(id = id)
    form = forms.CreateEventForm(instance=event)
    if request.method == 'POST':
        form = forms.CreateEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('user_events')
    context = {'form': form}
    return render(request, 'update_event_page.html', context)


def created_event_page_view(request):
    currentUser = request.user
    createdEvents = models.Events.objects.filter(organizer=currentUser)
    print(createdEvents)

    # adding event filter
    filter = EventFilter(request.GET, queryset=createdEvents)
    createdEvents = filter.qs

    context = {'createdEvents': createdEvents, 'filter':filter}
    return render(request, 'my_events.html', context)


def delete_event_view(request):
    data = json.loads(request.body)
    if data['action'] == 'delete_booking':
        event = models.Events.objects.get(id=data['id'])
        event_name = event.eventName
        
        #check if there is any booked user first b4 deleting with
        booking = models.BookedEvent.objects.filter(event=event)
        if booking:
            emails = []
            print('booked by:',booking)
            for booked_event in booking:
                emails.append(booked_event.userEmail)
                
            # send emails to booked users
            message_title = f'{event_name} has been deleted by its owner'
            message = f'We are sorry to announce {event_name} event has been deleted by its owner'
            message_sender = 'awesomeferanmi@gmail.com'
            print(emails)
            send_mail(
                message_title,
                message,
                message_sender,
                emails,
                fail_silently=False, 
            )
        event.delete()
        return JsonResponse('Event was removed successfully', safe=False)


def booked_event_page_view(request):
    currentUser = request.user
    bookedEvents = models.BookedEvent.objects.filter(user=currentUser)

    # adding event filter
    filter = BookedEventFilter(request.GET, queryset=bookedEvents)
    bookedEvents = filter.qs

    context = {'bookedEvents': bookedEvents, 'filter':filter}
    return render(request, 'booked_events.html', context)


def create_event_page_view(request):
    currentUser = request.user
    initialUser = {'organizer': currentUser}
    if request.method == 'POST':
        createEventForm = forms.CreateEventForm(data=request.POST, files=request.FILES)
        if createEventForm.is_valid():
            createEventForm.save()
            return redirect('user_events')

    else:
        createEventForm = forms.CreateEventForm(initial=initialUser)

    context = {'createEventForm': createEventForm}
    return render(request, 'create_events.html', context)

