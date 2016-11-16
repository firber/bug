from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://baike.baidu.com/view/1256.htm")
bs0bj = BeautifulSoup(html,"html.parser")
for link in bs0bj.find("body").findAll("a", href=re.compile("^(\/subview\/|\/view\/)[0-9\/]*")):
    if 'href' in link.attrs:
        print("http://baike.baidu.com" + link.attrs['href'])