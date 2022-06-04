from typing import Optional

from nonebot.adapters.telegram.event import Event as TelegramEvent, EventWithChat, PrivateMessageEvent, MessageEvent
import nonebot
from loguru import logger
from nonebot.adapters import Bot
from nonebot.adapters.telegram.model import Chat
from nonebot.internal.adapter import Event
from loguru import logger

from src.adapters.console import Bot as ConsoleBot
from nonebot.adapters.telegram import Bot as TelegramBot


def get_event(bot) -> Event | None:
    if isinstance(bot, TelegramBot):
        from src.config import telegram_config
        return MessageEvent(
            message_id=0, date=0,
            chat=Chat(
                type="private",
                id=telegram_config.telegram_chat))
    elif isinstance(bot, ConsoleBot):
        return None


async def bot_send(msg):
    # bot = None
    # while bot is None:
    bot = get_bot()
    event: Event = get_event(bot)
    if bot:
        await bot.send(event=event, message=msg)
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
