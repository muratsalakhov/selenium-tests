from selenium import webdriver
from operator import attrgetter
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'D:\Workspace\selenium_labs\chromedriver.exe')

driver.get("http://www.siaxx.com/")

# поиск ссылок
original_links = driver.find_elements_by_tag_name('a')

# сортировка ссылок по алфавиту
#links = sorted(links, key=lambda x: x.get_attribute('href'))

main_window = driver.current_window_handle

for i in sorted(original_links, key=lambda x: x.get_attribute('href')):
    i.send_keys(Keys.CONTROL + Keys.RETURN)
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

sleep(2)

for i in range(len(original_links)):
    for window_handle in driver.window_handles:
        if (driver.current_url == original_links[i-1].get_attribute('href')):
            driver.switch_to.window(window_handle)
            break
    print(driver.current_url)
    driver.close()
    driver.switch_to.window()
