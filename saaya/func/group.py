from .utils import get


class groupHelper:
    def __init__(self, group_id) -> None:
        self.gid = group_id

    def set_card(self, target, card):
        params = {
            "group_id": self.gid,
            "user_id": target,
            "card": card
        }
        get('/set_group_card', params)
