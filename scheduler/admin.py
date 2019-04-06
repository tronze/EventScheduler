from django.contrib import admin
from scheduler.models import Event, Alarm

# Register your models here.
admin.site.register(Event)
admin.site.register(Alarm)
