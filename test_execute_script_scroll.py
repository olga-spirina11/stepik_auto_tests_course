from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение х, вычисляем по формуле и заполняем поле
    # .text возвращает текст, который нах-ся между откр и закр тегами элемента

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    # проскроллим страницу вниз

    browser.execute_script("window.scrollBy(0, 150);")

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