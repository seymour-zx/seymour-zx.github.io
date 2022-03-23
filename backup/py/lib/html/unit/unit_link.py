#!/usr/bin/python
# -*- coding: UTF-8 -*-


from lib.tool.frinfo import frinfo
from lib.tool.fwinfo import fwinfo
from lib.tool.linkpath import linkpath
import urllib.request
import os 

def unit_link(file, index_folder, txt_folder, html_folder, mystyle_css):
# 'link.txt'
    info = ''
    rel_ico = os.path.relpath("../image/favicon.ico", html_folder)
    rel_ico = urllib.request.pathname2url(rel_ico)
    rel_css = os.path.relpath(mystyle_css, html_folder)
    rel_css = urllib.request.pathname2url(rel_css)
    infolist = []        
    infolist.append('\n    <link href="')
    infolist.append(rel_ico)
    infolist.append('" rel="shortcut icon" type="image/x-icon" />\n        <!--调用网页图标-->')
    infolist.append('\n    <link href="')
    infolist.append(rel_css)
    infolist.append('" rel="stylesheet" type="text/css" />\n        <!--调用css样式-->\n')
    for i in range(len(infolist)):
        info = info + infolist[i]
    return info


if __name__ == '__main__':
    print('执行程序', 'unit_link.py')
else:
    print('导入模块', 'unit_link.py')