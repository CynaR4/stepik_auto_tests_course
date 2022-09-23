import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    find_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

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
