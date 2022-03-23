#!/usr/bin/python
# -*- coding: UTF-8 -*-


def linkpath(children, parents=''):
    import os
    import urllib.request
# 相对链接路径
    path = os.path.join(parents, children)
    path = urllib.request.pathname2url(path)
    if not os.path.exists(path):
        print('......目标不存在:\n', os.path.abspath(path))
    return path





if __name__ == '__main__':
    print('执行程序', 'linkpath.py')
else:
    print('导入模块', 'linkpath.py')