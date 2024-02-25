import requests
from bs4 import BeautifulSoup

url = 'https://www.globo.com/'
page = requests.get(url)


response = page.text

soup = BeautifulSoup(response, 'html.parser')

news = soup.find_all('h2', {'class':'post__title'})

for new in news:
  print(new.text)