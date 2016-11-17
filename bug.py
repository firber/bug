# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://baike.baidu.com" + pageUrl)
    bs0bj = BeautifulSoup(html, "html.parser")
    ''' 筛选最后编辑日期
    date = bs0bj.find("body").find("span", {"class":"j-modified-time", "style":"display:none"})
    if date and re.match("2014-[0-9]{1,2}-[0-9]{1,2}", date.get_text()):
        print(bs0bj.h1.get_text() + ' ' + date.get_text())
        print(pageUrl + "\n--------")
    '''
    key = bs0bj.find("body").find("li", text=re.compile('^编辑次数：[1-9]*次历史版本$'))
    print(key)
    if key:
        words = key.get_text()
        num = int(words[5:-5])
        if num:
            print(bs0bj.h1.get_text() + ' ' + num)
            print(pageUrl + "\n--------")
    for link in bs0bj.find("body").findAll("a", href=re.compile("^(\/subview\/|\/view\/)[0-9\/]*")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                pages.add(newpage)
                getLinks(newpage)
getLinks("")