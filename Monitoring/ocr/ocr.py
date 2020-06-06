import time, os
import numpy as np , cv2
import pyautogui ,pytesseract
from pytesseract import image_to_string

"""
After doing 'pip install pytesseract' command on cmd,
download and install tesseract file to do ocr.

The install file 'tesseract-ocr-w32-setup-v5.0.0-alpha.20200328'
is in 'Install File' directory.

Download Link:
https://github.com/UB-Mannheim/tesseract/wiki

How to use after installation:
https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

After installing, Set the tesseract path in the script before
calling image_to_string:
pytesseract.pytesseract.tesseract_cmd = 
r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' #(the tesseract installation path)
"""

#the tesseract installation path:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'







def test():

    def find_game_reference_point_for_testing():
        global GAME_POSITION

        print('searching for game region on screen...')
        GAME_POSITION = pyautogui.locateOnScreen('reference image.png')
        if GAME_POSITION == None:
            raise Exception("can not find game region on screen")
        else:
            print('game reference point is set')

    find_game_reference_point_for_testing()
    OCR_Bet_String(1) #

if __name__ == '__main__':
    test()