from django import forms
from .models import Events
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['eventName'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'event name'
        })

        self.fields['endDate'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'enter address'
        })

        self.fields['eventDescription'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'enter event description'
        })

        self.fields['eventImage'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['organizer'].widget = forms.HiddenInput()

    startDate = forms.DateField(widget=DateInput, label='Start date')
    startDate.widget.attrs.update({'class': 'form-control'})

    endDate = forms.DateField(widget=DateInput, label='End date')
    endDate.widget.attrs.update({'class': 'form-control'})

    startTime = forms.CharField(label='Start time')
    startTime.widget.attrs.update({
        'class': 'form-control',
        'placeholder': '00:00'})

    endTime = forms.CharField(label='End time')
    endTime.widget.attrs.update({
        'class': 'form-control',
        'placeholder': '00:00'
    })

    class Meta:
        model = Events
        fields = '__all__'
        labels = {
            'eventName': 'Event name',
            'eventDescription': 'Event description',
            'eventImage': 'Event image'
        }


