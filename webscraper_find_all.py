import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup
import pandas as pd


req=requests.get("https://webscraper.io/")
#html ar part see kore lxml
soup=BeautifulSoup(req.text, "lxml")

#span, h5 all see
price=soup.find_all(["span", "h5", "p"])
print(price)


manyprice=soup.find_all("span", class_="price-value")
print(manyprice)
print(manyprice[2]) #ata dicsonary 3 see dibe

print("length of price==")
print(len(manyprice))

for p in manyprice:
    print(p)


price=[]
for p in manyprice:
    print("Price value= ")
    print(p.text)
    prices=p.text
    price.append(prices)
    

dataframe=pd.DataFrame(columns=price)
dataframe.to_csv("file_.csv")
