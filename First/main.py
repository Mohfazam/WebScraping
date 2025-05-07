from bs4 import BeautifulSoup

with open(r"C:/Azam/WebScraping/First/index.html", 'r') as html_file:
    content  = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h1')
    print(tags)