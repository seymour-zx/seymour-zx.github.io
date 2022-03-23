#!/usr/bin/python
# -*- coding: UTF-8 -*-

def setting():
    from lib.tool.folders import folders
    from lib.material.footer import footer

    mystyle_css = '../css/2021-10-11_mystyle.css'

    txt_folder = '../txt/'
    html_folders, index_folders = folders('directory.txt', txt_folder)
    footer(txt_folder)
    
    return html_folders, index_folders, txt_folder, mystyle_css

if __name__ == '__main__':
    print('执行程序', 'setting.py')
else:
    print('导入模块', 'setting.py')