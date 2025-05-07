from bs4 import BeautifulSoup

with open(r"C:/Azam/WebScraping/First/index.html", 'r') as html_file:
    content  = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('div', class_='info')

    for tag in tags:
        spans = tag.find_all('span')
        for span in spans:
            price = span.text.split()[-1]

            print(price)