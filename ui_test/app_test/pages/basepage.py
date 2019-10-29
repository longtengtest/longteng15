import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import basedir, logging


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, element_loc):  # ('id', 'kw')
        """通过元素定位器定位元素"""
        logging.info("定位元素: {}".format(element_loc))
        try:
            return self.driver.find_element(*element_loc)
        except NoSuchElementException:
            logging.error("定位元素失败: {}".format(element_loc))
            self.snapshot("定位失败", "_".join(element_loc))  # element_loc = ('id', 'kw')
            raise

    def find_all(self, element_loc):
        """定位一组元素"""
        logging.info("定位一组元素: {}".format(element_loc))
        try:
            return self.driver.find_elements(*element_loc)
        except NoSuchElementException:
            logging.error("定位一组元素失败: {}".format(element_loc))
            self.driver.save_snapshot("1.png")
            raise

    def try_find(self, element_loc):
        """尝试定位, 处理偶现元素, 或判断元素是否存在"""
        logging.info("尝试定位元素: {}".format(element_loc))
        try:
            return self.driver.find_element(*element_loc)
        except NoSuchElementException:
            logging.warning("元素未出现: {}".format(element_loc))

    def wait_find(self, element_loc, timeout=20, interval=0.5):
        """显示等待, 循环检查一个元素"""
        logging.info("等待定位元素: {}".format(element_loc))
        return WebDriverWait(self.driver, timeout, interval).until(EC.presence_of_element_located(element_loc))

    def click(self, element_loc):
        """通过元素定位器点击元素"""
        logging.info("点击元素: {}".format(element_loc))
        self.find(element_loc).click()

    def input_to(self, element_loc, text):
        """给定元素定位器和文本, 清空并输入文本"""
        logging.info("向元素: {} 输入: {}".format(element_loc, text))
        element = self.find(element_loc)
        element.clear()
        element.send_keys(text)

    def wait(self, seconds=2):
        """强制等待, 默认2s"""
        logging.info("等待: {}s".format(seconds))
        sleep(seconds)

    def snapshot(self, prefix, title):
        title = title.replace('/', '').replace(':', '')
        file_path = os.path.join(basedir, 'snapshots', "{}_{}.png".format(prefix, title))
        logging.info("截图, 保存路径: {}".format(file_path))
        self.driver.get_screenshot_as_file(file_path)
        self.wait(0.5)
