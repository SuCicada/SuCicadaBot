import time

import pytz
import tzlocal
from apscheduler.events import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from pydantic import Field

scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))


# scheduler.configure({"apscheduler.timezone": "Asia/Shanghai"})


# 通过 scheduled_job 装饰器添加
# @sched.scheduled_job('interval', seconds=5)
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


# scheduler.add_job(my_job, CronTrigger.from_crontab("* * * * *"))
# job = scheduler.get_jobs()[0]

def add():
    c = CronTrigger(minute="0,30", hour="*")
    @scheduler.scheduled_job(
        trigger=c,
        id="xxx",
        args=[1, 3],
        # kwargs={"arg2": 2}
    )
    # @scheduler.scheduled_job('interval', seconds=5, args=[1], kwargs={"arg2": 2})
    async def run_every_2_hour(arg1, arg2):
        print(arg1, arg2)


def run_every_day_from_program_start():
    print("run_every_day_from_program_start")


# scheduler.add_job(run_every_day_from_program_start, "interval", days=1, id="xxx")

def my_listener(event):
    if isinstance(event, JobEvent):
        job = scheduler.get_job(event.job_id)
        print(f"{job.name} next: {job.next_run_time}")


scheduler.add_listener(my_listener, EVENT_JOB_ADDED)


def test1():
    add()
    scheduler.start()


from croniter import croniter
from datetime import datetime, timezone

def test2():
    c = croniter('*/5 * * * *')
    res = c.get_next(datetime, start_time=datetime.now(pytz.timezone("Asia/Shanghai")))
    print(res)
    print(c.get_next(datetime))
    print(c.get_next(datetime))


# test2()
test1()
