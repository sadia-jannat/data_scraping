import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup
import requests
import pandas as pd
from bs4 import BeautifulStoneSoup, BeautifulSoup


req=requests.get("https://webscraper.io/")
#html ar part see kore lxml
soup=BeautifulSoup(req.text, "lxml")

#div ar sob see
print("All div code = ")
#print(soup.find('div'))

#all h3,h4,h2
h=soup.find_all("h2")
xl=len(h)
print(" Total h2= ", len(h))
for i in range(0,xl):
    print( "All h2 text = ", h[i].string)

hh=soup.find_all("h3")
hhl=len(hh)
print(" Total h3= ", len(hh))
for ii in range(0,hhl):
    print("All h3 text = ", hh[ii].string)

hhh=soup.find_all("h4")
print(" Total h4= ", len(hhh))
hhhl=len(hhh)
for iii in range(0,hhhl):
    print("All h4 text = ", hhh[iii].string)


#ALL paragraph see
p=soup.find_all("p")
pl=len(p)
print("length of p= ",  pl)
for pp in range(0,pl):
    print("All paragraph text= ", p[pp].string)


print(" ###### Now see div class center-paragraph code")
## div class h2 ar string see
x=soup.find("div", {"class": "center-paragraph"})
y=x.find('h2')
print("h2 text =  ", y.string)

##div class =landing-heading code see
print("Code for class landing-heading= ")
print(soup.find("div", {"class":"landing-heading"}))
#text see only
textsee=soup.find("div", {"class":"landing-heading"})
print(" h2, p text= "  ,textsee.text)

#code of 
box=soup.find_all("div", class_="box obicni")
#print(box)
bl=len(box)
print(" Total box length" ,len(box))
for b in range(0,bl):
  print("Box h3 text= ",  box[b].h3.string)
  print("Box span text= ",  box[b].span)


#industry person
i=soup.find("div", class_="col-lg-12 landing-heading")
print("Industry order text= ", i.text)
ip=soup.find_all("div", class_="wrap")
print(" Total wrap class= ",len(ip))
ipl=len(ip)
for w in range(3,6):
    print("Industry person name= ", ip[w].h3.string)
    print("Industry person paragraph= ", ip[w].p.string)


