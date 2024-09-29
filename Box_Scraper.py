import requests
import pandas as pd
from bs4 import BeautifulStoneSoup, BeautifulSoup


url="https://quotes.toscrape.com/"
r=requests.get(url)

soup=BeautifulSoup(r.text, "lxml")
box=soup.find_all("div", class_="quote")
l=len(box)
print(l)

#loop range ar page
for i in range(1,4):
    x="https://quotes.toscrape.com/page/"+str(i)+"/"
    print("url link :" + x)
    #url create
    url=x
    r=requests.get(url)
    soup=BeautifulSoup(r.text, "lxml")
    box2=soup.find_all("div", class_="quote")
    l=len(box2)
    #print(l)
    print("Total Box= "+ str(l))

    alltt=soup.find_all(["span"])
    ll=len(alltt)
    print("Total Details= "+ str(ll))


    allttt=soup.find_all("a", class_="tag")
    lll=len(allttt)
    print("Total Tags= "+ str(lll))
