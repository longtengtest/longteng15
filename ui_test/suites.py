import os
import unittest
from config import basedir

loader = unittest.TestLoader()   # 用例加载器, 全局变量


def get_app_test_suite():  # 将所有app测试用例组成一个testsuite
    app_testcases_dir = os.path.join(basedir, 'app_test', 'testcases')
    suite = loader.discover(app_testcases_dir)
    title = 'app测试报告'
    desciption = ''
    return title, desciption, suite


def get_web_test_suite():
    web_case_dir = os.path.join(basedir, 'web_test', 'testcases')
    suite = loader.discover(web_case_dir)
    title = 'web测试报告'
    desciption = ''
    return title, desciption, suite


def get_all_cases():   # test suite嵌套
    app_suite = get_app_test_suite()
    web_suite = get_web_test_suite()
    suite = unittest.TestSuite([app_suite, web_suite])
    title = 'ui测试报告'
    desciption = ''
    return title, desciption, suite


def get_smoke_suite():
    suite = loader.loadTestsFromNames([
        'app_test.testcases.test_login.TestLogin.test_login',
        'app_test.testcases.chat.test_chat.TestChat.test_2'
    ])
    print(suite)
    return suite


get_smoke_suite()

