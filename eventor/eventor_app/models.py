from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE )
    eventName = models.CharField(max_length=100, null=False)
    startDate = models.DateTimeField(null=False)
    startTime = models.CharField(max_length=5, null= True, blank=True)
    endDate = models.DateTimeField(null=False)
    endTime = models.CharField(max_length=5, null= True, blank=True, default='00:00')    
    address = models.CharField(max_length=200)
    eventDescription = models.TextField( null=True, blank=True)
    eventImage = models.ImageField(null = True, blank = True)
    
    @property
    def imageUrl(self):
        try:
            url = f'/static{self.eventImage.url}'
            
        except:
            url = ''
        return url
    
    @property
    def getSummary(self):
        if len(self.eventDescription) > 104:
            try:
                summary = f'{self.eventDescription[0:104]}...'
            except:
                pass
        else:
            summary = f'{self.eventDescription}'
        return summary

    @property
    def isBooked(self):
        # check if event is in BookedEvent Table
        return BookedEvent.objects.filter(event = self).exists()
    
    def __str__(self):
        return self.eventName
    
class BookedEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    @property
    def userEmail(self):
        return self.user.email
        
    