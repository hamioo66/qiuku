# -*- coding=UTF-8 -*-
import time
import os
from HTMLTestRunner_jpg import HTMLTestRunner
import unittest

class TestRunner(object):
    """重写html生成报告"""

    def __init__(self, cases="./", title=u"测试报告",description=u"用例执行"):
        self.cases = cases
        self.title = title
        self.des = description

    def run(self):
        now = time.strftime("%Y.%m.%d %H_%M_%S")
        fp = open( os.path.dirname(os.path.abspath('.'))+"/report/" + now +"result.html", 'wb')
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='test*.py',top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()

if __name__ == '__main__':
    test = TestRunner()
    test.run()
