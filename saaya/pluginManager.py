from __future__ import annotations

import asyncio

from saaya.event import Event, Message, Notice, Request, Unknown
from collections import defaultdict as ddict


class BaseManager:
    plugins = {}

    def __init__(self):
        self.plugins = ddict(lambda: 0, {
            'OnLoad': []
        })
        # 这里一般使用'指纹'来添加事件类型
        # 你也可以手动添加事件类型，比如'Onload'

    def broadCast(self, event: Event):
        fp = event.fingerprint
        if self.plugins[fp] != 0:
            for plugin in self.plugins[fp]:
                plugin(event)

    def registerEvent(self, fingerprint: str):
        def plugin(func):
            print(f'Registering {func} on {fingerprint}')
            if self.plugins[fingerprint] == 0:
                self.plugins[fingerprint] = []
            self.plugins[fingerprint].append(func)

        return plugin


PluginManager = BaseManager()
