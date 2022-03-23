#!/usr/bin/python
# -*- coding: UTF-8 -*-


from lib.html.unit.unit import unit


def html(html_folder, index_folder, txt_folder, mystyle_css):
    if html_folder=='../../':
        pass
    elif not html_folder.find('../../unit/')==-1:
        unit(html_folder=html_folder, index_folder=index_folder, txt_folder=txt_folder, mystyle_css=mystyle_css)
    else:
        pass


if __name__ == '__main__':
    print('执行程序', 'html.py')
else:
    print('导入模块', 'html.py')