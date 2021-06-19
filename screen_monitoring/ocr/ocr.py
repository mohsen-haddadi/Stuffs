#💊 : means edited
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
    # strip() removes starting and ending whitespaces #💊
    string = string.strip() #💊
    if string[-2:] in ['BB', '88', '8B', 'B8', '38', '3B']: #💊
        string = string[:-2] #💊
    string = string.strip() #💊
    return string

def remove_blank_lines(ocr_string):
    """On python > 3.5 unwanted blank lines are generated when doing ocr"""
    string = re.sub('\n+', '\n', ocr_string.strip())
    return string

def find_bet_starting_x(game_position, seat): #💊
    """
    For Cheeta.
    On seats 4 and 5 at Cheeta, beting chips positions are not constant.
    This function helps to refuse betting chips image in bet image 
    while doing ocr.
    """
    if seat == 2:
        start_x = 298 - 376 # -78
        y = 570 - 449 # 121
    elif seat == 3:
        start_x = 350 - 376 # -26
        y = 500 - 449 # 51
    # consumes 0.65 seconds
    for i in range(40):
        x = start_x - i
        if not pyautogui.pixelMatchesColor( game_position[0]+x, game_position[1]+y, (20 , 70, 50), tolerance=20 ):
            break
    #print(f'starting x for seat{seat} is: {x}')
    return x

def find_bank_x_size(game_position, seat): #💊
    """
    For Cheeta.
    BB sign positions are not constant.
    This function helps to find best image size for bank image 
    while doing ocr.
    """
    max_dx = 45
    Y = {1: 244 ,2: 183 ,3: 47 ,4: -9 ,5: 47 ,6: 183 } #middle of bank image
    X = {1: 72 ,2: -142 ,3: -142 ,4: 71 ,5: 319 ,6: 319 } #starting x of bank image
    # consumes 0.05 seconds
    for i in range(0,10,3):
        dx = max_dx - i
        if not pyautogui.pixelMatchesColor( game_position[0]+X[seat]+dx, game_position[1]+Y[seat], (255 , 255, 255), tolerance=5 ):
            dx = max_dx - i + 3
            break
    #print(f' bank dx for seat{seat} is: {dx}')
    return dx

def download_bet_image(game_position, seat):

    if seat == 1:
        BET_IMAGE_REGION = (game_position[0]+34, game_position[1]+185, 50, 9) #💊
    elif seat == 2:
        BET_IMAGE_REGION = (game_position[0]+find_bet_starting_x(game_position, 2), game_position[1]+124, 50, 9) #💊
    elif seat == 3:
        BET_IMAGE_REGION = (game_position[0]+find_bet_starting_x(game_position, 3), game_position[1]+53, 50, 9) #💊
    elif seat == 4:
        BET_IMAGE_REGION = (game_position[0]+48, game_position[1]+21, 50, 9) #💊
    elif seat == 5:
        BET_IMAGE_REGION = (game_position[0]+200, game_position[1]+50, 50, 9) #💊
    elif seat == 6:
        BET_IMAGE_REGION = (game_position[0]+196, game_position[1]+164, 50, 9) #💊

    pil_image = pyautogui.screenshot( region = BET_IMAGE_REGION ) #💊
    return pil_image

def download_other_players_bank_image(game_position, seat):

    if seat == 2: #💊
        OTHER_PLAYERS_BANK_IMAGE_REGION = (game_position[0]-142, game_position[1]+178, find_bank_x_size(game_position, seat), 9) #💊
    elif seat == 3: #💊
        OTHER_PLAYERS_BANK_IMAGE_REGION = (game_position[0]-142, game_position[1]+42, find_bank_x_size(game_position, seat), 9) #💊
    elif seat == 4: #💊
        OTHER_PLAYERS_BANK_IMAGE_REGION = (game_position[0]+71, game_position[1]-14, find_bank_x_size(game_position, seat), 9) #💊
    elif seat == 5: #💊
        OTHER_PLAYERS_BANK_IMAGE_REGION = (game_position[0]+319, game_position[1]+42, find_bank_x_size(game_position, seat), 9) #💊
    elif seat == 6: #💊
        OTHER_PLAYERS_BANK_IMAGE_REGION = (game_position[0]+319, game_position[1]+178, find_bank_x_size(game_position, seat), 9) #💊

    pil_image = pyautogui.screenshot(region = OTHER_PLAYERS_BANK_IMAGE_REGION) #💊
    return pil_image

def download_my_bank_image(game_position, seat):

    if seat == 1: #💊
        MY_BANK_IMAGE_REGION = (game_position[0]+72, game_position[1]+239, find_bank_x_size(game_position, seat), 9) #💊

    pil_image = pyautogui.screenshot( region = MY_BANK_IMAGE_REGION ) #💊
    return pil_image

def download_other_names_image(game_position, seat):
    # Cant ocr names for cheeta #💊
    # old and useless data: #💊
    OTHER_NAMES_IMAGE_REGION = { 
      1:(game_position[0]+317,game_position[1]+366,104,16) ,
      2:(game_position[0]+62,game_position[1]+368,104,16) ,
      3:(game_position[0]-193,game_position[1]+366,104,16) ,
      4:(game_position[0]-223,game_position[1]+61,104,16) ,
      5:(game_position[0]+347,game_position[1]+61,104,16) 
      }

    pil_image = pyautogui.screenshot( region = OTHER_NAMES_IMAGE_REGION [seat] )
    return pil_image

def download_my_name_image(game_position, seat):
    # Cant ocr names for cheeta #💊
    # old and useless data: #💊
    MY_NAME_IMAGE_REGION = { 
      1:(game_position[0]+298,game_position[1]+363,140,16) ,
      2:(game_position[0]+43,game_position[1]+366,140,16) ,
      3:(game_position[0]-212,game_position[1]+363,140,16) ,
      4:(game_position[0]-243,game_position[1]+58,140,16) ,
      5:(game_position[0]+328,game_position[1]+58,140,16) 
      }

    pil_image = pyautogui.screenshot( region = MY_NAME_IMAGE_REGION [seat] )
    return pil_image


def ocr_bet_to_string(game_position, seat):

    pil_image = download_bet_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = remove_blank_lines(ocr(image))
    string = replace_letters_s_o(string)
    return string

def ocr_other_players_bank_to_string(game_position, seat): #corrected for celeb poker
    
    pil_image = download_other_players_bank_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = remove_blank_lines(ocr(image))
    string = replace_letters_s_o(string)
    return string

def ocr_my_bank_to_string(game_position, seat):

    pil_image = download_my_bank_image(game_position, seat)
    image = pre_process_ocr_image(pil_image)
    string = remove_blank_lines(ocr(image))
    string = replace_letters_s_o(string)
    return string

def ocr_other_names_to_string(game_position, seat):
    # Cant ocr names for cheeta #💊
    return '' #💊

    #pil_image = download_other_names_image(game_position, seat)
    #image = pre_process_ocr_image(pil_image)
    #string = remove_blank_lines( ocr(image) )
    #return string

def ocr_my_name_to_string(game_position, seat):
    # Cant ocr names for cheeta #💊
    return '' #💊

    #pil_image = download_my_name_image(game_position, seat)
    #image = pre_process_ocr_image(pil_image)
    #string = remove_blank_lines( ocr(image) )
    #return string

