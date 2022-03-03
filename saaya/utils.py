import json
import requests as r
from collections import defaultdict as ddict
from saaya.logger import logger
from saaya.config import config_mg
import saaya.config as config


class Msg:

    def At(qq: list):
        return ''.join([f"[CQ:at,qq={i}]" for i in qq])

    def pic(url: str):
        # [CQ:image,file=http://baidu.com/1.jpg]
        # [CQ:image,file=file:///...]
        return f"[CQ:image,file={url}]"


def get(terminal, params):
    """
    add access_token to params
    and put infos to logger
    """
    params = ddict(lambda: None, params)
    url = config.base_url+terminal
    if not params['access_token']:
        params["access_token"] = config_mg.authKey
    if not terminal.startswith('/'):
        logger.error("terminal must be like '/xxxx' !!!")
    logger.debug(url)
    logger.debug(params)
    status = str(r.get(url, params=params))
    logger.debug(status)
