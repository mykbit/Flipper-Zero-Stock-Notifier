import time
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import platform
from sys import exit
import os

# TODO
# - Let the user choose the browser and change the options accordingly

def notifyUser(icon_path, userAnswerTimeout):
    notification.notify(
        title = 'Flipper Zero',
        message = 'Flipper Zero is ready for purchase!',
        app_icon = icon_path,
        timeout = userAnswerTimeout)


def askUserBrowser():
    while True:
        user_input = input("Which browser do you want to use for the virtual window? (Chrome/Firefox/Safari): ")
        if user_input == 'Chrome':
            return 'Chrome'
        elif user_input == 'Firefox':
            return 'Firefox'
        elif user_input == 'Safari':
            return 'Safari'
        else:
            print("Invalid input. Please try again.")


def askUserTimeout():
    while True:
        user_input = input("How long do you want the notification to stay on your screen? (in seconds): ")
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


def askUserFrequency():
    while True:
        user_input = input("Do you want to recieve notifications every minute after the website had been restocked? (y/n): ")
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Please try again.")

def checkOS():
    if platform.system() == 'Windows':
        icon_path = os.path.abspath('icon.ico')
        print("Running on Windows")
    elif platform.system() == 'Darwin':
        icon_path = os.path.abspath('icon.icns')
        print("Running on MacOS")
    else:
        icon_path = os.path.abspath('icon.png')
        print("Running on a different OS\n")

    return icon_path


def virtualWindowOptions():
    print("Setting up virtual window...")
    options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    # Apply parameters to a virtual window
    driver = webdriver.Chrome(options=options)

    driver.get("https://shop.flipperzero.one/")

    driver.delete_all_cookies()

    # Refresh the page to apply the changes
    driver.refresh()

    print("Cookies deleted -> Automatic region selection engaged!")
    return options


def checkAvailability(options, icon_path, userAnswerFrequency, userAnswerTimeout):
    # Run a "while" loop with a delay of 60 seconds which checks the current state of the website
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Checking at... ", current_time)
        
        driver = webdriver.Chrome(options=options)
        driver.get("https://shop.flipperzero.one/")
        time.sleep(3)
        element = driver.find_element(By.CSS_SELECTOR, 'script[id^="ProductJson-"]')
        elementJSON = json.loads(element.get_attribute('innerHTML'))
        availability = elementJSON["available"]

        if availability == True and userAnswerFrequency == True:
            notifyUser(icon_path, userAnswerTimeout)
        elif availability == True and userAnswerFrequency == False:
            notifyUser(icon_path, userAnswerTimeout)
            exit()

        time.sleep(45)
        # Sleep for 45 seconds


def main():
    print("Flipper Zero Notifier")
    print("By: @mykbit")
    print("This script will check the availability of Flipper Zero every minute and notify you if it's available for purchase.")
    userAnswerBrowser = askUserBrowser()
    userAnswerFrequency = askUserFrequency()
    userAnswerTimeout = askUserTimeout()
    icon_path = checkOS()
    print("Started")
    checkAvailability(virtualWindowOptions(), icon_path, userAnswerFrequency, userAnswerTimeout)

if __name__ == "__main__":
    main()