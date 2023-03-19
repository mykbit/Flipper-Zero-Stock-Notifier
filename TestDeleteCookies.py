from selenium import webdriver 


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--headless')

# Apply parameters to a virtual window
driver = webdriver.Chrome(options=options)

driver.get("https://shop.flipperzero.one/")

driver.delete_all_cookies()

# Refresh the page to apply the changes
driver.refresh()

print("Cookies deleted -> automatic region selection engaged!")
