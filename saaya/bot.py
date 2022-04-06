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
import importlib


class Bot:
    def __init__(self):
        logger.info('Bot initialized.')
        # self.cached_plugins = []
        self.loaded_modules = []
        self.plugins_loaded = False

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
        plugin_manager.plugins = ddict(list) # clear plugins
        if self.plugins_loaded: # reload plugins
            logger.info(f'reLoading plugins...')
            for i in self.loaded_modules:
                importlib.reload(i)
        else:   # load plugins
            for plugin in plugins:
                logger.info(f'Loading plugin: {plugin}')
                try:
                    self.loaded_modules.append(importlib.import_module(plugin))
                except Exception as e:
                    logger.error(e)
        
        self.plugins_loaded = True

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