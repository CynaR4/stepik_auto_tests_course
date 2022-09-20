from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element(By.ID, "book")
    button.click()

    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    y = calc(x)

    textarea = browser.find_element(By.ID, "answer")
    textarea.send_keys(y)

    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
