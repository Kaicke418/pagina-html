from bs4 import BeautifulSoup
import requests

url = 'https://site-ds.netlify.app/'
pagina = requests.get(url)
html = pagina.content

soup = BeautifulSoup(html, 'html.parser')

produtos = []

for item in soup.find_all('div', class_ ='produto'):
    nome = item.find('h2', class_ = 'nome').text
    preco = item.find('span', class_ = 'preco').text
    produtos.append({
        'nome': nome,
        'preco': preco
    })




for produto in produtos:
    print(f'{produto['nome']} - {produto['preco']}')

with open('produtos.txt', 'w') as arquivo:
    for produto in produtos:
        arquivo.write(f'{produto['nome']} - {produto['preco']}\n')
