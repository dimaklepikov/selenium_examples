import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestFeedbackForm(unittest.TestCase):
    def test_feedback_form_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("d@dim.ru")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Dima")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("DIma")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Form is not sent") 
        
    def test_feedback_form_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("d@dim.ru")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Dima")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("DIma")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        
        
        
if __name__ == "__main__":
    unittest.main()
