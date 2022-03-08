import json
class Config_manager:
    def __init__(self) -> None:
        self.root = 'private.json'
        self.data = json.load(open(self.root, 'r'))
        self.authKey = self.data["authKey"]
        self.master = self.data['master']
        self.admin = self.data["admin"]

    def reload(self):
        self.data = json.load(open(self.root, 'r'))
        self.authKey = self.data["authKey"]
        self.master = self.data['master']
        self.admin = self.data["admin"]

    def write(self):
        json.dump(self.data, open(self.root, 'w'), indent=4)

    def get_admin(self):
        return str(self.admin)[1:-1]

    def add_admin(self, uid: int):
        self.data['admin'].append(uid)
        self.write()

    def rm_admin(self, uid: int):
        self.data['admin'].remove(uid)
        self.write()


config_mg = Config_manager()

ws_addr = "0.0.0.0"
ws_port = 5701
port = 5700
addr = "localhost"
base_url = f"http://{addr}:{port}"

# class Info:
#     def __init__(self) -> None:
#         self.ws_addr = "0.0.0.0"
#         self.ws_port = 5701
#         self.port = 5700
#         self.addr = "localhost"
#         self.base_url = f"http://{self.addr}:{self.port}"
# info = Info()
