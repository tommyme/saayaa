# Event,Message,Notice,Request,Unknown
from private import admin


class Event:
    def __init__(self, base_type, data) -> None:
        self.type = data[base_type+"_type"]
        self.fingerprint = '.'.join([base_type, self.type])
        self.data = data


class Message(Event):
    def __init__(self, data) -> None:
        super().__init__("message", data)

        self.sender_id = data['sender']['user_id']
        self.group_id = data['group_id']  # 如果不存在的话就是‘unknown’
        self.msg = data["raw_message"]

        if self.sender_id in admin:
            self.fingerprint += ".admin"

    def back(self, content):
        from saaya.func.msg import MsgSender
        p = True if 'private' in self.fingerprint else False
        sender = self.sender_id if p else self.group_id
        MsgSender(p, sender, content).send()


class Notice(Event):
    def __init__(self, data) -> None:
        super().__init__("notice", data)

    def get_id(self):
        try:
            return self.data["group_id"], self.data['user_id']
        except:
            return 0, 0


class Request(Event):
    def __init__(self, data) -> None:
        super().__init__("request", data)


class Unknown(Event):
    def __init__(self, data) -> None:
        super().__init__("unknown", data)
