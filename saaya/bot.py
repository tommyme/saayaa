import asyncio
import logging
import websockets
from collections import defaultdict as ddict
from saaya.event import Message, Notice, Request, Unknown
import json
from saaya.pluginManager import PluginManager
from saaya.logger import logger
from saaya.info import info


class Bot:
    def __init__(self):
        logger.info('Bot initialized.')

    def loop(self):
        logger.info("start Loop!")

        async def getMsg(websocket, path):
            while 1:
                msg = await websocket.recv()
                await self.processor(msg)

        async def main():
            async with websockets.serve(getMsg, info.ws_addr, info.ws_port) as ws:
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
        await PluginManager.broadCast(event)

    def registerPlugins(self, plugins: list):
        for plugin in plugins:
            logger.info(f'Loading plugin: {plugin}')
            try:
                __import__(plugin)
            except Exception as e:
                logger.error(e)

        # 处理 OnLoad
        for func in PluginManager.plugins['OnLoad']:
            try:
                logger.debug(f'Calling OnLoad func from {func}')
                func(self)
            except Exception as e:
                logger.error(e)
