from saaya.pluginManager import PluginManager
from saaya.event import Message
from saaya.func.msg import MsgSender
from saaya.logger import logger


@PluginManager.registerEvent('message.group.admin')
def admin(event: Message):
    if event.data["raw_message"] == 'admin':
        target = event.data['group_id']
        ms = MsgSender('group', target, 'u are admin!')
        ms.send()


@PluginManager.registerEvent('message.private')
def ping(event: Message):
    if event.data["raw_message"] == 'ping':
        target = event.data['user_id']
        ms = MsgSender('private', target, 'pong')
        ms.send()
