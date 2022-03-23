#!/usr/bin/python
# -*- coding: UTF-8 -*-


def go():
    from lib.setup.setting import setting
    html_folders, index_folders, txt_folder, mystyle_css = setting()

    # 制作index.html
    from lib.html.html import html
    for n in range(len(html_folders)):
        html(html_folder=html_folders[n], index_folder=index_folders[n], txt_folder=txt_folder, mystyle_css=mystyle_css)

    # from lib.setup.refresh import refresh
    # refresh(txt_folder)
    

if __name__ == '__main__':
    from lib.ready.ready import ready
    if ready():
        print('执行程序', 'maintain.py')
        go()
else:
    print('导入模块', 'maintain.py')