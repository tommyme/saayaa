from saaya.bot import Bot


if __name__ == '__main__':
    bot = Bot()  # 创建一个 Bot 实例
    bot.register_plugins([
        'plugins.base.default',
        'plugins.daily.main',
        'plugins.get_out.main'
    ])
    bot.loop()  # 开始监听事件循环
