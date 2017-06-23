---
Linux让生活更美好之ssh小技巧
---

本文主要介绍通过配置ssh客户端，使ssh会话保持长连接，使用跳板机登录特定服务器。


Linux上主要配置如下：
``` shell
mkdir ~/.ssh/sockets/
cat ~/.ssh/config 
Host *
   StrictHostKeyChecking no
   Compression yes
   ControlMaster yes
   ControlPath ~/.ssh/sockets/%r@%h-%p
   ControlPersist yes
   User root
Host 10.20.*
   ProxyCommand sshpass -p [passoword] ssh root@[跳转机IP] -W %h:%p

```
## 解释

### Host *
Host只对能够匹配后面字符串的计算机有效。 可以是ip也可以是主机名，支持“*”和“?”通配符。
“*”匹配0个或多个字符，“?”匹配一个字符
例如：Host *.cnnic.cn 表示以cnnic.cn为后缀的主机名
Host 192.168.0.? 表示匹配192.168.0.[0-9]

### StrictHostKeyChecking no 
连接新主机时不进行公钥确认
SSH 公钥检查是一个重要的安全机制，可以防范中间人劫持等黑客攻击。但是在特定情况下，严格的 SSH 公钥检查会破坏一些依赖 SSH 协议的自动化任务，就需要一种手段能够绕过 SSH 的公钥检查。

### Compression yes
启用压缩，加快数据传输速度

### ControlMaster yes 
打开ssh会话复用，如果不打开，每次会话都会在后台重新打开一个socket

### ControlPersist yes
在最后一个连接关闭之后也不真正的关掉连接，这样后面再连接的时候就还是不用输入密码。如果后面指定的是一个时间，则在后台的master连接会在服务器保持空闲（没有客户端连接）的指定时间后断开连接。时间单位如下：
默认为秒，s/S 秒，m/M 分钟，h/H 时，d/D 天，w/W 周
Example：
- 600 ：600秒
- 10m：10分钟
- 1h30m：1小时30分钟

### ControlPath ~/.ssh/sockets/%r@%h-%p
将socket文件存储在~/.ssh/sockets/目录下，以%r@%h-%p 格式命名。
- %r: 远程服务器用户名
- %h: 远程主机主机名
- %p: 远程主机端口号

```
ControlMaster yes
ControlPersist yes
ControlPath ~/.ssh/sockets/%r@%h-%p
上面三条配合使用
```
### User root
ssh连接默认使用root用户，除非指定其他用户名。

### ProxyCommand sshpass -p [passoword] ssh root@[跳转机IP] -W %h:%p
使用跳板登录，
ProxyCommand 后面指定使用代理登录的命令 sshpass可以明文指定ssh密码，
sshpass需要自行安装，Ubuntu上安装命令为sudo apt install sshpass。


#### 更高级内容见 http://man.openbsd.org/ssh_config
