from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://baike.baidu.com" + pageUrl)
    bs0bj = BeautifulSoup(html)
    for link in bs0bj.find("body").findAll("a", href=re.compile("^(\/subview\/|\/view\/)[0-9\/]*")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getLinks(newpage)
getLinks("")