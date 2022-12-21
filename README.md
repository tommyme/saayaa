## saayaa -- 力求打造 简单 易上手 的机器人框架

### 简介

#### **saayaa力求简单，核心代码目前只有300行左右**

```shell
# flag @ flag-mbp in ~/repos/saayaa/saaya on git:main
$ tokei
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Python                  8          406          306           25           75
===============================================================================
 Total                   8          406          306           25           75
===============================================================================
```

saayaa灵感源于好友[jerrita的saaya框架](https://github.com/jerrita/saaya) 

saayaa基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)

go-cqhttp有二维码登录功能，大大降低了登录难度。

### go-cqhttp usage
使用二维码登录时 手机上面的qq和go-cqhttp需要在同一网络下
so, when logging in, you can run cqhttp on your macbook and dump the cqhttp folder, then upload the folder to the cloud server.

alternatively, you can use 网页滑条 method, I don't like that.

### TODO_LIST

- [x] logger（彩色）
- [x] @和pic消息类型支持
- [x] 版本适配
- [x] 权限管理
- [x] 借助指纹进行事件区分
- [x] 异步支持
- [x] 容器分离

### 快速使用

1. 创建private.json
   
   ```python
   {
       "authKey": "1234567890",
       "master": 12345689,
       "admin": [
           1234567,
           1256,
           123456789,
           1234
       ]
   }
   ```

2. 运行代码：

```
docker-compose up -d
```

> 注意：由于我用的是Mrs4s最新做的镜像（[Package go-cqhttp · GitHub](https://github.com/Mrs4s/go-cqhttp/pkgs/container/go-cqhttp)）他放在ghcr.io上了，所以拉镜像比较慢，我使用了[GitHub - togettoyou/hub-mirror: 🚀 gcr.io、k8s.gcr.io、quay.io、ghcr.io 等国外镜像加速下载服务](https://github.com/togettoyou/hub-mirror)的解决方案 非常好用

3. 通过容器的日志里面的二维码进行登陆

### 框架概念

1. Event（事件）
   
   1. message包括 private 私聊消息 和 group 群聊消息
   2. notice包括 群文件上传 群成员增加/减少
   3. request包括 新朋友 和 进群邀请
   4. unknown (考虑到未来的兼容性)

2. fingerprint（指纹）
   
   1. 指纹是什么
      
      1. 指纹用于标识事件类型，插件根据这个类型来进行处理
   
   2. n级指纹是什么
      
      1. n级指纹是目前的指纹系统，目前最长的指纹只有四级 e.g. : message.private.admin.master 范围逐渐缩小
      2. 高等级的指纹可以去执行低等级指纹的任务
         1. message.private.admin 可以触发`message.private.admin``message.private` 和 `message`

3. action 构建主动行为

4. plugin manager 插件管理器，对事件进行广播，并且执行对应的函数

# 开发插件

> 参考plugins/base/default.py的内容进行开发

- PM.reg_event(fingerprint)
  
  - 接受指纹作为参数 装饰插件函数，当遇到具有该指纹类型的事件的时候，函数会被触发

- re_filter(pattern)
  
  - 根据正则表达式进行过滤，只有通过过滤的消息才会触发函数

- get_bot()
  
  - 获取bot实例，用于编写涉及到bot层的插件。
