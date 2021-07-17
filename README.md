# saayaa -- 力求打造 简单 易上手 的机器人框架



### 简介

#### **saayaa力求简单，核心代码目前只有150行左右**

saayaa灵感源于好友[jerrita的saaya框架](https://github.com/jerrita/saaya) 阅读了大佬的源码，自己决定手撸一个。

saayaa基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 不用Mirai是因为我使用mirai的时候登陆不上去...

go-cqhttp有二维码登录功能，大大降低了登录难度。

### 快速使用（for 萌新）

1. 在你的电脑上使用go-cqhttp登录你的qq（参考[go-cqhttp官网教程](https://github.com/Mrs4s/go-cqhttp)）
   1. 建议选择扫码登录
   2. 本步骤会产生device.json和config.hjson
2. 把第一步生成的 device.json 和 config.hjson 放到本项目内 并且转到下面的步骤👇

### 快速使用（for old_driver）

1. 创建private.py并且写入qq  passwd  authKey
2. 运行config.py
3. 运行代码：

```
docker-compose up -d
```

### 框架概念

1. fingerprint（指纹）
   1. 目前打算实现的指纹位于fingerprint.py中
2. ...待补充...