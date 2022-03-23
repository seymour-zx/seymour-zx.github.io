#!/usr/bin/python
# -*- coding: UTF-8 -*-


from lib.tool.frinfo import frinfo
from lib.tool.fwinfo import fwinfo
from lib.tool.linkpath import linkpath
import os 


def unit_description(file, index_folder, txt_folder):
# 'description.txt'
    info = '\n'
    infolist = []
    infolist.append(frinfo(file, txt_folder))
    path = linkpath(file, index_folder)
    if os.path.exists(path):
        infolist.append(frinfo(file, index_folder))
    else:
        fwinfo(path, '')
        # infolist.append('')
    infolist.append('" />')    
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info



if __name__ == '__main__':
    print('执行程序', 'unti_description.py')
else:
    print('导入模块', 'unti_description.py')