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
        guid = result["data"]["guid"]
        token = result["data"]["token"]
        user_info = {"guid": guid,
                     "token": token
                     }
        return user_info

    def get_guid(self):
        result = self.login()["guid"]
        return result

    def get_token(self):
        result = self.login()["token"]
        return result


if __name__ == '__main__':
    s = requests
    user = User(s)
    print(user.login())
