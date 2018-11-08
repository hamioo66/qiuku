# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/11/6
describle:读取配置文件数据
"""
# 解析配置文件的模块，python2.x中名为ConfigParser，3.x已更名小写，并加入一些新功能
import ConfigParser
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
curent_file = os.path.abspath(os.path.join(parent_dir,'config/config.ini'))
conf = ConfigParser.ConfigParser()
conf.read(curent_file)
