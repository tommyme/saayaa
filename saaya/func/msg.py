import requests as r
from saaya.info import info
from saaya.logger import logger
from private import authKey


class MsgSender:
    def __init__(self, type, target, content) -> None:
        assert(type in ["private", "group"])
        self.type = type
        self.terminal = f"/send_{self.type}_msg"
        self.content = content
        self.target = target

    def send(self):
        xx_id = "user_id" if self.type.startswith("p") else "group_id"
        params = {
            "access_token": authKey,
            xx_id: self.target,
            "message": self.content
        }
        logger.debug(info.base_url+self.terminal, params)
        r.get(info.base_url+self.terminal, params=params)

    def At(qq: list):
        return ''.join([f"[CQ:at,qq={i}]" for i in qq])

    def pic(url: str):
        # [CQ:image,file=http://baidu.com/1.jpg]
        # [CQ:image,file=file:///...]
        return f"[CQ:image,file={url}]"
