# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/5/18
describle:
"""
import unittest
import time
from pageobjects.baidu_homepage import HomePage
from common.TestRunner import TestRunner
from common.browser_engine import BrowserEngine

class test_baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前提准备工作
        """
        # cls.driver = webdriver.Chrome()
        # cls.driver.get('http://www.baidu.com')
        # cls.driver.maximize_window()
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser()
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        cls.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print(u'测试通过.')
        except Exception as e:
            print(u'测试异常.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
# if __name__ == '__main__':
#     unittest.main()

if __name__ == "__main__":
    runner = TestRunner('./', u'用例测试', u'测试环境：Chrome')
    runner.run()