#!/usr/bin/python
# -*- coding: UTF-8 -*-


def ready():
    import os
    cmdfolder = 'D:\\Workspace'
    pyfolder = 'D:\\Workspace\\zhengxie.info\\assets\\py'
    if os.getcwd()==cmdfolder or os.getcwd()==pyfolder:
        os.chdir(pyfolder)
        print('......确认运行目录切换至py文件夹！......')        
        return True
    else:
        print('......当前运行目录错误！......')
        print(os.getcwd())
        print('......运行中断......')
        return False


if __name__ == '__main__':
    print('执行程序', 'ready.py')
else:
    print('导入模块', 'ready.py')