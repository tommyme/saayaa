import requests as r
from config import base_url, data


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
            "access_token": data['authKey'],
            xx_id: self.target,
            "message": self.content
        }
        print(base_url+self.terminal, params)
        r.get(base_url+self.terminal, params=params)
