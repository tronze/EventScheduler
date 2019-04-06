from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from scheduler.controller import SchedulerHolder
from scheduler.models import Alarm


# Create your alarms here.


def alarm_event(event):
    print("Alarming Event")
    print("%s" % event.name)
    print("%s" % event.dt.astimezone().strftime("%Y년 %m월 %d일 %H시 %M분"))
    print()
    print()
    scheduler = SchedulerHolder.get_instance()
    scheduler.print_schedules()
    print()


@receiver(post_save, sender=Alarm)
def register_event_alarm(sender, instance, created, **kwargs):
    alarm = instance
    scheduler = SchedulerHolder.get_instance()
    if alarm.alarm_dt >= timezone.localtime():
        if created:
            print("Alarm Event: %s" % scheduler.schedule_event(aid=str(alarm.aid), dt=alarm.alarm_dt, event=alarm_event, args=[alarm.event]))
        else:
            print("Alarm Event: %s" % scheduler.update_event(aid=str(alarm.aid), dt=alarm.alarm_dt, event=alarm_event, args=[alarm.event]))
        scheduler.print_schedules()
    else:
        print("Alarm datetime is expired already.")
