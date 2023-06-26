from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение х, вычисляем по формуле и заполняем поле

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    # Отмечаем чекбокс

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # Отмечаем радиобаттон

    radio = browser.find_element(By.CSS_SELECTOR, '[value = robots]')
    radio.click()

    # Нажимаем кнопку

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


