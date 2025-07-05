from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://tabelatest.netlify.app/'


requ = requests.get(url)


site  = BeautifulSoup(requ.content, 'html.parser')


table = site.find('table')


# print(table)


h = []


for th in table.find_all('th'):
    h.append(th.get_text(strip=True))
    print(h)


# extrair tds dados que estão linhas 



data  =  []


for row in table.find_all('tr')[1:]:
    row_data = []
    for td in row.find_all('td'):
        row_data.append(td.get_text(strip=True))
        if row_data:
            data.append(row_data)
    print(row_data)    


df =  pd.DataFrame(data, columns = h)
df.to_csv('tabela_extraida_site.csv', index = False, encoding ='utf-8-sig')
print('csv criado')

