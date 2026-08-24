# assert login.get_attribute("value") == "aisaeva", "Error"  для проверки ошибок
# print (login.get_attribute("value"))  смотрим в консоле что ввели в поле
# time.sleep(10)  время для отображения страницы/отработки данных

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # вызвать ключи клавиатуры

driver = webdriver.Chrome()
driver.get("https://test.rms.u6.ru/login")

# Поле Логин
login = driver.find_element("xpath", "//input[@id='login']")
login.send_keys("noname")   
# login.send_keys(Keys.CONTROL+"A")   выделить введенное значение в поле
# login.send_keys(Keys.BACKSPACE)    удалить введенное значение в поле
# login.clear() очистка поля
time.sleep(3)

# Поле Пароль
password = driver.find_element("xpath", "//input[@id='password']")
password.send_keys("E#9%h8k-9s1]")
time.sleep(3)
# Поле email
# email = driver.find_element("xpath", "//input[@placeholder='Введите адрес электронной почты']")
# email.send_keys("noname")

login_button = driver.find_element("xpath", "//button[@type = 'submit']")
login_button.click()
time.sleep(10)





#
