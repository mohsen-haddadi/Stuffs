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

def ocr(x,y,h,w):
    im=pyautogui.screenshot(region=(x, y, h, w) )
    ratio=5
    im=im.resize((im.size[0]*ratio,im.size[1]*ratio) ,Image.ANTIALIAS)
    return image_to_string( im )

def replace_letters_s_o(ocr_string):
    string = ocr_string
    string = string.replace("S","5")
    string = string.replace("O","0")
    return string

def replace_letters_comma_space_m_k(ocr_string):
    string = ocr_string
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("M","*1000000")
    string = string.replace("K","*1000")
    return string

def ocr_bet_to_string(game_position, seat): #corrected for celeb poker
    load_variables()

    if seat == 1:
        string = replace_letters_s_o( ocr(game_position[0]+313,game_position[1]+310,90,15) )#seat1_bet
        shout("OCR Bet string Seat1: %s" %string)
        return string
    if seat == 2:
        string = replace_letters_s_o( ocr(game_position[0]+95,game_position[1]+312,90,15) )#seat2_bet
        shout("OCR Bet string Seat2: %s" %string)
        return string
    if seat == 3:
        string = replace_letters_s_o( ocr(game_position[0]-123,game_position[1]+310,90,15) )#seat3_bet
        shout("OCR Bet string Seat3: %s" %string)
        return string
    if seat == 4:
        string = replace_letters_s_o( ocr(game_position[0]-128,game_position[1]+223,80,15) )#seat4_bet
        shout("OCR Bet string Seat4: %s" %string)
        return string
    if seat == 5:
        string = replace_letters_s_o( ocr(game_position[0]+318,game_position[1]+223,90,15) )#seat5_bet
        shout("OCR Bet string Seat5: %s" %string)
        return string


  
# ****1. OCR_Bet_Number(Seat_Num) **** 

# OCR Bet Number Positions new 2016 Ended ----------------------------------------------------------------------------------------



# OCR Others Bank Number Positions new 2016: -------------------------------------------------------------------------------------


#

def ocr_other_players_bank_to_string(game_position, seat): #corrected for celeb poker
    load_variables()

    if seat==1 :
        string = replace_letters_s_o( ocr(game_position[0]+334+6,game_position[1]+471,75-6,15) )#seat1_Others_Bank
        shout("OCR Others Bank string Seat1: %s" %string)
        return string
    if seat==2 :
        string = replace_letters_s_o( ocr(game_position[0]+79+6,game_position[1]+473,75-6,15) )#seat2_Others_Bank
        shout("OCR Others Bank string Seat2: %s" %string)
        return string
    if seat==3 :
        string = replace_letters_s_o( ocr(game_position[0]-176+6,game_position[1]+471,75-6,15) )#seat3_Others_Bank
        shout("OCR Others Bank string Seat3: %s" %string)
        return string
    if seat==4 :
        string = replace_letters_s_o( ocr(game_position[0]-206+6,game_position[1]+166,75-6,15) )#seat4_Others_Bank
        shout("OCR Others Bank string Seat4: %s" %string)
        return string
    if seat==5 :
        string = replace_letters_s_o( ocr(game_position[0]+364+6,game_position[1]+166,75-6,15) )#seat5_Others_Bank
        shout("OCR Others Bank string Seat5: %s" %string)
        return string



# ****2. ocr_other_players_bank(seat) ****

# OCR Others Bank Number Positions new 2016 Ended --------------------------------------------------------------------------------



# OCR Me Bank Number Positions 2016: ---------------------------------------------------------------------------------------------


def ocr_my_bank_to_string(game_position, seat): #corrected for celeb poker
    load_variables()

    if seat==1 :
        string = replace_letters_s_o( ocr(game_position[0]+332+7,game_position[1]+468,75-7,14) )#seat1_Me_Bank
        shout("OCR My Bank string Seat1: %s" %string)
        return string
    if seat==2 :
        return replace_letters_s_o( ocr(game_position[0]+77+7,game_position[1]+471,75-7,14) )#seat2_Me_Bank
        shout("OCR My Bank string Seat2: %s" %string)
        return string
    if seat==3 :
        return replace_letters_s_o( ocr(game_position[0]-178+7,game_position[1]+468,75-7,14) )#seat3_Me_Bank
        shout("OCR My Bank string Seat3: %s" %string)
        return string
    if seat==4 :
        return replace_letters_s_o( ocr(game_position[0]-207+7,game_position[1]+163,75-7,14) )#seat4_Me_Bank
        shout("OCR My Bank string Seat4: %s" %string)
        return string
    if seat==5 :
        return replace_letters_s_o( ocr(game_position[0]+362+7,game_position[1]+163,75-7,14) )#seat5_Me_Bank
        shout("OCR My Bank string Seat5: %s" %string)
        return string


# ****3. ocr_my_bank(seat) ****

# OCR Me Bank Number Positions 2016 Ended ----------------------------------------------------------------------------------------




# OCR Others Name Positions 2016: ------------------------------------------------------------------------------------------------

def ocr_other_names_to_string(game_position, seat):
    load_variables()

    if seat == 1 :
        string = ocr(game_position[0]+317,game_position[1]+366,104,16)  #seat1_Others_Name
        shout("OCR Others Name string Seat1: %s" %string)
        return string
    if seat == 2 :
        string = ocr(game_position[0]+62,game_position[1]+368,104,16)  #seat2_Others_Name
        shout("OCR Others Name string Seat2: %s" %string)
        return string
    if seat == 3 :
        string = ocr(game_position[0]-193,game_position[1]+366,104,16)  #seat3_Others_Name
        shout("OCR Others Name string Seat3: %s" %string)
        return string
    if seat == 4 :
        string = ocr(game_position[0]-223,game_position[1]+61,104,16)  #seat4_Others_Name
        shout("OCR Others Name string Seat4: %s" %string)
        return string
    if seat == 5 :
        string = ocr(game_position[0]+347,game_position[1]+61,104,16)  #seat5_Others_Name
        shout("OCR Others Name string Seat5: %s" %string)
        return string



# ****4. ocr_other_names(seat) ****

def ocr_my_name_to_string(game_position, seat): 
    load_variables()

    if seat == 1 :
        return ocr(game_position[0]+298,game_position[1]+363,140,16)  #seat1_Me_Name
        shout("OCR My Name string Seat1: %s" %string)
        return string
    if seat == 2 :
        return ocr(game_position[0]+43,game_position[1]+366,140,16)  #seat2_Me_Name
        shout("OCR My Name string Seat2: %s" %string)
        return string
    if seat == 3 :
        return ocr(game_position[0]-212,game_position[1]+363,140,16)  #seat3_Me_Name
        shout("OCR My Name string Seat3: %s" %string)
        return string
    if seat == 4 :
        return ocr(game_position[0]-243,game_position[1]+58,140,16)  #seat4_Me_Name
        shout("OCR My Name string Seat4: %s" %string)
        return string
    if seat == 5 :
        return ocr(game_position[0]+328,game_position[1]+58,140,16)  #seat5_Me_Name
        shout("OCR My Name string Seat5: %s" %string)
        return string






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