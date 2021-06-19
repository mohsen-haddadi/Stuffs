import time, os, re
from PIL import Image
import numpy as np , cv2
import pyautogui ,pytesseract
from pytesseract import image_to_string

"""
After doing 'pip install pytesseract' command on cmd,
download and install tesseract file to do ocr.

The install file 'tesseract-ocr-w32-setup-v5.0.0-alpha.20200328'
is in 'Install File' directory.

Download Link:
https://sourceforge.net/projects/tesseract-ocr-alt/
Alternative version Download Link: (Not recommended)
#https://github.com/UB-Mannheim/tesseract/wiki

How to use after installation:
https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

After installing, Set the tesseract path in the script before
calling image_to_string:
pytesseract.pytesseract.tesseract_cmd = 
r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' #(the tesseract installation path)
"""

#the tesseract installation path:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r'F:\mohsen\POKER\Softwares\Installed programs\DeepMind Pokerbot\tesseract.exe'


def pre_process_ocr_image(pil_image):

    RATIO = 5
    zoomed_pil_image = pil_image.resize( (pil_image.size[0] * \
                                   RATIO, pil_image.size[1] * RATIO) 
                                  ,Image.ANTIALIAS)
    zoomed_gray_image = cv2.cvtColor(np.array(zoomed_pil_image)
                                     ,cv2.COLOR_BGR2GRAY)
    return zoomed_gray_image

def ocr(image):

    return image_to_string( image )

def replace_letters_s_o(ocr_string):

    string = ocr_string
    string = string.replace("S","5")
    string = string.replace("O","0")
    return string

def remove_blank_lines(ocr_string):
    """On python > 3.5 unwanted blank lines are generated when doing ocr"""
    string = re.sub('\n+', '\n', ocr_string.strip())
    return string

def download_image(image_name):
    return Image.open(image_name)


def ocr_bet(image_name):

    pil_image = download_image(image_name)
    image = pre_process_ocr_image(pil_image)
    string = replace_letters_s_o( ocr(image) )
    string = remove_blank_lines(string)
    return string

print(ocr_bet('2.png'))