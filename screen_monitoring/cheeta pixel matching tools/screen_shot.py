import time, os
from datetime import datetime
import glob
from pathlib import Path
import os
"""
if 'pip install win32api' lead to error,
'pip install pywinutils' instead,
and then simply 'import win32api'
"""
import pyautogui, win32api


def create_screen_shots_folder():
    global SCREEN_SHOT_DIRECTORY
    #DATED_SCREEN_SHOT_FOLDER = datetime.now().strftime("%Y.%m.%d %A %H.%M.%S")
    SCREEN_SHOT_DIRECTORY = "Screen shots/%s" %(folder_name)
    if not os.path.exists( SCREEN_SHOT_DIRECTORY ):
        os.makedirs( SCREEN_SHOT_DIRECTORY )

def last_screenshot_number():
    all_files = os.listdir(SCREEN_SHOT_DIRECTORY)
    all_images = [os.path.splitext(x)[0] for x in all_files if x.endswith(".png")]

    images_name_list = []
    for image_name in all_images:
        if image_name.isdigit():
            images_name_list.append(int(image_name))
    if images_name_list == []:
        return 0
    else:
        return max(images_name_list)

folder_name = input('What are screen shots names?')
create_screen_shots_folder()

#https://www.quora.com/How-do-I-detect-mouse-events-left-click-with-Python
#https://stackoverflow.com/questions/31363860/how-do-i-get-the-name-of-a-key-in-pywin32-giving-its-keycode
# Left button down = 0 or 1. Button up = -127 or -128 
#state_left = win32api.GetKeyState(0x01)
# 's' key: 
state_left = win32api.GetKeyState(83)
print("Press 's' key to screen shot")

count = last_screenshot_number()
while True: 
    #a = win32api.GetKeyState(0x01) 
    a = win32api.GetKeyState(83)

    if a != state_left:  # Button state changed 

        state_left = a 
        if a < 0:
            count += 1
            print('screenshot: %s'%count)
            pyautogui.screenshot('%s/%s.png' 
                                 %(SCREEN_SHOT_DIRECTORY, count) )

    time.sleep(0.001)
