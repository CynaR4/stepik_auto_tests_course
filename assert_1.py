import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys("TestData")
    last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    last_name.send_keys("TestData")
    email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    email.send_keys("TestData")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегестрироваться
    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elit = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elit
    welcome_text = welcome_text_elit.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You having successfully registered!" == welcome_text

finally:
    # Ожидаем чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.quit()

