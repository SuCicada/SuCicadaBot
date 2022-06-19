import tzlocal
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.utils.export import export

scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))

export().scheduler = scheduler
export().scheduler_after = lambda i: print(i)
from .main import *

scheduler.start()
