"""登录测试"""
from ddt import ddt, data
from app_test.testcases.basecase import BaseCase
from app_test.pages.launchpage import LaunchPage
from app_test.pages.login_page import LoginPage
from app_test.pages.mainpage import MainPage
from config import logging
from utils.data import read_yaml
import unittest

@ddt
class TestLogin(BaseCase):
    """登录测试"""
    @unittest.skip("临时跳过")
    def test_login(self):
        logging.info("正常登录测试")
        LaunchPage(self.driver).click_login()
        data = read_yaml('test_app_data.yaml', 'test_login')
        LoginPage(self.driver).login_action(data['phone'], data['pwd'])
        self.wait()
        self.assertIsNotNone(MainPage(self.driver).check_contants_ico())

    @data(*read_yaml('test_app_data.yaml', 'test_login_negative'))
    def test_login_negative(self, data):
        LaunchPage(self.driver).click_login()
        LoginPage(self.driver).login_action(data['phone'], data['pwd'])
        self.wait()



