from saaya.pluginManager import PluginManager as PM
from saaya.event import Message
from saaya.utils import config


@PM.registerEvent('message.group.admin')
async def admin(event: Message):
    if event.msg == 'admin':
        event.back("u are admin")


@PM.registerEvent('message')
async def ping(event: Message):
    if event.msg == 'ping':
        event.back("pong")


@PM.registerEvent('message.private.admin.master')
async def get_admin(event: Message):
    if event.msg == "get_admin":
        event.back(config.get_admin())


@PM.registerEvent('message.private.admin.master')
async def add_admin(event: Message):
    if event.msg.startswith("add_admin"):
        uid = event.msg.replace(' ', '').replace("add_admin", '')
        try:
            config.add_admin(int(uid))
            event.back("added")
        except:
            event.back('usage: add_admin <uid>, uid must be num!')


@PM.registerEvent('message.private.admin.master')
async def rm_admin(event: Message):
    if event.msg.startswith("rm_admin"):
        uid = event.msg.replace(' ', '').replace("rm_admin", '')
        try:
            config.rm_admin(int(uid))
            event.back("removed")
        except:
            event.back('usage: rm_admin <uid>, uid must be num!')
