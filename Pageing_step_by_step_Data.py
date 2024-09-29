import requests
import pandas as pd
from bs4 import BeautifulStoneSoup, BeautifulSoup


url="https://quotes.toscrape.com/"
r=requests.get(url)

soup=BeautifulSoup(r.text, "lxml")

#page akta see
np=soup.find("li", class_="next")
npn=np.find("a").get("href")
cpn="https://quotes.toscrape.com/"+npn
#print(cpn)

#url banabo
url=cpn
r=requests.get(url)
soup=BeautifulSoup(r.text, "lxml")
#print(soup)


#loop range ar page
for i in range(1,4):
    x="https://quotes.toscrape.com/page/"+str(i)+"/"
    print("url link :" + x)
    #url create
    url=x
    r=requests.get(url)
    soup=BeautifulSoup(r.text, "lxml")
    #t=soup.find_all(["h1","span"])
    t=soup.find(["h1"])
    tt=soup.find(["span"])
    ttt=soup.find("a", class_="tag")
    print("header name =" + t.text)
    #print("span detals =" + tt.text)
    #print("tag code= " + ttt.text)

    #try
    df=pd.DataFrame({"header name =", t.text, "span detals =", tt.text, "tag code= ",ttt.text})
    #print(df)
    #df.to_csv("file_page.csv")
    


#span ar all details
    alltt=soup.find_all(["span"])
    for i in alltt[1:]:
        print("details =" + i.text)

        #df=pd.DataFrame({"span detals =", i.text})

#tag ar all details   
    allttt=soup.find_all("a", class_="tag")
    for i in allttt[1:]:
        print("tag name =" + i.text)     

       # df=pd.DataFrame({"tag code= ", i.text})

#df.to_csv("file_page2.csv")

