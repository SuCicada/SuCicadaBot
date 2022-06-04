#!/usr/bin/env python3

from src.adapters.console import Adapter as ConsoleAdapter
from nonebot.adapters.telegram import Adapter as TelegramAdapter
from src.base_bot import BaseBot

bot = BaseBot(env_file="conf/.env.dev", adapters=[TelegramAdapter, ConsoleAdapter])
app = bot.get_app()

if __name__ == "__main__":
    bot.run()
