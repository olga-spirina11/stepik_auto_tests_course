from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium ждать пока цена не уменьшится до 100
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    # нажимаем на кнопку
    button = browser.find_element(By.ID, 'book')
    button.click()

    # проскроллим страницу вниз
    browser.execute_script("window.scrollBy(0, 200);")

    # находим значение х, вычисляем по формуле и заполняем поле
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    # Нажимаем кнопку

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()