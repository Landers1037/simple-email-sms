#coding: utf-8
import schedule

import time
import json

from mail import pymail
from sms import pysms
from log import pylog

with open('service.json', 'r', encoding='utf8') as file:
    data = json.load(file)
logdata = {}


def main():
    email = pymail()
    sms = pysms()
    log = pylog()
    try:

        if data["mail"] == 'true':
            schedule.every().day.at(data["mailtime"]).do(email.email)
            logdata["mail"] = "mail status active"

        if data["sms"] == 'true':
            schedule.every().day.at(data["smstime"]).do(sms.sendsms)
            logdata["sms"] = "sms status active"

        if data["mail"] != "true":
            logdata["mail"] = "mail status inactive"

        if data["sms"] != "true":
            logdata["sms"] = "sms status inactive"
    except Exception as err:
        logdata["error"] = str(err.args)

    log.logout(logdata)

    while True:
        schedule.run_pending()
        time.sleep(1)


main()
