from .utils import get


class requestHelper:
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
