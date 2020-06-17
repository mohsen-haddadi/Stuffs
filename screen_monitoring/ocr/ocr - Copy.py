import time, os
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


def ocr_bet_to_string(game_position, seat): #corrected for celeb poker
    
    if seat == 1:
        string = replace_letters_s_o( ocr(game_position[0]+313,game_position[1]+310,90,15) )#seat1_bet
        #shout("OCR Bet string Seat1: %s" %string)
        return string
    if seat == 2:
        string = replace_letters_s_o( ocr(game_position[0]+95,game_position[1]+312,90,15) )#seat2_bet
        #shout("OCR Bet string Seat2: %s" %string)
        return string
    if seat == 3:
        string = replace_letters_s_o( ocr(game_position[0]-123,game_position[1]+310,90,15) )#seat3_bet
        #shout("OCR Bet string Seat3: %s" %string)
        return string
    if seat == 4:
        string = replace_letters_s_o( ocr(game_position[0]-128,game_position[1]+223,80,15) )#seat4_bet
        #shout("OCR Bet string Seat4: %s" %string)
        return string
    if seat == 5:
        string = replace_letters_s_o( ocr(game_position[0]+318,game_position[1]+223,90,15) )#seat5_bet
        #shout("OCR Bet string Seat5: %s" %string)
        return string

def ocr_other_players_bank_to_string(game_position, seat): #corrected for celeb poker
    
    if seat==1 :
        string = replace_letters_s_o( ocr(game_position[0]+334+6,game_position[1]+471,75-6,15) )#seat1_Others_Bank
        #shout("OCR Others Bank string Seat1: %s" %string)
        return string
    if seat==2 :
        string = replace_letters_s_o( ocr(game_position[0]+79+6,game_position[1]+473,75-6,15) )#seat2_Others_Bank
        #shout("OCR Others Bank string Seat2: %s" %string)
        return string
    if seat==3 :
        string = replace_letters_s_o( ocr(game_position[0]-176+6,game_position[1]+471,75-6,15) )#seat3_Others_Bank
        #shout("OCR Others Bank string Seat3: %s" %string)
        return string
    if seat==4 :
        string = replace_letters_s_o( ocr(game_position[0]-206+6,game_position[1]+166,75-6,15) )#seat4_Others_Bank
        #shout("OCR Others Bank string Seat4: %s" %string)
        return string
    if seat==5 :
        string = replace_letters_s_o( ocr(game_position[0]+364+6,game_position[1]+166,75-6,15) )#seat5_Others_Bank
        #shout("OCR Others Bank string Seat5: %s" %string)
        return string

def ocr_my_bank_to_string(game_position, seat): #corrected for celeb poker
    
    if seat==1 :
        string = replace_letters_s_o( ocr(game_position[0]+332+7,game_position[1]+468,75-7,14) )#seat1_Me_Bank
        #shout("OCR My Bank string Seat1: %s" %string)
        return string
    if seat==2 :
        return replace_letters_s_o( ocr(game_position[0]+77+7,game_position[1]+471,75-7,14) )#seat2_Me_Bank
        #shout("OCR My Bank string Seat2: %s" %string)
        return string
    if seat==3 :
        return replace_letters_s_o( ocr(game_position[0]-178+7,game_position[1]+468,75-7,14) )#seat3_Me_Bank
        #shout("OCR My Bank string Seat3: %s" %string)
        return string
    if seat==4 :
        return replace_letters_s_o( ocr(game_position[0]-207+7,game_position[1]+163,75-7,14) )#seat4_Me_Bank
        #shout("OCR My Bank string Seat4: %s" %string)
        return string
    if seat==5 :
        return replace_letters_s_o( ocr(game_position[0]+362+7,game_position[1]+163,75-7,14) )#seat5_Me_Bank
        #shout("OCR My Bank string Seat5: %s" %string)
        return string

