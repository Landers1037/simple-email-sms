import smtplib
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import time
import json

# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。


class pymail:

    with open('service.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    smtpserver = data["smtp"]
    username = data["username"]
    password = data["password"]
    sender = data["sender"]
    receiver = data["receiver"]
    text = data["text"]
    subject = data["subject"]
    sslflag = data["ssl"]

    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = data["source"]
    msg['To'] = ";".join(receiver)

    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    def email(self):
        if self.sslflag == "true":
            smtp = smtplib.SMTP_SSL(self.data["smtp"], self.data["port"])
        else:
            smtp = smtplib.SMTP(self.data["smtp"], self.data["port"])
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp.quit()
