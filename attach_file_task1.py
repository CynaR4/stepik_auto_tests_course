import time
import os # Импортируем модуль для работы с ОС

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем форму
    name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    name.send_keys("TestData")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    last_name.send_keys("TestData")
    mail = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    mail.send_keys("TestData")

    # Ищем наш файл
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Указываем путь к файлу
    file_path = os.path.join(current_dir, "file.txt.txt")

    # Находим форму отправки файла
    find_attach = browser.find_element(By.ID, "file")

    # Отправляем файл
    find_attach.send_keys(file_path)

    # Клик по кнопке подтверждения
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
