#!/usr/bin/python
# -*- coding: UTF-8 -*-


def frinfo(file, folder=""):
    import os
    from lib.tool.linkpath import linkpath
# 读取信息
    path = linkpath(file, folder)
    if not os.path.exists(path):
        info = '\n'
        print('信息读取失败:\n', os.path.abspath(path))
    else:
        with open(path, 'r', encoding='utf-8') as fr:
            info = fr.read()
    return info


if __name__ == '__main__':
    print('执行程序', 'frinfo.py')
else:
    print('导入模块', 'frinfo.py')