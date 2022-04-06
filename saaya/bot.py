import asyncio
import logging
import websockets
from collections import defaultdict as ddict
from saaya.event import Message, Notice, Request, Unknown
import json
from saaya.plugin_manager import plugin_manager
from saaya.logger import logger
from saaya import config
from saaya.utils import bot_store, get
import time


class Bot:
    def __init__(self):
        logger.info('Bot initialized.')
        self.cached_plugins = []

    def loop(self):
        logger.info("start Loop!")

        async def getMsg(websocket, path):
            while 1:
                msg = await websocket.recv()
                await self.processor(msg)

        async def main():
            async with websockets.serve(getMsg, config.ws_addr, config.ws_port) as ws:
                await asyncio.Future()

        asyncio.run(main())

    async def processor(self, msg):
        msg = ddict(lambda: "unknown", json.loads(msg))
        switch, default = {
            "message": Message,
            "notice": Notice,
            "request": Request
        }, Unknown
        event = switch.get(msg['post_type'], default)(msg)
        logger.debug(event.fingerprint) if not event.fingerprint.startswith(
            "u") else None
        await plugin_manager.broadcast(event)

    async def register_plugins(self, plugins: list=[]):
        if self.cached_plugins:
            plugins = self.cached_plugins
            
        for plugin in plugins:
            logger.info(f'Loading plugin: {plugin}')
            try:
                __import__(plugin)
            except Exception as e:
                logger.error(e)
        
        self.cached_plugins = plugins

    def wait4online(self):
        while True:
            # https://docs.go-cqhttp.org/api/#获取状态
            try:
                logger.debug("waiting for online...")
                resp = get("/get_status").json()
                if resp["data"]["online"]:
                    return True
            except:
                logger.debug("sleeping...")
                time.sleep(0.5)


    async def boot_hook(self):
        # boot 
        asyncio.gather(
            *[func() for func in plugin_manager.plugins['Boot']]
        )

    def store_bot(self):
        bot_store.bot = self