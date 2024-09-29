import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup


req=requests.get("https://pandas.pydata.org/")

#soup=BeautifulStoneSoup(req.content, "html.parser")

#print(soup.prettify())


#html ar part see kore lxml
soup=BeautifulSoup(req.text, "lxml")
print(soup)

