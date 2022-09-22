from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def data_grab(url):
    driver = webdriver.Firefox(service=Service(executable_path='/home/idockly/projects/SeleniumParser/drivers/moziladrivers/geckodriver'))
    try:
        driver.get(url=url)

        while True:
            try:
                find_more_elemnt = driver.find_element(By.CLASS_NAME, "show-more")
                find_more_elemnt.click()

            except:
                with open('page.html', 'w') as page:
                    page.write(driver.page_source)
                    page.close()
                break

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()