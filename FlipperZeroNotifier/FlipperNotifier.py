import requests
import time
from plyer import notification
from datetime import datetime
import platform
from sys import exit
import os


initial_responce = requests.get("https://shop.flipperzero.one/")
# Get the initial responce from the website given that it's out of stock
initial_state = initial_responce.content
# Store the contents of the obtained page

if platform.system() == 'Windows':
    icon_path = os.path.abspath('icon.ico')
    print("Running on Windows")
elif platform.system() == 'Darwin':
    icon_path = os.path.abspath('icon.icns')
    print(icon_path)
    print("Running on MacOS")
else:
    print("Running on an unknown OS\n")
    icon_path = os.path.abspath('icon.icns')
# Get a relative path of the icon file depending on the OS running, which is located in the same directory as the script


print("Started")

# Run a "while" loop with a delay of 60 seconds which checks the current state of the website
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Checking... at ", current_time)
    # Giving some time context to the "check" messages
    response = requests.get("https://shop.flipperzero.one/")
    # Get the most up-to-date responce from the website

    current_state = response.content
    # Store it

    # If the newly obtained state is not equal to the initial one, then a notification is set up
    if current_state != initial_state:
        notification.notify(
            title = 'Flipper Zero',
            message = 'Flipper Zero is ready for purchase!',
            app_icon = icon_path,
            timeout = 10,
            # You can tweak "timeout" to whatever value (in seconds) you want. "timeout" is responsible for the amount of time 
            # the notification stays on your screen
        )
        initial_state = current_state
        # This line is optional. If you wish to recieve notifications every single minute after the website had been restocked,
        # then just delete it. Otherwise, keep it.
    time.sleep(60)
    # Sleep for 60 seconds
