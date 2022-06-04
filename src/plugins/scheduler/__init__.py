from apscheduler.events import EVENT_JOB_ADDED, JobEvent
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from nonebot import require
import nonebot_plugin_apscheduler
from src.utils.export import export
from src.utils import utils

scheduler: AsyncIOScheduler = require("nonebot_plugin_apscheduler").scheduler
export().scheduler = scheduler
async def scheduler_after(i):
    await utils.bot_send(i)
export().scheduler_after = scheduler_after

from . import main
