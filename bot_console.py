#!/usr/bin/env python3

from src.adapters.console import Adapter as ConsoleAdapter
from src.base_bot import BaseBot

bot = BaseBot(env_file="conf/.env.console", adapters=[ConsoleAdapter])
app = bot.get_app()

if __name__ == "__main__":
    bot.run()
