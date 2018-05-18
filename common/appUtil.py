# -*- coding=UTF-8 -*-
import random, time, os
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.logger import Logger
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

device = '69GY6SNN99999999'  # 此处设备号
pack = 'com.datamatch.coolball'  # 此处是app的package名称
activity = 'com.jdd.datapredict.StartupActivity'  # 此处是app的主activity
# com.jdd.datapredict.StartupActivity

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
desired_caps = {}
desired_caps['device'] = 'android'
desired_caps['platformName'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['Version'] = '4.4.4'
desired_caps['deviceName'] = device
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



