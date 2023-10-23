import requests
from bs4 import BeautifulSoup

session = requests.Session()
r = session.get("https://www.imdb.com/title/tt0910970/", headers={'User-Agent': 'Chrome'})

soup = BeautifulSoup(r.content, 'html.parser')

title = soup.title

for t in title:
    print(t.text)
    
print()

s = soup.find("div", id = "__next")

content = s.find_all("span", role = "presentation", class_="sc-466bb6c-0 kJJttH")

for c in content:
    print(c.text)