from urllib.request import urlopen
from bs4 import BeautifulSoup

'''初步开始使用beautifulsoup'''

html = urlopen("https://github.com/cyrlus/learn_python3_spider/wiki")

bs=BeautifulSoup(html.read(),"html.parser")
print(bs.title)

