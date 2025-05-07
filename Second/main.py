from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')
books  = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

for book in books:
    title = book.h3.a['title']
    print(title)