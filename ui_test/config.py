"""config.py: 全局配置文件"""
from os.path import dirname, abspath, join
import logging

# 路径配置
basedir = abspath(dirname(__file__))  # 当前文件(__file__) 所在目录(dirname) 的绝对路径(abspath)


# 日志配置
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(funcName)s: %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                    handlers=[
                        logging.StreamHandler(),  # 将日志输出到屏幕的日志处理器
                        logging.FileHandler(join(basedir, 'logs', 'log.txt'), encoding='utf-8')
                    ])


# app配置
caps = {
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'deviceName': '127.0.0.1:62025',
            'appPackage': 'com.lqr.wechat',
            'appActivity': 'ui.activity.SplashActivity',
        }

appium_server = 'http://127.0.0.1:4723/wd/hub'