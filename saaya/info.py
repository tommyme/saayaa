class Info:
    """
    saayaa运行中需要使用到的信息
    """

    def __init__(self) -> None:
        self.ws_addr = "0.0.0.0"
        self.ws_port = 5701
        self.port = 5700
        self.addr = "localhost"
        self.base_url = f"http://{self.addr}:{self.port}"


info = Info()
