import json
import traceback
from asyncio.exceptions import TimeoutError

import httpx
from httpx import ConnectTimeout
from loguru import logger
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import (
    ActionFailed,
    Bot,
    GroupMessageEvent,
    MessageEvent,
)
from nonebot.log import logger

from bot import driver

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


async def get_Pupu_msg():
    try:
        url = "https://v1.hitokoto.cn"
        params = {}
        client_default = httpx.AsyncClient()
        resp = await client_default.get(url, params=params, timeout=5)
        result = json.loads(resp.content)
        if resp.status_code == 200:
            return result["hitokoto"]
        else:
            return "噗噗出问题了>_<"
    except (TimeoutError, ConnectTimeout):
        logger.warning(traceback.format_exc())
    except Exception:
        logger.error(traceback.format_exc())
        return "噗噗出问题了>_<"
