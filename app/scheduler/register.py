from apscheduler.schedulers.background import BackgroundScheduler

from app.scheduler.jobs import SampleJob, send_scheduled_messages

scheduler = BackgroundScheduler() 

def register_jobs(scheduler: BackgroundScheduler):
    scheduler.add_job(send_scheduled_messages, "interval", minutes=15)
    scheduler.add_job(SampleJob, "interval", seconds=10)
