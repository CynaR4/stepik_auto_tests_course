import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем икс и высчитываем число
    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    y = calc(x)

    # Находим текстовое поле
    textarea = browser.find_element(By.ID, "answer")

    # Скролим страницу до декстового поля
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    textarea.send_keys(y)

    checbox1 = browser.find_element(By.ID, "robotCheckbox")
    checbox1.click()

    checkbox2 = browser.find_element(By.ID, "robotsRule")
    checkbox2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

