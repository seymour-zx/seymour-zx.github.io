#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.tool.frinfo import frinfo
from lib.tool.fwinfo import fwinfo
from lib.tool.linkpath import linkpath
import os 
import time


def unit_core(html_folder, index_folder, txt_folder, gmtime):
    if True: # 简化条件判断语句
        x=0
        if html_folder=='../../':
            x=100
        elif not html_folder.find('../../private/')==-1:
            x=200
            if not html_folder.find('/bookmark/')==-1:
                x=201
        elif not html_folder.find('../../base/')==-1:
            x=300
            if not html_folder.find('/sitemap/')==-1:
                x=301
        elif not html_folder.find('../../unit/')==-1:
            x=400
        print(x,html_folder)    
    info = '\n\n    <!-- 页面核心 -->\n    <div class="core">'
    if True:
        if x==0:
            info = info + '\n        <main>\n'
        elif x==100:
            info = info + '\n        <main>\n'
        elif x==200:
            info = info + '\n        <main>\n'
        elif x==300:
            info = info + '\n        <main>\n'
        elif x==301:
            info = info + '\n        <main>\n'
        elif x==400:
            info = info + '\n        <main>\n'
        else:
            info = info + '\n        <main>\n'
    if True:
        if x==300 or x==301 or x==400:
            info = info + '\n            <div class="title"><h1>' + frinfo('title.txt', index_folder) + '</h1></div>'
            info = info + '\n            <hr />'
    if True:
        file = 'main.html'
        path = linkpath(file, index_folder)
        if os.path.exists(path):
            info = info + frinfo(file, index_folder)
        else:
            message = ''
            message = message + '\n            <article>'
            message = message + '\n<!--'
            message = message + '\n                <h3>  </h3>'
            message = message + '\n                <p>  </p>'
            message = message + '\n                <div class="in-p-box">'
            message = message + '\n                    <p>  </p>'
            message = message + '\n                </div>'
            message = message + '\n                <h2>  </h2>'
            message = message + '\n                <p style="text-indent: 2em;">  </p>'
            message = message + '\n                <h3>  </h3>'
            message = message + '\n                <h4>  </h4>'
            message = message + '\n                <pre class="code" >  </pre>'
            message = message + '\n                <hr />'
            message = message + '\n                <br />'
            message = message + '\n                <h2>参考 / Reference</h2>'
            message = message + '\n                <p style="text-indent: 2em;">1. <a href="" ></a></p>'
            message = message + '\n-->'
            if x==400:
                message = message + '\n            <hr /><h6 style="text-indent: 2em;">华朝颐亲王 | 正协信息客栈 | '
                datetime1 = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
                datetime2 = time.strftime('%Y年%m月%d日', gmtime)
                datetime = '<time datetime="' + datetime1 + '" pubtime >' + datetime2 + '</time>'
                message = message + datetime
                message = message + '</h6><hr />'
            message = message + '\n            </article>'
            fwinfo(path, message)
            info = info + message
    message = '''

            <div class="ad">
                <hr />
                <!-- Google广告——横向展示 -->
                <ins class="adsbygoogle"
                    style="display:block"
                    data-ad-client="ca-pub-6434243103158481"
                    data-ad-slot="4856101005"
                    data-ad-format="auto"
                    data-full-width-responsive="true"></ins>
                <script>
                    (adsbygoogle = window.adsbygoogle || []).push({});
                </script>
                <hr />
            </div>
'''
    info = info + message
    info = info + '\n        </main>'
    info = info + '\n    </div>\n\n'
    return info



if __name__ == '__main__':
    print('执行程序', 'unit_core.py')
else:
    print('导入模块', 'unit_core.py')