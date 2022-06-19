from nonebot import get_driver

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

from nonebot.rule import to_me
from nonebot.adapters import *
from nonebot.plugin import *

SayakaBot = on_command('', rule=to_me(), priority=5)



@SayakaBot.handle()
async def handle_first_receive(bot: Bot, event: Event):
    # print(bot)
    # print(event)
    # f"你说了：{event.get_message()}"
    await SayakaBot.send("嗯")

# async def test():
#     while True:
#         await asyncio.sleep(1)
#         await utils.bot_send("bot 上线了")
#         print("en")
# # asyncio.run(test ())
print("load")
