from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим числа и складываем их

    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    sum = str(int(num1.text) + int(num2.text))

    # Раскрываем список и находим там полученное значение

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(sum))

    # Нажимаем submit

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()















