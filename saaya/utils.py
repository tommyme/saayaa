import json


def strip(fp):
    return '.'.join(fp.split('.')[:-1])


def FingerPrints(fp):
    fps = []
    while(fp != ''):
        fps.append(fp)
        fp = strip(fp)
    return fps


class Config:
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
        return str(self.admin)

    def add_admin(self, uid: int):
        self.data['admin'].append(uid)
        self.write()

    def rm_admin(self, uid: int):
        self.data['admin'].remove(uid)
        self.write()


config = Config()
