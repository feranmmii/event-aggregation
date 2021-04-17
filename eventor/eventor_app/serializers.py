from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Events, BookedEvent

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: User
        fields = ['url', 'username', 'email', 'password']

class EventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ['id','url', 'eventName', 'startDate', 'startTime', 'endDate', 'endTime', 'address', 'eventDescription', 'eventImage']


class BookedEventserializers (serializers.HyperlinkedModelSerializer):
        class Meta:
            model = BookedEvent
            fields = ['id','event']