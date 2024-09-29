import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup
import pandas as pd


req=requests.get("https://pandas.pydata.org/")
#html ar part see kore lxml
soup=BeautifulSoup(req.text, "lxml")

#print(soup.div)
#print(soup.div.ul)
#print(soup.section)
#print(soup.section.h1)

#h1
htext=soup.find_all("h1")
print('Total h1=' , len(htext))
htextt=soup.find("h1")
print("h1 text= ",htextt.string)


#p tag
ptext=soup.find_all("p")
print('Total p=' , len(ptext))
pl=len(ptext)
for i in range(0,3):
    print("Text of p= ", ptext[i].text)

#a tag
atext=soup.find_all("a", class_="dropdown-item")
print('Total a tag=' , len(atext))
tagl=len(atext)

x=[]
for i in range(0,tagl):
    print("Text of a= ", atext[i].text)
    y=atext[i].text
    x.append(y)

#x=soup.div    it's work by columns=x

dataframee=pd.DataFrame(columns=x)
#dataframee.to_csv("file_pandas.csv")