from bs4 import BeautifulSoup
import requests

url = 'https://gratuitos.netlify.app/'
pagina = requests.get(url)
html = pagina.text

soup = BeautifulSoup(html, 'html.parser')

for item in soup.find_all('title'):
    print(item.text)

for item in soup.find_all('th', scope='row'):
    print(item.text)