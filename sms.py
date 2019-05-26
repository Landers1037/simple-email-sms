from twilio.rest import Client
import psutil
import schedule
import json
from notice import system


class pysms:

    with open('service.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    sms = data["message"]
    account_sid = data["account_sid"]
    auth_token = data["auth_token"]
    from_phone = data["from_phone"]
    to_phone = data["to_phone"]
    flag = data["notice"]

    def sendsms(self):
        if self.flag == 'true':
            spy = system()
            mess = spy.spy()
        else:
            mess = self.sms

        account_sid = self.account_sid
        auth_token = self.auth_token
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=self.to_phone,
            from_=self.from_phone,
            body=mess)
