from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        import scheduler.alarms
