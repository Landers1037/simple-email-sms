# simple-email-sms
一个简单的python实现的邮件服务，短信服务

### 😁Demand

python3.7 ,twilio ,shcedule ,twilio token

### ⚙Install

```shell
git clone git@github.com:Landers1037/simple-email-sms.git
```



```python
pip install schedule
pip install twilio
```

get a Twilio account at  [Twilio](https://www.twilio.com/try-twilio)

------

use service.json to add your infomation

```json
{
    "mail": "true",
    "sms": "true",
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
    "smstime": "18:30"
}
```

`mail service use smtp.163.com as default`

### 📝Instructions

`mail` is true,the mail.service is active
`sms` is true,the sms.service is active
`username` is your mail account
`password` is your mail passwd
`sender` is the same as username
`receiver` is the receive mailbox,it's a list
`subject` is the mail theme
`source` is the mail source,same as username
`text` is the text you want to mail
`smtp` is the default smtp address
`port` for smtp use 25,for ssl use 465
`mailtime` is the time your want to set for mail
`account_sid` is your twilio accound_sid
`auth_token` is your twilio token
`from_phone` is your twilio phone number
`to_phone` is your own phone number 
`message` is the message you want to send by sms
`smstime` is the time you want to set for sms

### ❌Log output

once you have active or inactive your service,the log will be saved in `log.json`

once an error happend,it will be saved in `log.json`

### 🤪Start

```bash
python3 ~/simple-email-sms/service.py
```

to run in background

```bash
nohup python3 ~/simple-email-sms/service.py &
```

see log

```bash
cat ~/simple-email-sms/log.json
```

