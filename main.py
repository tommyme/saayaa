from saaya.bot import Bot
import os
from threading import Thread
import asyncio

if __name__ == '__main__':
    t1 = Thread(target=os.system, args=('cd cqhttp && ./go-cqhttp -faststart',))
    t1.start()
    bot = Bot()  # 创建一个 Bot 实例
    bot.store_bot()  # 将 bot 存储到 bot_store 中
    asyncio.run(
        bot.register_plugins([
        'plugins.base.default',
        'plugins.daily.main',
        'plugins.get_out.main'
        ])
    )
    bot.wait4online()
    asyncio.run(bot.boot_hook())
    bot.loop()  # 开始监听事件循环
