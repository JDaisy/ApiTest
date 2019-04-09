#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests
import HTMLTestRunner
import os
import time
from common.User import User
from config.readcfg import ReadConfig

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(case_name="case", rule="test*.py"):
    # 加载测试用例
    case_path = os.path.join(cur_path, case_name)
    # 如果不存在这个文件夹就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    print("test case path: %s" % case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, report_name="report"):
    # 执行所有的用例,并把结果写入HTML测试报告
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, report_name)
    # 如果不存在这个文件夹就自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + "result.html")
    print("report path: %s" % report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试报告,测试结果如下: ", description="用例执行情况: ")
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    # 获取最新的测试报告
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print("最新的测试报告: " + lists[-1])
    report_file = os.path.join(report_path, lists[-1])
    return report_file


if __name__ == '__main__':
    s = requests
    # 用户登录
    user = User(s)
    user_info = user.login()
    # 将此次登录的用户信息写入config文件
    rc = ReadConfig()
    rc.set_user_info(user_info)
    # 用例
    test_case = add_case(case_name="case")
    run_case(test_case)
    rep_path = os.path.join(cur_path, "report")
    rep_file = get_report_file(rep_path)


# def all_case():
#
#     case_dir = "/Users/yanll/PycharmProjects/apitest/case"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
#
#     testcase.addTests(discover)
#     print(testcase)
#     return testcase

# if __name__ == '__main__':
#     report_path = "/Users/yanll/PycharmProjects/apitest/report/result.html"
#     fp = open(report_path, "wb")
#     # runner = unittest.TextTestRunner()
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="全用例自动化测试报告", description="用例执行情况: ")
#     runner.run(all_case())
#     fp.close()
