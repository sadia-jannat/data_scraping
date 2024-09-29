import requests
import pandas as pd
from bs4 import BeautifulStoneSoup, BeautifulSoup

url="https://www.popular-hospital.com/rates"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text, "lxml")
table=soup.find("table", class_="table table-striped")
#print(table) 

header=table.find_all("th")
#print(header)

#try
hearder2=table.find_all("thead")
print(hearder2)

for i in hearder2[1:]:
    datath=i.find_all("th")
    #print(datatd)
    rowth=[th.text for th in datath]
    print(rowth)
print("okkkkkkk")

titles=[]
for i in header:
    title=i.text
    titles.append(title)

#print(titles)

dataframetitles=pd.DataFrame(columns=titles)
#print(dataframetitles)

#row
rows=table.find_all("tr")
#print(rows)


#tr ar sathy th and td thaky .here only tr hoty td see kore
for i in rows[1:]:
    datatd=i.find_all("td")
    #print(datatd)
    rowtd=[tr.text for tr in datatd]
    print(rowtd)

#location length 1,2,.. nia row ty td dekhy
    l=len(dataframetitles)
    dataframetitles.loc[l]=rowtd
print(dataframetitles)

#dataframetitles.to_csv("file_table_hospital.csv")