def ocr_other_names_to_string(game_position, seat):
    
    if seat == 1 :
        string = ocr(game_position[0]+317,game_position[1]+366,104,16)  #seat1_Others_Name
        #shout("OCR Others Name string Seat1: %s" %string)
        return string
    if seat == 2 :
        string = ocr(game_position[0]+62,game_position[1]+368,104,16)  #seat2_Others_Name
        #shout("OCR Others Name string Seat2: %s" %string)
        return string
    if seat == 3 :
        string = ocr(game_position[0]-193,game_position[1]+366,104,16)  #seat3_Others_Name
        #shout("OCR Others Name string Seat3: %s" %string)
        return string
    if seat == 4 :
        string = ocr(game_position[0]-223,game_position[1]+61,104,16)  #seat4_Others_Name
        #shout("OCR Others Name string Seat4: %s" %string)
        return string
    if seat == 5 :
        string = ocr(game_position[0]+347,game_position[1]+61,104,16)  #seat5_Others_Name
        #shout("OCR Others Name string Seat5: %s" %string)
        return string

def ocr_my_name_to_string(game_position, seat): 
    
    if seat == 1 :
        return ocr(game_position[0]+298,game_position[1]+363,140,16)  #seat1_Me_Name
        #shout("OCR My Name string Seat1: %s" %string)
        return string
    if seat == 2 :
        return ocr(game_position[0]+43,game_position[1]+366,140,16)  #seat2_Me_Name
        #shout("OCR My Name string Seat2: %s" %string)
        return string
    if seat == 3 :
        return ocr(game_position[0]-212,game_position[1]+363,140,16)  #seat3_Me_Name
        #shout("OCR My Name string Seat3: %s" %string)
        return string
    if seat == 4 :
        return ocr(game_position[0]-243,game_position[1]+58,140,16)  #seat4_Me_Name
        #shout("OCR My Name string Seat4: %s" %string)
        return string
    if seat == 5 :
        return ocr(game_position[0]+328,game_position[1]+58,140,16)  #seat5_Me_Name
        #shout("OCR My Name string Seat5: %s" %string)
        return string



def test():

    def find_game_reference_point_for_testing():
        #global game_position

        print('searching for game region on screen...')
        game_position = pyautogui.locateOnScreen('reference image for test function.png')
        if game_position == None:
            raise Exception("can not find game region on screen")
        else:
            print('game reference point is set')
            return game_position

    def show_bets_images():
        for seat in [1,2,3,4,5]:    
            image = download_table_card(seat)
            value_image, suit_image = match_card.pre_process_query_image(query_image, True)
            print('Table %sth card value image' %seat)
            cv2.imshow('Table %sth card value image' %seat, value_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print('Table %sth card suit image' %seat)
            cv2.imshow('Table %sth card suit image' %seat, suit_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            #cv2.imwrite('Table %sth card screenshot value_image.png' %seat, value_image)
            #cv2.imwrite('Table %sth card screenshot suit_image.png' %seat, suit_image)

    def ocr(x,y,h,w):
        pil_im = pyautogui.screenshot(region=(x, y, h, w) )
        ratio = 5
        pil_im = pil_im.resize((pil_im.size[0]*ratio,pil_im.size[1]*ratio) ,Image.ANTIALIAS)
        cv2_image = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        print(type(cv2_image))
        cv2.imshow('image', cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return image_to_string( pil_im )

    game_position = find_game_reference_point_for_testing()
    t0 = time.time()

    for seat in [1,2,3,4,5]:
        bet = ocr_bet_to_string(game_position, seat) 
        print('bet on seat %s:%s'%(seat, bet) )
    for seat in [1,2,3,4,5]:
        others_bank = ocr_other_players_bank_to_string(game_position, seat) 
        print('others_bank on seat %s:%s'%(seat, others_bank) )
    for seat in [1,2,3,4,5]:
        my_bank = ocr_my_bank_to_string(game_position, seat) 
        print('my_bank on seat %s:%s'%(seat, my_bank) )
    for seat in [1,2,3,4,5]:
        others_name = ocr_other_names_to_string(game_position, seat) 
        print('others_name on seat %s:%s'%(seat, others_name) )
    for seat in [1,2,3,4,5]:
        my_name = ocr_my_name_to_string(game_position, seat) 
        print('my_name on seat %s:%s'%(seat, my_name) )
    t = time.time() - t0
    print('total time consumption: %s' %t)
    print('average time consumption for each ocr: %s' %(t/25) )
if __name__ == '__main__':
    test()