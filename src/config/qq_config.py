import nonebot

__all__ = [
    "master_code"
]
__config = nonebot.get_driver().config
master_code = __config.master_code
