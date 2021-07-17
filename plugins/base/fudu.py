from saaya.pluginManager import PluginManager
from saaya.event import Message
from saaya.func.msg import MsgSender


@PluginManager.registerEvent('message.group')
def hello(event: Message):
    if event.data["raw_message"].startswith("/echo"):
        target = event.data['group_id']

        try:
            msg = event.data["raw_message"].split("/echo")[1]
        except:
            msg = "fuck"
        ms = MsgSender('group', target, msg)
        ms.send()
