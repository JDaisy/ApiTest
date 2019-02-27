#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from config import readcfg

urllib3.disable_warnings(InsecureRequestWarning)

rc = readcfg.ReadConfig()


class User:
    def __init__(self, s):
        self.s = s

    def login(self):
        headers = {'Accept-Encoding': 'identity',
                   'Content-Length': '0',
                   'Host': 'id.ifeng.com',
                   'Connection': 'Keep-Alive'
                   }
        url = rc.get_url("simple_login")
        payload = {'u': rc.get_user("username"),
                   'k': rc.get_user("psw"),
                   'type': 3
                   }
        res = self.s.post(url, data=payload, headers=headers, verify=False)
        result = res.json()
        return result

    def get_guid(self):
        result = str(self.login()["data"]["guid"])
        return result

    def get_token(self):
        result = self.login()["data"]["token"]
        return result


if __name__ == '__main__':
    s = requests.session()
    user = User(s)
    guid = user.get_guid()
    token = user.get_token()
    print(type(guid))
    print(type(token))
