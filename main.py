from saaya.bot import Bot


if __name__ == '__main__':
    bot = Bot()  # 创建一个 Bot 实例
    bot.registerPlugins([
        'plugins.base.default',
    ])
    bot.loop()  # 开始监听事件循环
