import uuid

from django.db import models
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    dt = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return "[%s] %s" % (self.dt.astimezone().strftime("%Y년 %m월 %d일 %H시 %M분"), self.name)


class Alarm(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    aid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    alarm_dt = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return "[%s]" % self.alarm_dt.astimezone().strftime("%Y년 %m월 %d일 %H시 %M분")
