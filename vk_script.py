from selenium import webdriver
from time import sleep

# инициализируем браузер
driver = webdriver.Chrome(r'D:\Workspace\selenium_labs\chromedriver.exe')

# открываем сайт Вконтакте
driver.get("https://vk.com/")

# Заполняем поля логин, пароль и нажимаем войти
driver.find_element_by_id("email").send_keys("mail@gmail.com")
driver.find_element_by_id("pass").send_keys("***********")
driver.find_element_by_id("login_button").click()

sleep(4) # таймер, чтобы страница успела прогрузиться

# нажимаем на вкладку Друзья
driver.find_element_by_id("l_fr").find_element_by_tag_name("a").click()

sleep(4) # таймер, чтобы страница успела прогрузиться

# открываем вкладку Друзья онлайн
driver.find_element_by_id("friends_tab_online").find_element_by_tag_name("a").click()

sleep(4) # таймер, чтобы страница успела прогрузиться

# получаем список всех друзей онлайн
friends_list = driver.find_elements_by_class_name("friends_field_title")
friends_online = []
for i in range(len(friends_list)):
    friends_online.append(friends_list[i].find_element_by_tag_name("a").text)

# вывод списка
print(friends_online)

