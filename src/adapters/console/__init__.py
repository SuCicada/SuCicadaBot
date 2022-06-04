try:
    from nonebot.adapters.console import *
except ImportError:
    try:
        from nonebot_console_adapter.src.nonebot.adapters.console import *
    except ImportError:
        print("please git clone submodule")
