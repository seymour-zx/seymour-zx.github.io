#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import os
from lib.html.html import html
from lib.tool.frinfo import frinfo
from lib.tool.fwinfo import fwinfo
from lib.tool.linkpath import linkpath

def refresh(txt_folder):
# 更新目录
    n = 999
    html_folder = '../../unit/' + str(n) +'/'
    info = ''
    info = info + '\n            <table class="contents"><!-- 目录列表 -->\n'
    while not n==0:
        if os.path.exists(html_folder):
            index_folder = linkpath('index', html_folder)
            # info = info + '                <tr>\n                    <td nowrap="nowrap">'
            info = info + '                <tr>\n                    <td class="date">'
            gmtime = time.gmtime()
            gmtime = time.strftime('%Y-%m-%d', gmtime)
            info = info + gmtime
            info = info + '</td>\n'
            info = info + '                    <td class="contents"><a href="https://zhengxie.info/unit/' + str(n) +'/"'
            # info = info + ' title="" target="_blank">'
            info = info + ' title="">'
            info = info + frinfo('title.txt', index_folder)
            info = info + '</a></td>\n                </tr>\n'            
        n = n - 1
        htmlfolder = '../../unit/' + str(n) +'/'
    info = info + '            </table><!-- // 目录列表 <table class="contents"> -->'
    path = linkpath('main.html', '../../base/sitemap/index/')
    fwinfo(path, info)
    html(html_folder='../../base/sitemap/', index_folder='../../base/sitemap/index/', txt_folder=txt_folder, mystyle_css='../css/2021-10-11_mystyle.css')


if __name__ == '__main__':
    print('执行程序', 'refresh.py')
else:
    print('导入模块', 'refresh.py')