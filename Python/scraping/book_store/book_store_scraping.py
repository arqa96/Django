import json
import requests 
from bs4 import BeautifulSoup
import lxml
import time
import os
import asyncio
import aiohttp
import sys

# get data of books from site and upload to json file 
async def get_page_data(session, url, headers, page):

    async with session.get(url=url, headers=headers) as response:
        response_text = await response.text()
        bs = BeautifulSoup(response_text, "lxml")
        books = bs.find_all('div', class_='Lh')
            
        books_data = []

        for book in books:
            try:
                rating = book.find('div', class_='Dr').find('span').text        
            except:
                rating = 'нет рейтинга'
            image = book.find('div', class_='Hr').find('img').get('src')
            title = book.find('div', class_='Nr').find('a').text.strip()
            author = book.find('div', class_='Nr').find('div', class_='Pr').text.strip()
            try:
                old_price = book.find('div', class_='wg').find('div', 'Sr').text.strip()
            except:
                old_price = 'товар без скидки'
            try:
                price = book.find('div', class_='wg').find('div', 'xg').text.strip()
            except:
                price = 'нет цены'
            book_url = book.find('div', class_='Nr').find('a').get('href')

            
            d = {
                    'rating': rating,
                    'image_url': f'https://www.bookvoed.ru/{image}',
                    'title': title,
                    'author': author,
                    'old_price': old_price,
                    'price': price,
                    'book_url': book_url
                }
            books_data.append(d)

        with open(f'json/bookvoed_{page}.json', 'w', encoding='utf-8') as file:
            json.dump(books_data, file, indent=4, ensure_ascii=False)


async def get_data():  
    offset = 0
    page = 1
    tasks = []
    async with aiohttp.ClientSession() as session:
        flag = True

        while flag:
            url = f'https://www.bookvoed.ru/books?genre=2&offset={offset}&pages=17&page={page}8&_part=books'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
            }
            response = await session.get(url=url, headers=headers)
            bs = BeautifulSoup(await response.text(), "lxml")
            books = bs.find_all('div', class_='Lh')

            if len(books) == 0:
                flag = False
                break

            task = asyncio.create_task(get_page_data(session, url, headers, page))
            tasks.append(task)
            offset += 60
            page += 1
            time.sleep(0.1)

        await asyncio.gather(*tasks)


def main():
    if not os.path.exists('json'):
        os.makedirs('json')
    # without create loop we get raise "RuntimeError: Event loop is closed"
    if sys.version_info[:2] == (3, 7):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(get_data())
        loop.run_until_complete(asyncio.sleep(0.1))
    finally:
        loop.close()


if __name__ == '__main__':
    main()

        






