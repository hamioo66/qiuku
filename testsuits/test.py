# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/12
describle:
"""

import unittest
from selenium import webdriver
from utils.TestRunner import TestRunner
class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前提准备工作
        """
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        cls.driver.quit()
    def test_a_add_agent(self):
        """测试后台正常登录"""
        # Login(self.driver).login("1", "18888888888", "123456")
        # Login(self.driver).get_windows_img()
        # # Common(self.driver).find_menu(0, u"商品列表")
        # Common(self.driver).find_menu(1, u"代理商列表")
        print('hello world!')
        


if __name__ == "__main__":
    runner = TestRunner('./', u'用例测试', u'测试环境：Chrome')
    runner.run()