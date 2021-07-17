from private import qq, passwd, authKey
data = {"addr": "localhost",
        "port": 5700,
        "ws_port": 5701,
        "authKey": authKey,
        "botqq": qq}
base_url = f"http://{data['addr']}:{data['port']}"


if __name__ == "__main__":
    with open("cqhttp/config.hjson", "r+", encoding="utf-8") as f:
        content = f.read()
    with open("cqhttp/config.hjson", "w", encoding="utf-8")as f:
        content = content.replace('access_token: "12345678"',
                                  f'access_token: "{authKey}"').replace('uin: 12345678',
                                                                        f'uin: {qq}').replace('password: "12345678"',
                                                                                              f'password: "{passwd}"')
        f.write(content)
