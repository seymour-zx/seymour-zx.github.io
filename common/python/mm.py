# coding: utf-8
import os
import urllib.request
import webbrowser
import time

def common_txt(txtdir):
    # 创建"footer2.txt"
    path = openpath("footer2.txt", txtdir)
    strtime = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    message = """
    <div class="support"><!--版本更新-->      
      &nbsp;|&nbsp;
      &lt;&nbsp;
      版本更新：%s+00:00
      &nbsp;&gt;
      &nbsp;|&nbsp;
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

def self_txt(htmldir, indexdir):
    # 创建"title.txt"
    path = openpath("title.txt", indexdir)
    if not os.path.exists(path):
        message = """
  <title>颐亲王的小栈 | 颐亲王 | 正协信息客栈</title>
  <meta name="keywords" content="颐亲王, 郑協, zhengxie.info, 正协, 正协信息" />
  <meta name="description" content="本站点是“颐亲王的小栈”，站点名称为“正协信息客栈”，由“华朝颐亲王郑協”创建并维护，借助“GitHub Pages”，发布于域名“zhengxie.info”内。" />
"""
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(message)
        print("创建self-txt：", os.path.abspath(path))
    # 创建"author.txt"
    path = openpath("author.txt", indexdir)
    if not os.path.exists(path):
        message = """
  <meta name="author" content="华朝颐亲王郑協, seymour.zx@foxmail.com" />
"""
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
    # 创建"article.txt"
    path = openpath("article.txt", indexdir)
    if not os.path.exists(path):
        message = """
        <h1>欢迎作客颐亲王的小栈</h1>
        <p></p>
        <br /><br /><br /><br /><br />
        <br /><br /><br /><br /><br />
        <br /><br /><br /><br /><br />
        <br /><br /><br /><br /><br />
        <br /><br /><br /><br /><br />
"""
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
        fw.writelines(readinfo('link.txt', indexdir))
        fw.writelines(readinfo('author.txt', indexdir))
        fw.writelines(readinfo('body.txt', txtdir))
        fw.writelines(readinfo('header.txt', txtdir))
        fw.writelines('\n  <div class="central">')
        fw.writelines('\n    <main>')
        fw.writelines('\n      <article>')
        fw.writelines(readinfo('article.txt', indexdir))
        fw.writelines('\n      </article>')
        fw.writelines('\n    </main>')
        fw.writelines('\n  </div>')
        fw.writelines(readinfo('footer.txt', txtdir))
        fw.writelines(readinfo('script.txt', txtdir))
        fw.writelines(readinfo('html.txt', txtdir))
    webbrowser.open(path,new = 0, autoraise=True)

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
        self_txt(htmldir=htmldirs[n], indexdir=indexdirs[n])
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


# # 网址拼接

# # from urllib.parse import urljoin
# # a = urljoin("https://zhengxie.info/folder/currentpage.html", "../")  

# # b = urljoin("https://zhengxie.info/folder/currentpage.html", "folder2/anotherpage.html")  

# # c = urljoin("https://zhengxie.info/folder/currentpage.html", "/folder3/anotherpage.html")  

# # d = urljoin("https://zhengxie.info/folder/currentpage.html", "../finalpage.html")  

# # print (a)
# # print (b)
# # print (c)
# # print (d)
# # import webbrowser
# # webbrowser.open(a,new = 1) path = 'D:\\Workshop\\python\\zhengxie.info\\common\\css\\mystyle.css'
# start = 'background.jpg'
# import urllib.request
# pathname = os.path.relpath(path, start)
# print(pathname)
# url = urllib.request.pathname2url(pathname)
# print(url)
# pathname = urllib.request.url2pathname(url)
# print(pathname)
# print(os.getcwd())