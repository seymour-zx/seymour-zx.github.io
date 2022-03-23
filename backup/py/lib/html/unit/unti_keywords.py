#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.tool.frinfo import frinfo
from lib.tool.fwinfo import fwinfo
from lib.tool.linkpath import linkpath
import os 


def unit_keywords(file, index_folder, txt_folder):
# 'keywords.txt'
    info = '\n'
    infolist = []
    infolist.append(frinfo(file, txt_folder))
    path = linkpath(file, index_folder)
    if os.path.exists(path):
        infolist.append(frinfo(file, index_folder))
    else:
        fwinfo(path, '信息,目录,导航,网页,网址导航,网站大全,客栈,亲王,网站导航,网站搜索,导航网站,网站收录,信息分类,网站分类,网址收录,颐亲王,华朝颐亲王,正协信息,正协信息客栈,视频,直播')
        infolist.append('信息,目录,导航,网页,网址导航,网站大全,客栈,亲王,网站导航,网站搜索,导航网站,网站收录,信息分类,网站分类,网址收录,颐亲王,华朝颐亲王,正协信息,正协信息客栈,视频,直播')
    infolist.append('" />')    
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info



if __name__ == '__main__':
    print('执行程序', 'unti_keywords.py')
else:
    print('导入模块', 'unti_keywords.py')