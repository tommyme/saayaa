import asyncio
import websockets
from collections import defaultdict as ddict
from saaya.event import Message, Notice, Request, Unknown
import json
from saaya.pluginManager import PluginManager


class Bot:
    def __init__(self, data):
        self.__dict__.update(data)
        print('Bot initialized.')

    def loop(self):
        print("start Loop!")

        async def getMsg(websocket, path):
            while 1:
                msg = await websocket.recv()
                self.processor(msg)

        async def main():
            async with websockets.serve(getMsg, self.addr, self.ws_port) as ws:
                await asyncio.Future()

        asyncio.run(main())

    def processor(self, msg):
        msg = ddict(lambda: "unknown", json.loads(msg))
        switch, default = {
            "message": Message,
            "notice": Notice,
            "request": Request
        }, Unknown
        event = switch.get(msg['post_type'], default)(msg)
        print(event.fingerprint) if not event.fingerprint.startswith("u") else None
        PluginManager.broadCast(event)

    def registerPlugins(self, plugins: list):
        for plugin in plugins:
            print(f'Loading plugin: {plugin}')
            try:
                __import__(plugin)
            except Exception as e:
                print(e)

        # 处理 OnLoad
        for func in PluginManager.plugins['OnLoad']:
            try:
                print(f'Calling OnLoad func from {func}')
                func(self)
            except Exception as e:
                print(e)
