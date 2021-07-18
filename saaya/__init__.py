from saaya.logger import logger
import logging

# 日志级别，logger 和 handler以最高级别为准，不同handler之间可以不一样，不相互影响
logger.setLevel(logging.DEBUG)

version = '0.1.0 dev'
logger.info(f'Welcome to use saayaa({version}) based on mirai!')
