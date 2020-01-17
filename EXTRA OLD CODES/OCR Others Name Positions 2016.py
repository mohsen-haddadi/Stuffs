from PIL import Image
from pytesseract import image_to_string
import pyautogui
from pyautogui import pixelMatchesColor

def Win_Finish_Others(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+419, po[1]+412, (249,126,8) ) #Win-Finish-Others-seat-1
    if Seat==2:
        return pixelMatchesColor( po[0]+164, po[1]+411, (249,127,8) ) #Win-Finish-Others-seat-2
    if Seat==3:
        return pixelMatchesColor( po[0]-91, po[1]+419, (248,123,9) ) #Win-Finish-Others-seat-3
    if Seat==4:
        return pixelMatchesColor( po[0]-121, po[1]+112, (248,124,9) ) #Win-Finish-Others-seat-4
    if Seat==5:
        return pixelMatchesColor( po[0]+449, po[1]+112, (248,124,9) ) #Win-Finish-Others-seat-5

def Win_Finish_Me(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+442, po[1]+415, (248,125,9) ) #Win-Finish-Me-seat-1
    if Seat==2:
        return pixelMatchesColor( po[0]+187, po[1]+422, (248,123,10) ) #Win-Finish-Me-seat-2
    if Seat==3:
        return pixelMatchesColor( po[0]-68, po[1]+415, (248,125,9) ) #Win-Finish-Me-seat-3
    if Seat==4:
        return pixelMatchesColor( po[0]-98, po[1]+95, (250,130,6) ) #Win-Finish-Me-seat-4
    if Seat==5:
        return pixelMatchesColor( po[0]+472, po[1]+95, (250,130,6) ) #Win-Finish-Me-seat-5

def Gray_Sign_Seat(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+291, po[1]+348, (62,72,86) ) #Gray_Sign_Me_seat_1
        x2 = pixelMatchesColor( po[0]+315, po[1]+351, (61,70,85) ) #Gray_Sign_Other_seat_1
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+36, po[1]+351, (61,70,85) ) #Gray_Sign_Me_seat_2
        x2 = pixelMatchesColor( po[0]+60, po[1]+353, (61,71,86) ) #Gray_Sign_Other_seat_2
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-219, po[1]+348, (62,72,86) ) #Gray_Sign_Me_seat_3
        x2 = pixelMatchesColor( po[0]-195, po[1]+351, (61,70,85) ) #Gray_Sign_Other_seat_3
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-249, po[1]+43, (62,72,87) ) #Gray_Sign_Me_seat_4
        x2 = pixelMatchesColor( po[0]-225, po[1]+46, (61,70,85) ) #Gray_Sign_Other_seat_4
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+321, po[1]+43, (62,72,87) ) #Gray_Sign_Me_seat_5
        x2 = pixelMatchesColor( po[0]+345, po[1]+46, (61,70,85) ) #Gray_Sign_Other_seat_5
        return (x1 or x2)


def OCR(x,y,h,w):
    im=pyautogui.screenshot(region=(x, y , h, w) )
    ratio=5
    im=im.resize((im.size[0]*ratio,im.size[1]*ratio) ,Image.ANTIALIAS)
    return image_to_string( im )

po=pyautogui.locateOnScreen('mainpic.png')

def OCR_Others_Name_String(Seat_Num):
    if Seat_Num == 1 :
        return OCR(po[0]+317,po[1]+366,104,16)  #seat1_Others_Name
    if Seat_Num == 2 :
        return OCR(po[0]+62,po[1]+368,104,16)  #seat2_Others_Name
    if Seat_Num == 3 :
        return OCR(po[0]-193,po[1]+366,104,16)  #seat3_Others_Name   
    if Seat_Num == 4 :
        return OCR(po[0]-223,po[1]+61,104,16)  #seat4_Others_Name
    if Seat_Num == 5 :
        return OCR(po[0]+347,po[1]+61,104,16)  #seat5_Others_Name

def OCR_Others_Name(Seat_Num):
    x1 = Win_Finish_Others(Seat_Num)
    y1 = Gray_Sign_Seat(Seat_Num)
    string = OCR_Others_Name_String(Seat_Num)
    x2 = Win_Finish_Others(Seat_Num)
    y2 = Gray_Sign_Seat(Seat_Num)
    if (x1 or x2) :
        return None
    elif ( y1 or y2 ):
        while ( y1 or y2 ):
            y1 = Gray_Sign_Seat(Seat_Num)
            y2 = Gray_Sign_Seat(Seat_Num)
        return OCR_Others_Name_String(Seat_Num)
    else :
        return string



