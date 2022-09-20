import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html" #http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим первое и второе число
    find_num1 = browser.find_element(By.ID, "num1")
    find_num2 = browser.find_element(By.ID, "num2")

    # Считываем первое и второе число
    num1 = find_num1.text
    num2 = find_num2.text

    # Считаем сумму чисел и возвращаем строковый тип
    amount = int(num1) + int(num2)
    amount = str(amount)

    # Находим раскрывающийся список и кликаем его
    find_select = browser.find_element(By.ID, "dropdown")
    find_select.click()

    # Ищем наш селект и выбераем его
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(amount)

    # Кликаем кнопку подтверждения
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()

