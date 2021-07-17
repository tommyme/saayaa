from saaya.bot import Bot
from config import data


if __name__ == '__main__':
    bot = Bot(data)  # 创建一个 Bot 实例
    bot.registerPlugins([
        'plugins.base.hello',
        'plugins.base.fudu'
    ])
    bot.loop()  # 开始监听事件循环
