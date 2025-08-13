from apscheduler.schedulers.background import BackgroundScheduler

from app.scheduler.jobs import SampleJob, SendScheduledMessages

scheduler = BackgroundScheduler() 

def register_jobs(scheduler: BackgroundScheduler):
    scheduler.add_job(SendScheduledMessages, "interval", minutes=15)
    scheduler.add_job(SampleJob, "interval", seconds=10)
    #scheduler.add_job(job_two, "interval", hours=1)
    #scheduler.add_job(job_three, "cron", day_of_week='mon', hour=8)