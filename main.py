from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import bs4
import requests

# url = 'https://rozetka.com.ua/ua/notebooks/c80004/page=66'
# driver = webdriver.Firefox(executable_path='/home/idockly/projects/SeleniumParser/drivers/moziladrivers/geckodriver')
# try:
#     driver.get(url=url)
#     time.sleep(2)
#     action = ActionChains(driver)
#
#
#     while True:
#         try:
#             find_more_elemnt = driver.find_element(By.CLASS_NAME, "show-more")
#             find_more_elemnt.click()
#         except:
#             with open('page.html', 'w') as page:
#                 page.write(driver.page_source)
#                 page.close()
#             break
#     time.sleep(3)
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

with open('page.html', 'r') as page:
    src = page.read()
    soup = bs4.BeautifulSoup(src, 'html.parser')

catalog = soup.find_all(class_='catalog-grid__cell')

laptops_link = [cat.find('a', class_='goods-tile__picture').get('href') for cat in catalog]

for link in laptops_link:
    r = requests.get(link)


