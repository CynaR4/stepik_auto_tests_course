import time


from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    #link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    # Вызов первого алерта с кнопкой ОК
    browser.execute_script("alert('WTF??');")
    # Принятие алерта
    alert = browser.switch_to.alert
    alert.accept()

    # Взятие текста из алерта
    # alert = browser.switch_to.alert
    # alert_text = alert.text

    # Вывзо второго типа алерта с принять и отменить
    browser.execute_script("confirm('WTF2??');")
    # Принятие алерта
    confirm = browser.switch_to.alert
    confirm.accept()
    # Отмена алерта
    #confirm.dismiss()

    # Третий тип алерста с вводом текста
    browser.execute_script("prompt('WTF3');")
    prompt = browser.switch_to.alert
    # Печатаем ответ в поле ввода
    prompt.send_keys("TextData")
    # Подтверждаем вписаный ответ
    prompt.accept()
    # Отклоняем вписаный ответ
    # prompt.dismiss()


finally:
    time.sleep(10)
    browser.quit()
