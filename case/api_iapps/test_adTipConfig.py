#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import os
import time
import unittest
import urllib3
from config.readcfg import ReadConfig
from common.logger import Log
from common.excel_pub import ExcelUtil
from common.jschema_validate import JsonSchema


#忽略SSl警告
urllib3.disable_warnings()

#JsonSchema校验文件地址
cur_path = os.path.dirname(os.path.realpath(__file__))
exl_path = os.path.join(cur_path, "api_iapps.xlsx")



class AdTipConfig(unittest.TestCase):
    log = Log()
    log.info("被测接口: 小羊接口（正式）")
    rc = ReadConfig()
    exl = ExcelUtil(exl_path, 'adTipConfig')

    def setUp(self):
        self.s = requests


    def test_adTipConfig(self):
        '''验证小羊接口（正式）字段类型'''

        #接口拼接以及发送接口请求
        headers = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; LYA-AL00 Build/HUAWEILYA-AL00)",
            "Host": "api.iapps.ifeng.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        payload = self.rc.get_stdPmt()
        url = "https://api.iapps.ifeng.com/news/adTipConfig"
        r = self.s.get(url=url, params=payload, headers=headers, verify=False)

        print(r.url)

        # 接口返回值
        result = r.json()

        # 结果比对
        self.assertEqual(r.status_code, 200)

        # json格式校验
        schema = self.exl.case_data(0, "schema")
        jsonschema = JsonSchema(schema)
        self.assertTrue(jsonschema.validate(result))


    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()

