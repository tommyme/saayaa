# Event,Message,Notice,Request,Unknown
from saaya.config import config_mg


class Event:
    def __init__(self, base_type, data) -> None:
        self.type = data[base_type+"_type"]
        self.fingerprint = '.'.join([base_type, self.type])
        self.data = data


class Message(Event):
    def __init__(self, data) -> None:
        super().__init__("message", data)

        self.sender_id = data['sender']['user_id']  # int
        self.group_id = data['group_id']  # 如果不存在的话就是'unknown'
        self.msg = data["raw_message"]
        self.message_id = data['message_id']
        self.message = data['message']

        if self.sender_id in config_mg.admin:
            self.fingerprint += ".admin"
        if self.sender_id == config_mg.master:
            self.fingerprint += ".master"

    def back(self, content, reply=False):
        from saaya.action import Message_action
        p = True if 'private' in self.fingerprint else False
        sender = self.sender_id if p else self.group_id
        content = f"[CQ:reply,id={self.message_id}]{content}" if reply else content
        Message_action(p, sender, content).send()
    
    def delete(self):
        from saaya.action import Request_action
        Request_action.chehui(self.message_id)


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

    def info_new_friend(self):
        return self.data['user_id'], self.data['comment'], self.data['flag']

    def info_new_member(self):
        pass


class Unknown(Event):
    def __init__(self, data) -> None:
        super().__init__("unknown", data)
