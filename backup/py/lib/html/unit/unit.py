#!/usr/bin/python
# -*- coding: UTF-8 -*-


def unit(html_folder, index_folder, txt_folder, mystyle_css):
    import os
    import time
    from lib.tool.frinfo import frinfo
    from lib.tool.fwinfo import fwinfo
    from lib.tool.linkpath import linkpath
    from lib.html.unit.unit_link import unit_link
    from lib.html.unit.unti_title import unit_title
    from lib.html.unit.unti_keywords import unit_keywords
    from lib.html.unit.unti_description import unit_description
    from lib.html.unit.unti_core import unit_core

     # 当前格林尼治时间
    gmtime = time.gmtime()
    datetime = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
    info = ''
    # 通用
    info = info + frinfo('head.txt', txt_folder)
    info = info + unit_title('title.txt', index_folder, txt_folder)
    info = info + unit_keywords('keywords.txt', index_folder, txt_folder)
    info = info + unit_description('description.txt', index_folder, txt_folder)
    # 通用
    info = info + frinfo('author.txt', txt_folder)
    # if True:
    info = info + unit_link('link.txt', index_folder, txt_folder, html_folder, mystyle_css)
    # 通用
    info = info + frinfo('body.txt', txt_folder)
    # 通用
    info = info + frinfo('header.txt', txt_folder)
    info = info + unit_core(html_folder, index_folder, txt_folder, gmtime)
    # 通用
    info = info + frinfo('footer.txt', txt_folder)
    # 通用
    info = info + frinfo('html.txt', txt_folder)
    if True: # 写入信息'index.html'
        html = linkpath('index.html', html_folder)      
        with open(html, 'w', encoding='utf-8') as fw:
            fw.writelines(info)
    if True: # 在默认浏览器中打开html文件        
        html = os.path.abspath(html)
        # import webbrowser
        # webbrowser.open(html,new = 0, autoraise=True)


if __name__ == '__main__':
    print('执行程序', 'unit.py')
else:
    print('导入模块', 'unit.py')