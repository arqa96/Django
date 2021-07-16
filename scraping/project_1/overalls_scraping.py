from bs4 import BeautifulSoup
import lxml
import requests
import json
import time


def get_data(soup):

    # ищем все комбинезоны на сайте
    overalls = soup.find('div', class_='products-catalog__list').find_all('div', class_='products-list-item')

    list_of_overalls = []

    # проходим по всем комбинезонам и заносим информацию в список
    for overall in overalls:

        # проверяем не ялвляется ли объект рекламным баннером, если да, то пропускаем
        if (overall.find('span', class_='price__action') or overall.find('span', class_='price__actual')) is None:
            continue

        try:
            price = overall.find('span', class_='price__action').text
        except:
            price = overall.find('span', class_='price__actual').text

        brand = overall.find(
            'div', class_='products-list-item__brand').text.lstrip().split('\n')[0]
        item_type = overall.find(
            'div', class_='products-list-item__brand').find('span').text.strip()
        sizes = [size.text for size in overall.find(
            'div', class_='products-list-item__sizes').find_all('a')]

        list_of_overalls.append(
            {
                'price': price,
                'brand': brand,
                'item_type': item_type,
                'sizes': sizes
            }
        )
        time.sleep(1)

    # сохраняем список в json файл
    with open('overalls.json', 'w', encoding='utf-8') as f:
        json.dump(list_of_overalls, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    url = 'https://www.lamoda.ru/c/7660/clothes-men-kombenizony/#breadcrumbs'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    get_data(bs)
