from app_test.pages.basepage import BasePage
from config import logging


class MainPage(BasePage):
    # 页面元素
    contacts_ico_loc = ('id', 'com.lqr.wechat:id/tvContactsPress')
    # 元素操作

    def check_contants_ico(self):
        logging.info("检查联系人图标是否存在")
        return self.try_find(self.contacts_ico_loc)
