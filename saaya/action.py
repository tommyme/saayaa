from saaya.utils import get

class Group_action:
    def __init__(self, group_id) -> None:
        self.gid = group_id

    def set_card(self, target, card):
        params = {
            "group_id": self.gid,
            "user_id": target,
            "card": card
        }
        get('/set_group_card', params)

    def mute(self, target, min=30):
        params = {
            "group_id": self.gid,
            "user_id": target,
            "duration": min*60
        }
        get("/set_group_ban", params)

class Message_action:
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

class Request_action:
    def __init__(self) -> None:
        pass

    def passNewFriend(flag):
        params = {
            "flag": flag
        }
        get('/set_friend_add_request', params)

    def passNewMember(sub_type, flag):
        params = {
            "flag": flag,
            "sub_type": sub_type
        }
        get("/set_group_add_request", params)
    
    def chehui(msg_id):
        get("/delete_msg", {"message_id":msg_id})
