#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import time
import unittest
import urllib3
from common.logger import Log
from common.excel_pub import ExcelUtil
from common.jschema_validate import JsonSchema

# 对应当前接口的测试用例
cur_path = os.path.dirname(os.path.realpath(__file__))
exl_path = os.path.join(cur_path, "id_case.xlsx")


class CheckMail(unittest.TestCase):
    log = Log()
    log.info("被测接口: 验证邮箱唯一性接口")

    # 获得当前测试接口的全部用例数据
    exl = ExcelUtil(exl_path, "check_mail")
    dict_data = exl.dict_data()

    def setUp(self):
        urllib3.disable_warnings()
        self.headers = {'Accept-Encoding': 'identity',
                        'Content-Length': '0',
                        'Host': 'id.ifeng.com',
                        'Connection': 'Keep-Alive'
                        }
        self.url = "https://id.ifeng.com/api/checkmail"
        self.s = requests

    def tearDown(self):
        time.sleep(1)

    def check_mail(self, i):
        # 用例描述
        desc = self.exl.case_data(i, "desc")
        # 校验项
        code = self.exl.case_data(i, "code")
        msgcode = self.exl.case_data(i, "msgcode")
        data_res = self.exl.case_data(i, "data_res")
        # 参数
        u = self.exl.case_data(i, "u")
        payload = {
            "u": u
        }
        # 执行当前行用例
        self.log.info("执行测试用例: %s" % desc)
        r = self.s.post(self.url, data=payload, headers=self.headers, verify=False)
        self.log.info("请求: %s" % r.url)
        # 接口返回值
        result = r.json()
        self.log.info("返回: %s" % result)
        # 结果比对
        self.assertEqual(r.status_code, 200)
        self.assertEqual(result['code'], code)
        self.assertEqual(result['msgcode'], msgcode)
        self.assertEqual(result['data']['res'], data_res)
        # json格式校验
        schema = self.exl.case_data(i, "schema")
        jsonschema = JsonSchema(schema)
        self.assertTrue(jsonschema.validate(result))
        jsonschema.validate(result)

    def test01(self):
        self.check_mail(0)

    def test02(self):
        self.check_mail(1)

    def test03(self):
        self.check_mail(2)


if __name__ == '__main__':
    unittest.main()
