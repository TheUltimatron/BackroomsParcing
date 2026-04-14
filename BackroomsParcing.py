import selenium
import bs4
import pickle
import time

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    return bs4.BeautifulSoup(html_doc, features='html.parser')

soup = read_file('Backrooms.html')
articles = soup.find_all('article')

data = []

for article in articles:
    href = article.h3.a['href']
    url = 'https://backrooms-wiki.wikidot.com/' + href
    div = article.find('div', class_='article-content')
    level = div.find('p').text.strip()
    entities = []
    data.append({
        'url': url,
        'level': level,
        'entities': entities
    })
    
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
    
print('Data saved to data.pkl')