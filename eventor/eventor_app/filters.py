import django_filters
from django_filters import DateFilter

from .models import Events, BookedEvent

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Events
        fields = ['eventName', 'startDate', 'endDate', 'address']


class BookedEventFilter(django_filters.FilterSet):
    eventName = django_filters.CharFilter(field_name='event__eventName', label='Event name')
    startDate = DateFilter(field_name='event__startDate', label='Date')
    address = DateFilter(field_name='event__address', label='Location')
    class Meta:
        model = BookedEvent
        fields = ['eventName', 'startDate', 'address']
