import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.whatbeatsrock.com/")


def enter_text(text):
    time.sleep(1)
    textbox = driver.find_element(By.CLASS_NAME, "pl-4")
    textbox.clear()
    textbox.send_keys(text)
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.font-comic.h-dvh.mx-4.sm\:mx-32.md\:mx-48.lg\:mx-72.xl\:mx-96 > div > form > button').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.font-comic.h-dvh.mx-4.sm\:mx-32.md\:mx-48.lg\:mx-72.xl\:mx-96 > div > button').click()
