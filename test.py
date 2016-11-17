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
    try:
        print(bs0bj.h1.get_text())
    except AttributeError:
        print("未在该页面找到主题词！")

    for link in bs0bj.find("body").find_all("a", href=re.compile("^(\/subview\/|\/view\/)[0-9\/]*")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print("------------\n"+newpage)
                pages.add(newpage)
                getLinks(newpage)
getLinks("")