from saaya.pluginManager import PluginManager
from saaya.event import Message
from saaya.func.msg import MsgSender


@PluginManager.registerEvent('message.group')
def hello(event: Message):
    if event.data["raw_message"] == 'ping':
        print(event.data)
        target = event.data['group_id']
        ms = MsgSender('group', target, 'pong')
        ms.send()
