#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import nonebot
from nonebot.adapters.telegram import Adapter as TelegramAdapter
from src.adapter.console import Adapter as ConsoleAdapter

nonebot.init(_env_file="../.env.telegram")
app = nonebot.get_asgi()

driver = nonebot.get_driver()
# driver.register_adapter(ConsoleAdapter)
driver.register_adapter(TelegramAdapter)

nonebot.load_builtin_plugins("echo")
os.chdir("../")
nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
