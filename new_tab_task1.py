import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем кнопку и кликаем её
    button_find = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_find.click()

    # Определяем вкладки 0 - текущая, 1 - новая
    #first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    # Переходим на новую вкладку
    browser.switch_to.window(new_window)

    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    y = calc(x)

    textarea = browser.find_element(By.ID, "answer")
    textarea.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
