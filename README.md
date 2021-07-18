## saayaa -- 力求打造 简单 易上手 的机器人框架



### 简介

#### **saayaa力求简单，核心代码目前只有150行左右**

saayaa灵感源于好友[jerrita的saaya框架](https://github.com/jerrita/saaya) 阅读了大佬的源码，自己决定手撸一个。

saayaa基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 不用Mirai是因为我使用mirai的时候登陆不上去...

go-cqhttp有二维码登录功能，大大降低了登录难度。

### TODO_LIST

- [x] logger（彩色）
- [x]  @和pic消息类型支持
- [x] 版本适配 -- [v1.0.0-beta4
- [x] 权限管理
- [x] 三级指纹事件处理
- [ ] 异步支持
- [ ] nonebot迁移
- [ ] saayaa通知板
- [ ] 定时任务模块支持

### 快速使用（for 萌新）

1. 在你的电脑上使用go-cqhttp登录你的qq（参考[go-cqhttp官网教程](https://github.com/Mrs4s/go-cqhttp)）
   1. 建议选择扫码登录
   2. 本步骤会产生device.json和config.yml
2. 把第一步生成的 device.json 和 config.yml 放到本项目的cqhttp目录内 并且转到下面的步骤👇

### 快速使用（for old_driver）

1. 创建private.py并且写入qq  passwd  authKey
2. 运行config.py
3. 运行代码：

```
docker-compose up -d
```

### 框架概念

1. Event（事件）
   1. 目前打算实现三种事件类型（message notice request）这在fingerprint.py中就有体现
   2. message包括 private 私聊消息 和 group 群聊消息
   3. notice包括 群文件上传 群成员增加/减少
   4. request包括 新朋友 和 进群邀请
   5. 后续会逐渐增加

1. fingerprint（指纹）
   1. 指纹是什么
      1. 指纹用于标识事件类型，插件根据这个类型来进行处理
   2. 三级指纹是什么
      1. 三级指纹是目前的指纹系统，目前最长的指纹只有三级 e.g. : message.private.admin
      2. 高等级的指纹可以去执行低等级指纹的任务
         1. message.private.admin 可以执行 message.private 和 message
   3. 目前打算实现的指纹位于fingerprint.py中
2. ...待补充...