import logging
import colorlog

log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

logger = logging.getLogger('saayaa_logger')

# 输出到控制台
ch = logging.StreamHandler()
# 输出到文件
fh = logging.FileHandler(
    filename="saayaa.log", mode='a', encoding='utf8')

ch.setLevel(logging.DEBUG)
fh.setLevel(logging.INFO)

# 日志输出格式
file_formatter = logging.Formatter(
    fmt='[%(asctime)s.%(msecs)03d %(filename)s] [%(levelname)s] : %(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S'
)
console_formatter = colorlog.ColoredFormatter(
    fmt='%(log_color)s[%(asctime)s.%(msecs)03d %(filename)s] [%(levelname)s] : %(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S',
    log_colors=log_colors_config
)
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

# 重复日志问题：
# 1、防止多次addHandler；
# 2、loggername 保证每次添加的时候不一样；
# 3、显示完log之后调用removeHandler

if not logger.handlers:
    logger.addHandler(ch)
    logger.addHandler(fh)

ch.close()
fh.close()
