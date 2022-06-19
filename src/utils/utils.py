from typing import Optional, Union

from nonebot.adapters.telegram.event import Event as TelegramEvent, EventWithChat, PrivateMessageEvent, MessageEvent
import nonebot
from loguru import logger
from nonebot.adapters import Bot
from nonebot.adapters.telegram.model import Chat
from nonebot.internal.adapter import Event
from loguru import logger

from src.adapters.console import Bot as ConsoleBot
from nonebot.adapters.telegram import Bot as TelegramBot
from nonebot.adapters.onebot import V11Bot as ONEBOT_V11Bot


# def get_event(bot) -> Union[Event, None]:
#     if isinstance(bot, TelegramBot):
#         from src.config import telegram_config
#         return MessageEvent(
#             message_id=0, date=0,
#             chat=Chat(
#                 type="private",
#                 id=telegram_config.telegram_chat))
#
#     elif isinstance(bot, ONEBOT_V11Bot):
#         from src.config import qq_config
#
#         qq_config.master_code
#
#     elif isinstance(bot, ConsoleBot):
#         return None

# noinspection PyTypeChecker
async def bot_send(msg):
    # bot = None
    # while bot is None:
    bot = get_bot()
    if bot:
        if isinstance(bot, TelegramBot):
            bot: TelegramBot = bot
            from src.config import telegram_config
            event: Event = MessageEvent(
                message_id=0, date=0,
                chat=Chat(
                    type="private",
                    id=telegram_config.telegram_chat))
            await bot.send(event=event, message=msg)

        elif isinstance(bot, ONEBOT_V11Bot):
            bot: ONEBOT_V11Bot = bot
            from src.config import qq_config
            await bot.send_msg(user_id=qq_config.master_code,
                               message=msg)

        elif isinstance(bot, ConsoleBot):
            bot: ConsoleBot = bot
            await bot.send(message=msg)

    else:
        logger.info("bot is not exist")


def get_bot() -> Optional[Bot]:
    """
    说明：
        获取 bot 对象
    """
    try:
        return list(nonebot.get_bots().values())[0]
    except IndexError:
        return None
