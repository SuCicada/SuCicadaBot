#!/usr/bin/env python3
import os
import sys
from typing import Type
from loguru import logger

import nonebot
from nonebot.adapters.telegram import Adapter as TelegramAdapter
from nonebot.internal.adapter import Adapter


class BaseBot:
    app = None
    name = "bot"

    def __init__(self,
                 adapters: [Type["Adapter"]],
                 env_file=None,
                 ):
        self.adapters = adapters
        self.env_file = env_file
        if env_file is not None:
            self.name = os.path.basename(sys.argv[0])[:-3]
            os.environ["ENVIRONMENT"] = self.name

    def init(self):
        nonebot.init(_env_file=self.env_file)
        driver = nonebot.get_driver()
        for adapter in self.adapters:
            driver.register_adapter(adapter)

        nonebot.load_builtin_plugins("echo")
        # os.chdir("../")
        toml = f"{os.path.dirname(__file__)}/../pyproject.toml"
        print("toml", toml)
        nonebot.load_from_toml(toml)

    def get_app(self):
        return self.app

    def run(self):
        self.init()
        self.app = nonebot.get_asgi()

        # nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
        # app_name = f"{os.path.basename(__file__)[:-3]}:app"
        app_name = f"{self.name}:app"
        logger.info(f"app_name: {app_name}")

        # nonebot.run(app=app_name)
        nonebot.run()
        # nonebot.run(app="__mp_main__:app")
