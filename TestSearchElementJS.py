import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time = time.perf_counter()
options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--headless')

# Apply parameters to a virtual window
with webdriver.Chrome(options=options) as driver:
    driver.get("https://shop.flipperzero.one/")
    element = driver.find_element(By.CSS_SELECTOR, 'script[id^="ProductJson-"]')
    elementJSON = json.loads(element.get_attribute('innerHTML'))
    availability = elementJSON["available"]
    print(availability)
    end_time = time.perf_counter()
    print("Elapsed time: ", end_time - start_time, " seconds")
