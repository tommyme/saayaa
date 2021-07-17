# Event,Message,Notice,Request,Unknown
class Event:
    def __init__(self, base_type, data) -> None:
        self.type = data[base_type+"_type"]
        self.fingerprint = '.'.join([base_type, self.type])
        self.data = data


class Message(Event):
    def __init__(self, data) -> None:
        super().__init__("message", data)

        self.sender = data['sender']


class Notice(Event):
    def __init__(self, data) -> None:
        super().__init__("notice", data)


class Request(Event):
    def __init__(self, data) -> None:
        super().__init__("request", data)


class Unknown(Event):
    def __init__(self, data) -> None:
        super().__init__("unknown", data)
