# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os
# import pymysql
from common.logger import Logger
import random
from ConfigParser import ConfigParser
from selenium.webdriver.common.keys import Keys

# 创建日志实例
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver


        # quit browser and end testing

    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作

    def forward(self):
        self.driver.forward()
        logger.info(u"当前页面前进操作.")

        # 浏览器后退操作

    def back(self):
        self.driver.back()
        logger.info(u"当前页面后退操作.")

        # 隐式等待

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info(u"等待 %d 秒." % seconds)

        # 点击关闭当前窗口

    def close(self):
        try:
            self.driver.close()
            logger.info(u"关闭并退出浏览器.")
        except NameError as e:
            logger.error(u"退出浏览器失败 %s" % e)

            # 保存图片

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(u"截图成功，保存为: /screenshots")
        except NameError as e:
            logger.error(u"截图失败！%s" % e)
            self.get_windows_img()

            # 定位元素方法

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info(u"找到元素\'%s\' 成功 "
                            u"通过%s值:%s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error(u"无元素异常:%s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info(u"找到元素\'%s\' 成功 "
                            u"通过 %s值:%s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error(u"无元素异常:%s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError(u"请输入一个有效类型的元素")

        return element

      #定位多个元素
    def find_elements(self, selectors):
        elements = ''
        if '=>' not in selectors:
            return self.driver.find_elements_by_id(selectors)
        selectors_by = selectors.split('=>')[0]
        selectors_value = selectors.split('=>')[1]

        if selectors_by == "i" or selectors_by == 'id':
            try:
                elements = self.driver.find_elements_by_id(selectors_value)
                logger.info(u"找到元素\'%s\'成功 "
                            u"通过%s值:%s" %(elements.text, selectors_by, selectors_value))
            except NoSuchElementException as e:
                logger.error(u"无元素异常:%s" % e)
                self.get_windows_img()  # take screenshot
        elif selectors_by == "n" or selectors_by == 'name':
            elements = self.driver.find_elements_by_name(selectors_value)
        elif selectors_by == "c" or selectors_by == 'class_name':
            elements = self.driver.find_elements_by_class_name(selectors_value)
        elif selectors_by == "l" or selectors_by == 'link_text':
            elements = self.driver.find_elements_by_link_text(selectors_value)
        elif selectors_by == "p" or selectors_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(selectors_value)
        elif selectors_by == "t" or selectors_by == 'tag_name':
            elements = self.driver.find_elements_by_tag_name(selectors_value)
        elif selectors_by == "x" or selectors_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath(selectors_value)
                logger.info(u"找到元素\'%s\' 成功 "
                            "by %s via value: %s " % (elements.text, selectors_by, selectors_value))
            except NoSuchElementException as e:
                logger.error(u"无元素异常:%s" % e)
                self.get_windows_img()
        elif selectors_by == "s" or selectors_by == 'selector_selector':
            elements = self.driver.find_elements_by_css_selector(selectors_value)
        else:
            raise NameError(u"请输入一个有效类型的元素")

        return elements

        # 输入

    def into(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info(u"输入值是\'%s\' " % text)
        except NameError as e:
            logger.error(u"输入%s失败" % e)
            self.get_windows_img()

            # 清除文本框

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info(u"清除输入框已存在的内容.")
        except NameError as e:
            logger.error(u"清除元素%s失败" % e)
            self.get_windows_img()

            # 点击元素

    def click(self, selector):

        el = self.find_element(selector)
        eltext = el.text
        try:
            el.click()
            logger.info(u"当前元素\'%s\'被点击." % el.text)
        except NameError as e:
            logger.error(u"点击%s失败" % e)


            # 或者网页标题

    def get_page_title(self):
        logger.info(u"当前Title是%s" % self.driver.title)
        return self.driver.title

    #         #连接数据库查询
    #
    # def get_order_quantity(self,last_value,sql):
    #     self.connection = pymysql.connect(host='123.206.66.110',
    #         user='vulcan_test',
    #         password='pKEUdIf2',
    #         db='vulcan_test',
    #         charset='utf8',
    #         cursorclass=pymysql.cursors.DictCursor)
    #
    #     cur = self.connection.cursor()
    #
    #     Sql = sql
    #     cur.execute(Sql)
    #     results = cur.fetchall()
    #    # return (results[0]['count(id)'])
    #
    #     if last_value == results[0]['count(id)']:
    #          logger.info("==========总订单数量核对正确===========")
    #     else:
    #          logger.info("==========总订单数量核对错误===========")
    #     self.connection.close()
    #
    #     ####操作数据库
    # def database_handle(self,sql):
    #     self.connection = pymysql.connect(host='123.206.66.110',
    #               user='vulcan_test',
    #               password='pKEUdIf2',
    #               db='vulcan_test',
    #               charset='utf8',
    #               cursorclass=pymysql.cursors.DictCursor)
    #
    #     cur = self.connection.cursor()
    #     Sql = sql
    #     cur.execute(Sql)
    #     self.connection.commit()
    #     self.connection.close()
    #
    #         ###寻找元素，循环
    #
    # def search_order(self,now,current,pramas,status):
    #
    #          try:
    #             resultsstatus = pramas.find_elements(status)
    #             time.sleep(1)
    #
    #             for resultsstatu in (resultsstatus[random.randint(0,len(resultsstatus)-1)].text
    #                                  ,resultsstatus[random.randint(0,len(resultsstatus)-1)].text
    #                                  ,resultsstatus[random.randint(0,len(resultsstatus)-1)].text
    #                                  ):
    #                 if resultsstatu == now:
    #                     logger.info("============列表状态核对通过===========")
    #                 else:
    #                     logger.info("============列表状态核对异常============")
    #          except:
    #             logger.info("没有订单数据")
    #
    #
    #         ##切割字符串
    #
    # def login(self,login,telphone,password):
    #     #配置文件获取
    #     config = ConfigParser()
    #     file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    #     config.read(file_path)
    # #登录
    #     select_frame = "n=>roleCode"
    #     telphone_frame = "n=>telphone"
    #     password_frame = "n=>password"
    #     login_button = "n=>loginBtn"
    #     logintype = "t=>option"
    #
    #
    #     self.find_element(select_frame)
    #     options = self.find_elements(logintype)
    #     self.wait(1)
    #     self.click(options[int(config.get(login,"options"))])
    #     self.into(telphone_frame,config.get(login,telphone))
    #     self.into(password_frame,config.get(login,password))
    #     self.wait(1)
    #     try:
    #         self.click(login_button)
    #     except:
    #         pass
    #
    #
    # def check_list(self):
    #
    #     list_number = "s=>td[class = 'sorting_1']"
    #     page2 = "s=>[class = 'paginate_button '] "
    #     previou_page = "s=>[class = 'paginate_button previous']"
    #     next_page = "s=>[class = 'paginate_button next']"
    #     first_page = "s=>[class = 'paginate_button first']"
    #     end_page = "s=>[class = 'paginate_button last']"
    #
    #     listnumber1 = self.find_elements(list_number)
    #     num = []
    #     for i in listnumber1:
    #         num.append(i.text)
    #     if '1' in num:
    #         logger.info("===========分页点击刷新正确（第一页）===========")
    #     else:
    #         logger.info("===========分页点击刷新错误（第一页）===========")
    #     self.sleep(0.5)
    #     try:
    #             ###点击第二页
    #         self.click(page2)
    #         self.sleep(0.5)
    #         listnumber11 = self.find_elements(list_number)
    #         num = []
    #         for i in listnumber11:
    #             num.append(i.text)
    #         if '11' in num:
    #             logger.info("==========分页点击刷新正确（第二页）============")
    #         else:
    #             logger.info("==========分页点击刷新错误（第二页）===========")
    #         self.sleep(0.5)
    #             ###点击上一页
    #         self.click(previou_page)
    #         self.sleep(0.5)
    #         listnumber1 = self.find_elements(list_number)
    #         num = []
    #         for i in listnumber1:
    #             num.append(i.text)
    #         if '1' in num:
    #             logger.info("===========分页点击刷新正确（上一页）===========")
    #         else:
    #             logger.info("============分页点击刷新错误（上一页）===========")
    #         self.sleep(0.5)
    #                 ###点击下一页
    #         self.click(next_page)
    #         self.sleep(0.5)
    #         listnumber11 = self.find_elements(list_number)
    #         num = []
    #         for i in listnumber11:
    #             num.append(i.text)
    #         if '11' in num:
    #             logger.info("==========分页点击刷新正确（下一页）===========")
    #         else:
    #             logger.info("==========分页点击刷新错误（下一页）==========")
    #         self.sleep(0.5)
    #                 ###点击首页
    #         self.click(first_page)
    #         self.sleep(0.5)
    #         listnumber1 = self.find_elements(list_number)
    #         num = []
    #         for i in listnumber1:
    #             num.append(i.text)
    #         if '1' in num:
    #             logger.info("==========分页点击刷新正确（首页）============")
    #         else:
    #             logger.info("==========分页点击刷新错误（首页）===========")
    #         self.sleep(0.5)
    #                 ###点击末页
    #         self.click(end_page)
    #         self.sleep(0.5)
    #         listnumber11 = self.find_elements(list_number)
    #         num = []
    #         for i in listnumber11:
    #             num.append(i.text)
    #         if '1' not in num:
    #             logger.info("==============分页点击刷新正确（末页）==============")
    #         else:
    #             logger.info("==============分页点击刷新错误（末页）==============")
    #
    #
    #     except:
    #         logger.info("==============第二页没有数据或者数据对不上,已截图============")
    #         self.get_windows_img()
    #
    #
    #
    #         ###地址下拉框选择，drodownbar为统计下拉框list的位置，intobar为地址选择输入框list的位置。
    #
    # def drop_down_box(self, dropdownbar, intobar):
    #
    #     dropdownlist = "s=>button[title~='请选择']"
    #     searchbar = "c=>form-control"
    #
    #     dropdownlists = self.find_elements(dropdownlist)
    #     print(len(dropdownlists))
    #     dropdownlists[dropdownbar].click()
    #     searchbars = self.find_elements(searchbar)
    #     print(len(searchbars))
    #
    #     searchbars[intobar].send_keys("重庆市")
    #     searchbars[intobar].send_keys(Keys.ENTER)
    #     dropdownlists[dropdownbar + 1].click()
    #     searchbars[intobar + 1].send_keys("市辖区")
    #     searchbars[intobar + 1].send_keys(Keys.ENTER)
    #     dropdownlists[dropdownbar + 2].click()
    #     searchbars[intobar + 2].send_keys("江北区")
    #     searchbars[intobar + 2].send_keys(Keys.ENTER)
    #


    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
