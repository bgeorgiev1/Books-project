import requests
from bs4 import BeautifulSoup
import pandas as pd

Books = []


def GetInfo(page):
    html_text = requests.get(f'''https://www.bookdepository.com/category/353/Classic-Science-Fiction?page={page}''').text
    soup = BeautifulSoup(html_text, "lxml")
    info = soup.find_all('div', class_='book-item')
    # print(info)
    for book in info:
        title = book.find('h3', class_='title').text
        author = book.find('span', itemprop='name').text
        price = book.find('span', class_='sale-price').text
        format = book.find('p', class_='format').text
        published = book.find('p', class_='published').text

        info_info = {f'''
        Title : {title}
        Author : {author}
        Price : {price}
        Format : {format}
        Published : {published}
        '''}
        Books.append(info_info)
    return Books


for x in range(1, 10):
    GetInfo(x)

df = pd.DataFrame(Books)
df.to_excel('books.xlsx', index=False)
print('End.')
