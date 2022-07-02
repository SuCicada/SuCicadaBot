from datetime import datetime

import pytz
from apscheduler.events import EVENT_JOB_ADDED, JobEvent
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from src.utils.export import export
from typing import Callable

scheduler: AsyncIOScheduler = export().scheduler
scheduler_after: Callable = export().scheduler_after


class Job:
    def __init__(self, cron, *args):
        self.cron = cron
        self.args = args


scheduler_list = [
    Job("00 08 * * *", *["起床了吗"]),
    Job("10 09 * * *", *["吃早饭"]),
    Job("30 12 * * *", *["滚去吃午饭"]),
    Job("00 19 * * *", *["滚去吃晚饭"]),

    Job(" 0,30 10-12,14-23 * * *", *["起来休息活动一下,并且补充水杯"]),
    Job(" 0 0 * * *", *["起来休息活动一下,并且补充水杯"]),
    Job(" 0 21 * * *", *["当日运动, 耗时30min"]),
    Job("30 00 * * *", *["你该睡觉呢"]),
    Job("00 01 * * *", *["滚去睡觉了吧"]),
    # Job(CronTrigger(second="*/5", minute='*'), "test 测试我是谁，"),
]

timezone = pytz.timezone("Asia/Shanghai")
for scheduler_info in scheduler_list:
    cron = scheduler_info.cron
    trigger = None
    if isinstance(cron, str):
        trigger = CronTrigger.from_crontab(cron, timezone)
    elif isinstance(cron, CronTrigger):
        trigger = cron


    @scheduler.scheduled_job(
        trigger=trigger,
        args=scheduler_info.args
    )
    async def run_alert(alert_msg):
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = f"{alert_msg}\n{now_time}"
        print(msg)
        await scheduler_after(msg)


def listener_add_job(event):
    if isinstance(event, JobEvent):
        job = scheduler.get_job(event.job_id)
        print(f"{job.name} next: {job.next_run_time}")


scheduler.add_listener(listener_add_job, EVENT_JOB_ADDED)

print("scheduler load over ")
