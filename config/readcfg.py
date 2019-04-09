#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os
import codecs


curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "cfg.ini")


class ReadConfig:
    def __init__(self):
        fd = open(cfgpath, encoding="utf-8")
        data = fd.read()

        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(cfgpath, "w")
            file.write(data)
            file.close()
        fd.close()

        # 创建管理对象
        self.conf = configparser.ConfigParser()

        # 读取ini文件
        self.conf.read(cfgpath, encoding="utf-8")

    # 对user_info中的option进行设置,写入配置文件
    def set_user_info(self, user_info):
        self.conf.set("user_info", "guid", user_info["guid"])
        self.conf.set("user_info", "token", user_info["token"])
        self.conf.write(open("config/cfg.ini", "w", encoding="utf-8"))

    # 获取所有的section
    def get_all_sections(self):
        value = self.conf.sections()
        return value

    # 获取凤凰通用户账号
    def get_user(self, item):
        value = self.conf.get("user", item)
        return value

    # 获取用户登录信息
    def get_user_info(self, item):
        value = self.conf.get("user_info", item)
        return value

    # 获取标参
    def get_stdPmt(self):
        value = dict(self.conf.items("stdPmt"))
        return value

    # 获取接口
    def get_url(self, item):
        value = self.conf.get("url", item)
        return value

    # 获取headers
    def get_headers(self, item):
        value = self.conf.get("headers", item)
        return value


if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_stdPmt())


