import pytz
from croniter import croniter
from datetime import datetime, timezone


def show(cron):
    print(cron)
    c = croniter(cron)
    now_datetime = datetime.now(pytz.timezone("Asia/Shanghai"))
    start_of_day_datetime=now_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59, microsecond=999999)
    print("now", now_datetime)
    print("start", start_of_day_datetime)
    print("end", end_of_day_datetime)
    next_datetime = start_of_day_datetime
    while next_datetime <= end_of_day_datetime:
        next_datetime = c.get_next(datetime, start_time=next_datetime)
        print(next_datetime)


show('0,30 10-12,14-22 * * *')
