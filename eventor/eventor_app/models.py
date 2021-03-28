from django.db import models

# Create your models here.
class Users (models.Model):
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)

class Events(models.Model):
    organizer = models.ForeignKey(Users, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100, null=False)
    startDate = models.DateTimeField()
    starTime = models.CharField(max_length=5, default='00:00')
    endDate = models.DateField()
    address = models.CharField(max_length=200)
    eventDescription = models.CharField(max_length= 400, null=True, blank=True)
    eventImage = models.ImageField(upload_to='items')
    
class bookEvent(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    event = models.ForeignKey(Users, on_delete=models.CASCADE)
