#!/usr/bin/python
# -*- coding: UTF-8 -*-


def folders(directory, txt_folder):
    import os
    from lib.tool.linkpath import linkpath
# 读取文件夹目录
    html_folders = []
    index_folders = []
    path = linkpath(directory, txt_folder)
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            html_folders.append(line)        
            path = linkpath('index', line)
            if not os.path.exists(path):
                os.makedirs(path)
                print('......新建目录：\n', os.path.abspath(path))
            index_folders.append(path)
    return html_folders, index_folders


if __name__ == '__main__':
    print('执行程序', 'folders.py')
else:
    print('导入模块', 'folders.py')