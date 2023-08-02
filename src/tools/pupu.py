import json
import traceback
from asyncio.exceptions import TimeoutError

import httpx
from httpx import ConnectTimeout
from loguru import logger

from nonebot.log import logger
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
