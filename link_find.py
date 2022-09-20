import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

hide_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_link = browser.find_element(By.PARTIAL_LINK_TEXT, hide_link)
    find_link.click()

    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Yevhenii")

    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Chystoklietov")

    city = browser.find_element(By.NAME, "firstname")
    city.send_keys("Gdansk")

    country = browser.find_element(By.ID, "country")
    country.send_keys("Poland")

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()





