from saaya.bot import Bot
import os
from threading import Thread

if __name__ == '__main__':
    t1 = Thread(target=os.system, args=('cd cqhttp && ./go-cqhttp faststart',))
    t1.start()
    bot = Bot()  # 创建一个 Bot 实例
    bot.register_plugins([
        'plugins.base.default',
        'plugins.daily.main',
        'plugins.get_out.main'
    ])
    bot.loop()  # 开始监听事件循环
