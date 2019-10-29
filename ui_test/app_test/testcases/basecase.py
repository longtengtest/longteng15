"""用例基础类"""
import unittest
from appium import webdriver
from config import logging, caps, appium_server
from time import sleep

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """用例类初始化方法"""
        logging.info("启动app")
        cls.driver = webdriver.Remote(appium_server, caps)

    @classmethod
    def tearDownClass(cls):
        logging.info("关闭app会话")
        cls.driver.quit()

    def wait(self, seconds=2):
        logging.info("等待: {}s".format(seconds))
        sleep(seconds)