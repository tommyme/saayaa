import requests as r
from saaya.info import info
from private import authKey
from collections import defaultdict as ddict
from saaya.logger import logger


def get(terminal, params):
    """
    add access_token to params
    and put infos to logger
    """
    params = ddict(lambda: 0, params)
    url = info.base_url+terminal
    if params['access_token'] == 0:
        params["access_token"] = authKey
    if not terminal.startswith('/'):
        logger.error("terminal must be like '/xxxx' !!!")
    logger.debug(url)
    logger.debug(params)
    status = str(r.get(url, params=params))
    logger.debug(status)
