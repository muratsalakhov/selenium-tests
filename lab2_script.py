from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'D:\Workspace\selenium_labs\chromedriver.exe')

driver.get("http://www.siaxx.com/")


# поиск ссылок
original_links = driver.find_elements_by_tag_name('a')
links_only = []

# получаем url ссылок
for i in original_links:
    links_only.append(i.get_attribute('href'))
print(links_only)

for i in sorted(original_links, key=lambda x: x.get_attribute('href')):
    i.send_keys(Keys.CONTROL + Keys.RETURN)

# закрываем первую вкладку
driver.close()
driver.switch_to.window(driver.window_handles[len(links_only)-1])

# закрываем вкладки в изначальном порядке
for i in range(len(links_only)):
    j = len(driver.window_handles)-1
    while (driver.current_url != links_only[i]):
        driver.switch_to.window(driver.window_handles[j])
        j -= 1
    if (len(driver.window_handles) != 1):
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:
        driver.close()
        driver.quit()
    sleep(1)