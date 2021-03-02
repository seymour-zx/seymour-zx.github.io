# coding: utf-8
import os
import urllib.request
import webbrowser
import time

def openpath(filename, filedir=''):
# 路径
    path = os.path.join(filedir, filename)
    path = urllib.request.pathname2url(path)
    if not os.path.exists(path):
        print('......目标不存在:\n', path)
    return path

def dirlist(dirtxt):
# 生成目录列表
    htmldirs = []
    indexdirs = []
    with open(dirtxt, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            htmldirs.append(line)        
            indexdir = openpath(filename="index", filedir=line)
            if not os.path.exists(indexdir):
                os.makedirs(indexdir)
                print("创建目录：", indexdir)
            indexdirs.append(indexdir)
    return htmldirs, indexdirs

def fwinfo(path, info):
# 写入信息
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines(info)
    print("创建:", os.path.abspath(path))

def frinfo(filename, filedir=""):
# 读取信息
    path = openpath(filename, filedir)
    if not os.path.exists(path):
        info = "\n"
        print("缺少文件:", os.path.abspath(path))
    else:
        with open(path, 'r', encoding='utf-8') as fr:
            info = fr.read()
    return info

def info_title(filename, indexdir, txtdir):
# 'title.txt'
    message = ''
    path = openpath(filename, indexdir)
    if os.path.exists(path):
        message = frinfo(filename, indexdir)
    else:
        fwinfo(path, message)
    info = ''
    infolist = []
    infolist.append('\n')
    infolist.append('  <title>')
    infolist.append(message)
    infolist.append(frinfo(filename, txtdir))
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_keywords(filename, indexdir, txtdir):
# 'keywords.txt'
    message = '正协, 华朝颐亲王'
    path = openpath(filename, indexdir)
    if os.path.exists(path):
        message = frinfo(filename, indexdir)
    else:
        fwinfo(path, message)
    info = ''
    infolist = []
    infolist.append('\n')
    infolist.append(frinfo(filename, txtdir))
    infolist.append(message)
    infolist.append('" />')
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_description(filename, indexdir, txtdir):
# 'description.txt'
    message = ''
    path = openpath(filename, indexdir)
    if os.path.exists(path):
        message = frinfo(filename, indexdir)
    else:
        fwinfo(path, message)
    info = ''
    infolist = []
    infolist.append('\n')
    infolist.append(frinfo(filename, txtdir))
    infolist.append(message)
    infolist.append('" />')
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_link(filename, indexdir, txtdir, htmldir):
# 'link.txt'
    path = openpath(filename, indexdir)
    if os.path.exists(path):
        info = frinfo(filename, indexdir)
    else:
        rel_ico = os.path.relpath("../image/favicon.ico", htmldir)
        rel_ico = urllib.request.pathname2url(rel_ico)
        rel_css = os.path.relpath("../css/mystyle.css", htmldir)
        rel_css = urllib.request.pathname2url(rel_css)
        info = ''
        infolist = []        
        infolist.append('\n  <link href="')
        infolist.append(rel_ico)
        infolist.append('" rel="shortcut icon" type="image/x-icon" />\n    <!--调用网页图标-->\n  <link href="')
        infolist.append(rel_css)
        infolist.append('" rel="stylesheet" type="text/css" />\n    <!--调用css样式-->\n')
        for i in range(len(infolist)):
            info = info + infolist[i]
    return info

def info_article(filename, indexdir, txtdir, htmldir, datetime):
# 'article.html'
    message = ''
    path = openpath(filename, indexdir)
    if os.path.exists(path):
        message = frinfo(filename, indexdir)
    else:
        fwinfo(path, message)
    info = ''
    infolist = []
    infolist.append('\n    <article>')
    infolist.append('\n      <hr />')
    infolist.append('\n      <h1>' + frinfo('title.txt', indexdir) + '</h1>')
    infolist.append('\n      <hr />')
    # 特殊
    if not htmldir.find("/unit/")==-1:
        infolist.append('\n      <h4>朝颐亲王 | 正协信息客栈</h4>')
        path = openpath('datetime.txt', indexdir)
        if not os.path.exists(path):
            fwinfo(path, datetime)
            infolist.append('\n      <h4>发布于：' + datetime +'</h4>\n      <hr />\n')
        else:
            infolist.append('\n      <h4>发布于：' + frinfo('datetime.txt', indexdir) +'</h4>\n      <hr />\n')
    infolist.append(message)    
    infolist.append('\n    </article>')
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_footer(txtdir, datetime):
# 'footer.txt'
    path = openpath('footer.txt', txtdir)    
    infolist = []
    infolist.append('\n  <footer>\n    <!-- 站点更新 -->\n    <div>\n      |&nbsp;\n      &lt;&nbsp;\n      站点更新：')
    infolist.append(datetime)
    infolist.append('\n      &nbsp;&gt;\n      &nbsp;|\n    </div>\n    <!-- /站点更新 -->\n  </footer>')
    info = ''
    for i in range(len(infolist)):
        info = info + infolist[i]
    fwinfo(path, info)

def creat_html(htmldir, indexdir, txtdir, datetime):
# 创建index.html文件
    path = openpath('index.html', htmldir)
    path = os.path.abspath(path)
    print(".......开始编写：\n", path)
    infolist = []
    # 通用
    infolist.append(frinfo("head.txt", txtdir))
    # 个性化
    infolist.append(info_title(filename='title.txt', indexdir=indexdir, txtdir=txtdir))
    # 个性化
    infolist.append(info_keywords(filename='keywords.txt', indexdir=indexdir, txtdir=txtdir))
    # 个性化
    infolist.append(info_description(filename='description.txt', indexdir=indexdir, txtdir=txtdir))
    # 个性化
    infolist.append(info_link(filename='link.txt', indexdir=indexdir, txtdir=txtdir, htmldir=htmldir))
    # 通用
    infolist.append(frinfo("author.txt", txtdir))
    # 通用
    infolist.append(frinfo("body.txt", txtdir))
    # 通用
    infolist.append(frinfo("header.txt", txtdir))
    # 通用
    infolist.append('\n  <main>')
    # 个性化
    if not htmldir.find("/bookmark")==-1:
        infolist.append(frinfo('article.html', indexdir))
    else:
        infolist.append(info_article(filename='article.html', indexdir=indexdir, txtdir=txtdir, htmldir=htmldir, datetime=datetime))
    # 通用filename='article.html', indexdir=indexdir
    infolist.append('\n  </main>')
    # 通用
    infolist.append(frinfo("footer.txt", txtdir))
    # 通用
    infolist.append(frinfo("html.txt", txtdir))

    with open(path, 'w', encoding='utf-8') as fw:
        for i in range(len(infolist)):
            fw.writelines(infolist[i])
    # 在默认浏览器中打开html文件
    webbrowser.open(path,new = 0, autoraise=True)

def execute():
# 执行
    print('......默认目录正确！\n')
    txtdir = '../txt'
    print('......指定存放txt文件的目录:', txtdir)
    datetime = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    info_footer(txtdir=txtdir, datetime=datetime)
    # 读取目录列表
    dirtxt = openpath('dirtxt.txt', txtdir)
    htmllist, indexlist = dirlist(dirtxt=dirtxt)
    for n in range(len(htmllist)):
        creat_html(htmldir=htmllist[n], indexdir=indexlist[n], txtdir=txtdir, datetime=datetime)

if __name__ == '__main__':
    print('......cmd命令目录：')
    cmddir = 'D:\\Workspace'
    print(cmddir)
    print('......py存放目录：')
    pydir = 'D:\\Workspace\\Html\\seymour-zx.github.io\\common\\py'
    print(pydir)
    print('......判断默认目录：')
    if os.getcwd()==cmddir:
        # 切换目录
        os.chdir(pydir)
        execute()
    elif os.getcwd()==pydir:
        execute()
    else:
        print("......运行目录错误！")
        print("......当前运行目录：\n", os.getcwd())
    # pydir = input("\n......\n程序执行完毕！\n按Enter关闭窗口...")
    """
    # 网址拼接

    # from urllib.parse import urljoin
    # a = urljoin("https://zhengxie.info/folder/currentpage.html", "../")  

    # b = urljoin("https://zhengxie.info/folder/currentpage.html", "folder2/anotherpage.html")  

    # c = urljoin("https://zhengxie.info/folder/currentpage.html", "/folder3/anotherpage.html")  

    # d = urljoin("https://zhengxie.info/folder/currentpage.html", "../finalpage.html")  

    # print (a)
    # print (b)
    # print (c)
    # print (d)
    """