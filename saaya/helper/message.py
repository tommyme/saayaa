from .utils import get


class MsgHelper:
    def __init__(self, private: bool, target, content) -> None:
        self.type = "private" if private else "group"
        self.terminal = f"/send_{self.type}_msg"
        self.content = content
        self.target = target

    def send(self):
        xx_id = "user_id" if self.type.startswith("p") else "group_id"
        params = {
            xx_id: self.target,
            "message": self.content
        }
        get(self.terminal, params)
