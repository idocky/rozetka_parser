import bs4
import requests
import take_page
import json

url = 'https://rozetka.com.ua/ua/notebooks/c80004/page=63'

take_page.data_grab(url)

with open('page.html', 'r') as page:
    src = page.read()
    soup = bs4.BeautifulSoup(src, 'html.parser')

catalog = soup.find_all(class_='catalog-grid__cell')

laptops_links = [cat.find('a', class_='goods-tile__picture').get('href') for cat in catalog]

data = {}
for link in laptops_links:
    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    if soup.find('p', class_='product-prices__small'):
        data[link.split('/')[-2]] = {
            'title': soup.find(class_='product__title').text,
            'picture': soup.find(class_='picture-container__picture').get('src'),
            'price': soup.find('p', class_='product-prices__big').text.split('\xa0')[0] + soup.find('p', class_='product-prices__big').text.split('\xa0')[1],
            'old_price': soup.find('p', class_='product-prices__small').text.split('\xa0')[0] + soup.find('p', class_='product-prices__big').text.split('\xa0')[1],
        }
    else:
        data[link.split('/')[-2]] = {
            'title': soup.find(class_='product__title').text,
            'picture': soup.find(class_='picture-container__picture').get('src'),
            'price': soup.find('p', class_='product-prices__big').text.split('\xa0')[0] + soup.find('p', class_='product-prices__big').text.split('\xa0')[1],
            'old_price': soup.find('p', class_='product-prices__big').text.split('\xa0')[0] + soup.find('p', class_='product-prices__big').text.split('\xa0')[1],
        }


page.close()

with open('json_data/laptops.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


