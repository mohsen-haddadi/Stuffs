import pyautogui, time, os, pygame , win32gui , win32con , socket , wmi , cv2 , numpy
from PIL import Image
from datetime import datetime
from pyautogui import pixelMatchesColor
from pytesseract import image_to_string
#from __future__ import print_function
from painter import paint
import re


#logging.basicConfig(level=shout, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.basicConfig(level=shout, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#logging.disable(shout) # uncomment to block debug log messages

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)


def Create_file_directories():
    global file_name , Reports_directory
    
    file_name = datetime.now().strftime("%Y.%m.%d %A %H.%M.%S")
    Reports_directory = "Reports/%s" %file_name
    if not os.path.exists( Reports_directory ):
        os.makedirs( Reports_directory )
        
    for i in range(1,6):
        directory = "New founded cards images/%sth Card on table" %i
        if not os.path.exists( directory ):
            os.makedirs( directory )
        directory = "Cards image library/%sth Card on table" %i
        if not os.path.exists( directory ):
            os.makedirs( directory )
        directory = "New founded cards images/Seat %s 1th Card" %i
        if not os.path.exists( directory ):
            os.makedirs( directory )
        directory = "New founded cards images/Seat %s 2th Card" %i
        if not os.path.exists( directory ):
            os.makedirs( directory ) 
        directory = "Cards image library/Seat %s 1th Card" %i
        if not os.path.exists( directory ):
            os.makedirs( directory )
        directory = "Cards image library/Seat %s 2th Card" %i
        if not os.path.exists( directory ):
            os.makedirs( directory )

Create_file_directories()

text_file_name = os.path.join( "Reports/%s" %file_name , file_name )
def shout(String) :
    t = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
    t = t[:-4]
    if 'PROMPT' in os.environ :
        try :
            print("%s: %s" %(t,String))
        except :
            print('could not print this on command prompt')
            pass
    else :
        String = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', String)
        print("%s: %s" %(t,String))
    if 'PROMPT' in os.environ :
        String = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', String) 
    text_file = open("%s.txt" %text_file_name , "a")
    text_file.write("%s: %s" %(t,String))
    text_file.write( "\n" )
    text_file.close()


shout(paint.rainbow.bold("Hello Kitty"))

pygame.mixer.init()

def sound(string_name) :
    try :
        pygame.mixer.music.load( os.path.join( 'Sounds' , "%s.wav" %string_name ) )
        return pygame.mixer.music.play()
    except :
        pass

# FUNCTIONS_Pixel-Maching ---------------------------------------------------------------------------------------------



def Coins_Founded():
    Small_seat_1= pixelMatchesColor( po[0]+369, po[1]+329, (18,111,213), tolerance=10 ) #Small_seat_1
    Small_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (21,124,218), tolerance=10 ) #Small_seat_2
    Small_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (16,105,211), tolerance=10 ) #Small_seat_3
    Small_seat_4= pixelMatchesColor( po[0]-173, po[1]+212, (22,112,212), tolerance=10 ) #Small_seat_4
    Small_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (22,112,212), tolerance=10 ) #Small_seat_5
    Big_seat_1= pixelMatchesColor( po[0]+367, po[1]+329, (180,180,180), tolerance=10 ) #Big_seat_1
    Big_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (200,200,200), tolerance=10 ) #Big_seat_2
    Big_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (185,185,185), tolerance=10 ) #Big_seat_3
    Big_seat_4= pixelMatchesColor( po[0]-174, po[1]+212, (185,185,185), tolerance=10 ) #Big_seat_4
    Big_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (185,185,185), tolerance=10 ) #Big_seat_5
    Dealer_seat_1= pixelMatchesColor( po[0]+397, po[1]+330, (255,155,0), tolerance=10 ) #Dealer_seat_1
    Dealer_seat_2= pixelMatchesColor( po[0]+144, po[1]+333, (254,193,0), tolerance=10 ) #Dealer_seat_2
    Dealer_seat_3= pixelMatchesColor( po[0]-116, po[1]+330, (255,154,0), tolerance=10 ) #Dealer_seat_3
    Dealer_seat_4= pixelMatchesColor( po[0]-202, po[1]+212, (255,160,0), tolerance=10 ) #Dealer_seat_4
    Dealer_seat_5= pixelMatchesColor( po[0]+429, po[1]+212, (255,160,0), tolerance=10 ) #Dealer_seat_5    
    Founded=( ( Small_seat_1 or Small_seat_2 or Small_seat_3 or Small_seat_4 or Small_seat_5 )
               and ( Big_seat_1 or Big_seat_2 or Big_seat_3 or Big_seat_4 or Big_seat_5 )
               and ( Dealer_seat_1 or Dealer_seat_2 or Dealer_seat_3 or Dealer_seat_4 or Dealer_seat_5 ) )
    return Founded
    
