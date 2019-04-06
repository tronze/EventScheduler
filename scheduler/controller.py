from apscheduler.schedulers.background import BackgroundScheduler

# Create your controller here.


class Scheduler:
    scheduler = None

    def __init__(self) -> None:
        super().__init__()
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.print_schedules()

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        self.scheduler.shutdown()

    def schedule_event(self, aid, dt, event, args):
        scheduled = self.scheduler.add_job(func=event, trigger='date', id=aid, run_date=dt, args=args)
        return scheduled.id

    def update_event(self, aid, dt, event, args):
        scheduled = self.scheduler.get_job(job_id=aid)
        if scheduled:
            return scheduled.id
        else:
            return self.schedule_event(aid=aid, dt=dt, event=event, args=args)

    def print_schedules(self):
        return self.scheduler.print_jobs()


class SchedulerHolder:

    _scheduler = None

    @staticmethod
    def get_instance():
        if not SchedulerHolder._scheduler:
            SchedulerHolder._scheduler = Scheduler()
        return SchedulerHolder._scheduler
