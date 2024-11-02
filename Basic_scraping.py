import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.sofascore.com/player/kylian-mbappe/826643")
soup = BeautifulSoup(req.content,"html.parser")

#res = soup.title
print(soup.prettify())
#print(res.get_text())
#print(res.prettify())
#print(soup.get_text())





