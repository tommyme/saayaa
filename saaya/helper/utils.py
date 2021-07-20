import requests as r
from saaya.info import info
from saaya.utils import config
from collections import defaultdict as ddict
from saaya.logger import logger


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
    params = ddict(lambda: 0, params)
    url = info.base_url+terminal
    if params['access_token'] == 0:
        params["access_token"] = config.authKey
    if not terminal.startswith('/'):
        logger.error("terminal must be like '/xxxx' !!!")
    logger.debug(url)
    logger.debug(params)
    status = str(r.get(url, params=params))
    logger.debug(status)
