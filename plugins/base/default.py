from saaya.pluginManager import PluginManager
from saaya.event import Message


@PluginManager.registerEvent('message.group.admin')
def admin(event: Message):
    if event.msg == 'admin':
        event.back("u are admin")


@PluginManager.registerEvent('message.private')
def ping(event: Message):
    if event.msg == 'ping':
        event.back("pong")
