from django.contrib import admin
from .models import Events, BookedEvent, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Events)
admin.site.register(BookedEvent)
