#!/usr/bin/python
# -*- coding: UTF-8 -*-


def footer(txt_folder):
    import time
    from lib.tool.frinfo import frinfo
    from lib.tool.fwinfo import fwinfo
    from lib.tool.linkpath import linkpath
# 'footer.txt'
    # 当前格林尼治时间
    gmtime = time.gmtime()
    datetime = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
    file = 'footer.txt'
    infolist = []
    infolist.append('\n    <!-- 页底 -->')
    infolist.append('\n    <footer>')
    infolist.append('\n')
    infolist.append('\n        <!-- 正协信息客栈（zhengxie.info）版权所有 -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            正协信息客栈（zhengxie.info）版权所有')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n        <!-- Copyright © 2020-2021 All Rights Reserved. -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            Copyright © 2020-2021 All Rights Reserved')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n        <!-- 举报中心 -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            <a href="https://www.12377.cn/" target="_blank">违法信息举报中心</a>&nbsp;&nbsp;')
    infolist.append('\n            <a href="https://www.12321.cn/" target="_blank">垃圾信息举报中心</a>')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n        <!-- 上次维护 -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            |&nbsp;&lt;&nbsp;')
    infolist.append('\n            上次维护：<time datetime="')
    infolist.append(time.strftime('%Y-%m-%dT%H:%MZ', gmtime))
    infolist.append('">')
    infolist.append(time.strftime('%Y-%m-%dT%H:%MZ', gmtime))
    infolist.append('</time>')
    infolist.append('\n            &nbsp;&gt;&nbsp;|')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n    </footer>')
    info = ''
    for i in range(len(infolist)):
        info = info + infolist[i]
    path = linkpath(file, txt_folder)
    fwinfo(path, info)


if __name__ == '__main__':
    print('执行程序', 'footer.py')
else:
    print('导入模块', 'footer.py')