from saaya.plugin_manager import plugin_manager as PM
from saaya.event import Message
from saaya.utils import config_mg


@PM.reg_event('message.group.admin')
async def admin(event: Message):
    if event.msg == 'admin':
        event.back("u are admin")


@PM.reg_event('message')
async def ping(event: Message):
    if event.msg == 'ping':
        event.back("pong")


@PM.reg_event('message.private.admin.master')
async def get_admin(event: Message):
    if event.msg == "get_admin":
        event.back(config_mg.get_admin())


@PM.reg_event('message.private.admin.master')
async def add_admin(event: Message):
    if event.msg.startswith("add_admin"):
        uid = event.msg.replace(' ', '').replace("add_admin", '')
        try:
            config_mg.add_admin(int(uid))
            event.back("added")
        except:
            event.back('usage: add_admin <uid>, uid must be num!')


@PM.reg_event('message.private.admin.master')
async def rm_admin(event: Message):
    if event.msg.startswith("rm_admin"):
        uid = event.msg.replace(' ', '').replace("rm_admin", '')
        try:
            config_mg.rm_admin(int(uid))
            event.back("removed")
        except:
            event.back('usage: rm_admin <uid>, uid must be num!')

@PM.reg_event('message.group')
async def reply_me(event: Message):
    if event.msg.startswith("reply"):
        event.back("fuck you!",True)

