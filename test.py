from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://baike.baidu.com" + articleUrl)
    bs0bj = BeautifulSoup(html,"html.parser")
    return bs0bj.find("body").findAll("a", href=re.compile("^(\/subview\/|\/view\/)[0-9\/]*"))
links = getLinks("/view/1256")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)