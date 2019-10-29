from app_test.pages.basepage import BasePage
from config import logging


class LoginPage(BasePage):
    # 页面元素
    mobile_ipt_loc = ('id', "com.lqr.wechat:id/etPhone")
    pwd_ipt_loc = ('id', "com.lqr.wechat:id/etPwd")
    login_btn_loc = ('id', "com.lqr.wechat:id/btnLogin")

    # 页面操作
    def input_mobile(self, phone):
        """输入手机号"""
        logging.info("输入手机号: {}".format(phone))
        self.input_to(self.mobile_ipt_loc, phone)

    def input_pwd(self, pwd):
        """输入密码"""
        logging.info("输入密码: {}".format(pwd))
        self.input_to(self.pwd_ipt_loc, pwd)

    def click_login(self):
        """点击登录按钮"""
        logging.info("点击登录按钮")
        self.click(self.login_btn_loc)

    def login_action(self, phone, pwd):
        """登录操作"""
        logging.info("登录操作, 手机号: {}, 密码: {}".format(phone, pwd))
        self.input_mobile(phone)
        self.input_pwd(pwd)
        self.click_login()
