from app_test.pages.basepage import BasePage
from config import logging


class LaunchPage(BasePage):
    # 页面元素
    login_btn_loc = ('id', 'com.lqr.wechat:id/btnLogin')
    reg_btn_loc = ('id', 'com.lqr.wechat:id/btnRegister')

    # 元素操作
    def click_login(self):
        logging.info("点击登录按钮")
        self.click(self.login_btn_loc)

    def click_reg(self):
        logging.info("点击注册按钮")
        self.click(self.reg_btn_loc)


# driver = None
#
#
# class LaunchPage2(BasePage):
#     @property
#     def login_btn(self):
#         return driver.find_element('id', 'com.lqr.wechat:id/btnLogin')
#
#     @property
#     def reg_btn(self):
#         return driver.find_element('id', 'com.lqr.wechat:id/btnRegister')
#
#
# class LaunchPage3(BasePage):
#     # 页面元素
#     login_btn_loc = ('id', 'com.lqr.wechat:id/btnLogin')
#     reg_btn_loc = ('id', 'com.lqr.wechat:id/btnRegister')
#
#     def __getattr__(self, item):
#         """获取属性的魔术方法, 如果正常情况下找不到,则调用该方法"""
#         element_loc = item + "_loc"  # login_btn_loc
#         if hasattr(self, element_loc):
#             return self.find(element_loc)
#         else:
#             raise AttributeError("未配置该元素的定位器")
#
#
#
#
# driver = None
# l = LaunchPage3(driver)
# l.login_btn.click()
# l.reg_btn.click()