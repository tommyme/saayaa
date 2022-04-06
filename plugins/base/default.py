from saaya.plugin_manager import plugin_manager as PM
from saaya.event import Message
from saaya.utils import config_mg, re_filter
from saaya.action import Message_action
from saaya.config import config_mg
from saaya.bot import Bot
from saaya.utils import get_bot

@PM.reg_event('message.group.admin')
@re_filter("^admin$")
async def admin(event: Message):
    event.back("u are admin")


@PM.reg_event('message')
@re_filter("^ping$")
async def ping(event: Message):
    event.back("pong")


@PM.reg_event('message.private.admin.master')
@re_filter("^(get|add|rm)\ admin")
async def op_admin(event: Message):
    if event.msg.startswith("get"):
        event.back(config_mg.get_admin())
    elif event.msg.startswith("add"):
        uid = event.msg.split()[-1]
        try:
            config_mg.add_admin(int(uid))
            event.back("added")
        except:
            event.back('usage: add_admin <uid>, uid must be num!')
    elif event.msg.startswith("rm"):
        uid = event.msg.split()[-1]
        try:
            config_mg.rm_admin(int(uid))
            event.back("removed")
        except:
            event.back('usage: rm_admin <uid>, uid must be num!')

@PM.reg_event('message.group')
@re_filter("^reply$")
async def reply_me(event: Message):
    event.back("just replied",True)

@PM.reg_event("Boot")
async def hello():
    Message_action(True, config_mg.master, "hello").send()

@PM.reg_event("message.private.admin.master")
@re_filter("^reload$")
async def reload(event):
    bot = get_bot()
    await bot.register_plugins()
    event.back("reloaded")

