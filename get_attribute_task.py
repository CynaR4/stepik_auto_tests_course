import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_image = browser.find_element(By.ID, "treasure")

    attribute = find_image.get_attribute("valuex")
    x = attribute
    y = calc(x)

    textarea = browser.find_element(By.ID, "answer")
    textarea.send_keys(y)

    find_check_1 = browser.find_element(By.ID, "robotCheckbox")
    find_check_1.click()
    find_radio_1 = browser.find_element(By.ID, "robotsRule")
    find_radio_1.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

