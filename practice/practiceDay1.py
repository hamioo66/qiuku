# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/11/6
describle:平时练习
"""
import os
import datetime
import urllib2
myfiles = ['user.txt','accounts.txt','password.txt']
for filename in myfiles:
    print(os.path.join('c:\\user\\desktop',filename))
print(myfiles[0])
weekday = datetime.datetime.now().weekday()+1
print type(weekday)
print (u'今天是星期%d'%(weekday))
request = urllib2.Request("http://blog.sina.com.cn/s/blog_4701280b0102egl0.html")
response = urllib2.urlopen(request)
print response.read()
