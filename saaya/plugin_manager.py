from __future__ import annotations
from saaya.event import Event
from collections import defaultdict as ddict
from saaya.logger import logger
import asyncio


class Base_manager:
    def __init__(self):
        self.plugins = ddict(lambda: None, {
            'OnLoad': []
        })
        # 这里一般使用'指纹'来添加事件类型
        # 你也可以手动添加事件类型，比如'Onload'
        self.strip = lambda x : x[:x.rfind('.')]

    def split_fp(self, fp):
        """
        turn 'a.b.c' -> ['a.b.c','a.b','a']
        """
        fps = []
        while(fp):
            fps.append(fp)
            fp = self.strip(fp)
        return fps


    async def broadcast(self, event: Event):
        """
        拥有'aaa.bbb.admin'指纹的event
        会先找对应的'aaa.bbb.admin'类型
        再找'aaa.bbb'类型
        再找'aaa'类型
        """
        origin_fp = event.fingerprint
        fps = self.split_fp(origin_fp)
        task_list = []
        for fp in fps:
            if self.plugins[fp]:
                for plugin in self.plugins[fp]:
                    logger.debug("broadcast to: "+str(plugin))
                    task_list.append(asyncio.create_task(plugin(event)))
                await asyncio.wait(task_list)

    def reg_event(self, fingerprint: str):
        def plugin(func):
            logger.debug(f'Registering {func} on {fingerprint}')
            if not self.plugins[fingerprint]:
                self.plugins[fingerprint] = []
            self.plugins[fingerprint].append(func)

        return plugin


plugin_manager = Base_manager()
