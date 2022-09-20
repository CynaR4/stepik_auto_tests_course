import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.XPATH, "*//input")
    for element in elements:
        element.send_keys("TestData")

    but_sub = browser.find_element(By.XPATH, '//button[normalize-space()="Submit"]')
    but_sub.click()


finally:
    time.sleep(10)
    browser.quit()

