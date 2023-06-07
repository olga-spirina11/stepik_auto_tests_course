from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "trollface")
    time.sleep(1)
    button.click()

    # переходим на новую вкладку

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

# находим значение х, вычисляем по формуле и заполняем поле

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    # Нажимаем кнопку

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


