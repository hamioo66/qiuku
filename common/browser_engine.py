# -*- coding:utf-8 -*-

import os.path
from ConfigParser import ConfigParser
from selenium import webdriver
from common.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    # ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config.ini file, return the driver

    def open_browser(self):
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info(u"您选择了 %s 浏览器." % browser)
        url = config.get("testServer","URL")
        logger.info(u"测试服务url是: %s" % url)

        global driver
        # if browser == "Firefox":
        #     driver = webdriver.Firefox()
        #     logger.info("Starting firefox browser.")
        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info(u"启动Chrome浏览器.")
        # elif browser == "IE":
        #     driver = webdriver.Ie(self.ie_driver_path)
        #     logger.info("Starting IE browser.")

        driver.get(url)
        logger.info(u"打开url: %s" % url)
        driver.maximize_window()
        logger.info(u"最大化当前窗口.")
        driver.implicitly_wait(10)
        logger.info(u"设置智能等待10秒.")
        return driver

    def quit_browser(self):
        logger.info(u"现在关闭并退出浏览器.")
        self.driver.quit()