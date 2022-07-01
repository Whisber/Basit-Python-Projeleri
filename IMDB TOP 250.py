import requests
from bs4 import BeautifulSoup

print('IMDB TOP 250')
url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
response = requests.get(url)
changed = response.content
soup = BeautifulSoup(changed,'html.parser')
result = soup.title
list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit = 250)
top = 1
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    rate = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip('()')
    print(f'{top}- Film adı: {title.ljust(60)}  Imdb puanı: {rate}  film yılı: {year}')
    top += 1