# coding: utf-8
import os
import urllib.request
import webbrowser
import time

def common_txt(txtdir):
    # 创建"footer2.txt"
    path = openpath("footer2.txt", txtdir)
    strtime = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    message = """
    <div class="support"><!--版本更新-->      
      |&nbsp;
      &lt;&nbsp;
      版本更新：%s
      &nbsp;&gt;
      &nbsp;|
    </div>
"""%(strtime)
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines(message)
    print("创建common-txt：", os.path.abspath(path))
    # 创建"footer.txt"
    path = openpath("footer.txt", txtdir)  
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines('\n  <footer>')
        fw.writelines(readinfo("footer1.txt", txtdir))
        fw.writelines(readinfo("footer2.txt", txtdir))
        fw.writelines(readinfo("footer3.txt", txtdir))
        fw.writelines('\n  </footer>')
    print("创建common-txt：", os.path.abspath(path))

def self_txt(htmldir, indexdir, txtdir):
    # 创建"title.txt"
    path = openpath("title.txt", indexdir)
    if not os.path.exists(path):
        message = readinfo("title.txt", txtdir)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"keywords.txt"
    path = openpath("keywords.txt", indexdir)
    if not os.path.exists(path):
        message = readinfo("keywords.txt", txtdir)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"description.txt"
    path = openpath("description.txt", indexdir)
    if not os.path.exists(path):
        message = readinfo("description.txt", txtdir)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"author.txt"
    path = openpath("author.txt", indexdir)
    if not os.path.exists(path):
        message = readinfo("author.txt", txtdir)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"article.txt"
    path = openpath("article.txt", indexdir)
    if not os.path.exists(path):
        message = readinfo("article.txt", txtdir)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"link.txt"
    path = openpath("link.txt", indexdir)
    if not os.path.exists(path):
        rel_ico = os.path.relpath("../image/favicon.ico", htmldir)
        rel_ico = urllib.request.pathname2url(rel_ico)
        rel_css = os.path.relpath("../css/mystyle.css", htmldir)
        rel_css = urllib.request.pathname2url(rel_css)
        message = """
  <link href="%s" rel="shortcut icon" type="image/x-icon" />
    <!--调用网页图标-->
  <link href="%s" rel="stylesheet" type="text/css" />
    <!--调用css样式-->
"""%(rel_ico, rel_css)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"pubdate.txt"
    path = openpath("pubdate.txt", indexdir)
    if not os.path.exists(path):
        strtime = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
        message = "%s"%(strtime)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"lastmod.txt"
    path = openpath("lastmod.txt", indexdir)
    if not os.path.exists(path):
        strtime = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
        message = "%s"%(strtime)
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"info_top.txt"
    path = openpath("info_top.txt", indexdir)
    title = readinfo("title.txt", indexdir)
    title = title.strip()
    title = title.strip("<title>")
    title = title.strip(" | 颐亲王 | 正协信息客栈</title>")
    datetime = readinfo("pubdate.txt", indexdir)
    message = """
    <h2>%s</h2>
    <hr />
    <h6>颐亲王&nbsp;&nbsp;正协信息客栈</h6>
    <h6><time datetime="%s" pubdate="pubdate">发布于 %s</time></h6>
    <hr />
    """%(title, datetime, datetime)
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines(message)
    print("创建self-txt：", os.path.abspath(path))
    # 创建"info_bottom.txt"
    path = openpath("info_bottom.txt", indexdir)
    datetime = readinfo("lastmod.txt", indexdir)
    message = """
    <hr />
    <h6><time datetime="%s">修改于 %s</time></h6>
    <hr />
    """%(datetime, datetime)
    with open(path, 'w', encoding='utf-8') as fw:
        fw.writelines(message)
    print("创建self-txt：", os.path.abspath(path))

def openpath(file, dirf=""):
    path = os.path.join(dirf, file)
    path = urllib.request.pathname2url(path)
    if not os.path.exists(path):
        print("文件不存在：", path)
    return path

def pathlist(dirstxt):
    htmldirs = []
    indexdirs = []
    with open(dirstxt, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            htmldirs.append(line)
            if not os.path.exists(line):
                os.makedirs(line)
                print("创建目录：", line)
            else:
                print(line)            
            indexdir = openpath(file="index", dirf=line)
            if not os.path.exists(indexdir):
                os.mkdir(indexdir)
            indexdirs.append(indexdir)
    return htmldirs, indexdirs

def readinfo(selffile, selfdir=""):
    path = openpath(selffile, selfdir)
    if not os.path.exists(path):
        message = "\n"
        print("缺少文件", os.path.abspath(path))
    else:
        with open(path, 'r', encoding='utf-8') as fr:
            message = fr.read()
    return message

def creat_html(htmldir, indexdir, txtdir):
    path = openpath('index.html', htmldir)
    path = os.path.abspath(path)
    print("创建：", path)
    with open(path, 'w', encoding='utf-8') as fw:        
        fw.writelines(readinfo("head.txt", txtdir))
        fw.writelines(readinfo('title.txt', indexdir))
        fw.writelines(readinfo('keywords.txt', indexdir))
        fw.writelines(readinfo('description.txt', indexdir))
        fw.writelines(readinfo('link.txt', indexdir))
        fw.writelines(readinfo('author.txt', indexdir))
        fw.writelines(readinfo('body.txt', txtdir))
        fw.writelines(readinfo('header.txt', txtdir))
        fw.writelines('\n  <div class="central">')
        fw.writelines('\n    <main>')
        fw.writelines('\n      <article>')
        if not htmldir.find("/blogpost/")==-1:
            fw.writelines(readinfo('info_top.txt', indexdir))
        elif not htmldir.find("/test")==-1:
            fw.writelines(readinfo('info_top.txt', indexdir))
        fw.writelines(readinfo('article.txt', indexdir))
        if not htmldir.find("/blogpost/")==-1:
            fw.writelines(readinfo('info_bottom.txt', indexdir))
        elif not htmldir.find("/test")==-1:
            fw.writelines(readinfo('info_bottom.txt', indexdir))
        fw.writelines('\n      </article>')  
        fw.writelines('\n    </main>')
        fw.writelines('\n  </div>')
        fw.writelines(readinfo('footer.txt', txtdir))
        fw.writelines(readinfo('script.txt', txtdir))
        fw.writelines(readinfo('html.txt', txtdir))
    # webbrowser.open(path,new = 0, autoraise=True)

def execute(pydir):
    txtdir = openpath("../txt")
    print("通用txt存放目录：", txtdir)    
    print("创建通用txt：")
    common_txt(txtdir=txtdir)
    dirstxt = openpath("htmldirs.txt", txtdir)
    print("记录目录的txt：", dirstxt)
    print("index.html的目录列表htmldirs：")
    htmldirs, indexdirs = pathlist(dirstxt=dirstxt)
    for n in range(len(htmldirs)):
        self_txt(htmldir=htmldirs[n], indexdir=indexdirs[n], txtdir=txtdir)
        creat_html(htmldir=htmldirs[n], indexdir=indexdirs[n], txtdir=txtdir)


if __name__ == "__main__":
    pydir = "D:\\Workshop\\python\\seymour-zx.github.io\\common\\python"
    if pydir==os.getcwd():
        print("初始位置正确！")
        execute(pydir=pydir)
    else:
        print("初始位置错误！")
        print("预设位置：", pydir)
        print("实际位置：", os.getcwd())
    pydir = input("按Enter关闭窗口......")


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