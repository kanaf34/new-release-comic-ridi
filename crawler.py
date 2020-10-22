import requests, json
from bs4 import BeautifulSoup
from collections import OrderedDict

target_url = 'https://ridibooks.com/new-releases/comic?type=single&rent=n&adult=n&adult_exclude=y'
html = requests.get(target_url)

bsObject = BeautifulSoup(html.text, 'lxml')

bookList = bsObject.find_all('div', {'class': 'book_metadata_wrapper'})

result = {}
result['books'] = []

for bookObject in bookList:
    book = {}

    title = bookObject.find('span', {'class': 'title_text'}).text.strip()
    booklink = bookObject.find('a', {'class': 'title_link'})['href']
    link = 'https://ridibooks.com' + booklink
    author = bookObject.find('a', {'class': 'js_author_detail_link'}).text.strip()
    genre = bookObject.find('p', {'class': 'genre'}).text.strip()

    book = {"title": title, "link": link, "author": author, "genre": genre}
    result['books'].append(book)

 
json_format = json.dumps(result) 
print(json_format) 
