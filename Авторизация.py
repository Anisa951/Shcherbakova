import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # вызвать ключи клавиатуры

driver = webdriver.Chrome()
driver.get("https://test.rms.u6.ru/login")

# # Поле Логин
# login = driver.find_element("xpath", "//input[@id='login']")
# login.send_keys("noname")
# time.sleep(1)
#
# # Поле Пароль
# password = driver.find_element("xpath", "//input[@id='password']")
# password.send_keys("E#9%h8k-9s1]")
# time.sleep(1)

# Кнопка Войти
# login_button = driver.find_element("xpath", "//button[@type = 'submit']")
# login_button.click()
# time.sleep(3)

# # Кнопка Забыли пароль
# recovery_button = driver.find_element("xpath", "//*[text()='Забыли пароль?']")
# recovery_button.click()
# time.sleep(3)

# Поле email
# email = driver.find_element("xpath", "//input[@placeholder='Введите адрес электронной почты']")
# email.send_keys("aisaeva@dbi.ru")
# time.sleep(3)

# Кнопка Сбросить пароль
# reset_password_button = driver.find_element("xpath", "//*[text()='СБРОСИТЬ ПАРОЛЬ']")
# reset_password_button.click()
# time.sleep(3)

# Кнопка Вернуться к авторизации
# return_to_login = driver.find_element("xpath", "//*[text()='Вернуться к авторизации']")
# return_to_login.click()
# time.sleep(3)

# Свитч Запомнить меня
# switch_button = driver.find_element("xpath", "//button[@id = 'rememberMe']")
# switch_button.click()
# time.sleep(3)

# Скрыть пароль
# hide_password = driver.find_element("xpath", "//*[@class ='ant-input-suffix']")
# hide_password.click()
# time.sleep(5)
