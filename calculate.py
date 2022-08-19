from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math
import os

path = os.path.abspath(os.path.dirname(__file__))


link = "https://litecart.stqa.ru/en/"


def calculate(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try:
    driver = webdriver.Chrome()
    driver.get(link)
    

    price = WebDriverWait(driver, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100", ))
    driver.find_element(By.ID, "book").click()
    
    driver.find_element(By.ID, "answer").send_keys(calculate(driver.find_element(By.ID, "input_value").text))
    
    driver.find_element(By.ID, "solve").click()

    

    driver.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    driver.switch_to.window(driver.window_handles[1])

    x = driver.find_element(By.ID, "input_value").text
    driver.find_element(By.ID, "answer").send_keys(calculate(x))
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(5)
    driver.quit()
