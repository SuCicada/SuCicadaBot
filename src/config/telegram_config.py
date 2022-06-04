import nonebot

__all__ = [
    "telegram_chat"
]
__config = nonebot.get_driver().config
telegram_chat = __config.telegram_chat
