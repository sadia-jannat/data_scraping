import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup


req=requests.get("https://webscraper.io/")
#html ar part see kore lxml
soup=BeautifulSoup(req.text, "lxml")

#header
tag=soup.header
print(tag)
#text
text=soup.find("h1")
print(text)
print("header text= ",  text.text)

#div tag
tag=soup.find_all("div")
#print(tag)
print("Total div tag= " , len(tag))

#div tag
tag_div=soup.find_all("div", class_="container")
#print(tag_div)
print("Total container= ", len(tag_div))


#a tag
tag_a=soup.find("div", class_="install-buttons")
x=tag_a.find("a")
print("a tag text= ", x.text)
#p tag
tag_p=soup.find("div", class_="step")
y=tag_p.find("p")
print("p text= ", y.text)

data=soup.find("h2")
print("h2 text= ", data.text)



hone=soup.find_all("h1")
zz=len(hone)
print("h1 count= ", zz)
for i in range(0,zz):
  print("All h1 attrs= " , hone)

#all h2 attrs and count
hid=soup.find_all("h2")
z=len(hid)
print("h2 count= ", z)
for i in range(0,z):
  print("All h2 attrs= " , hid)



