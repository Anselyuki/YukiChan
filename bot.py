import traceback

import nonebot
from nonebot import on_fullmatch, logger
from nonebot.adapters.onebot.v11 import Adapter
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import (
    ActionFailed,
    Bot,
    GroupMessageEvent,
    MessageEvent,
)

from src.tools.pupu import get_Pupu_msg

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(Adapter)
driver.config.help_text = {}

nonebot.load_plugins("src/maimaidx")

bot_pupu = on_fullmatch("噗噗", block=False, priority=5)


@bot_pupu.handle()
async def send_pupu_msg(ev: MessageEvent, bot: Bot):
    try:
        if driver.config.pupu:
            msg = await get_Pupu_msg()
            await bot.send(ev, msg)
    except ActionFailed:
        logger.warning(traceback.format_exc())
        try:
            await bot.send(ev, "噗噗寄了>_<可能被风控了QAQ")
        except Exception:
            pass
        return


if __name__ == "__main__":
    nonebot.run()
