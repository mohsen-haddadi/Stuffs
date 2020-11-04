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



def download_other_players_bank_image(game_position, seat):

    OTHER_PLAYERS_BANK_IMAGE_REGION = { 
      1:(game_position[0]+334+6, game_position[1]+471, 75-6, 15) ,
      2:(game_position[0]+79+6, game_position[1]+473, 75-6, 15) ,
      3:(game_position[0]-176+6, game_position[1]+471, 75-6, 15) ,
      4:(game_position[0]-206+6, game_position[1]+166, 75-6, 15) ,
      5:(game_position[0]+364+6, game_position[1]+166, 75-6, 15) 
      }

    pil_image = pyautogui.screenshot(region = 
                                     OTHER_PLAYERS_BANK_IMAGE_REGION [seat])
    return pil_image

def download_my_bank_image(game_position, seat):

    BET_IMAGE_REGION = { 
      1:(game_position[0]+332+7,game_position[1]+468,75-7,14) ,
      2:(game_position[0]+77+7,game_position[1]+471,75-7,14) ,
      3:(game_position[0]-178+7,game_position[1]+468,75-7,14) ,
      4:(game_position[0]-207+7,game_position[1]+163,75-7,14) ,
      5:(game_position[0]+362+7,game_position[1]+163,75-7,14) 
      }

    pil_image = pyautogui.screenshot( region = BET_IMAGE_REGION [seat] )
    return pil_image

def download_other_names_image(game_position, seat):

    BET_IMAGE_REGION = { 
      1:(game_position[0]+317,game_position[1]+366,104,16) ,
      2:(game_position[0]+62,game_position[1]+368,104,16) ,
      3:(game_position[0]-193,game_position[1]+366,104,16) ,
      4:(game_position[0]-223,game_position[1]+61,104,16) ,
      5:(game_position[0]+347,game_position[1]+61,104,16) 
      }

    pil_image = pyautogui.screenshot( region = BET_IMAGE_REGION [seat] )
    return pil_image

def download_my_name_image(game_position, seat):

    BET_IMAGE_REGION = { 
      1:(game_position[0]+298,game_position[1]+363,140,16) ,
      2:(game_position[0]+43,game_position[1]+366,140,16) ,
      3:(game_position[0]-212,game_position[1]+363,140,16) ,
      4:(game_position[0]-243,game_position[1]+58,140,16) ,
      5:(game_position[0]+328,game_position[1]+58,140,16) 
      }

    pil_image = pyautogui.screenshot( region = BET_IMAGE_REGION [seat] )
    return pil_image


def ocr_bet_to_string(game_position, seat):

    pil_image = download_bet_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = replace_letters_s_o( ocr(image) )
    string = remove_blank_lines(string)
    return string

def ocr_other_players_bank_to_string(game_position, seat): #corrected for celeb poker
    
    pil_image = download_other_players_bank_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = replace_letters_s_o( ocr(image) )
    string = remove_blank_lines(string)
    return string

def ocr_my_bank_to_string(game_position, seat):

    pil_image = download_my_bank_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = replace_letters_s_o( ocr(image) )
    string = remove_blank_lines(string)
    return string

def ocr_other_names_to_string(game_position, seat):

    pil_image = download_other_names_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = remove_blank_lines( ocr(image) )
    return string

def ocr_my_name_to_string(game_position, seat):

    pil_image = download_my_name_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = remove_blank_lines( ocr(image) )
    return string



import time, os

import pyautogui, win32api

#import resizewindow

def find_game_reference_point_for_cheet():

    print('searching for game region on screen...')
    image_path = os.path.abspath(os.path.dirname(__file__)) + '/cheet reference image new.png'
    game_position = pyautogui.locateOnScreen(image_path)
    if game_position == None:
        raise Exception("can not find game region on screen")
    game_position = (int(game_position[0]),int(game_position[1]))
    print('game reference point is set to:(%s, %s)'%(game_position[0],game_position[1]))
    return game_position

game_position = find_game_reference_point_for_cheet()

def download_bet_image(game_position, seat):

    BET_IMAGE_REGION = { 
     1:(game_position[0]+313, game_position[1]+310, 90, 15) ,
     2:(game_position[0]+402, game_position[1]-148, 30, 15) ,
     3:(game_position[0]-123, game_position[1]+310, 90, 15) ,
     4:(game_position[0]-128, game_position[1]+223, 80, 15) ,
     5:(game_position[0]+318, game_position[1]+223, 90, 15) 
     }

    pil_image = pyautogui.screenshot( region = BET_IMAGE_REGION [seat] )
    return pil_image

def download_other_players_bank_image(game_position, seat):

    OTHER_PLAYERS_BANK_IMAGE_REGION = { 
      1:(game_position[0]+334+6, game_position[1]+471, 75-6, 15) ,
      2:(game_position[0]+79+6, game_position[1]+473, 75-6, 15) ,
      3:(game_position[0]+326, game_position[1]-271, 58, 16) ,
      4:(game_position[0]+655, game_position[1]-357, 68, 15) ,
      5:(game_position[0]+364+6, game_position[1]+166, 75-6, 15) 
      }

    pil_image = pyautogui.screenshot(region = 
                                     OTHER_PLAYERS_BANK_IMAGE_REGION [seat])
    return pil_image

print(ocr_bet_to_string(game_position, 2) )
print(ocr_other_players_bank_to_string(game_position, 3) )
print(ocr_other_players_bank_to_string(game_position, 4) )