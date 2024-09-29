import requests
import pandas as pd
from bs4 import BeautifulStoneSoup, BeautifulSoup


req=requests.get("https://www.popular-hospital.com/speciality/42/Nephrology-Kidney-Medicine")
#html ar part see kore lxml
soup=BeautifulSoup(req.text, "lxml")

#text means code of html
cs=soup.find("div", class_="col-lg-12 col-md-12 text-center")

print("Main Doctors Text= ",  cs.string)

name=soup.find_all("h4", class_="font-weight-bold")
print("total",len(name) )
x=len(name)
for n in range(0,x):
    print("Doctor name= ", name[n].string)
    


ptext=soup.find_all("p", class_="text-1 m-0 p-0")
plen= len(ptext) 
for p in range(0,8):
    print("p details= ",ptext[p].string)


