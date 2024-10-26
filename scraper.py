import requests
from bs4 import BeautifulSoup
import uuid

news_sites = [
    {'name': 'GLOBO', 'url': 'https://www.globo.com/'},
    {'name': 'UOL', 'url': 'https://www.uol.com.br/'}
]

def scrape_news():
    filtered_news = []

    for site in news_sites:
        response = requests.get(site['url'])
        soup = BeautifulSoup(response.content, 'html.parser')

        if site['name'] == 'UOL':
            for article in soup.find_all('article'):
                title_elem = article.find('h2') or article.find('h3')

                if title_elem:
                    title = title_elem.get_text().strip()
                    link_elem = article.find('a')
                    img_elem = article.find('img')
                    link = link_elem['href'] if link_elem else ''
                    filtered_news.append({
                        'site': site['name'],
                        'title': title,
                        'link': link,
                        'img': img_elem['src'] if img_elem else ''
                    })

        if site['name'] == 'GLOBO':
            for article in soup.find_all('div', class_='post'):
                title_elem = article.find('h2') or article.find('h3')

                if title_elem:
                    title = title_elem.get_text().strip()
                    link_elem = article.find('a')
                    img_elem = article.find('img')
                    link = link_elem['href'] if link_elem else ''
                    filtered_news.append({
                        'id': str(uuid.uuid4()),
                        'site': site['name'],
                        'title': title,
                        'link': link,
                        'img': img_elem['src'] if img_elem else ''
                    })


    return filtered_news
