#!/usr/bin/env python3

from nonebot.adapters.onebot import V11Adapter as ONEBOT_V11Adapter
from src.base_bot import BaseBot


bot = BaseBot(env_file="conf/.env.qq", adapters=[ONEBOT_V11Adapter])
app = bot.get_app()

if __name__ == "__main__":
    bot.run()