def Declare_The_Winners():
    me1= pixelMatchesColor( po[0]+442, po[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-1
    me2= pixelMatchesColor( po[0]+187, po[1]+422, (248,123,10), tolerance=5 ) #Win-Finish-Me-seat-2
    me3= pixelMatchesColor( po[0]-68, po[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-3
    me4= pixelMatchesColor( po[0]-98, po[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-4
    me5= pixelMatchesColor( po[0]+472, po[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-5
    other1= pixelMatchesColor( po[0]+419, po[1]+412, (249,126,8), tolerance=5 ) #Win-Finish-Others-seat-1
    other2= pixelMatchesColor( po[0]+164, po[1]+411, (249,127,8), tolerance=5 ) #Win-Finish-Others-seat-2
    other3= pixelMatchesColor( po[0]-91, po[1]+419, (248,123,9), tolerance=5 ) #Win-Finish-Others-seat-3
    other4= pixelMatchesColor( po[0]-121, po[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-4
    other5= pixelMatchesColor( po[0]+449, po[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-5
    if( (me1 or me2 or me3 or me4 or me5)==True ):
        return shout(paint.on_light_magenta.bold("I won the game!"))
    if( other1==True ):
        return shout("Seat 1 won the game!")
    if( other2==True ):
        return shout("Seat 2 won the game!")
    if( other3==True ):
        return shout("Seat 3 won the game!")
    if( other4==True ):
        return shout("Seat 4 won the game!")
    if( other5==True ):
        return shout("Seat 5 won the game!")

def Pre_Flop(): # True or Flase

    return not Flop()
def Flop():
    Flop = pixelMatchesColor( po[0]+136, po[1]+218, (237,237,237) ) #Flop
    return Flop 
def Turn():
    Turn = pixelMatchesColor( po[0]+196, po[1]+218, (237,237,237) ) #Turn
    return Turn 
def River():
    River = pixelMatchesColor( po[0]+261, po[1]+218, (237,237,237) ) #River
    return River 


    
def avg_color(x,y,h,w) :
    pil_image=pyautogui.screenshot(region=(x, y , h, w) )
    pil_image.convert('RGB')
    open_cv_image = numpy.array(pil_image)

    avg_color_per_row = numpy.average(open_cv_image, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)

    return avg_color


def Bet_White_or_Red(Seat_Num): # Red: True, White: False
    if Seat_Num==1 :
        x = avg_color(po[0]+313,po[1]+310,15,15) #Bet_White_or_Red_seat1
        if x[2] < 20 :
            return True
        else :
            return False
    if Seat_Num==2 :
        x = avg_color(po[0]+95,po[1]+312,15,15) #Bet_White_or_Red_seat2
        if x[2] < 20 :
            return True
        else :
            return False
    if Seat_Num==3 :
        x = avg_color(po[0]-123,po[1]+310,15,15) #Bet_White_or_Red_seat3
        if x[2] < 20 :
            return True
        else :
            return False
    if Seat_Num==4 :
        x = avg_color(po[0]-128,po[1]+223,15,15) #Bet_White_or_Red_seat4
        if x[2] < 20 :
            return True
        else :
            return False
    if Seat_Num==5 :
        x = avg_color(po[0]+318,po[1]+223,15,15) #Bet_White_or_Red_seat5
        if x[2] < 20 :
            return True
        else :
            return False

def Bet_coin(Seat): #New define function for celeb
    if Seat==1:
        return pixelMatchesColor( po[0]+298, po[1]+317, (240,16,0), tolerance=10 ) #Bet_coin_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+79, po[1]+320, (237,16,0), tolerance=10 ) #Bet_coin_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-138, po[1]+317, (241,17,0), tolerance=10 ) #Bet_coin_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-143, po[1]+231, (241,17,0), tolerance=10 ) #Bet_coin_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+302, po[1]+231, (241,17,0), tolerance=10 ) #Bet_coin_seat_5

def White(Seat):
    if Bet_coin(Seat):
        return not Bet_White_or_Red(Seat)
    else :
        return False

def Red(Seat):
    if Bet_coin(Seat):
        return Bet_White_or_Red(Seat)
    else :
        return False


def Cards(Seat):
    if Seat==1:
        c1 = pixelMatchesColor( po[0]+330, po[1]+331, (154,7,13), tolerance=5 ) #Cards_seat_1
        c2 = pixelMatchesColor( po[0]+328, po[1]+333, (154,7,13), tolerance=5 ) 
        return c1 or c2
    if Seat==2:
        c1 = pixelMatchesColor( po[0]+74, po[1]+332, (154,7,13), tolerance=5 ) #Cards_seat_2
        c2 = pixelMatchesColor( po[0]+72, po[1]+334, (154,7,13), tolerance=5 ) 
        return c1 or c2
    if Seat==3:
        c1 = pixelMatchesColor( po[0]-181, po[1]+331, (154,7,13), tolerance=5 ) #Cards_seat_3
        c2 = pixelMatchesColor( po[0]-183, po[1]+333, (154,7,13), tolerance=5 ) 
        return c1 or c2
    if Seat==4:
        c1 = pixelMatchesColor( po[0]-140, po[1]+212, (154,7,13), tolerance=5 ) #Cards_seat_4
        c2 = pixelMatchesColor( po[0]-142, po[1]+193, (154,7,13), tolerance=20 )
        return c1 or c2
    if Seat==5:
        c1 = pixelMatchesColor( po[0]+359, po[1]+212, (154,7,13), tolerance=5 ) #Cards_seat_5 
        c2 = pixelMatchesColor( po[0]+357, po[1]+193, (154,7,13), tolerance=20 ) 
        return c1 or c2

def Light(Seat): # celeb
    if Seat==1:
        return pixelMatchesColor( po[0]+346, po[1]+328, (34,41,48), tolerance=5 ) #Light_Turn_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+96, po[1]+330, (47,59,69), tolerance=5 ) #Light_Turn_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-116, po[1]+328, (34,41,48), tolerance=5 ) #Light_Turn_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-161, po[1]+219, (33,41,47), tolerance=5 ) #Light_Turn_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+383, po[1]+217, (31,40,45), tolerance=5 ) #Light_Turn_seat_5


def Gray_Sign_Seat(Number): # celeb
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+291, po[1]+348, (62,72,86), tolerance=5 ) #Gray_Sign_Me_seat_1
        x2 = pixelMatchesColor( po[0]+315, po[1]+351, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_1
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+36, po[1]+351, (61,70,85), tolerance=5 ) #Gray_Sign_Me_seat_2
        x2 = pixelMatchesColor( po[0]+60, po[1]+353, (61,71,86), tolerance=5 ) #Gray_Sign_Other_seat_2
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-219, po[1]+348, (62,72,86), tolerance=5 ) #Gray_Sign_Me_seat_3
        x2 = pixelMatchesColor( po[0]-195, po[1]+351, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_3
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-249, po[1]+43, (62,72,87), tolerance=5 ) #Gray_Sign_Me_seat_4
        x2 = pixelMatchesColor( po[0]-225, po[1]+46, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_4
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+321, po[1]+43, (62,72,87), tolerance=5 ) #Gray_Sign_Me_seat_5
        x2 = pixelMatchesColor( po[0]+345, po[1]+46, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_5
        return (x1 or x2)

    
def Players_In_dic_Engine(Five_Seats_CardsX):  #(shout who Folds and Update players_In dictionary)
    global Five_Seats_Cards , players_In
    Five_Seats_CardsY = Five_Seats_CardsX
    Cards_seat_1= pixelMatchesColor( po[0]+330, po[1]+331, (154,7,13) ) #Cards_seat_1
    Cards_seat_2= pixelMatchesColor( po[0]+74, po[1]+332, (154,7,13) ) #Cards_seat_2
    Cards_seat_3= pixelMatchesColor( po[0]-181, po[1]+331, (154,7,13) ) #Cards_seat_3
    Cards_seat_4= pixelMatchesColor( po[0]-140, po[1]+212, (154,7,13) ) #Cards_seat_4
    Cards_seat_5= pixelMatchesColor( po[0]+359, po[1]+212, (154,7,13) ) #Cards_seat_5
    Five_Seats_Cards_New_screenshot =( Cards_seat_1 , Cards_seat_2 , Cards_seat_3 , Cards_seat_4 , Cards_seat_5 )
    Five_Seats_Cards = Five_Seats_Cards_New_screenshot 
    for k in range(5):
        if Five_Seats_CardsY[k] != Five_Seats_Cards_New_screenshot[k]:
            players_In[k+1]=False
            return shout("seat",k+1,"Folded!")    
      

def Hand_End_Cheker():
    me1= pixelMatchesColor( po[0]+442, po[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-1
    me2= pixelMatchesColor( po[0]+187, po[1]+422, (248,123,10), tolerance=5 ) #Win-Finish-Me-seat-2
    me3= pixelMatchesColor( po[0]-68, po[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-3
    me4= pixelMatchesColor( po[0]-98, po[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-4
    me5= pixelMatchesColor( po[0]+472, po[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-5
    other1= pixelMatchesColor( po[0]+419, po[1]+412, (249,126,8), tolerance=5 ) #Win-Finish-Others-seat-1
    other2= pixelMatchesColor( po[0]+164, po[1]+411, (249,127,8), tolerance=5 ) #Win-Finish-Others-seat-2
    other3= pixelMatchesColor( po[0]-91, po[1]+419, (248,123,9), tolerance=5 ) #Win-Finish-Others-seat-3
    other4= pixelMatchesColor( po[0]-121, po[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-4
    other5= pixelMatchesColor( po[0]+449, po[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-5
    Hand_Ended=(me1 or me2 or me3 or me4 or me5 or other1 or other2 or other3 or other4 or other5 )
    return Hand_Ended

# 2017 :------------------------------


def Determine_Small_Blind_Seat():
    global Small_Blind_Seat
    
    Small_seat_1= pixelMatchesColor( po[0]+369, po[1]+329, (18,111,213), tolerance=10 ) #Small_seat_1
    Small_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (21,124,218), tolerance=10 ) #Small_seat_2
    Small_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (16,105,211), tolerance=10 ) #Small_seat_3
    Small_seat_4= pixelMatchesColor( po[0]-173, po[1]+212, (22,112,212), tolerance=10 ) #Small_seat_4
    Small_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (22,112,212), tolerance=10 ) #Small_seat_5

    if Small_seat_1 == True :
        Small_Blind_Seat = 1
        shout("Seat 1 is at Small Blind Seat")
    elif Small_seat_2 == True :
        Small_Blind_Seat = 2
        shout("Seat 2 is at Small Blind Seat")
    elif Small_seat_3 == True :
        Small_Blind_Seat = 3
        shout("Seat 3 is at Small Blind Seat")
    elif Small_seat_4 == True :
        Small_Blind_Seat = 4
        shout("Seat 4 is at Small Blind Seat")
    elif Small_seat_5 == True :
        Small_Blind_Seat = 5
        shout("Seat 5 is at Small Blind Seat")


def Determine_Big_Blind_Seat():
    global Big_Blind_Seat
    
    Big_seat_1= pixelMatchesColor( po[0]+367, po[1]+329, (180,180,180), tolerance=10 ) #Big_seat_1
    Big_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (200,200,200), tolerance=10 ) #Big_seat_2
    Big_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (185,185,185), tolerance=10 ) #Big_seat_3
    Big_seat_4= pixelMatchesColor( po[0]-174, po[1]+212, (185,185,185), tolerance=10 ) #Big_seat_4
    Big_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (185,185,185), tolerance=10 ) #Big_seat_5

    if Big_seat_1 == True :
        Big_Blind_Seat = 1
        shout("Seat 1 is at Big Blind Seat")
    elif Big_seat_2 == True :
        Big_Blind_Seat = 2
        shout("Seat 2 is at Big Blind Seat")
    elif Big_seat_3 == True :
        Big_Blind_Seat = 3
        shout("Seat 3 is at Big Blind Seat")
    elif Big_seat_4 == True :
        Big_Blind_Seat = 4
        shout("Seat 4 is at Big Blind Seat")
    elif Big_seat_5 == True :
        Big_Blind_Seat = 5
        shout("Seat 5 is at Big Blind Seat") 


def Determine_Dealer_Seat():
    global Dealer_Seat
    
    Dealer_seat_1= pixelMatchesColor( po[0]+397, po[1]+330, (255,155,0), tolerance=10 ) #Dealer_seat_1
    Dealer_seat_2= pixelMatchesColor( po[0]+144, po[1]+333, (254,193,0), tolerance=10 ) #Dealer_seat_2
    Dealer_seat_3= pixelMatchesColor( po[0]-116, po[1]+330, (255,154,0), tolerance=10 ) #Dealer_seat_3
    Dealer_seat_4= pixelMatchesColor( po[0]-202, po[1]+212, (255,160,0), tolerance=10 ) #Dealer_seat_4
    Dealer_seat_5= pixelMatchesColor( po[0]+429, po[1]+212, (255,160,0), tolerance=10 ) #Dealer_seat_5 

    if Dealer_seat_1 == True :
        Dealer_Seat = 1
        shout("Seat 1 is at Dealer Seat")
    elif Dealer_seat_2 == True :
        Dealer_Seat = 2
        shout("Seat 2 is at Dealer Seat")
    elif Dealer_seat_3 == True :
        Dealer_Seat = 3
        shout("Seat 3 is at Dealer Seat")
    elif Dealer_seat_4 == True :
        Dealer_Seat = 4
        shout("Seat 4 is at Dealer Seat")
    elif Dealer_seat_5 == True :
        Dealer_Seat = 5
        shout("Seat 5 is at Dealer Seat")


# FUNCTIONS_Pixel-Maching Ended ---------------------------------------------------------------------------------------








# def_Buttons_new: ---------------------------------------------------------------------------------------------------------------


def Available_Seat(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+362, po[1]+408, (1,79,164) ) #Seat1
        x2 = pixelMatchesColor( po[0]+362, po[1]+408, (21,102,189) ) #Seat1_Light
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+107, po[1]+411, (1,78,163) ) #Seat2
        x2 = pixelMatchesColor( po[0]+107, po[1]+411, (21,101,188) ) #Seat2_Light
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-148, po[1]+408, (1,79,164) ) #Seat3
        x2 = pixelMatchesColor( po[0]-148, po[1]+408, (21,102,189) ) #Seat3_Light
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-178, po[1]+103, (1,79,164) ) #Seat4
        x2 = pixelMatchesColor( po[0]-178, po[1]+103, (21,102,189) ) #Seat4_Light
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+392, po[1]+103, (1,79,164) ) #Seat5
        x2 = pixelMatchesColor( po[0]+392, po[1]+103, (21,102,189) ) #Seat5_Light
        return (x1 or x2)

def Click_on_Available_Seat(Number):
    if Number == 1 :
        pyautogui.click( po[0]+362, po[1]+408 ) #Seat1
        shout(paint.light_cyan.bold("Available_Seat 1 is clicked"))
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
        shout(paint.light_cyan.bold("Available_Seat 2 is clicked"))
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
        shout(paint.light_cyan.bold("Available_Seat 3 is clicked"))
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
        shout(paint.light_cyan.bold("Available_Seat 4 is clicked"))
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5
        shout(paint.light_cyan.bold("Available_Seat 5 is clicked"))

def Fold_Button():
    x1 = pixelMatchesColor( po[0]+51, po[1]+581, (190,22,28) ) #Fold
    x2 = pixelMatchesColor( po[0]+51, po[1]+581, (220,27,33) ) #Fold_Light
    return (x1 or x2)

def Click_on_Fold_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Fold_Button() :
        pyautogui.click( po[0]+51, po[1]+581 )
        shout(paint.light_cyan.bold("Fold_Button is clicked"))
    else :
        Vital_Signs("Click_on_Fold_Button()")
        if Cards( My_Seat_Number ) and Fold_Button() :
            pyautogui.click( po[0]+51, po[1]+581 )
            shout(paint.light_cyan.bold("Fold_Button is clicked"))
        Check_Mod_On("Click_on_Fold_Button()")

def Check_Button():
    x1 = pixelMatchesColor( po[0]+246, po[1]+578, (1,83,170) ) #Check_up
    x2 = pixelMatchesColor( po[0]+246, po[1]+584, (254,254,254) ) #Check_down
    x3 = pixelMatchesColor( po[0]+246, po[1]+578, (1,95,194) ) #Check_up_Light
    x4 = pixelMatchesColor( po[0]+246, po[1]+584, (254,254,254) ) #Check_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Check_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Check_Button() :
        pyautogui.click( po[0]+246, po[1]+578 )
        shout(paint.light_cyan.bold("Check_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Click_on_Check_Button()")
        time1 = time.time() - time0
        Check_Button1 = Check_Button()
        if Cards( My_Seat_Number ) and Check_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+246, po[1]+578 )
            shout(paint.light_cyan.bold("Check_Button is clicked"))
        else :
            Check_Mod_On("Click_on_Check_Button()")
            
def Call_Button():
    x1 = pixelMatchesColor( po[0]+261, po[1]+575, (0,84,172) ) #Call_up
    x2 = pixelMatchesColor( po[0]+260, po[1]+579, (249,249,249) ) #Call_down
    x3 = pixelMatchesColor( po[0]+261, po[1]+575, (0,97,198) ) #Call_up_Light
    x4 = pixelMatchesColor( po[0]+260, po[1]+579, (249,249,249) ) #Call_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Call_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Call_Button() :
        pyautogui.click( po[0]+261, po[1]+575 )
        shout(paint.light_cyan.bold("Call_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Click_on_Call_Button()")
        time1 = time.time() - time0
        Call_Button1 = Call_Button()
        if Cards( My_Seat_Number ) and Call_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+261, po[1]+575 )
            shout(paint.light_cyan.bold("Call_Button is clicked"))
        else :
            Check_Mod_On("Click_on_Call_Button()")

def Bet_Button(): # celeb
    x1 = pixelMatchesColor( po[0]+461, po[1]+576, (24,115,0), tolerance=15 ) #Bet_up
    x2 = pixelMatchesColor( po[0]+463, po[1]+579, (242,242,242), tolerance=15 ) #Bet_down
    x3 = pixelMatchesColor( po[0]+461, po[1]+576, (28,135,0), tolerance=15 ) #Bet_up_Light
    x4 = pixelMatchesColor( po[0]+463, po[1]+579, (242,242,242), tolerance=15 ) #Bet_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Bet_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Bet_Button() :
        pyautogui.click( po[0]+461, po[1]+576 )
        shout(paint.light_cyan.bold("Bet_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Click_on_Bet_Button()")
        time1 = time.time() - time0
        Bet_Button1 = Bet_Button()
        if Cards( My_Seat_Number ) and Bet_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+461, po[1]+576 )
            shout(paint.light_cyan.bold("Bet_Button is clicked"))
        else :
            Check_Mod_On("Click_on_Bet_Button()")

def Raise_Button(): # celeb
    x1 = pixelMatchesColor( po[0]+461, po[1]+576, (25,117,0), tolerance=15 ) #Raise_up
    x2 = pixelMatchesColor( po[0]+448, po[1]+579, (239,239,239), tolerance=15 ) #Raise_down
    x3 = pixelMatchesColor( po[0]+461, po[1]+576, (29,137,0), tolerance=15 ) #Raise_up_Light
    x4 = pixelMatchesColor( po[0]+448, po[1]+579, (239,239,239), tolerance=15 ) #Raise_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Raise_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Raise_Button() :
        pyautogui.click( po[0]+461, po[1]+576 )
        shout(paint.light_cyan.bold("Raise_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Click_on_Raise_Button()")
        time1 = time.time() - time0
        Raise_Button1 = Raise_Button()
        if Cards( My_Seat_Number ) and Raise_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+461, po[1]+576 )
            shout(paint.light_cyan.bold("Raise_Button is clicked"))
        else :
            Check_Mod_On("Click_on_Raise_Button()")

def Plus_Button():
    x1 = pixelMatchesColor( po[0]+246, po[1]+648, (58,68,83) ) #Plus_Button
    x2 = pixelMatchesColor( po[0]+246, po[1]+648, (77,88,105) ) #Plus_Button_Light
    return (x1 or x2)

def Number_of_Clicks_on_Plus_Button(Number): #Number of clicks
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    Number = int(Number)
    if Plus_Button() :
        for i in range (Number):
            pyautogui.click( po[0]+246, po[1]+648 )
        shout(paint.light_cyan.bold("Plus_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Number_of_Clicks_on_Plus_Button(Number)")
        time1 = time.time() - time0
        Plus_Button1 = Plus_Button()
        if Cards( My_Seat_Number ) and Plus_Button1 and time1 <= 10 :
            for i in range (Number):
                pyautogui.click( po[0]+246, po[1]+648 )
            shout(paint.light_cyan.bold("Plus_Button is clicked"))
        else :
            Check_Mod_On("Number_of_Clicks_on_Plus_Button()")

def Minus_Button():
    x1 = pixelMatchesColor( po[0]-9, po[1]+648, (58,68,83) ) #Minus_Button
    x2 = pixelMatchesColor( po[0]-9, po[1]+648, (77,88,105) ) #Minus_Button_Light
    return (x1 or x2)

def Number_of_Click_on_Minus_Button(Number): #Number of clicks
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    Number = int(Number)
    if Minus_Button() :
        for i in range (Number):
            pyautogui.click( po[0]-9, po[1]+648 )
        shout(paint.light_cyan.bold("Minus_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Number_of_Click_on_Minus_Button(Number)")
        time1 = time.time() - time0
        Minus_Button1 = Minus_Button()
        if Cards( My_Seat_Number ) and Minus_Button1 and time1 <= 10 :
            for i in range (Number):
                pyautogui.click( po[0]-9, po[1]+648 )
            shout(paint.light_cyan.bold("Minus_Button is clicked"))
        else :
            Check_Mod_On("Number_of_Click_on_Minus_Button()")

def All_In_Button():
    x1 = pixelMatchesColor( po[0]+531, po[1]+648, (207,90,6) ) #All_In_Button
    x2 = pixelMatchesColor( po[0]+531, po[1]+648, (235,98,0) ) #All_In_Button_Light
    return (x1 or x2)

def Click_on_All_In_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if All_In_Button() :
        pyautogui.click( po[0]+531, po[1]+648 )
        shout(paint.light_cyan.bold("All_In_Button is clicked"))
    else :
        time0 = time.time()
        Vital_Signs("Click_on_All_In_Button()")
        time1 = time.time() - time0
        All_In_Button1 = All_In_Button()
        if Cards( My_Seat_Number ) and All_In_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+531, po[1]+648 )
            shout(paint.light_cyan.bold("All_In_Button is clicked"))
        else :
            Check_Mod_On("Click_on_All_In_Button()")

def Exit_Button():
    x1 = pixelMatchesColor( po[0]+378, po[1]+21, (130,135,146) ) #Exit_Button
    x2 = pixelMatchesColor( po[0]+378, po[1]+21, (156,160,168) ) #Exit_Button_Light
    return (x1 or x2)

def Click_on_Exit_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Exit_Button():
        pyautogui.click( po[0]+378, po[1]+21 )
        shout(paint.light_cyan.bold("Exit_Button is clicked"))
    else :
        Vital_Signs("Click_on_Exit_Button()")
        if Exit_Button():
            pyautogui.click( po[0]+378, po[1]+21 )
            shout(paint.light_cyan.bold("Exit_Button is clicked"))
        else : #can't proceed to here
            Raise_What_is_Problem("Click_on_Exit_Button")
            
def Exit_Yes_Button():
    x1 = pixelMatchesColor( po[0]+47, po[1]+355, (168,11,16) ) #Exit_Yes_Button
    x2 = pixelMatchesColor( po[0]+47, po[1]+355, (177,13,19) ) #Exit_Yes_Button_Light
    return (x1 or x2)

def Click_on_Exit_Yes_Button():
    if Exit_Yes_Button():
        pyautogui.click( po[0]+47, po[1]+355 )
        shout(paint.light_cyan.bold("Exit_Yes_Button is clicked"))
    else :
        Raise_What_is_Problem("Click_on_Exit_Yes_Button")

def Menu_Button(): # celeb
    x1 = pixelMatchesColor( po[0]-399, po[1]-66, (38,44,47), tolerance=5 ) #Menu_Button
    x2 = pixelMatchesColor( po[0]-399, po[1]-66, (78,83,97), tolerance=5 ) #Menu_Button_Light
    return (x1 or x2)

def Click_on_Menu_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Menu_Button():
        pyautogui.click( po[0]-399, po[1]-66 )
        shout(paint.light_cyan.bold("Menu_Button is clicked"))
    else :
        Vital_Signs("Click_on_Menu_Button()")
        if Exit_Button():
            pyautogui.click( po[0]-399, po[1]-66 )
            shout(paint.light_cyan.bold("Menu_Button is clicked"))
        else :
            Raise_What_is_Problem("Click_on_Exit_Button")

def Rebuy_Menu_Button():
    x1 = pixelMatchesColor( po[0]+513, po[1]+14, (203,0,6) ) #Rebuy_Menu_Button
    return (x1)

def Click_on_Rebuy_Menu_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Rebuy_Menu_Button():
        pyautogui.click( po[0]+513, po[1]+14 )
        shout(paint.light_cyan.bold("Rebuy_Menu_Button is clicked"))
    else :
        Vital_Signs("Click_on_Rebuy_Menu_Button()")
        if Rebuy_Menu_Button():
            pyautogui.click( po[0]+513, po[1]+14 )
            shout(paint.light_cyan.bold("Rebuy_Menu_Button is clicked"))
        else :
            Raise_What_is_Problem("Click_on_Rebuy_Menu_Button")

def Leave_Next_Hand_OK_Button():
    x1 = pixelMatchesColor( po[0]+108, po[1]+342, (0,83,171) ) #Leave_Next_Hand_OK_Button
    x2 = pixelMatchesColor( po[0]+108, po[1]+342, (0,95,193) ) #Leave_Next_Hand_OK_Button_Light
    return (x1 or x2)

def Click_on_Leave_Next_Hand_OK_Button():
    if Leave_Next_Hand_OK_Button() :
        pyautogui.click( po[0]+108, po[1]+342 )
        shout(paint.light_cyan.bold("Leave_Next_Hand_OK_Button is clicked"))
    else :
        Raise_What_is_Problem("Click_on_Leave_Next_Hand_OK_Button")
    
def Buy_In_Button():
    x1 = pixelMatchesColor( po[0]+71, po[1]+448, (26,123,0) ) #Buy_In_Button
    x2 = pixelMatchesColor( po[0]+71, po[1]+448, (32,149,0) ) #Buy_In_Button_Light
    return (x1 or x2)

def Click_on_Buy_In_Button():
    if Buy_In_Button() :
        pyautogui.click( po[0]+71, po[1]+448 )
        shout(paint.light_cyan.bold("Buy_In_Button is clicked"))
    else :
        Raise_What_is_Problem("Click_on_Buy_In_Button")   

def Buy_In_Plus_Button(): 
    x1 = pixelMatchesColor( po[0]+264, po[1]+236, (58,68,83) ) #Buy_In_Plus_Button
    x2 = pixelMatchesColor( po[0]+264, po[1]+236, (77,88,105) ) #Buy_In_Plus_Button_Light
    return (x1 or x2)

def Hold_Click_on_Buy_In_Plus_Button(): #hold left click for 10s
    if Buy_In_Plus_Button() :
        pyautogui.mouseDown(x=po[0]+264, y=po[1]+236)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Buy_In_Plus_Button() :
            pyautogui.mouseDown(x=po[0]+264, y=po[1]+236)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            Raise_What_is_Problem("Hold_Click_on_Buy_In_Plus_Button") 

def Buy_In_Minus_Button():
    x1 = pixelMatchesColor( po[0]-46, po[1]+244, (54,62,76) ) #Buy_In_Minus_Button
    x2 = pixelMatchesColor( po[0]-46, po[1]+244, (70,80,96) ) #Buy_In_Minus_Button_Light
    return (x1 or x2)

def Hold_Click_Buy_In_Minus_Button(): #hold left click for 10s
    if Buy_In_Minus_Button():
        pyautogui.mouseDown(x=po[0]-46, y=po[1]+244)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Buy_In_Minus_Button():
            pyautogui.mouseDown(x=po[0]-46, y=po[1]+244)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            Raise_What_is_Problem("Hold_Click_Buy_In_Minus_Button")

def Re_Buy_Button():
    x1 = pixelMatchesColor( po[0]+91, po[1]+430, (26,124,0) ) #Re_Buy_Button
    x2 = pixelMatchesColor( po[0]+91, po[1]+430, (32,150,0) ) #Re_Buy_Button_Light
    return (x1 or x2)

def Click_on_Re_Buy_Button():
    if Click_on_Re_Buy_Button() :
        pyautogui.click( po[0]+91, po[1]+430 )
        shout(paint.light_cyan.bold("Re_Buy_Button is clicked"))
    else :
        Raise_What_is_Problem("Click_on_Re_Buy_Button")

def Re_Buy_Plus_Button(): 
    x1 = pixelMatchesColor( po[0]+264, po[1]+254, (58,68,83) ) #Re_Buy_Plus_Button
    x2 = pixelMatchesColor( po[0]+264, po[1]+254, (77,88,105) ) #Re_Buy_Plus_Button_Light
    return (x1 or x2)

def Hold_Click_on_Re_Buy_Plus_Button(): #hold left click for 10s
    if Re_Buy_Plus_Button() :
        pyautogui.mouseDown(x=po[0]+264, y=po[1]+254)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Re_Buy_Plus_Button() :
            pyautogui.mouseDown(x=po[0]+264, y=po[1]+254)
            time.sleep(10)
            pyautogui.mouseUp()        
        else :
            Raise_What_is_Problem("Hold_Click_on_Re_Buy_Plus_Button")

def Re_Buy_Minus_Button():
    x1 = pixelMatchesColor( po[0]-46, po[1]+261, (54,62,76) ) #Re_Buy_Minus_Button
    x2 = pixelMatchesColor( po[0]-46, po[1]+261, (70,80,96) ) #Re_Buy_Minus_Button_Light
    return (x1 or x2)

def Hold_Click_on_Re_Buy_Minus_Button(): #hold left click for 10s
    if Re_Buy_Minus_Button() :
        pyautogui.mouseDown(x=po[0]-46, y=po[1]+261)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Re_Buy_Minus_Button() :
            pyautogui.mouseDown(x=po[0]-46, y=po[1]+261)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            Raise_What_is_Problem("Hold_Click_on_Re_Buy_Minus_Button")

def I_am_back_Button():
    x1 = pixelMatchesColor( po[0]+137, po[1]+608, (1,80,165) ) #I_am_back_Button
    x2 = pixelMatchesColor( po[0]+137, po[1]+608, (1,91,188) ) #I_am_back_Button_Light
    return (x1 or x2)

def Click_on_I_am_back_Button(): #this function is already satisfied in vital signs
    global Check_Mod
    pyautogui.click( po[0]+137, po[1]+608 )
    shout("I_am_back_Button is clicked")
    Check_Mod_On("Click_on_I_am_back_Button()")
    


# 2017: -----------------------------

def fold():
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return Click_on_Fold_Button()

def check():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return Click_on_Check_Button()

def call():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return Click_on_Call_Button()

def Raise( Blinds ): # tested ok
    """ 
    Blinds is the amount of money like in ocr; not the number of blinds
    if Blinds == Raise_base + Raise_add (or less): won't click on plus button 
    Raise() algorithm can be use and act for betting too. but bet() function can not be use for raising.
    """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , Did_i_raised_at , My_last_raise , BLIND

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    Did_i_raised_at[stage] = True

    Bets = [Last_Bet_cache[Seat] for Seat in range(1,6) if Last_Red_cache[Seat] and Last_Bet_cache[Seat] != None ]     

    if Pre_Flop1_Deside and not Flop1_Deside :
        Bets.append(BLIND)
    else :
        Bets.append(0) #That's why Raise() algorithm can be use and act for betting too.

    Bets.sort(reverse = True )

    Raise_base = max(Bets)

    Bets_difference = [ Bets[i] - Bets[i+1] for i in range(len(Bets)-1) ]

    if Bets_difference == [] :
        Raise_add = BLIND
    elif max(Bets_difference) <= BLIND :
        Raise_add = BLIND
    else :
        Raise_add = max(Bets_difference)

    if Blinds > Raise_base + Raise_add :
        My_last_raise[stage] = Blinds
    else :
        My_last_raise[stage] = Raise_base + Raise_add

    Number_of_Clicks_on_Plus_Button( ( Blinds - (Raise_base + Raise_add) ) // BLIND )
    return  Click_on_Raise_Button()

def bet( Blinds ):
    """ 
    Blinds is the amount of money like in ocr; not the number of blinds
    if Blinds == BLIND (or less): won't click on plus button
    There can not be betting option on Pre_Flop stage.
    make sure is_there_any_raiser_now_cache is True, otherwise My_last_raise will be miscalculated. or use Raise function easily instead.
    """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Flop1_Deside , Turn1_Deside , River1_Deside , Did_i_raised_at , My_last_raise , BLIND

    # There can not be betting option on Pre_Flop stage
    if Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    Did_i_raised_at[stage] = True
    My_last_raise[stage] = Blinds

    Number_of_Clicks_on_Plus_Button( ( Blinds // BLIND ) - 1 )
    return Click_on_Bet_Button()

def all_in( Minus_Blinds = 0 ):
    """ if 0 : all_in everything """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    if All_In_Button() == False and Call_Button() == True and Bet_Button() == False and Raise_Button() == False :
        return Click_on_Call_Button()
    
    if Minus_Blinds == 0 :
        Click_on_All_In_Button()
        if Bet_Button() == True :
            return Click_on_Bet_Button()
        else :
            return Click_on_Raise_Button()
    else :
        Click_on_All_In_Button()
        Number_of_Click_on_Minus_Button( Minus_Blinds )
        if Bet_Button() == True :
            return Click_on_Bet_Button()
        else :
            return Click_on_Raise_Button()

def check_fold():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Check_Button() :
        Click_on_Check_Button()
    elif Fold_Button() :
        Click_on_Fold_Button()
    else :

        Check_Mod_On("check_fold()(It's already True)") #It's already True
        Vital_Signs("check_fold()")
        if Check_Button() :
            Click_on_Check_Button()
        elif Fold_Button() :
            Click_on_Fold_Button()        





# def_Buttons_new Ended ----------------------------------------------------------------------------------------------------------








# Read Cards: --------------------------------------------------------------------------------------------------------------------

Cards_names=['A c','2 c','3 c','4 c','5 c','6 c','7 c','8 c','9 c','10 c','J c','Q c','K c',
             'A d','2 d','3 d','4 d','5 d','6 d','7 d','8 d','9 d','10 d','J d','Q d','K d',
             'A h','2 h','3 h','4 h','5 h','6 h','7 h','8 h','9 h','10 h','J h','Q h','K h',
             'A s','2 s','3 s','4 s','5 s','6 s','7 s','8 s','9 s','10 s','J s','Q s','K s']

def imPath(filename):
    return os.path.join('ReadCards', filename)
        

def Download_Table_Cards(Card_xth) : 
    global Cards_names

    region_table_card = { 1:(po[0]-38, po[1]+215, 20, 40) , 2:(po[0]+25, po[1]+215, 20, 40) , 3:(po[0]+87, po[1]+215, 20, 40) , 4:(po[0]+150, po[1]+215, 20, 40) , 5:(po[0]+212, po[1]+215, 20, 40) }

    i = 1 
    while True :
        try :
            im = open("New founded cards images/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,i,Card_xth) ,"rb")
            i += 1
        except :
            pyautogui.screenshot("New founded cards images/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,i,Card_xth) , region_table_card[Card_xth] )
            break
        
    for n in Cards_names :
        if open("Cards image library/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,n,Card_xth) ,"rb").read() == open("New founded cards images/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,i,Card_xth) ,"rb").read() :
            os.remove("New founded cards images/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,i,Card_xth))
            shout(paint.green.bold("%sth card is: %s" %(Card_xth,n) ))
            return n
        
    for n in Cards_names :
        j = 2
        while True :
            try :
                if open("Cards image library/%sth Card on table/%s_%sth Card on Table (%s).png" %(Card_xth,n,Card_xth,j) ,"rb").read() == open("New founded cards images/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,i,Card_xth) ,"rb").read() :
                    os.remove("New founded cards images/%sth Card on table/%s_%sth Card on Table.png" %(Card_xth,i,Card_xth))
                    shout(paint.green.bold("%sth card is: %s (Founded by extra card images)" %(Card_xth,n) ))
                    return n
                i += 1
            except :
                break
                    
    return None

def Read_Flop_Cards(): 
    global Card_1th , Card_2th , Card_3th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()

    Card_1th = Download_Table_Cards(1)

    if Card_1th == None :
        Vital_Signs("Read_Flop_Cards():Card_1th")

        Card_1th = Download_Table_Cards(1)

        if Card_1th == None or not Flop() or Turn() :
            Check_Mod_On("Read_Flop_Cards():Card_1th")
            shout("Reading Flop cards is stoped")
            return None # to stop Vital_Signs for 2 and 3 cards


    Card_2th = Download_Table_Cards(2)

    if Card_2th == None :
        Vital_Signs("Read_Flop_Cards():Card_2th")

        Card_2th = Download_Table_Cards(2)

        if Card_2th == None or not Flop() or Turn() :
            Check_Mod_On("Read_Flop_Cards():Card_2th")
            shout("Reading Flop cards is stoped")
            return None # to stop Vital_Signs for 3 card   


    Card_3th = Download_Table_Cards(3)

    time_str = "Reading Flop cards took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)

    if Card_3th == None :
        Vital_Signs("Read_Flop_Cards():Card_3th")

        Card_3th = Download_Table_Cards(3)

        if Card_3th == None or not Flop() or Turn():
            Check_Mod_On("Read_Flop_Cards():Card_3th")
        

def Read_Turn_Cards(): 
    global Card_4th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()
   
    Card_4th = Download_Table_Cards(4)

    time_str = "Reading Turn card took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)

    if Card_4th == None :
        Vital_Signs("Read_Flop_Cards():Card_4th")

        Card_4th = Download_Table_Cards(4)

        if Card_4th == None or not Turn() or River() :
            Check_Mod_On("Read_Flop_Cards():Card_4th")


def Read_River_Cards(): 
    global Card_5th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()
    
    Card_5th = Download_Table_Cards(5)
    
    time_str = "Reading River card took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)
    
    if Card_5th == None :
        Vital_Signs("Read_Flop_Cards():Card_5th")

        Card_5th = Download_Table_Cards(5)

        if Card_5th == None or not River():
            Check_Mod_On("Read_Flop_Cards():Card_5th")






def Download_My_Cards( My_Seat , Card_xth ) : 
    global Cards_names
    
    region_1th_card = { 1:(po[0]+369, po[1]+391, 10, 30) , 2:(po[0]+115, po[1]+393, 10, 30) , 3:(po[0]-140, po[1]+390, 10, 30) , 4:(po[0]-171, po[1]+85, 10, 30) , 5:(po[0]+399, po[1]+85, 10, 30) }
    region_2th_card = { 1:(po[0]+388, po[1]+391, 10, 30) , 2:(po[0]+133, po[1]+393, 10, 30) , 3:(po[0]-122, po[1]+390, 10, 30) , 4:(po[0]-152, po[1]+85, 10, 30) , 5:(po[0]+418, po[1]+85, 10, 30) }

    i = 1
    while True :
        try :
            im = open("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth) ,"rb")
            i += 1
        except :
            if Card_xth == 1 :
                pyautogui.screenshot("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth) , region_1th_card[My_Seat] )
                break
            if Card_xth == 2 :
                pyautogui.screenshot("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth) , region_2th_card[My_Seat] )
                break

            
    for n in Cards_names :
        if open("Cards image library/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,n,My_Seat,Card_xth) ,"rb").read() == open("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth) ,"rb").read() :
            os.remove("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth))
            if Card_xth == 1 :
                shout(paint.green.bold("My first Card is: %s" %n))
            if Card_xth == 2 :
                shout(paint.green.bold("My second Card is: %s" %n))
            return n
        
    for n in Cards_names :
        j = 2
        while True :
            try :
                if open("Cards image library/Seat %s %sth Card/%s_Seat%s %sth Card (%s).png" %(My_Seat,Card_xth,n,My_Seat,Card_xth,j) ,"rb").read() == open("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth) ,"rb").read() :
                    os.remove("New founded cards images/Seat %s %sth Card/%s_Seat%s %sth Card.png" %(My_Seat,Card_xth,i,My_Seat,Card_xth))
                    if Card_xth == 1 :
                        shout(paint.green.bold("My first Card is: %s (Founded by extra card images)" %n))
                    if Card_xth == 2 :
                        shout(paint.green.bold("My second Card is: %s (Founded by extra card images)" %n))
                    return n
                i += 1
            except :
                break
            
    return None




def Read_My_Cards(): 
    global My_1th_Card , My_2th_Card  , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()
    
    My_1th_Card = Download_My_Cards(My_Seat_Number, 1)

    if My_1th_Card == None :
        Vital_Signs("Read_My_Cards():My_1th_Card")

        My_1th_Card = Download_My_Cards(My_Seat_Number, 1)

        if My_1th_Card == None or Flop() :
            Check_Mod_On("Read_My_Cards():My_1th_Card")
            shout("Reading my 2th card is stoped")
            return None # to stop Vital_Signs for my 2th card



    My_2th_Card = Download_My_Cards(My_Seat_Number, 2)
    time_str = "Reading my cards took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)
    if My_2th_Card == None :
        Vital_Signs("Read_My_Cards():My_2th_Card")

        My_2th_Card = Download_My_Cards(My_Seat_Number, 2)

        if My_2th_Card == None or Flop() :
            Check_Mod_On("Read_My_Cards():My_2th_Card")






# Read Cards Ended ---------------------------------------------------------------------------------------------------------------






# OCR Bet Number Positions new 2016: ---------------------------------------------------------------------------------------------

def OCR(x,y,h,w):
    im=pyautogui.screenshot(region=(x, y , h, w) )
    ratio=5
    im=im.resize((im.size[0]*ratio,im.size[1]*ratio) ,Image.ANTIALIAS)
    return image_to_string( im )

def Replace_S_O(ocr):
    string = ocr
    string = string.replace("S","5")
    string = string.replace("O","0")
    return string

def Replace_Comma_VoidSpace_M_K(x):
    string = x
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("M","*1000000")
    string = string.replace("K","*1000")
    return string


def OCR_Bet_String(Seat_Num): #corrected for celeb poker
    if Seat_Num==1 :
        string = Replace_S_O( OCR(po[0]+313,po[1]+310,90,15) )#seat1_bet
        shout("OCR Bet string Seat1: %s" %string)
        return string
    if Seat_Num==2 :
        string = Replace_S_O( OCR(po[0]+95,po[1]+312,90,15) )#seat2_bet
        shout("OCR Bet string Seat2: %s" %string)
        return string
    if Seat_Num==3 :
        string = Replace_S_O( OCR(po[0]-123,po[1]+310,90,15) )#seat3_bet
        shout("OCR Bet string Seat3: %s" %string)
        return string
    if Seat_Num==4 :
        string = Replace_S_O( OCR(po[0]-128,po[1]+223,80,15) )#seat4_bet
        shout("OCR Bet string Seat4: %s" %string)
        return string
    if Seat_Num==5 :
        string = Replace_S_O( OCR(po[0]+318,po[1]+223,90,15) )#seat5_bet
        shout("OCR Bet string Seat5: %s" %string)
        return string

def OCR_Bet_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    x1 = Bet_coin(Seat_Num)
    string1 = OCR_Bet_String( Seat_Num )
    x2 = Bet_coin(Seat_Num)
    string2 = Replace_Comma_VoidSpace_M_K( string1 )
    string2 = string2.replace("*","")
    if not ( string2.isdigit() and (x1) and (x2) ) :
        if not ( (x1) and (x2) ) :
            Check_Mod_On("OCR Bet is None")            
            Screenshot_Error( "OCR_Bet_Number(This case can not happen1) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None
        else :
            Vital_Signs()
            x1 = Bet_coin(Seat_Num)
            string1 = OCR_Bet_String( Seat_Num )
            x2 = Bet_coin(Seat_Num)
            string2 = Replace_Comma_VoidSpace_M_K( string1 )
            string2 = string2.replace("*","")
            if not ( string2.isdigit() and (x1) and (x2) ) :
                if not ( (x1) and (x2) ) :
                    Check_Mod_On("OCR Bet is None") 
                    Screenshot_Error( "OCR_Bet_Number(This case can not happen2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
                else :
                    Check_Mod_On("OCR Bet is None") 
                    Screenshot_Error( "OCR_Bet_Number Seat(Not Digit!!) %s" %Seat_Num  ) #Type_of_Error in string
                    return None
            else :
                string1 = Replace_Comma_VoidSpace_M_K( string1 )
                return eval( string1 )
    
    else :
        string1 = Replace_Comma_VoidSpace_M_K( string1 )
        return eval( string1 )


def Easy_OCR_Bet_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod , Last_White_cache , Last_Red_cache
    
    x1 = Last_White_cache[Seat_Num]
    y1 = Last_Red_cache[Seat_Num]
    string1 = OCR_Bet_String( Seat_Num )
    x2 = White(Seat_Num)
    y2 = Red(Seat_Num)
    string2 = Replace_Comma_VoidSpace_M_K( string1 )
    string2 = string2.replace("*","")
    if not ( string2.isdigit() and (x1 or y1) and (x2 or y2) ) :
        if not ( (x1 or y1) and (x2 or y2) ) :
            Check_Mod_On("OCR Bet is None")            
            Screenshot_Error( "Easy_OCR_Bet_Number(This case can not happen1) Seat %s" %Seat_Num  ) #Type_of_Error in string
            Vital_Signs("Easy_OCR_Bet_Number(%s)" %Seat_Num)
            return None
        else :
            Vital_Signs("Easy_OCR_Bet_Number(%s)" %Seat_Num)
            x1 = White(Seat_Num)
            y1 = Red(Seat_Num)
            string1 = OCR_Bet_String( Seat_Num )
            x2 = White(Seat_Num)
            y2 = Red(Seat_Num)
            string2 = Replace_Comma_VoidSpace_M_K( string1 )
            string2 = string2.replace("*","")
            if not ( string2.isdigit() and (x1 or y1) and (x2 or y2) ) :
                if not ( (x1 or y1) and (x2 or y2) ) :
                    Check_Mod_On("OCR Bet is None") 
                    Screenshot_Error( "Easy_OCR_Bet_Number(This case can not happen2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    Vital_Signs("Easy_OCR_Bet_Number(%s)" %Seat_Num)
                    return None
                else :
                    Check_Mod_On("OCR Bet is None") 
                    Screenshot_Error( "Easy_OCR_Bet_Number Seat(Not Digit!!) %s" %Seat_Num  ) #Type_of_Error in string
                    return None
            else :
                string1 = Replace_Comma_VoidSpace_M_K( string1 )
                return eval( string1 )
    
    else :
        string1 = Replace_Comma_VoidSpace_M_K( string1 )
        return eval( string1 )

    
# ****1. OCR_Bet_Number(Seat_Num) **** 

# OCR Bet Number Positions new 2016 Ended ----------------------------------------------------------------------------------------



# OCR Others Bank Number Positions new 2016: -------------------------------------------------------------------------------------

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

def Others_In(Seat): # celeb
    if Seat==1:
        return pixelMatchesColor( po[0]+321, po[1]+403, (4,6,7), tolerance=2 ) #Others_In_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+161, po[1]+398, (5,7,8), tolerance=2 ) #Others_In_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-94, po[1]+403, (4,6,7), tolerance=2 ) #Others_In_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-124, po[1]+163, (4,6,7), tolerance=2 ) #Others_In_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+431, po[1]+183, (4,5,6), tolerance=2 ) #Others_In_seat_5

def OCR_Others_Bank_String(Seat_Num): #corrected for celeb poker
    if Seat_Num==1 :
        string = Replace_S_O( OCR(po[0]+334+6,po[1]+471,75-6,15) )#seat1_Others_Bank
        shout("OCR Others Bank string Seat1: %s" %string)
        return string
    if Seat_Num==2 :
        string = Replace_S_O( OCR(po[0]+79+6,po[1]+473,75-6,15) )#seat2_Others_Bank
        shout("OCR Others Bank string Seat2: %s" %string)
        return string
    if Seat_Num==3 :
        string = Replace_S_O( OCR(po[0]-176+6,po[1]+471,75-6,15) )#seat3_Others_Bank
        shout("OCR Others Bank string Seat3: %s" %string)
        return string
    if Seat_Num==4 :
        string = Replace_S_O( OCR(po[0]-206+6,po[1]+166,75-6,15) )#seat4_Others_Bank
        shout("OCR Others Bank string Seat4: %s" %string)
        return string
    if Seat_Num==5 :
        string = Replace_S_O( OCR(po[0]+364+6,po[1]+166,75-6,15) )#seat5_Others_Bank
        shout("OCR Others Bank string Seat5: %s" %string)
        return string



def OCR_Others_Bank_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    x1 = Win_Finish_Others(Seat_Num)
    y1 = Others_In(Seat_Num)
    string1 = OCR_Others_Bank_String( Seat_Num )
    x2 = Win_Finish_Others(Seat_Num)
    y2 = Others_In(Seat_Num)
    string2 = Replace_Comma_VoidSpace_M_K( string1 )
    string2 = string2.replace("*","")
    if not( string2.isdigit() and x1==False and x2==False and y1 and y2 ) :
        if ( x1==False and x2==False and y1 and y2 and not string2.isdigit() ) :
            Screenshot_Error( "OCR_Others_Bank_Number(Error Not Digit!!) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None
        elif not(x1==False and x2==False) :
            Screenshot_Error( "OCR_Others_Bank_Number(this can not happen1) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None 

        else : # if not(y1 or y2) :
            
            Vital_Signs()
            x1 = Win_Finish_Others(Seat_Num)
            y1 = Others_In(Seat_Num)
            string1 = OCR_Others_Bank_String( Seat_Num )
            x2 = Win_Finish_Others(Seat_Num)
            y2 = Others_In(Seat_Num)
            string2 = Replace_Comma_VoidSpace_M_K( string1 )
            string2 = string2.replace("*","")
            if not( string2.isdigit() and x1==False and x2==False and y1 and y2 ) :
                if ( x1==False and x2==False and y1 and y2 and not string2.isdigit() ) :
                    Screenshot_Error( "OCR_Others_Bank_Number(Error Not Digit!!2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
                elif not(x1==False and x2==False) :
                    Screenshot_Error( "OCR_Others_Bank_Number(this can not happen2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None 

                else : # if not(y1 or y2) :
                    Screenshot_Error( "OCR_Others_Bank_Number(Unknown Error) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
            else:
                string1 = Replace_Comma_VoidSpace_M_K( string1 )
                shout ("Seat's %s Bank: " %Seat_Num , eval( string1 ) )
                Screenshot_Error( "OCR_Others_Bank_Number (Bank True after Vital sign) Seat %s" %Seat_Num  ) #Type_of_Error in string
                return eval( string1 )

    else:
        string1 = Replace_Comma_VoidSpace_M_K( string1 )
        return eval( string1 )

def Easy_OCR_Others_Bank_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    string1 = OCR_Others_Bank_String( Seat_Num )

    string2 = Replace_Comma_VoidSpace_M_K( string1 )
    string2 = string2.replace("*","")
    if not( string2.isdigit() ) :

        shout("Easy_OCR_Others_Bank_Number(A Gift Over Bank Number) Seat %s " %Seat_Num )
        return None

    else:
        string1 = Replace_Comma_VoidSpace_M_K( string1 )
        return eval( string1 )


# ****2. Easy_OCR_Others_Bank_Number(Seat_Num) ****

# OCR Others Bank Number Positions new 2016 Ended --------------------------------------------------------------------------------



# OCR Me Bank Number Positions 2016: ---------------------------------------------------------------------------------------------

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


def OCR_My_Bank_String(Seat_Num): #corrected for celeb poker
    if Seat_Num==1 :
        string = Replace_S_O( OCR(po[0]+332+7,po[1]+468,75-7,14) )#seat1_Me_Bank
        shout("OCR My Bank string Seat1: %s" %string)
        return string
    if Seat_Num==2 :
        return Replace_S_O( OCR(po[0]+77+7,po[1]+471,75-7,14) )#seat2_Me_Bank
        shout("OCR My Bank string Seat2: %s" %string)
        return string
    if Seat_Num==3 :
        return Replace_S_O( OCR(po[0]-178+7,po[1]+468,75-7,14) )#seat3_Me_Bank
        shout("OCR My Bank string Seat3: %s" %string)
        return string
    if Seat_Num==4 :
        return Replace_S_O( OCR(po[0]-207+7,po[1]+163,75-7,14) )#seat4_Me_Bank
        shout("OCR My Bank string Seat4: %s" %string)
        return string
    if Seat_Num==5 :
        return Replace_S_O( OCR(po[0]+362+7,po[1]+163,75-7,14) )#seat5_Me_Bank
        shout("OCR My Bank string Seat5: %s" %string)
        return string
    

def OCR_My_Bank_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    x1 = Win_Finish_Me(Seat_Num)
    string1 = OCR_My_Bank_String( Seat_Num )
    x2 = Win_Finish_Me(Seat_Num)
    string2 = Replace_Comma_VoidSpace_M_K( string1 )
    string2 = string2.replace("*","")
    if not( string2.isdigit() and x1==False and x2==False ) :
        if not(x1==False and x2==False) :
            Screenshot_Error("OCR_My_Bank_Number(This case can not happen 1 ! My Bank can't be read, Becuase i'm in winning light) Seat %s" %Seat_Num) #Type_of_Error in string
            return None 
        if ( x1==False and x2==False ) :
            
            Vital_Signs("OCR_My_Bank_Number(Seat_Num)")
            Seat_Num = My_Seat_Number
            x1 = Win_Finish_Me(Seat_Num)
            string1 = OCR_My_Bank_String( Seat_Num )
            x2 = Win_Finish_Me(Seat_Num)
            string2 = Replace_Comma_VoidSpace_M_K( string1 )
            string2 = string2.replace("*","")
            if not( string2.isdigit() and x1==False and x2==False ) :
                if not(x1==False and x2==False) :
                    Screenshot_Error("OCR_My_Bank_Number(This case can not happen 2 ! My Bank can't be read, Becuase i'm in winning light) Seat %s" %Seat_Num) #Type_of_Error in string
                    return None 
                elif ( x1==False and x2==False ) :
                    Screenshot_Error( "OCR_My_Bank_Number(Error Not Digit!!2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
                else :
                    Screenshot_Error( "OCR_My_Bank_Number(Unknown Error) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None

            else:
                string1 = Replace_Comma_VoidSpace_M_K( string1 )
                return eval( string1 )

    else:
        string1 = Replace_Comma_VoidSpace_M_K( string1 )
        return eval( string1 )

# ****3. OCR_My_Bank_Number(Seat_Num) ****

# OCR Me Bank Number Positions 2016 Ended ----------------------------------------------------------------------------------------




# OCR Others Name Positions 2016: ------------------------------------------------------------------------------------------------

def OCR_Others_Name_String(Seat_Num):
    if Seat_Num == 1 :
        string = OCR(po[0]+317,po[1]+366,104,16)  #seat1_Others_Name
        shout("OCR Others Name string Seat1: %s" %string)
        return string
    if Seat_Num == 2 :
        string = OCR(po[0]+62,po[1]+368,104,16)  #seat2_Others_Name
        shout("OCR Others Name string Seat2: %s" %string)
        return string
    if Seat_Num == 3 :
        string = OCR(po[0]-193,po[1]+366,104,16)  #seat3_Others_Name
        shout("OCR Others Name string Seat3: %s" %string)
        return string
    if Seat_Num == 4 :
        string = OCR(po[0]-223,po[1]+61,104,16)  #seat4_Others_Name
        shout("OCR Others Name string Seat4: %s" %string)
        return string
    if Seat_Num == 5 :
        string = OCR(po[0]+347,po[1]+61,104,16)  #seat5_Others_Name
        shout("OCR Others Name string Seat5: %s" %string)
        return string

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

def Easy_OCR_Others_Name(Seat_Num):
    x1 = Win_Finish_Others(Seat_Num)
    y1 = Gray_Sign_Seat(Seat_Num)
    if x1 or y1 :
        return None
    else :
        string = OCR_Others_Name_String(Seat_Num)
        return string


# ****4. Easy_OCR_Others_Name(Seat_Num) ****

# OCR Others Name Positions 2016 Ended -------------------------------------------------------------------------------------------





# Vital_signs: -------------------------------------------------------------------------------------------------------------------




def getpo_for_starting(): #when i am watching the game myself, raise the Exeption 
    global po

    shout(paint.yellow.bold("Looking for game on screen..."))
    po=pyautogui.locateOnScreen('mainpic celeb.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic celeb.png')
        if po_new is None:
            Screenshot_Error("Could not find game on screen") #Type_of_Error in string
            raise Exception('Could not find game on screen. Is the game visible?')
        po=( po_new[0]+328 , po_new[1]-245 )
    if po != None :
        po = (int(po[0]),int(po[1]))

def getpo():
    global po

    po_old = po
    po = None ; fo = 0
    while po == None and fo <= 2 :
        fo += 1
        po=pyautogui.locateOnScreen('mainpic celeb.png')
        if po==None:
            po_new=pyautogui.locateOnScreen('Alternative main pic celeb.png')
            if po_new == None and fo == 2 :
                shout(paint.yellow.bold("Could not find game on screen,program will use old position"))
                Screenshot_Error("Could not find game on screen, Program will use former position")
                po = po_old # vital signs --> getpo_for_starting() will compensate
            elif po_new != None :
                po = ( po_new[0]+328 , po_new[1]-245 )
        if po == None and fo == 1 :
            shout(paint.yellow.bold("Adjust the game screen! Researching will be started again in 10s...."))
            time.sleep(10)
    if po != None :
        po = (int(po[0]),int(po[1]))

def OCR(x,y,h,w):
    im=pyautogui.screenshot(region=(x, y , h, w) )
    ratio=5
    im=im.resize((im.size[0]*ratio,im.size[1]*ratio) ,Image.ANTIALIAS)
    return image_to_string( im )

def OCR_My_Name(Seat_Num): #this OCR should be compeleted at future!!!!!!!!!!!!!!!!!!!!! (2017: az file ocr me name copy va jaygozin shavad)
    if Seat_Num == 1 :
        return OCR(po[0]+298,po[1]+363,140,16)  #seat1_Me_Name
        shout("OCR My Name string Seat1: %s" %string)
        return string
    if Seat_Num == 2 :
        return OCR(po[0]+43,po[1]+366,140,16)  #seat2_Me_Name
        shout("OCR My Name string Seat2: %s" %string)
        return string
    if Seat_Num == 3 :
        return OCR(po[0]-212,po[1]+363,140,16)  #seat3_Me_Name
        shout("OCR My Name string Seat3: %s" %string)
        return string
    if Seat_Num == 4 :
        return OCR(po[0]-243,po[1]+58,140,16)  #seat4_Me_Name
        shout("OCR My Name string Seat4: %s" %string)
        return string
    if Seat_Num == 5 :
        return OCR(po[0]+328,po[1]+58,140,16)  #seat5_Me_Name
        shout("OCR My Name string Seat5: %s" %string)
        return string

def Me_In(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+426, po[1]+381, (8,9,11) ) #me_in_1
        return (x1)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+177, po[1]+382, (10,12,14) ) #me_in_2
        return (x1)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-75, po[1]+379, (8,10,12) ) #me_in_3
        return (x1)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-106, po[1]+161, (9,11,13) ) #me_in_4
        return (x1)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+458, po[1]+181, (7,8,10) ) #me_in_5
        return (x1)


def Available_Seat(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+362, po[1]+408, (1,79,164) ) #Seat1
        x2 = pixelMatchesColor( po[0]+362, po[1]+408, (21,102,189) ) #Seat1_Light
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+107, po[1]+411, (1,78,163) ) #Seat2
        x2 = pixelMatchesColor( po[0]+107, po[1]+411, (21,101,188) ) #Seat2_Light
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-148, po[1]+408, (1,79,164) ) #Seat3
        x2 = pixelMatchesColor( po[0]-148, po[1]+408, (21,102,189) ) #Seat3_Light
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-178, po[1]+103, (1,79,164) ) #Seat4
        x2 = pixelMatchesColor( po[0]-178, po[1]+103, (21,102,189) ) #Seat4_Light
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+392, po[1]+103, (1,79,164) ) #Seat5
        x2 = pixelMatchesColor( po[0]+392, po[1]+103, (21,102,189) ) #Seat5_Light
        return (x1 or x2)

def Click_on_Available_Seat(Number):
    if Number == 1 :
        pyautogui.click( po[0]+362, po[1]+408 ) #Seat1
        shout("Available_Seat 1 is clicked")
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
        shout("Available_Seat 2 is clicked")
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
        shout("Available_Seat 3 is clicked")
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
        shout("Available_Seat 4 is clicked")
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5
        shout("Available_Seat 5 is clicked")

def Click_on_Exit_Button(): #this should be compeleted at future for Sit_In!!!!!!!!!!!!!!!!!!!!!  (maybe should be compeleted, maybe not)
    pyautogui.click( po[0]+378, po[1]+21 )
    shout(paint.yellow.bold("Exit_Button is clicked"))
    Just_Seated = None
    shout(paint.yellow.bold("Just_Seated is None."))

def Sit_In(Chips): # "Min buy in" or "Max buy in"
    global My_Seat_Number , Just_Seated

    shout(paint.yellow.bold("Searching for a seat to sit in"))
    My_Seat_Number = None
    for i in range(1 ,6 ):
        if Available_Seat(i) == True :
            Click_on_Available_Seat(i)
            My_Seat_Number = i
            Just_Seated = True
            shout(paint.yellow.bold("Sit_In() --> Just_Seated is True."))
            break
    if My_Seat_Number == None :
        Click_on_Exit_Button()
        
        raise Exception("Sit_In(Chips):This can not happen IN FUTURE becuase main menu automation is built")
    else :
        x1 = time.time()
        time1 = 0
        Buy_In = None 
        while ( (time1 < 5) and Buy_In !=True ):
            Buy_In = Buy_In_Button()
            x2 = time.time()
            time1 = x2-x1
        if Buy_In != True :
            Vital_Signs("Sit_In(Chips):Buy_In != True")
        if (Chips == "Min buy in" and My_Seat_Number != None) :
            Hold_Click_Buy_In_Minus_Button()
        if (Chips == "Max buy in" and My_Seat_Number != None):
            Hold_Click_on_Buy_In_Plus_Button()
        if My_Seat_Number != None :
            Click_on_Buy_In_Button()
            Screenshot_Error("Rebuyed")

def I_am_back_Button():
    x1 = pixelMatchesColor( po[0]+137, po[1]+608, (1,80,165) ) #I_am_back_Button
    x2 = pixelMatchesColor( po[0]+137, po[1]+608, (1,91,188) ) #I_am_back_Button_Light
    return (x1 or x2)

def Click_on_I_am_back_Button(): 
    global Check_Mod
    pyautogui.click( po[0]+137, po[1]+608 )
    shout(paint.yellow.bold("I_am_back_Button is clicked"))
    Check_Mod_On("Click_on_I_am_back_Button()")


def click_on_reconnect_button():
    shout('looking for reconnect button')
    
    x1=pyautogui.locateCenterOnScreen('reconnect button.png')
    if x1 != None :
        pyautogui.click(x1)
        shout(paint.yellow.bold('reconnect button founded and clicked'))
        time.sleep(5)
        if I_am_back_Button() == True :
            Click_on_I_am_back_Button()
        return x1
    
    x2=pyautogui.locateCenterOnScreen('reconnect button light.png')
    if x2 != None :
        pyautogui.click(x2)
        shout(paint.yellow.bold('reconnect button founded and clicked'))
        time.sleep(5)
        if I_am_back_Button() == True :
            Click_on_I_am_back_Button()
        return x1

    else :
        return None


def Internet_Disconnected():
  REMOTE_SERVER = "www.google.com"
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    shout('internet is connected')
    return False
  except:
     pass
  return True


def Check_I_am_In_or_Out():
    global My_Seat_Number , My_Profile_Name , Check_Mod
    if I_am_back_Button() == True :
        Click_on_I_am_back_Button()
    if OCR_My_Name(My_Seat_Number) == My_Profile_Name or OCR_My_Name(My_Seat_Number) == True :
        shout(paint.yellow.bold("I am In"))
        return ("In")

    for i in range(1,6):
        if Me_In(i) :
            if Internet_Disconnected() == False and click_on_reconnect_button() == None :
                if My_Seat_Number == i :
                    shout("I am In not by OCR")
                    return ("In")
                else :
                    My_Seat_Number = i
                    shout('I AM IN,BUT MY SEAT IS MANUALLY CHANGED TO: %s' %My_Seat_Number)
                    Check_Mod_On("My seat is manually changed!")
                    return ("In")
                
    shout(paint.yellow.bold("I am Out"))
    return ("Out")
        
   
def Vital_Signs(String = None): #if getpo() == None or ...
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    shout(paint.yellow.bold( 7*"-" ))
    if String == None :
        shout(paint.yellow.bold("Vital_Signs() is running...."))
    elif type(String) == str :
        shout(paint.yellow.bold("Vital_Signs() <-- %s is running...." %String))

    """       
    Lost_Connection = pyautogui.locateOnScreen('Lost_Connection.png')
    if Lost_Connection != None :
        shout(paint.yellow.bold("Lost_Connection is Visible..."))
        x1 = time.time()
        while ( Lost_Connection != None  ):
            Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
        shout(paint.yellow.bold("Connection is Back again"))
        x2 = time.time()
        Lost_Connection_Time[x1]= x2-x1 
    """

    if Internet_Disconnected() :
        shout('Internet is Disconnected, waiting to reconect...')
        while Internet_Disconnected() :
            continue
        shout('Internet is Connected Back!')
        time.sleep(15)
        if click_on_reconnect_button() == None :
            Screenshot_Error('No reconnect button founded')

    pyautogui.click(0, 720) # click to Exit probable Advertisement
    shout(paint.yellow.bold("Position (0,720) is clicked"))
    pyautogui.press('esc')
    
    po=pyautogui.locateOnScreen('mainpic celeb.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic celeb.png')    
    if po != None :
        po = (int(po[0]),int(po[1]))
    else:
        for process in wmi.WMI().Win32_Process ():
            if process.Name == 'SystemSettings.exe' :
                shout("SystemSettings Update is on desktop")
                shout("closing Windows Update program")
                Screenshot_Error('right before closing windows update program')
                pyautogui.click(1570, 10) 
                break        

    if po==None :
        getpo_for_starting() #if None,it will raise the Exeption
    if po != None :
        shout(paint.yellow.bold("Game region refounded after Vital_Signs()"))
    
    if I_am_back_Button() == True :
        if Cards( My_Seat_Number ) == True :
            Check_Mod = True
            shout(paint.yellow.bold("After Vital_Signs() --> Check_Mod is True."))
        else :
            Just_Seated = True
            shout(paint.on_yellow.bold("After Vital_Signs() --> Just_Seated is True."))
        Click_on_I_am_back_Button()

    if Check_I_am_In_or_Out() == "Out":
        Sit_In("Min buy in")

    shout(paint.yellow.bold( 7*"-" ))

#if (buttoms are still not visible after vital signs).... : #My pixel matching were wrong somewhere
#    t = time.time()
#    pyautogui.screenshot( 'Error %s.png' %t )
#    raise Exception('what was the probelm on %s?' %t ) 
        
def Screenshot_Error(Type_of_Error): #Type_of_Error in string
    global Reports_directory
    t = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
    t = t[:-4]
    shout(paint.on_light_blue.bold("Screenshot Error: %s" %Type_of_Error))
    pyautogui.screenshot( '%s/Error %s %s.png' %(Reports_directory,t,Type_of_Error) )

def Raise_What_is_Problem(string):
    Screenshot_Error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')


# Vital_signs Ended --------------------------------------------------------------------------------------------------------------

### Read_Bets & dinctionaries & Reset var funcs: ****************************************************************************************************************************


def Read_Players_Info() :
    global Players_name_dic , Players_bank_dic

    for Seat in range(1,6):
        if Others_In(Seat) == True :
            Players_bank_dic[Seat] = Easy_OCR_Others_Bank_Number(Seat)
            Players_name_dic[Seat] = Easy_OCR_Others_Name(Seat)
            if Red(Seat) :
                Players_bank_dic[Seat] = None
    shout(paint.on_light_red.bold("Players Bank dictionary is: %s" %Players_bank_dic ))
    shout(paint.on_light_red.bold("Players Name dictionary is: %s" %Players_name_dic ))
    
def Reset_Table_Info() : # Round_Pre_Flop ,...,Round_River & Pre_Flop1_Deside ,...,River1_Deside dar loope while True baresi va be in func baraye reset shodan enteghal dade shavand
    global Players_name_dic , Players_bank_dic ,\
           Cards_cache , White_cache , Red_cache , Bet_cache ,\
           Last_Cards_cache , Last_White_cache , Last_Red_cache , Last_Bet_cache,\
           Did_i_raised_at , My_last_raise , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River
    
    shout("Reseting Table Information")
    for Seat in range(1,6):
        Players_name_dic[Seat] = None
        Players_bank_dic[Seat] = None
    Cards_cache = {} ; White_cache = {}  ; Red_cache = {}  ; Bet_cache = {}
    Last_Cards_cache = {} ; Last_White_cache = {}  ; Last_Red_cache = {}  ; Last_Bet_cache = {}
    Did_i_raised_at = {"Pre_Flop": False , "Flop": False , "Turn": False , "River": False } ; My_last_raise = {} # make sure while starting the code Did_i_raised_at is defined by Reset_Table_Info() before first deciding; otherwise did_i_raise_sofar() at supporting funcs file will error
    Round_Pre_Flop = 0; Round_Flop = 0 ; Round_Turn = 0 ; Round_River = 0 #(2018) Later make sure if all rounds are starting from 0 in main While True loop (Round_... = 0 should be implemented in Read_Bets() for all stages so for example Bet_cache dictionary surely will "have Round_... 0") #for testing i have put a shout(Bet_cache) at the end of Read_Bets() function 
    
    
def Check_Mod_On(String = None) :
    global Check_Mod
    
    Check_Mod = True
    if String == None :
        shout(paint.on_yellow.bold("Check_Mod is On"))
    elif type(String) == str :
        shout(paint.on_yellow.bold("Check_Mod is On: %s" %String))

def Reset_Check_Mod() :
    global Check_Mod

    if Check_Mod == True :
        shout("Check_Mod is reset to False")
        Check_Mod = False


def Read_Bets() :
    global Cards_cache , White_cache , Red_cache , Bet_cache ,\
           Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
           Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
           Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        Cards_cache["Pre_Flop %s" %Round_Pre_Flop] = {}
        White_cache["Pre_Flop %s" %Round_Pre_Flop] = {}
        Red_cache["Pre_Flop %s" %Round_Pre_Flop] = {}
        Bet_cache["Pre_Flop %s" %Round_Pre_Flop] = {}
        Last_Cards_cache = {}
        Last_White_cache = {}
        Last_Red_cache = {}
        Last_Bet_cache = {}
        
        for Seat in range(1,6) :
            Cards_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = Cards(Seat)
            White_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = White(Seat)
            Red_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = Red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]
            Last_White_cache[Seat] = White_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]
            Last_Red_cache[Seat] = Red_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]

            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = Easy_OCR_Bet_Number(Seat)
                if Last_White_cache[Seat] == True : 
                    shout(paint.light_green.bold("Seat%s Call: $%s" %(Seat,Bet_cache["Pre_Flop %s" %Round_Pre_Flop][Seat])))
                elif Last_Red_cache[Seat] == True :
                    shout(paint.light_green.bold("Seat%s Raise: $%s" %(Seat,Bet_cache["Pre_Flop %s" %Round_Pre_Flop][Seat])))
            else :
                Bet_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = None
            Last_Bet_cache[Seat] = Bet_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]
            
    if Flop1_Deside == True and Turn1_Deside == False :
        Cards_cache["Flop %s" %Round_Flop] = {}
        White_cache["Flop %s" %Round_Flop] = {}
        Red_cache["Flop %s" %Round_Flop] = {}
        Bet_cache["Flop %s" %Round_Flop] = {}
        Last_Cards_cache = {}
        Last_White_cache = {}
        Last_Red_cache = {}
        Last_Bet_cache = {}

        for Seat in range(1,6) :
            Cards_cache["Flop %s" %Round_Flop][Seat] = Cards(Seat)
            White_cache["Flop %s" %Round_Flop][Seat] = White(Seat)
            Red_cache["Flop %s" %Round_Flop][Seat] = Red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["Flop %s" %Round_Flop][Seat]
            Last_White_cache[Seat] = White_cache["Flop %s" %Round_Flop][Seat]
            Last_Red_cache[Seat] = Red_cache["Flop %s" %Round_Flop][Seat]

            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["Flop %s" %Round_Flop][Seat] = Easy_OCR_Bet_Number(Seat)
                if Last_White_cache[Seat] == True : 
                    shout(paint.light_green.bold("Seat%s Call: $%s" %(Seat,Bet_cache["Flop %s" %Round_Flop][Seat])))
                elif Last_Red_cache[Seat] == True :
                    shout(paint.light_green.bold("Seat%s Raise: $%s" %(Seat,Bet_cache["Flop %s" %Round_Flop][Seat])))
            else :
                Bet_cache["Flop %s" %Round_Flop][Seat] = None
            Last_Bet_cache[Seat] = Bet_cache["Flop %s" %Round_Flop][Seat]

    if Turn1_Deside == True and River1_Deside == False :
        Cards_cache["Turn %s" %Round_Turn] = {}
        White_cache["Turn %s" %Round_Turn] = {}
        Red_cache["Turn %s" %Round_Turn] = {}
        Bet_cache["Turn %s" %Round_Turn] = {}
        Last_Cards_cache = {}
        Last_White_cache = {}
        Last_Red_cache = {}
        Last_Bet_cache = {}

        for Seat in range(1,6) :
            Cards_cache["Turn %s" %Round_Turn][Seat] = Cards(Seat)
            White_cache["Turn %s" %Round_Turn][Seat] = White(Seat)
            Red_cache["Turn %s" %Round_Turn][Seat] = Red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["Turn %s" %Round_Turn][Seat]
            Last_White_cache[Seat] = White_cache["Turn %s" %Round_Turn][Seat]
            Last_Red_cache[Seat] = Red_cache["Turn %s" %Round_Turn][Seat]
            
            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["Turn %s" %Round_Turn][Seat] = Easy_OCR_Bet_Number(Seat)
                if Last_White_cache[Seat] == True : 
                    shout(paint.light_green.bold("Seat%s Call: $%s" %(Seat,Bet_cache["Turn %s" %Round_Turn][Seat])))
                elif Last_Red_cache[Seat] == True :
                    shout(paint.light_green.bold("Seat%s Raise: $%s" %(Seat,Bet_cache["Turn %s" %Round_Turn][Seat])))
            else :
                Bet_cache["Turn %s" %Round_Turn][Seat] = None
            Last_Bet_cache[Seat] = Bet_cache["Turn %s" %Round_Turn][Seat]

    if River1_Deside == True :
        Cards_cache["River %s" %Round_River] = {}
        White_cache["River %s" %Round_River] = {}
        Red_cache["River %s" %Round_River] = {}
        Bet_cache["River %s" %Round_River] = {}
        Last_Cards_cache = {}
        Last_White_cache = {}
        Last_Red_cache = {}
        Last_Bet_cache = {}

        for Seat in range(1,6) :
            Cards_cache["River %s" %Round_River][Seat] = Cards(Seat)
            White_cache["River %s" %Round_River][Seat] = White(Seat)
            Red_cache["River %s" %Round_River][Seat] = Red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["River %s" %Round_River][Seat]
            Last_White_cache[Seat] = White_cache["River %s" %Round_River][Seat]
            Last_Red_cache[Seat] = Red_cache["River %s" %Round_River][Seat]

            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["River %s" %Round_River][Seat] = Easy_OCR_Bet_Number(Seat)
                if Last_White_cache[Seat] == True : 
                    shout(paint.light_green.bold("Seat%s Call: $%s" %(Seat,Bet_cache["River %s" %Round_River][Seat])))
                elif Last_Red_cache[Seat] == True :
                    shout(paint.light_green.bold("Seat%s Raise: $%s" %(Seat,Bet_cache["River %s" %Round_River][Seat])))
            else :
                Bet_cache["River %s" %Round_River][Seat] = None
            Last_Bet_cache[Seat] = Bet_cache["River %s" %Round_River][Seat]

    shout("shouting from Read_Bets(), Bet_cache is: %s"%Bet_cache) #(2018) delete this later. just for testing if rounds are started from 0, esp at preflop stage
    
### Read_Bets & dinctionaries & Reset var funcs Ended ***********************************************************************************************************************
            
def Play_sound() :
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside  , My_1th_Card , My_2th_Card

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        if hand1() :
            sound("Michel")
            shout(paint.light_cyan.bold("Playing Music: 'Michel'"))
        elif hand2() :
            sound("Alan Walker")
            shout(paint.light_cyan.bold("Playing Music: 'Alan Walker'"))
        elif hand3() :
            sound("Alan Walker")
            shout(paint.light_cyan.bold("Playing Music: 'Alan Walker'"))
        elif hand4() :
            sound("Pocket low pairs")
            shout(paint.light_cyan.bold("Playing Music: 'Pocket low pairs'"))
        elif hand5() :
            sound("Bob Marley")
            shout(paint.light_cyan.bold("Playing Music: 'Bob Marley'"))

def Pickle_Var() :
    """
    delete variables.p at the beginning to make sure all variables are new.
    By running main file if i have not assigned varibales from before, it will error. 
    By implementing globalization() I can delete all global lines from supporting and... funcitons. 
    But I keep them to see the varibales I've used for that functions. 
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    pickle.dump( [Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat], open( "variables.p", "wb" ) )

def Decide():
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    Pickle_Var()
    return Decide_File.decide()



# first line values: ----------------------
My_Profile_Name = "XXX"
if input("Is My Name: %s ?(Enter:yes/any keyword:no)"%My_Profile_Name) != "" :
    My_Profile_Name = input("Enter Profile Name: ")
My_Seat_Number = int( input("My Seat Number? ") )
Just_Seated = True # will be omitted (None,True,False)
Check_Mod = False
paint.enabled = True # for cmd use
BLIND = 100000000
Players_name_dic = {}
Players_bank_dic = {}
White_cache = {} ; Red_cache = {} ; Cards_cache = {} ; Bet_cache = {}
Lost_Connection_Time = {} 
# check later if reseting dictionaries in reset_table_info function works fine, do not repeat them here
# first line values Ended -----------------


getpo_for_starting()



while True :

    Pre_Flop1_Deside = False ; Flop1_Deside = False ; Turn1_Deside = False ; River1_Deside = False 

    if Just_Seated == True :

        shout(paint.on_green.bold("****** Running Just_Seated == True Section ******"))
        Reset_Check_Mod() #

        Reset_Table_Info() #

        if Win_Finish_Me( My_Seat_Number ) == False :
            My_Bank = OCR_My_Bank_Number( My_Seat_Number )
            if My_Bank != None :
                if My_Bank >= 15 * BLIND :
                    shout(paint.light_green.bold("My Bank is:%s" %My_Bank))
                elif My_Bank != 0 :
                    shout(paint.light_green.bold("My Bank is:%s" %My_Bank))
                    shout("Rebuying...")
                    pass # Later i'll build
        else :
            shout("My Bank can't be read")
            My_Bank = None
        
        Hand_End_Cheker1 = Hand_End_Cheker()
        while Hand_End_Cheker1 :
            Hand_End_Cheker1 = Hand_End_Cheker()

        if Light(My_Seat_Number) != True or ( Light(My_Seat_Number) == True and Gray_Sign_Seat(My_Seat_Number) == True ) :
            Read_Players_Info() #
        else :
            shout( paint.on_light_red.bold("Players Info is not Read") )

        time02 = 0 ; fo = 0 
        time1 = time.time()
        Cards1 = False
        shout(paint.light_magenta.bold("Looking for cards in Just_Seated == True Section..."))
        while Cards1 == False and time02 < 5 * 60 : #being alone time
            Cards1 = Cards( My_Seat_Number )
            time2 = time.time() - time1
            n60 = ( time2 - 120 ) // 60
            if not time2 < 2 * 60 and n60 >= fo :
                Vital_Signs("1")
                fo += 1
                time02 = time.time() - time1                

        if not time02 < 5 * 60 : #being alone time
            raise Exception("0.1.No one join, time to exit. Or Game is locked, force to restart(will be build in future), Just_Seated == None")

        if Cards1 == True :
            if Pre_Flop() == False or (Pre_Flop() == True and is_there_any_raiser() == True) :
                Check_Mod_On("this is Ok! Becuase i may start program from middle of the game")

            Just_Seated = False
            shout(paint.light_magenta.bold("Cards are founded"))
            shout (paint.on_green.bold("****** First hand Started ******"))
    
    elif Just_Seated == None :
        raise Exception("5.This can not happen IN FUTURE becuase main menu automation is built\
                        ( vital_signs --> Sit_In --> table is full --> exit -->\
                        Just_Seated = None --> main menu --> Just_Seated = True )")


#-------    

    if Hand_End_Cheker1 == False and Pre_Flop() == False and Just_Seated == False and Check_Mod != True :
        Vital_Signs("2")
        Check_Mod_On("2")
        Screenshot_Error('6.Pre_Flop() == False')
    elif Hand_End_Cheker1 == False and Just_Seated == False and Check_Mod != True :
        Pre_Flop1 = True
        Pre_Flop1_Deside = True

    if Hand_End_Cheker1 == False and Cards( My_Seat_Number ) == True and Just_Seated == False :  
        Read_My_Cards() #
        Play_sound() #


    Light1 = False
    Gray1 = True ; fo = 0 
    time1 = time.time()
    shout(paint.light_magenta.bold("Looking for light...")) 
    while Hand_End_Cheker1 == False and (Light1 == False or Gray1 == True) and Flop1_Deside == False and Just_Seated == False and time.time() - time1 < 5 * 60 :
        if I_am_back_Button() :
            Vital_Signs("2.5 I am back Button is True")
        Hand_End_Cheker1 = Hand_End_Cheker()
        Light1 = Light( My_Seat_Number )
        Gray1 = Gray_Sign_Seat( My_Seat_Number )
        Flop1_Deside = Flop()
        n20 = (time.time() - time1 - 60 ) // 20
        if time.time() - time1 > 1 * 60 and n20 >= fo :
            Vital_Signs("3")
            fo += 1
            
    if not time.time() - time1 < 5 * 60 :
        raise Exception("5.1.Game is locked, force to restart, Just_Seated == None")

    if Flop1_Deside == True :
        Check_Mod_On("1.5")
        Screenshot_Error("6.5 Pre Flop is Jumped, game must lagged")
        
         
    Round_Pre_Flop = 0 #(2018) shouldn't it be -1 ?! test it by printing for example Cards_cache dic which prints rounds too
    if Light( My_Seat_Number ) == True and Gray1 == False and Hand_End_Cheker() == False and Flop1_Deside == False and Just_Seated == False :
        Round_Pre_Flop += 1
        shout(paint.light_magenta.bold("light is founded"))
        Read_Bets() #
        Decide() # preflop
    elif Hand_End_Cheker() == False and Flop1_Deside == False and Just_Seated == False :
        Vital_Signs("4 Entering This section is not possible")
        Screenshot_Error("6.6 Entering This section is not possible")
        #(2018) shouldn't Round_Pre_Flop += 1 line be here too ?!
        Read_Bets() #
        Decide() # preflop



# PreFlop: -------

        
    if Just_Seated == False :

        shout("Running PreFlop Section")
        time01 = time.time()
        time02 = time.time() - time01
        
        while Hand_End_Cheker1 == False and Flop1_Deside == False and time02 < 5 * 60 and Just_Seated == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; Flop1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and Light1 == False and Flop1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                if I_am_back_Button() :
                    Vital_Signs("4.5 I am back Button is True")
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                Flop1 = Flop()
                time2 = time.time() - time1
                    
            if not time2 < 1 * 60 :
                Vital_Signs("5")

            if Hand_End_Cheker1 == False :

                if Light1 == True and Flop1 == False :
                    Round_Pre_Flop += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        Read_Bets() #
                        Decide() # preflop
                    elif Check_Mod != True :
                        Check_Mod_On("3")
                        Screenshot_Error("7.Red should be True here, check later why this happens")
                        Read_Bets() #
                        Decide() # preflop
                        
                if Flop1 == True :
                    Flop1_Deside = True
                    shout(paint.light_magenta.bold("Reading Flop Cards..."))
                    Read_Flop_Cards() #

        if not time02 < 5 * 60 :
            raise Exception("8.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            Vital_Signs("6")


# Flop: -------


    if Just_Seated == False :

        shout("Running Flop Section")
        time01 = time.time()
        time02 = time.time() - time01
        Round_Flop = -1
        while Hand_End_Cheker1 == False and Turn1_Deside == False and time02 < 5 * 60 and Just_Seated == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; Turn1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and Light1 == False and Turn1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                if I_am_back_Button() :
                    Vital_Signs("6.5 I am back Button is True")
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                Turn1 = Turn()
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                Vital_Signs("7")
                
            if Hand_End_Cheker1 == False :

                if Light1 == True and Turn1 == False :
                    Round_Flop += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        Read_Bets() #
                        Decide() # Flop
                    elif Round_Flop > 0 :
                        Check_Mod_On("4")
                        Screenshot_Error("9.Red should be True here")
                        Read_Bets() #
                        Decide() # Flop
                    else :
                        Read_Bets() #
                        Decide() # Flop
                        
                if Turn1 == True :            
                    Turn1_Deside = True
                    shout(paint.light_magenta.bold("Reading Turn Card"))
                    Read_Turn_Cards() #        
            
        if not time02 < 5 * 60 :
            raise Exception("10.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            Vital_Signs("8")    



# Turn: -------

    
    if Just_Seated == False :

        shout("Running Turn Section")
        time01 = time.time()
        time02 = time.time() - time01
        Round_Turn = -1
        while Hand_End_Cheker1 == False and River1_Deside == False and time02 < 5 * 60 and Just_Seated == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; River1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and Light1 == False and River1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                if I_am_back_Button() :
                    Vital_Signs("8.5 I am back Button is True")
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                River1 = River()
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                Vital_Signs("9")
                
            if Hand_End_Cheker1 == False :

                if Light1 == True and River1 == False :
                    Round_Turn += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        Read_Bets() #
                        Decide() # Turn
                    elif Round_Turn > 0 :
                        Check_Mod_On("5")
                        Screenshot_Error("11.Red should be True here")
                        Read_Bets() #
                        Decide() # Turn
                    else :
                        Read_Bets() #
                        Decide() # Turn
                        
                if River1 == True :            
                    River1_Deside = True
                    shout(paint.light_magenta.bold("Reading River Card"))
                    Read_River_Cards() #        
            
        if not time02 < 5 * 60 :
            raise Exception("12.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            Vital_Signs("10")            
            

# River: -------


    if Just_Seated == False :

        shout("Running River Section")
        time01 = time.time()
        time02 = time.time() - time01
        Round_River = -1
        while Hand_End_Cheker1 == False and time02 < 5 * 60 and Just_Seated == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and Light1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                if I_am_back_Button() :
                    Vital_Signs("10.5 I am back Button is True")
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                Vital_Signs("11")
                
            if Hand_End_Cheker1 == False :

                if Light1 == True and River() == True :
                    Round_River += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        Read_Bets() #
                        Decide() # River
                    elif Round_River > 0 :
                        Check_Mod_On("6")
                        Screenshot_Error("13.Red should be True here")
                        Read_Bets() #
                        Decide() # River
                    else :
                        Read_Bets() #
                        Decide() # River


                               
            
        if not time02 < 5 * 60 :
            raise Exception("14.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            Vital_Signs("12")            
            


#-------
            
    if Hand_End_Cheker1 == True and Just_Seated == True :

        Declare_The_Winners()
        shout (paint.on_green.bold("-------- Hand Ended --------"))

    if Hand_End_Cheker1 == True and Just_Seated == False :

        Declare_The_Winners()
        shout (paint.on_green.bold("-------- Hand Ended --------"))
        
        Reset_Check_Mod() #

        Reset_Table_Info() #

        if Win_Finish_Me( My_Seat_Number ) == False : 
            My_Bank = OCR_My_Bank_Number( My_Seat_Number )
            if My_Bank != None :
                if My_Bank >= 15 * BLIND : 
                    shout(paint.light_green.bold("My Bank is:%s" %My_Bank))
                elif My_Bank != 0 :
                    shout(paint.light_green.bold("My Bank is:%s" %My_Bank))
                    shout("Rebuying...")
                    pass # Later i'll build
        else :
            My_Bank = None
        
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Hand_End_Cheker1 == True and time02 < 1.5 * 60 :
            Hand_End_Cheker1 = Hand_End_Cheker()
            time2 = time.time() - time1
            if not time2 < 2 * 60 :
                if fo == 0 :
                    Vital_Signs("13")
                    fo = 1
                time02 = time.time() - time1                

        if not time02 < 1.5 * 60 :
            raise Exception("15.Game is locked, force to restart, Just_Seated == None")
            


    if Hand_End_Cheker1 == False and Just_Seated == False :

        if Light(My_Seat_Number) != True or ( Light(My_Seat_Number) == True and Gray_Sign_Seat(My_Seat_Number) == True ) :
            Read_Players_Info() #
        else :
            shout( paint.on_light_red.bold("Players Info is not Read") )

        Coins_Appeared = False
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Coins_Appeared == False and time02 < 5 * 60 : #being alone time
            Coins_Appeared = Coins_Founded()
            time2 = time.time() - time1
            if not time2 < 8 and fo == 0 :
                getpo()
                fo = 1
            if not time2 < 2 * 60 :
                if fo == 1 :
                    Vital_Signs("14")
                    fo = 2
                time02 = time.time() - time1                

        if not time02 < 5 * 60 : #being alone time
            raise Exception("16.No one join, time to exit. Or Game is locked, force to restart, Just_Seated == None")

        elif Just_Seated == False :
            shout (paint.on_green.bold("-------- New Hand Started --------"))
            shout ("Coins are Founded")
            Determine_Small_Blind_Seat()
            Determine_Big_Blind_Seat()
            Determine_Dealer_Seat()       


                    
            time02 = 0 ; fo = 0 
            time1 = time.time()
            Cards1 = False
            shout(paint.light_magenta.bold("Looking for cards..."))
            while Hand_End_Cheker1 == False and Cards1 == False and Just_Seated == False and time02 < 1.5 * 60 :
                if I_am_back_Button() :
                    Vital_Signs("14.5 I am back Button is True")
                Hand_End_Cheker1 = Hand_End_Cheker()
                Cards1 = Cards( My_Seat_Number )
                time2 = time.time() - time1
                if not time2 < 2 * 60 :
                    if fo == 0 :
                        Vital_Signs("15")
                        fo = 1
                    time02 = time.time() - time1                

            if not time02 < 1.5 * 60 :
                raise Exception("17.Game is locked, force to restart, Just_Seated == None")

            if Cards1 == True :
                shout(paint.light_magenta.bold("Cards are founded"))

            elif not time02 < 1.5 * 60 :
                Vital_Signs("15")

            if Hand_End_Cheker1 == True and Cards1 == False :
                Vital_Signs("16. I am maybe out")
            



