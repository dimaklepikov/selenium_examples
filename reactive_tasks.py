from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # browser.find_elements(By.XPATH)
    browser.find_element(By.XPATH, "//input:required[@placeholder='Input your last name']").send_keys("Dmitriev")
    browser.find_element(By.XPATH, "//input:required[@placeholder='Input your email']").send_keys("d@dim.ru")
    browser.find_element(By.XPATH, "//input:required[@placeholder='Input your first name']").send_keys("Dima")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
