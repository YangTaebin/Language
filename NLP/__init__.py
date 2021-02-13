import _jpype
import jpype
from konlpy.tag import Kkma
from re import match
from collections import Counter
import pytagcloud
import webbrowser
from bs4 import BeautifulSoup
import urllib.request as req

kkma = Kkma()

url="https://www.naver.com"
req=req.urlopen(url)
doc = req.read()

ex_sent = kkma.sentences(doc)
ex_nouns = kkma.nouns(doc)

nouns=[]
for sent in ex_sent:
    for noun in kkma.nouns(sent):
        if len(str(noun)) >= 2 and not(match('^[0-9]',noun)):
            nouns.append(noun)

word_count={}

for noun in nouns:
    word_count[noun] = word_count.get(noun,0)+1

counter = Counter(word_count)
top5 = counter.most_common(10)

word_count_list = pytagcloud.make_tags(top5,maxsize=80)
pytagcloud.create_tag_image(word_count_list,'wordcloud.jpg',size=(450,300),fontname='korean', rectangular=False)
