# 简单邮件&短信通知服务
一个简单的python实现的邮件服务，短信服务

还提供简单的服务器状态监听服务，使用短信服务发送短信通知

### 😁需求

python3.7 ,twilio ,shcedule ,twilio token,psutil

### ⚙安装

```shell
git clone git@github.com:Landers1037/simple-email-sms.git
```



```python
pip install schedule
pip install twilio
pip install psutil
```

获取Twilio的账户  [Twilio](https://www.twilio.com/try-twilio)

------

使用 service.json 自定义你的信息

```json
{
    "mail": "true",
    "sms": "true",
    "notice": "true",
    "username": "xxx@163.com",
    "password": "123456",
    "sender": "xxx@163.com",
    "receiver": ["xxx@qq.com"],
    "subject": "python mail test",
    "source": "xxx@163.com <xxx@163.com>",
    "text": "just a email test,please ignore",
    "smtp": "smtp.163.com",
    "port": 25,
    "mailtime": "06:30",
    "account_sid": "ACc986e47ssxxxxxxx",
    "auth_token": "d42852c86aae943e76",
    "from_phone": "+1555555",
    "to_phone": "+8610086",
    "message": "this is a sms test send from xxx",
    "smstime": "18:30",
    "sysprocess": ["nginx", "python", "aria2c"]
}
```

`使用smtp.163.com作为默认smtp服务器`

### 📝使用

`mail` 为true，邮件服务开启

`sms` 为true，短信服务开启

notice` 为true，发送系统状态监听短信

`username` 邮箱地址

`password` 邮箱密码

`sender` 同你的邮箱地址

`receiver` 收件人地址，一个列表可以添加多个邮箱

`subject` 邮件主题

`source` 邮件来源邮箱，同你的邮箱

`text` 要发送的文字

`smtp` smtp服务器地址

`port` smtp 端口25,ssl 端口465

`mailtime` 定时发送邮件的时间

`account_sid` 你的twilio accound_sid

`auth_token` 你的twilio token

`from_phone` 你的twilio phone number

`to_phone` 你需要接收短信的phone number 

`message` 要发送的短信信息

`smstime` 定时发送短信的时间

`sysprocess` 你想要监听的系统进程列表

### 🔴日志输出

服务一旦被启用，会记录启动状态在 `log.json`

一旦出现错误，错误日志保存在 `log.json`

### 🤪开始

```bash
python3 ~/simple-email-sms/service.py
```

在后台运行执行

```bash
nohup python3 ~/simple-email-sms/service.py &
```

查看日志

```bash
cat ~/simple-email-sms/log.json
```

启用系统状态监听短信服务

```json
"notice": "true",
"sysprocess": ["nginx", "python", "aria2c"]
```

添加想要监听的进程名称到`sysprocess`

一旦`notice` 为true系统监听短信服务开启，你会收到类似下面的消息,`message` 里定义的短信内容将不会生效

```
Sent from your Twilio trial account
内存占用率：37.6%
vsftpd:ok
aria2c:ok
nginx:ok
```

