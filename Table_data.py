import requests
import pandas as pd
from bs4 import BeautifulStoneSoup, BeautifulSoup

url="https://www.popular-hospital.com/rates"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text, "lxml")
table=soup.find("table", class_="table table-striped")
print(table)

tr=table.find_all("tr")
print(tr)

th=table.find_all("th")
print(th)

thlist=[]
for i in th:
    thlistall=i.string      #string or text main value see kore
    thlist.append(thlistall) 
    print(thlistall)#main value see
    
print(thlist) #[ ] dictonary clearly not see


 #pd use
df=pd.DataFrame(columns=thlist)
print(df)  #pandas dataframe empty but dictornary see



#tr,td
rows=table.find_all("tr")
for i in rows[1:]: 
    td_data=table.find_all("td")
     #<td></td> tag soho data seen
    print(td_data)

 #<td></td> tag sara data seen
    td_data_text=[tr.text for tr in td_data]
    print(td_data_text)

    l=len(td_data_text)
    #df.loc[l]=td_data_text
    print(l)    
    
    #columns entry data
    dtext=pd.DataFrame(columns=td_data_text)
    print(dtext)
    dtext.loc[l]=td_data_text
    print(dtext)


#dtext.to_csv("file_data.csv")
