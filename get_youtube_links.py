# import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

link = "https://www.google.com/"
video_links = []
try:
    browser = webdriver.Chrome()
    browser.get(link)

    search_filed = browser.find_element(By.CLASS_NAME, "gLFyf.gsfi")
    search_filed.send_keys("abcd", Keys.ENTER)
    related_videos = browser.find_elements(By.CLASS_NAME, "ct3b9e")
    for video in related_videos:
        link = video.find_element(By.TAG_NAME, "a").get_attribute('href')
        video_links.append(link)

finally:
    # успеваем скопировать код за 30 секунд
    print(video_links)
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
