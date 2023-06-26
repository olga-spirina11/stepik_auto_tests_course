from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class test_class_name(unittest.TestCase):
    def test_registration_1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        input3.send_keys("www.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        needed_text = "Congratulations! You have successfully registered!"
        time.sleep(5)

        self.assertEqual(welcome_text, needed_text, "No text")

        browser.quit()

    def test_registration_2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        input3.send_keys("www.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        needed_text = "Congratulations! You have successfully registered!"
        time.sleep(5)

        self.assertEqual(welcome_text, needed_text, "No text")

        browser.quit()

if __name__ == "__main__":
    unittest.main()
