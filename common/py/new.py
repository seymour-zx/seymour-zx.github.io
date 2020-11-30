# coding: utf-8
import os
import urllib.request
import webbrowser
import time

def openpath(filename, filedir=""):
    path = os.path.join(filedir, filename)
    path = urllib.request.pathname2url(path)
    if not os.path.exists(path):
        print("目标不存在:", path)
    return path


def fwinfo(path, info):
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines(info)
    print("创建:", os.path.abspath(path))


def frinfo(filename, filedir=""):
    path = openpath(filename, filedir)
    if not os.path.exists(path):
        info = "\n"
        print("缺少文件:", os.path.abspath(path))
    else:
        with open(path, 'r', encoding='utf-8') as fr:
            info = fr.read()
    return info


def pathlist(dirstxt):
    htmldirs = []
    indexdirs = []
    with open(dirstxt, 'r', encoding='utf-8') as fr:
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


def ctxt(txtdir):
    # 创建"footer2.txt"
    path = openpath("footer2.txt", txtdir)
    strtime = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    info = """
    <div><!--站点更新-->      
      |&nbsp;
      &lt;&nbsp;
      站点更新：%s
      &nbsp;&gt;
      &nbsp;|
    </div>
"""%(strtime)
    fwinfo(path, info)
    # 创建"footer.txt"
    path = openpath("footer.txt", txtdir)  
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines('\n  <footer>')
        fw.writelines(frinfo("footer1.txt", txtdir))
        fw.writelines(frinfo("footer2.txt", txtdir))
        fw.writelines(frinfo("footer3.txt", txtdir))
        fw.writelines('\n  </footer>')
    print("创建:", os.path.abspath(path))
    # 创建"pubdate.txt"&"lastmod.txt"
    path1 = openpath("pubdate.txt", txtdir)
    path2 = openpath("lastmod.txt", txtdir)
    strtime = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    info = "%s"%(strtime)
    fwinfo(path1, info)
    fwinfo(path2, info)
    

def cptxt(filename, indexdir, txtdir):
    path = openpath(filename, indexdir)
    if not os.path.exists(path):
        info = frinfo(filename, txtdir)
        fwinfo(path, info)


def stxt(htmldir, indexdir, txtdir):
    print(indexdir)
    # 创建"title.txt"
    cptxt("title.txt", indexdir, txtdir)
    # 创建"keywords.txt"
    cptxt("keywords.txt", indexdir, txtdir)
    # 创建"description.txt"
    cptxt("description.txt", indexdir, txtdir)
    # 创建"author.txt"
    cptxt("author.txt", indexdir, txtdir)
    # 创建"pubdate.txt"
    cptxt("pubdate.txt", indexdir, txtdir)
    # 创建"lastmod.txt"
    cptxt("lastmod.txt", indexdir, txtdir)
    # 创建"article.txt"
    cptxt("article.txt", indexdir, txtdir)
    # 创建"link.txt"
    path = openpath("link.txt", indexdir)
    if not os.path.exists(path):
        rel_ico = os.path.relpath("../image/favicon.ico", htmldir)
        rel_ico = urllib.request.pathname2url(rel_ico)
        rel_css = os.path.relpath("../css/mystyle.css", htmldir)
        rel_css = urllib.request.pathname2url(rel_css)
        info = """
  <link href="%s" rel="shortcut icon" type="image/x-icon" />
    <!--调用网页图标-->
  <link href="%s" rel="stylesheet" type="text/css" />
    <!--调用css样式-->
"""%(rel_ico, rel_css)
        fwinfo(path, info)
    # 创建"info_top.txt"
    path = openpath("info_top.txt", indexdir)
    title = frinfo("title.txt", indexdir)
    title = title.strip()
    title = title.strip("<title>")
    title = title.strip(" | 颐亲王 | 正协信息客栈</title>")
    datetime = frinfo("pubdate.txt", indexdir)
    info = """
    <h2>%s</h2>
    <hr />
    <h6>颐亲王&nbsp;&nbsp;正协信息客栈</h6>
    <h6><time datetime="%s" pubdate="pubdate">发布于 %s</time></h6>
    <hr />
"""%(title, datetime, datetime)
    fwinfo(path, info)
    # 创建"info_bottom.txt"
    path = openpath("info_bottom.txt", indexdir)
    datetime = frinfo("lastmod.txt", indexdir)
    info = """
    <hr />
    <h6><time datetime="%s">修改于 %s</time></h6>
    <hr />
    """%(datetime, datetime)
    fwinfo(path, info)


def creat_html(htmldir, indexdir, txtdir):
    path = openpath('index.html', htmldir)
    path = os.path.abspath(path)
    print("创建：", path)
    with open(path, 'w', encoding='utf-8') as fw:
        # 通用
        fw.writelines(frinfo("head.txt", txtdir))        
        # 特别
        fw.writelines(frinfo("title.txt", indexdir))
        # 特别
        fw.writelines(frinfo("keywords.txt", indexdir))
        # 特别
        fw.writelines(frinfo("description.txt", indexdir))
        # 特别
        fw.writelines(frinfo("link.txt", indexdir))
        # 特别
        fw.writelines(frinfo("author.txt", indexdir))
        # 通用
        fw.writelines(frinfo("body.txt", txtdir))
        # 通用
        fw.writelines(frinfo("header.txt", txtdir))
        # 通用
        fw.writelines('\n    <main>')
        # 通用
        fw.writelines('\n      <article>')
        # 特殊
        if not htmldir.find("/unit/")==-1:
            fw.writelines(frinfo('info_top.txt', indexdir))
        # 特别
        fw.writelines(frinfo("article.txt", indexdir))
        # 特殊
        if not htmldir.find("/unit/")==-1:
            fw.writelines(frinfo('info_bottom.txt', indexdir))
        # 通用
        fw.writelines('\n      </article>')
        # 通用
        fw.writelines('\n    </main>')
        # 通用
        fw.writelines(frinfo("footer.txt", txtdir))
        # 通用
        fw.writelines(frinfo("script.txt", txtdir))
        # 通用
        fw.writelines(frinfo("html.txt", txtdir))
    webbrowser.open(path,new = 0, autoraise=True)


def execute(pydir):
    print("\n开始准备通用txt...")
    txtdir = openpath("../txt")
    print("通用txt存放于:", txtdir)    
    ctxt(txtdir=txtdir)
    print("\n开始准备路径列表...")
    dirstxt = openpath("dirstxt.txt", txtdir)
    htmldirs, indexdirs = pathlist(dirstxt=dirstxt)
    print("\n开始创建html...")
    for n in range(len(htmldirs)):        
        stxt(htmldir=htmldirs[n], indexdir=indexdirs[n], txtdir=txtdir)
        creat_html(htmldir=htmldirs[n], indexdir=indexdirs[n], txtdir=txtdir)


if __name__ == "__main__":
    pydir = "D:\\Workshop\\zhengxie.info\\common\\py"
    if pydir==os.getcwd():
        print("初始位置正确！")
        execute(pydir=pydir)
    else:
        print("初始位置错误！")
        print("预设位置：", pydir)
        print("实际位置：", os.getcwd())
    pydir = input("\n按Enter关闭窗口...")

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