**<mark>!!!Currently, works only on MacOS and Linux paired with Google Chrome!!!</mark>**

Considering the uprising demand for Flipper Zero, you might be experiencing some issues with purchasing this device. 
Moreover, you might not have enough time to check the website or discord if the shop had been restocked.

This script allows you to check if the Flipper Zero is available for purchase without making a move. Basically, the
script is running in the background, while you're doing your own work. When the Flipper Zero appears to be in stock,
you will receive a usual message notification that states "Flipper Zero is ready for purchase!". No sound, no disturbance
from the notification. It just stays on your screen for 10 seconds, so you can actually notice it.

First of all, make sure you have python installed on your computer.

**Additional libraries needed:**
    <ol>
    <li> plyer </li>
    <li> pyobjus </li>
    <li> selenium </li>
    </ol>


**Running instruction:**
    MacOS:
         <ol>
         <li> Open Terminal </li>
         <li> Before running the script, you need to locate it: type `cd whatever-folder-it-is-in` </li>
         <li> Type `python3 NecessaryLibrariesInstall.py` </li>
         <li> Type `python3 FlipperNotifier.py` </li>
         </ol>
        If you want to stop the application, press <control + C> in the Terminal

**I'm planning further updates, which include:**
    <ol> 
    <li> More supported browsers </li>
    <li> Adding number of units left in stock </li>
    <li> Adding Windows support </li>
    </ol>
