import pyautogui, time, os, pygame , win32gui , win32con 
from PIL import Image
from datetime import datetime
from pyautogui import pixelMatchesColor
from pytesseract import image_to_string
#from __future__ import print_function
from painter import paint



#logging.basicConfig(level=shout, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.basicConfig(level=shout, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#logging.disable(shout) # uncomment to block debug log messages

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)


text_file_name = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
def shout(String) :
    t = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
    t = t[:-4]
    print("%s: %s" %(t,String))
    
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

# FUNCTIONS_Decide_and_Pixel-Maching ---------------------------------------------------------------------------------------------

def Turn_Finder(Seat_Starter , Xth) : #Return The seat number;for instance;(4,1)returns seat 4!
    Answer = (Seat_Starter - 1 + Xth ) % 5
    if Answer == 0 :
        return 5
    else :
        return Answer
            

def Coins_Founded():
    Small_seat_1= pixelMatchesColor( po[0]+369, po[1]+329, (18,111,213) ) #Small_seat_1
    Small_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (21,124,218) ) #Small_seat_2
    Small_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (16,105,211) ) #Small_seat_3
    Small_seat_4= pixelMatchesColor( po[0]-173, po[1]+212, (22,112,212) ) #Small_seat_4
    Small_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (22,112,212) ) #Small_seat_5
    Big_seat_1= pixelMatchesColor( po[0]+367, po[1]+329, (180,180,180) ) #Big_seat_1
    Big_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (200,200,200) ) #Big_seat_2
    Big_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (185,185,185) ) #Big_seat_3
    Big_seat_4= pixelMatchesColor( po[0]-174, po[1]+212, (185,185,185) ) #Big_seat_4
    Big_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (185,185,185) ) #Big_seat_5
    Dealer_seat_1= pixelMatchesColor( po[0]+397, po[1]+330, (255,155,0) ) #Dealer_seat_1
    Dealer_seat_2= pixelMatchesColor( po[0]+144, po[1]+333, (254,193,0) ) #Dealer_seat_2
    Dealer_seat_3= pixelMatchesColor( po[0]-116, po[1]+330, (255,154,0) ) #Dealer_seat_3
    Dealer_seat_4= pixelMatchesColor( po[0]-202, po[1]+212, (255,160,0) ) #Dealer_seat_4
    Dealer_seat_5= pixelMatchesColor( po[0]+429, po[1]+212, (255,160,0) ) #Dealer_seat_5    
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


def White(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+316, po[1]+312, (255,255,255), tolerance=10 ) #White_Dollar_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+97, po[1]+314, (255,255,255), tolerance=10 ) #White_Dollar_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-120, po[1]+312, (255,255,255), tolerance=10 ) #White_Dollar_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-125, po[1]+225, (255,255,255), tolerance=10 ) #White_Dollar_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+320, po[1]+225, (255,255,255), tolerance=10 ) #White_Dollar_seat_5

def Red(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+316, po[1]+312, (255,1,1), tolerance=10 ) #Red_Dollar_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+97, po[1]+314, (255,1,1), tolerance=10 ) #Red_Dollar_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-120, po[1]+312, (255,1,1), tolerance=10 ) #Red_Dollar_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-125, po[1]+225, (255,1,1), tolerance=10 ) #Red_Dollar_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+320, po[1]+225, (255,1,1), tolerance=10 ) #Red_Dollar_seat_5

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

def Light(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+346, po[1]+328, (34,41,48) ) #Light_Turn_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+96, po[1]+330, (47,59,69) ) #Light_Turn_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-116, po[1]+328, (34,41,48) ) #Light_Turn_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-161, po[1]+219, (33,41,47) ) #Light_Turn_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+383, po[1]+217, (31,40,45) ) #Light_Turn_seat_5


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
    
    Small_seat_1= pixelMatchesColor( po[0]+369, po[1]+329, (18,111,213) ) #Small_seat_1
    Small_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (21,124,218) ) #Small_seat_2
    Small_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (16,105,211) ) #Small_seat_3
    Small_seat_4= pixelMatchesColor( po[0]-173, po[1]+212, (22,112,212) ) #Small_seat_4
    Small_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (22,112,212) ) #Small_seat_5

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
    
    Big_seat_1= pixelMatchesColor( po[0]+367, po[1]+329, (180,180,180) ) #Big_seat_1
    Big_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (200,200,200) ) #Big_seat_2
    Big_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (185,185,185) ) #Big_seat_3
    Big_seat_4= pixelMatchesColor( po[0]-174, po[1]+212, (185,185,185) ) #Big_seat_4
    Big_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (185,185,185) ) #Big_seat_5

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
    
    Dealer_seat_1= pixelMatchesColor( po[0]+397, po[1]+330, (255,155,0) ) #Dealer_seat_1
    Dealer_seat_2= pixelMatchesColor( po[0]+144, po[1]+333, (254,193,0) ) #Dealer_seat_2
    Dealer_seat_3= pixelMatchesColor( po[0]-116, po[1]+330, (255,154,0) ) #Dealer_seat_3
    Dealer_seat_4= pixelMatchesColor( po[0]-202, po[1]+212, (255,160,0) ) #Dealer_seat_4
    Dealer_seat_5= pixelMatchesColor( po[0]+429, po[1]+212, (255,160,0) ) #Dealer_seat_5 

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


def my_turn_from_coins() :
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat , Check_Mod

    Pre_Flop1 = Pre_Flop()
    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( Big_Blind_Seat + 1 , i )
        elif Pre_Flop1 == False and Small_Blind_Seat != Dealer_Seat :
            Seat = Turn_Finder( Small_Blind_Seat , i )
        elif Pre_Flop1 == False and Small_Blind_Seat == Dealer_Seat :
            Seat = Turn_Finder( Big_Blind_Seat , i )
            
        if Seat != My_Seat_Number :
            if Cards(Seat) == True :
                Total += 1
        elif Seat == My_Seat_Number :
            if Cards(Seat) != True :
                Check_Mod_On("my_turn_from_coins()")
                Screenshot_Error("my_turn_from_coins() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Check_Mod_On("my_turn_from_coins()")
        Screenshot_Error("my_turn_from_coins() (This case can not happen) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )



def is_there_any_raiser():
    """ Except me """
    global My_Seat_Number
    
    for Seat in range(1,6):
        if Seat == My_Seat_Number :
            continue
        elif Red(Seat) :
            return True
    return False
           
def my_turn_from_last_raiser() :
    """ is_there_any_raiser() should be True, then we run this Function,
    otherwise Last_Red_Seat var can error not assigned """
    global My_Seat_Number , Check_Mod

    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Red(Seat) :
            Last_Red_Seat = Seat

    Total = 0
    for i in range(1,6):
        
        Seat = Turn_Finder( Last_Red_Seat , i )

        if Seat != My_Seat_Number :
            if Cards(Seat) == True :
                Total += 1
        elif Seat == My_Seat_Number :
            if Cards(Seat) != True :
                Check_Mod_On("my_turn_from_last_raiser()")
                Screenshot_Error("my_turn_from_last_raiser() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Check_Mod_On("my_turn_from_last_raiser()")
        Screenshot_Error("my_turn_from_last_raiser() (This case can not happen1) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )



def next_playing_player_seat( My_Seat_Number , forward_backward_number ) :
    """ forward_backward_number can be + or -
    if abs(forward_backward_number) > (4 or more than playing players) : return None """
    global Check_Mod

    if forward_backward_number > 0 :
        sign = +1
    elif forward_backward_number < 0 :
        sign = -1
    else :
        return None
    
    p = 0
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , sign * i )
        if Cards(Seat) == True :
            p += (sign * 1)
        if p == forward_backward_number :
            return Seat
    Check_Mod_On("next_playing_player_seat")
    Screenshot_Error("next_playing_player is None")


def last_raisers_list_seat( My_Seat_Number ) :
    """ Except me. My_Seat_Number = 1, raisers seat: 3 , 5. returns : [5,3]. if no raisers: [] """

    last_raisers_list = []
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Red(Seat) :
            last_raisers_list.append(Seat)

    last_raisers_list.reverse()
    return last_raisers_list

def number_of_raisers( My_Seat_Number ) :
    """ Except me """
    return len(last_raisers_list( My_Seat_Number ))


# 2017 cache :------------------------------

def my_turn_from_coins_cache() :
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat,\
           Last_Cards_cache , Check_Mod

    Pre_Flop1 = Pre_Flop()
    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( Big_Blind_Seat + 1 , i )
        elif Pre_Flop1 == False and Small_Blind_Seat != Dealer_Seat :
            Seat = Turn_Finder( Small_Blind_Seat , i )
        elif Pre_Flop1 == False and Small_Blind_Seat == Dealer_Seat :
            Seat = Turn_Finder( Big_Blind_Seat , i )
            
        if Seat != My_Seat_Number :
            if Last_Cards_cache[Seat] == True :
                Total += 1
        elif Seat == My_Seat_Number :
            if Last_Cards_cache[Seat] != True :
                Check_Mod_On("my_turn_from_coins_cache()")
                Screenshot_Error("my_turn_from_coins_cache() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Check_Mod_On("my_turn_from_coins_cache()")
        Screenshot_Error("my_turn_from_coins_cache() (This case can not happen) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )

def Players_turn_from_coins_cache( Player_Seat ) : # just for below function usage
    global Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat,\
           Last_Cards_cache , Check_Mod

    Pre_Flop1 = Pre_Flop()
    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( Big_Blind_Seat + 1 , i )
        elif Pre_Flop1 == False and Small_Blind_Seat != Dealer_Seat :
            Seat = Turn_Finder( Small_Blind_Seat , i )
        elif Pre_Flop1 == False and Small_Blind_Seat == Dealer_Seat :
            Seat = Turn_Finder( Big_Blind_Seat , i )
            
        if Seat != Player_Seat :
            if Last_Cards_cache[Seat] == True :
                Total += 1
        elif Seat == Player_Seat :
            if Last_Cards_cache[Seat] != True :
                Check_Mod_On("Players_turn_from_me_coins_cache()")
                Screenshot_Error("Players_turn_from_me_coins_cache() (This case can not happen) Player Cards (seat %s) is not visible" %Player_Seat)
            else :
                Total += 1
                Player_position = Total
    if Total < 2 :
        Check_Mod_On("Players_turn_from_me_coins_cache()")
        Screenshot_Error("Players_turn_from_me_coins_cache() (This case can not happen) Total lower than 2 my seat %s" %Player_Seat)
    else :
        return ( Player_position , Total )

def Players_turn_from_me_by_coins_cache( Player_Seat ) :
    "if before me :-2, if after me: +4(+4 is max)"
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat,\
           Last_Cards_cache , Check_Mod

    Answer = Players_turn_from_coins_cache( Player_Seat )[0] - my_turn_from_coins_cache()[0]
    return Answer
    
def is_there_any_raiser_cache():
    """ Except me """
    global My_Seat_Number , Last_Red_cache
    
    for Seat in range(1,6):
        if Seat == My_Seat_Number :
            continue
        elif Last_Red_cache[Seat] :
            return True
    return False
           
def my_turn_from_last_raiser_cache() :
    """ is_there_any_raiser_cache() should be True, then we run this Function,
    otherwise Last_Red_Seat var can error not assigned """
    global My_Seat_Number , Last_Red_cache , Last_Cards_cache , Check_Mod

    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Last_Red_cache[Seat] :
            Last_Red_Seat = Seat

    Total = 0
    for i in range(1,6):
        
        Seat = Turn_Finder( Last_Red_Seat , i )

        if Seat != My_Seat_Number :
            if Last_Cards_cache[Seat] == True :
                Total += 1
        elif Seat == My_Seat_Number :
            if Last_Cards_cache[Seat] != True :
                Check_Mod_On("my_turn_from_last_raiser_cache()")
                Screenshot_Error("my_turn_from_last_raiser_cache() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Check_Mod_On("my_turn_from_last_raiser_cache()")
        Screenshot_Error("my_turn_from_last_raiser_cache() (This case can not happen1) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )



def next_playing_player_seat_cache( My_Seat_Number , forward_backward_number ) :
    """ forward_backward_number can be + or -
    if abs(forward_backward_number) > (4 or more than playing players) : return None """
    global Last_Cards_cache , Check_Mod

    if forward_backward_number > 0 :
        sign = +1
    elif forward_backward_number < 0 :
        sign = -1
    else :
        return None
    
    p = 0
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , sign * i )
        if Last_Cards_cache[Seat] == True :
            p += (sign * 1)
        if p == forward_backward_number :
            return Seat
    Check_Mod_On("next_playing_player_seat_cache()")
    Screenshot_Error("next_playing_player at cache is None")


def last_raisers_list_seat_cache( My_Seat_Number ) :
    """ Except me. My_Seat_Number = 1, raisers seat: 3 , 5. returns : [5,3]. if no raisers: [] """
    global Last_Red_cache

    last_raisers_list = []
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Last_Red_cache[Seat] :
            last_raisers_list.append(Seat)

    last_raisers_list.reverse()
    return last_raisers_list

def number_of_raisers_cache( My_Seat_Number ) :
    """ Except me """
    global Last_Red_cache
    
    return len(last_raisers_list_cache( My_Seat_Number ))


# FUNCTIONS_Decide_and_Pixel-Maching Ended ---------------------------------------------------------------------------------------











# FUNCTIONS_hand -----------------------------------------------------------------------------------------------------------------


def s(Card) :
    if Card in ('A c','2 c','3 c','4 c','5 c','6 c','7 c','8 c','9 c','10 c','J c','Q c','K c') :
        return "c"
    if Card in ('A d','2 d','3 d','4 d','5 d','6 d','7 d','8 d','9 d','10 d','J d','Q d','K d') :
        return "d"
    if Card in ('A h','2 h','3 h','4 h','5 h','6 h','7 h','8 h','9 h','10 h','J h','Q h','K h') :
        return "h"
    if Card in ('A s','2 s','3 s','4 s','5 s','6 s','7 s','8 s','9 s','10 s','J s','Q s','K s') :
        return "s"

def n(Card) :
    if Card in ('2 c','2 d','2 h','2 s',2):
        return 2
    if Card in ('3 c','3 d','3 h','3 s',3):
        return 3
    if Card in ('4 c','4 d','4 h','4 s',4):
        return 4
    if Card in ('5 c','5 d','5 h','5 s',5):
        return 5
    if Card in ('6 c','6 d','6 h','6 s',6):
        return 6
    if Card in ('7 c','7 d','7 h','7 s',7):
        return 7
    if Card in ('8 c','8 d','8 h','8 s',8):
        return 8
    if Card in ('9 c','9 d','9 h','9 s',9):
        return 9
    if Card in ('10 c','10 d','10 h','10 s',10):
        return 10
    if Card in ('J c','J d','J h','J s',11):
        return 11
    if Card in ('Q c','Q d','Q h','Q s',12):
        return 12
    if Card in ('K c','K d','K h','K s',13):
        return 13
    if Card in ('A c','A d','A h','A s',14):
        return 14
#----

def hand1() :
    """ AA,KK """
    global  My_1th_Card , My_2th_Card 
    if  n( My_1th_Card ) == n( My_2th_Card )  and 13 <= n( My_1th_Card ) <= 14 :
        shout("hand1 is True")
        return True
    else :
        return None

def hand2() :
    """ QQ,JJ """
    global  My_1th_Card , My_2th_Card 
    if  n( My_1th_Card ) == n( My_2th_Card )  and 11 <= n( My_1th_Card ) <= 12 :
        shout("hand2 is True")
        return True
    else :
        return None

def hand3() :
    """ 1010,99 """
    global  My_1th_Card , My_2th_Card 
    if  n( My_1th_Card ) == n( My_2th_Card )  and 9 <= n( My_1th_Card ) <= 10 :
        shout("hand3 is True")
        return True
    else :
        return None

def hand4() :
    """ 88,77,...,22 """
    global  My_1th_Card , My_2th_Card 
    if  n( My_1th_Card ) == n( My_2th_Card )  and 2 <= n( My_1th_Card ) <= 8 :
        shout("hand4 is True")
        return True
    else :
        return None

def hand5() :
    """ A10,...,KQ  3 Blind raise """
    global  My_1th_Card , My_2th_Card 
    if  n( My_1th_Card ) != n( My_2th_Card ) :
        if ( 12 <= n( My_1th_Card ) <= 13 and 12 <= n( My_2th_Card ) <= 13 ) \
        or ( 14 in [ n( My_1th_Card ) , n( My_2th_Card ) ] and n( My_1th_Card ) >= 10 and n( My_2th_Card ) >= 10 ) :
            shout("hand5 is True")
            return True
    else :
        return None

def hand6() :
    """ KJ,QJ,,...,A2,...,(108,98 rang),109  1 Blind call """
    global  My_1th_Card , My_2th_Card 
    if  n( My_1th_Card ) != n( My_2th_Card ) :
        if hand5( My_1th_Card , My_2th_Card ) != True :
            if 14 in [ n( My_1th_Card ) , n( My_2th_Card ) ] \
            or ( n( My_1th_Card ) >= 8 and n( My_2th_Card ) >= 8 and s( My_1th_Card ) == s( My_2th_Card ) ) \
            or ( n( My_1th_Card ) >= 9 and n( My_2th_Card ) >= 9 ) :
                shout("hand6 is True")
                return True
    else :
        return None


def hand7() :
    """ 72,73,...,96,107 (gheir rang)  Fold small blind position (otherwise Small always call Blind) """
    global  My_1th_Card , My_2th_Card 
    if not( hand1( My_1th_Card , My_2th_Card ) or hand2( My_1th_Card , My_2th_Card ) or hand3( My_1th_Card , My_2th_Card ) or \
            hand4( My_1th_Card , My_2th_Card ) or hand5( My_1th_Card , My_2th_Card ) or hand6( My_1th_Card , My_2th_Card ) \
            or s( My_1th_Card ) == s( My_2th_Card ) ) :
        for i in range(2,8) :
            if i in ( n( My_1th_Card ) , n( My_2th_Card ) )  and abs( n( My_2th_Card ) - n( My_1th_Card ) ) >= 3 \
            and n( My_1th_Card ) <= 10 and n( My_2th_Card ) <= 10 :
                shout("hand7 is True")
                return True
    else :
        return None


#--------------------------------------------


def hand8() :
    """ AK,...,1010,...22,...,(65 rang) Blind position call 2 blind raise, otherwise fold that """
    global  My_1th_Card , My_2th_Card 
    if not( hand1( My_1th_Card , My_2th_Card ) or hand2( My_1th_Card , My_2th_Card ) ) :
        if hand3( My_1th_Card , My_2th_Card ) or hand4( My_1th_Card , My_2th_Card ) \
        or hand5( My_1th_Card , My_2th_Card ) or hand6( My_1th_Card , My_2th_Card ) \
        or ( n( My_1th_Card ) >= 5 and n( My_2th_Card ) >= 5 and \
             s( My_1th_Card ) == s( My_2th_Card ) and abs( n( My_2th_Card ) - n( My_1th_Card ) ) == 1 ) :
            shout("hand8 is True")
            return True
    else :
        return None

def hand9() :
    """ AK,...,1010,...,(98 rang) Small position call 2 blind raise, otherwise fold that """
    global  My_1th_Card , My_2th_Card 
    if not( hand1( My_1th_Card , My_2th_Card ) or hand2( My_1th_Card , My_2th_Card ) ) :
        if hand3( My_1th_Card , My_2th_Card ) or hand4( My_1th_Card , My_2th_Card ) \
        or hand5( My_1th_Card , My_2th_Card ) or hand6( My_1th_Card , My_2th_Card ) :
            shout("hand9 is True")
            return True
    else :
        return None    





# FUNCTIONS_hand Ended -----------------------------------------------------------------------------------------------------------



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

def Bet_Button():
    x1 = pixelMatchesColor( po[0]+461, po[1]+576, (24,115,0) ) #Bet_up
    x2 = pixelMatchesColor( po[0]+463, po[1]+579, (242,242,242) ) #Bet_down
    x3 = pixelMatchesColor( po[0]+461, po[1]+576, (28,135,0) ) #Bet_up_Light
    x4 = pixelMatchesColor( po[0]+463, po[1]+579, (242,242,242) ) #Bet_down_Light
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

def Raise_Button():
    x1 = pixelMatchesColor( po[0]+461, po[1]+576, (25,117,0) ) #Raise_up
    x2 = pixelMatchesColor( po[0]+448, po[1]+579, (239,239,239) ) #Raise_down
    x3 = pixelMatchesColor( po[0]+461, po[1]+576, (29,137,0) ) #Raise_up_Light
    x4 = pixelMatchesColor( po[0]+448, po[1]+579, (239,239,239) ) #Raise_down_Light
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

def Menu_Button():
    x1 = pixelMatchesColor( po[0]-399, po[1]-66, (38,44,47) ) #Menu_Button
    x2 = pixelMatchesColor( po[0]-399, po[1]-66, (78,83,97) ) #Menu_Button_Light
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


def Raise( Blinds ):
    """ if Blinds == 2 (or less): won't click on plus button """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    Number_of_Clicks_on_Plus_Button( Blinds - 2 )
    return  Click_on_Raise_Button()

def bet( Blinds ):
    """ if Blinds == 1 (or less): won't click on plus button """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    Number_of_Clicks_on_Plus_Button( Blinds - 1 )
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

def Read_Flop_Cards():
    global Card_1th , Card_2th , Card_3th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    time0 = time.time()
    for x in Cards_names :
        i= pyautogui.locateOnScreen(imPath('%s_1th Card on Table.png' %x),  region=(po[0]-38, po[1]+215, 20, 40) )
        if i != None :
            shout(paint.green.bold("1th card is: %s" %x))
            Card_1th = x
            break
    if i == None :
        Vital_Signs("Read_Flop_Cards():Card_1th")
        for x in Cards_names :
            i= pyautogui.locateOnScreen(imPath('%s_1th Card on Table.png' %x),  region=(po[0]-38, po[1]+215, 20, 40) )
            if i != None :
                shout(paint.green.bold("1th card is: %s" %x))
                Card_1th = x
                break
        time1 = time.time() - time0
        if (i == None or not Flop() or Turn() or time1 > 20 ) :
            if i == None :
                Screenshot_Error("Flop 1th card not founded!") #Type_of_Error in string
            Check_Mod_On("Read_Flop_Cards()1th")

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_2th Card on Table.png' %x),  region=(po[0]+25, po[1]+215, 20, 40) )
        if i != None :
            shout(paint.green.bold("2th card is: %s" %x))
            Card_2th = x
            break
    if i == None :
        Vital_Signs("Read_Flop_Cards():Card_2th")
        for x in Cards_names :
            i= pyautogui.locateOnScreen(imPath('%s_2th Card on Table.png' %x),  region=(po[0]+25, po[1]+215, 20, 40) )
            if i != None :
                shout(paint.green.bold("2th card is: %s" %x))
                Card_2th = x
                break
        time1 = time.time() - time0
        if (i == None or not Flop() or Turn() or time1 > 20 ) :
            if i == None :
                Screenshot_Error("Flop 2th card not founded!") #Type_of_Error in string
            Check_Mod_On("Read_Flop_Cards()2th")

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_3th Card on Table.png' %x),  region=(po[0]+87, po[1]+215, 20, 40) )
        if i != None :
            shout(paint.green.bold("3th card is: %s" %x))
            Card_3th = x
            break
    if i == None :
        Vital_Signs("Read_Flop_Cards():Card_3th")
        for x in Cards_names :
            i= pyautogui.locateOnScreen(imPath('%s_3th Card on Table.png' %x),  region=(po[0]+87, po[1]+215, 20, 40) )
            if i != None :
                shout(paint.green.bold("3th card is: %s" %x))
                Card_3th = x
                break
        time1 = time.time() - time0
        if (i == None or not Flop() or Turn() or time1 > 20 ) :
            if i == None :
                Screenshot_Error("Flop 3th card not founded!") #Type_of_Error in string
            Check_Mod_On("Read_Flop_Cards()3th")


def Read_Turn_Cards():
    global Card_4th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_4th Card on Table.png' %x),  region=(po[0]+150, po[1]+215, 20, 40) )
        if i != None :
            shout(paint.green.bold("4th card is: %s" %x))
            Card_4th = x
            break
    if i == None :
        Vital_Signs("Read_Turn_Cards()")
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_4th Card on Table.png' %x),  region=(po[0]+150, po[1]+215, 20, 40) )
            if i != None :
                shout(paint.green.bold("4th card is: %s" %x))
                Card_4th = x
                break
        time1 = time.time() - time0
        if (i == None or not Turn() or River() or time1 > 20 ) :
            if i == None :
                Screenshot_Error("Turn 4th card not founded!") #Type_of_Error in string
            Check_Mod_On("Read_Turn_Cards()")

def Read_River_Cards():
    global Card_5th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_5th Card on Table.png' %x),  region=(po[0]+212, po[1]+215, 20, 40) )
        if i != None :
            shout(paint.green.bold("5th card is: %s" %x))
            Card_5th = x
            break
    if i == None :
        Vital_Signs("Read_River_Cards()")
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_5th Card on Table.png' %x),  region=(po[0]+212, po[1]+215, 20, 40) )
            if i != None :
                shout(paint.green.bold("5th card is: %s" %x))
                Card_5th = x
                break        
        time1 = time.time() - time0
        if (i == None or not River() or time1 > 20 ) :
            if i == None :
                Screenshot_Error("River 5th card not founded!") #Type_of_Error in string
            Check_Mod_On("Read_River_Cards()")

def Read_My_Cards():
    global My_1th_Card , My_2th_Card  , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    if My_Seat_Number == 1 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat1 1th Card.png' %x),  region=(po[0]+369, po[1]+391, 10, 30) )
            if i != None :
                shout(paint.green.bold("My first Card is: %s" %x))
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat1:Card1")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat1 1th Card.png' %x),  region=(po[0]+369, po[1]+391, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My first Card is: %s" %x))
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My first card on seat 1 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat1 Read_My_Cards()1th")
                
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat1 2th Card.png' %x),  region=(po[0]+388, po[1]+391, 10, 30) )
            if i != None :
                shout(paint.green.bold("My second Card is: %s" %x))
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat1:Card2")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat1 2th Card.png' %x),  region=(po[0]+388, po[1]+391, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My second Card is: %s" %x))
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My second card on seat 1 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat1 Read_My_Cards()2th")       


    
    if My_Seat_Number == 2 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat2 1th Card.png' %x),  region=(po[0]+115, po[1]+393, 10, 30) )
            if i != None :
                shout(paint.green.bold("My first Card is: %s" %x))
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat2:Card1")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat2 1th Card.png' %x),  region=(po[0]+115, po[1]+393, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My first Card is: %s" %x))
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My first card on seat 2 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat2 Read_My_Cards()1th") 


        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat2 2th Card.png' %x),  region=(po[0]+133, po[1]+393, 10, 30) )
            if i != None :
                shout(paint.green.bold("My second Card is: %s" %x))
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat2:Card2")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat2 2th Card.png' %x),  region=(po[0]+133, po[1]+393, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My My second Card is: %s" %x))
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My second card on seat 2 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat2 Read_My_Cards()2th") 


    if My_Seat_Number == 3 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat3 1th Card.png' %x),  region=(po[0]-140, po[1]+390, 10, 30) )
            if i != None :
                shout(paint.green.bold("My first Card is: %s" %x))
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat3:Card1")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat3 1th Card.png' %x),  region=(po[0]-140, po[1]+390, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My first Card is: %s" %x))
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My first card on seat 3 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat3 Read_My_Cards()1th")

        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat3 2th Card.png' %x),  region=(po[0]-122, po[1]+390, 10, 30) )
            if i != None :
                shout(paint.green.bold("My second Card is: %s" %x))
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat3:Card2")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat3 2th Card.png' %x),  region=(po[0]-122, po[1]+390, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My My second Card is: %s" %x))
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My second card on seat 3 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat3 Read_My_Cards()2th")


    if My_Seat_Number == 4 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat4 1th Card.png' %x),  region=(po[0]-171, po[1]+85, 10, 30) )
            if i != None :
                shout(paint.green.bold("My first Card is: %s" %x))
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat4:Card1")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat4 1th Card.png' %x),  region=(po[0]-171, po[1]+85, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My first Card is: %s" %x))
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My first card on seat 4 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat4 Read_My_Cards()1th")

        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat4 2th Card.png' %x),  region=(po[0]-152, po[1]+85, 10, 30) )
            if i != None :
                shout(paint.green.bold("My second Card is: %s" %x))
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat4:Card2")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat4 2th Card.png' %x),  region=(po[0]-152, po[1]+85, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My My second Card is: %s" %x))
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My second card on seat 4 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat4 Read_My_Cards()2th")

    
    if My_Seat_Number == 5 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat5 1th Card.png' %x),  region=(po[0]+399, po[1]+85, 10, 30) )
            if i != None :
                shout(paint.green.bold("My first Card is: %s" %x))
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat5:Card1")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat5 1th Card.png' %x),  region=(po[0]+399, po[1]+85, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My first Card is: %s" %x))
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My first card on seat 5 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat5 Read_My_Cards()1th")

        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat5 2th Card.png' %x),  region=(po[0]+418, po[1]+85, 10, 30) )
            if i != None :
                shout(paint.green.bold("My second Card is: %s" %x))
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs("Read_My_Cards():Seat5:Card2")
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat5 2th Card.png' %x),  region=(po[0]+418, po[1]+85, 10, 30) )
                if i != None :
                    shout(paint.green.bold("My My second Card is: %s" %x))
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                if i == None :
                    Screenshot_Error("My second card on seat 5 is not founded!") #Type_of_Error in string
                Check_Mod_On("Seat5 Read_My_Cards()2th")




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


def OCR_Bet_String(Seat_Num):
    if Seat_Num==1 :
        return Replace_S_O( OCR(po[0]+320,po[1]+310,90,15) )#seat1_bet
    if Seat_Num==2 :
        return Replace_S_O( OCR(po[0]+101,po[1]+312,90,15) )#seat2_bet
    if Seat_Num==3 :
        return Replace_S_O( OCR(po[0]-116,po[1]+310,90,15) )#seat3_bet
    if Seat_Num==4 :
        return Replace_S_O( OCR(po[0]-121,po[1]+223,80,15) )#seat4_bet
    if Seat_Num==5 :
        return Replace_S_O( OCR(po[0]+324,po[1]+223,90,15) )#seat5_bet

def OCR_Bet_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    
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
            Screenshot_Error( "OCR_Bet_Number(This case can not happen1) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None
        else :
            Vital_Signs()
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
            return None
        else :
            Vital_Signs("Easy_OCR_Bet_Number(Seat_Num)")
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

def Replace_Comma_VoidSpace_Dollar_M_K(x):
    string = x
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("$","")
    string = string.replace("M","*1000000")
    string = string.replace("K","*1000")
    return string

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

def Others_In(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+321, po[1]+403, (4,6,7) ) #Others_In_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+161, po[1]+398, (5,7,8) ) #Others_In_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-94, po[1]+403, (4,6,7) ) #Others_In_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-124, po[1]+163, (4,6,7) ) #Others_In_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+431, po[1]+183, (4,5,6) ) #Others_In_seat_5

def OCR_Others_Bank_String(Seat_Num):
    if Seat_Num==1 :
        return Replace_S_O( OCR(po[0]+334,po[1]+471,75,15) )#seat1_Others_Bank
    if Seat_Num==2 :
        return Replace_S_O( OCR(po[0]+79,po[1]+473,75,15) )#seat2_Others_Bank
    if Seat_Num==3 :
        return Replace_S_O( OCR(po[0]-176,po[1]+471,75,15) )#seat3_Others_Bank
    if Seat_Num==4 :
        return Replace_S_O( OCR(po[0]-206,po[1]+166,75,15) )#seat4_Others_Bank
    if Seat_Num==5 :
        return Replace_S_O( OCR(po[0]+364,po[1]+166,75,15) )#seat5_Others_Bank


def OCR_Others_Bank_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    x1 = Win_Finish_Others(Seat_Num)
    y1 = Others_In(Seat_Num)
    string1 = OCR_Others_Bank_String( Seat_Num )
    x2 = Win_Finish_Others(Seat_Num)
    y2 = Others_In(Seat_Num)
    string2 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
    string2 = string2.replace("*","")
    if not( string1.count("$")==1 and string1.find('$')==0 and string2.isdigit()
            and x1==False and x2==False and y1 and y2 ) :
        if ( string1.count("$")==1 and string1.find('$')==0 and x1==False and x2==False and y1 and y2 and not string2.isdigit() ) :
            Screenshot_Error( "OCR_Others_Bank_Number(Error Not Digit!!) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None
        elif not(x1==False and x2==False) :
            Screenshot_Error( "OCR_Others_Bank_Number(this can not happen1) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None 
        elif ( y1 and y2 and not( string1.count("$")==1 and string1.find('$')==0 ) ) :
            shout("OCR_Others_Bank_Number(A Gift Over Bank Number) Seat %s " %Seat_Num )
            return None

        else : # if not(y1 or y2) :
            
            Vital_Signs()
            x1 = Win_Finish_Others(Seat_Num)
            y1 = Others_In(Seat_Num)
            string1 = OCR_Others_Bank_String( Seat_Num )
            x2 = Win_Finish_Others(Seat_Num)
            y2 = Others_In(Seat_Num)
            string2 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
            string2 = string2.replace("*","")
            if not( string1.count("$")==1 and string1.find('$')==0 and string2.isdigit()
                    and x1==False and x2==False and y1 and y2 ) :
                if ( string1.count("$")==1 and string1.find('$')==0 and x1==False and x2==False and y1 and y2 and not string2.isdigit() ) :
                    Screenshot_Error( "OCR_Others_Bank_Number(Error Not Digit!!2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
                elif not(x1==False and x2==False) :
                    Screenshot_Error( "OCR_Others_Bank_Number(this can not happen2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None 
                elif ( y1 and y2 and not( string1.count("$")==1 and string1.find('$')==0 ) ) :
                    shout("OCR_Others_Bank_Number(A Gift Over Seat %s Bank Number2) " %Seat_Num )
                    return None

                else : # if not(y1 or y2) :
                    Screenshot_Error( "OCR_Others_Bank_Number(Unknown Error) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
            else:
                string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
                shout ("Seat's %s Bank: " %Seat_Num , eval( string1 ) )
                Screenshot_Error( "OCR_Others_Bank_Number (Bank True after Vital sign) Seat %s" %Seat_Num  ) #Type_of_Error in string
                return eval( string1 )

    else:
        string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
        return eval( string1 )

def Easy_OCR_Others_Bank_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    string1 = OCR_Others_Bank_String( Seat_Num )

    string2 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
    string2 = string2.replace("*","")
    if not( string1.count("$")==1 and string1.find('$')==0 and string2.isdigit() ) :

        if ( not( string1.count("$")==1 and string1.find('$')==0 ) ) :
            shout("Easy_OCR_Others_Bank_Number(A Gift Over Bank Number) Seat %s " %Seat_Num )
            return None

        else :
            
            return None

    else:
        string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
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

def OCR_My_Bank_String(Seat_Num):
    if Seat_Num==1 :
        return Replace_S_O( OCR(po[0]+332,po[1]+468,75,14) )#seat1_Me_Bank
    if Seat_Num==2 :
        return Replace_S_O( OCR(po[0]+77,po[1]+471,75,14) )#seat2_Me_Bank
    if Seat_Num==3 :
        return Replace_S_O( OCR(po[0]-178,po[1]+468,75,14) )#seat3_Me_Bank
    if Seat_Num==4 :
        return Replace_S_O( OCR(po[0]-207,po[1]+163,75,14) )#seat4_Me_Bank
    if Seat_Num==5 :
        return Replace_S_O( OCR(po[0]+362,po[1]+163,75,14) )#seat5_Me_Bank


def OCR_My_Bank_Number(Seat_Num):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    x1 = Win_Finish_Me(Seat_Num)
    string1 = OCR_My_Bank_String( Seat_Num )
    x2 = Win_Finish_Me(Seat_Num)
    string2 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
    string2 = string2.replace("*","")
    if not( string1.count("$")==1 and string1.find('$')==0 and string2.isdigit()
            and x1==False and x2==False ) :
        if not(x1==False and x2==False) :
            Screenshot_Error("OCR_My_Bank_Number(This case can not happen 1 ! My Bank can't be read, Becuase i'm in winning light) Seat %s" %Seat_Num) #Type_of_Error in string
            return None 
        if ( x1==False and x2==False ) :
            
            Vital_Signs("OCR_My_Bank_Number(Seat_Num)")
            x1 = Win_Finish_Me(Seat_Num)
            string1 = OCR_My_Bank_String( Seat_Num )
            x2 = Win_Finish_Me(Seat_Num)
            string2 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
            string2 = string2.replace("*","")
            if not( string1.count("$")==1 and string1.find('$')==0 and string2.isdigit()
                    and x1==False and x2==False ) :
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
                string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
                return eval( string1 )

    else:
        string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
        return eval( string1 )

# ****3. OCR_My_Bank_Number(Seat_Num) ****

# OCR Me Bank Number Positions 2016 Ended ----------------------------------------------------------------------------------------




# OCR Others Name Positions 2016: ------------------------------------------------------------------------------------------------

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
    po=pyautogui.locateOnScreen('mainpic.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic.png')
        if po_new is None:
            Screenshot_Error("Could not find game on screen") #Type_of_Error in string
            raise Exception('Could not find game on screen. Is the game visible?')
        po=( po_new[0]+329 , po_new[1]-258 )


def getpo():
    global po

    po_old = po
    po = None ; fo = 0
    while po == None and fo <= 2 :
        fo += 1
        po=pyautogui.locateOnScreen('mainpic.png')
        if po==None:
            po_new=pyautogui.locateOnScreen('Alternative main pic.png')
            if po_new == None and fo == 2 :
                shout(paint.yellow.bold("Could not find game on screen,program will use old position"))
                Screenshot_Error("Could not find game on screen, Program will use former position")
                po = po_old # vital signs --> getpo_for_starting() will compensate
            elif po_new != None :
                po = ( po_new[0]+329 , po_new[1]-258 )
        if po == None and fo == 1 :
            shout(paint.yellow.bold("Adjust the game screen! Researching will be started again in 10s...."))
            time.sleep(10)

def OCR(x,y,h,w):
    im=pyautogui.screenshot(region=(x, y , h, w) )
    ratio=5
    im=im.resize((im.size[0]*ratio,im.size[1]*ratio) ,Image.ANTIALIAS)
    return image_to_string( im )

def OCR_My_Name(Seat_Num): #this OCR should be compeleted at future!!!!!!!!!!!!!!!!!!!!! (2017: az file ocr me name copy va jaygozin shavad)
    if Seat_Num == 1 :
        return OCR(po[0]+298,po[1]+363,140,16)  #seat1_Me_Name
    if Seat_Num == 2 :
        return OCR(po[0]+43,po[1]+366,140,16)  #seat2_Me_Name
    if Seat_Num == 3 :
        return OCR(po[0]-212,po[1]+363,140,16)  #seat3_Me_Name    
    if Seat_Num == 4 :
        return OCR(po[0]-243,po[1]+58,140,16)  #seat4_Me_Name
    if Seat_Num == 5 :
        return OCR(po[0]+328,po[1]+58,140,16)  #seat5_Me_Name

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

def Check_I_am_In_or_Out():
    global My_Seat_Number , My_Profile_Name
    if I_am_back_Button() == True :
        Click_on_I_am_back_Button()
    if OCR_My_Name(My_Seat_Number) == My_Profile_Name or OCR_My_Name(My_Seat_Number) == True :
        shout(paint.yellow.bold("I am In"))
        return ("In")
    #elif Me_In( My_Seat_Number ) tabe bayad dar ayande sakhte shavad :
        #shout("I am In not by OCR")
        #return ("In")
    else :
        shout(paint.yellow.bold("I am Out"))
        return ("Out")
        
   
def Vital_Signs(String = None): #if getpo() == None or ...
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    shout(paint.yellow.bold( 7*"-" ))
    if String == None :
        shout(paint.yellow.bold("Vital_Signs() is running...."))
    elif type(String) == str :
        shout(paint.yellow.bold("Vital_Signs() <-- %s is running...." %String))
    Lost_Connection = pyautogui.locateOnScreen('Lost_Connection.png')
    if Lost_Connection != None :
        shout(paint.yellow.bold("Lost_Connection is Visible..."))
        x1 = time.time()
        while ( Lost_Connection != None  ):
            Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
        shout(paint.yellow.bold("Connection is Back again"))
        x2 = time.time()
        Lost_Connection_Time[x1]= x2-x1 

    pyautogui.click(0, 720) # click to Exit probable Advertisement
    shout(paint.yellow.bold("Position (0,720) is clicked"))

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
    t = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
    t = t[:-4]
    shout(paint.on_light_blue.bold("Screenshot Error: %s" %Type_of_Error))
    pyautogui.screenshot( 'Error %s %s.png' %(t,Type_of_Error) )

def Raise_What_is_Problem(string):
    Screenshot_Error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')


# Vital_signs Ended --------------------------------------------------------------------------------------------------------------

### new functions: ****************************************************************************************************************************


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
    
def Reset_Table_Info() :
    global Players_name_dic , Players_bank_dic ,\
           Cards_cache , White_cache , Red_cache , Bet_cache ,\
           Last_Cards_cache , Last_White_cache , Last_Red_cache , Last_Bet_cache
    
    shout("Reseting Table Information")
    for Seat in range(1,6):
        Players_name_dic[Seat] = None
        Players_bank_dic[Seat] = None
    Cards_cache = {} ; White_cache = {}  ; Red_cache = {}  ; Bet_cache = {}
    Last_Cards_cache = {} ; Last_White_cache = {}  ; Last_Red_cache = {}  ; Last_Bet_cache = {}
    

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

def last_raise_cache() :
    global Last_Bet_cache , Last_Red_cache

    a = []
    for Seat in range(1,6) :
        if type(Last_Bet_cache[Seat]) == int :
            a.append( Last_Bet_cache[Seat] )
    if len(a) != 0 and is_there_any_raiser_cache() ==  True :
        return max(a)
    a = []

def last_raiser_seat_cache() :
    global Last_Red_cache , Last_Cards_cache , My_Seat_Number

    last_raiser = None
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        
        if Last_Red_cache[Seat] and Last_Cards_cache[Seat] :
            last_raiser = Seat
            
    return last_raiser 

#def former_stage_last_raise_cache() :
#    global 
    

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

    
### new funciotns ended ***********************************************************************************************************************
            
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
    
    
def Decide():
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
           Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated 

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Preflop*"))
    elif Flop1_Deside == True and Turn1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Flop*"))
    elif Turn1_Deside == True and River1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Turn*"))
    elif River1_Deside == True :
        shout(paint.light_cyan.bold("*Deciding on River*"))
    else :
        shout(paint.light_cyan.bold("*Deciding on Unknown*"))
    
    if Check_Mod == True :
        check_fold()

    else :
        
        if Pre_Flop1_Deside == True and Flop1_Deside == False :

            if Round_Pre_Flop == 0 and hand1() :
                Raise(5)
            elif Round_Pre_Flop != 0 and hand1() :
                all_in()

            elif Round_Pre_Flop == 0 and hand2() :
                Raise(4)
            elif Round_Pre_Flop != 0 and hand2() :
                check_fold()

            elif Round_Pre_Flop == 0 and hand3() :
                Raise(3)
            elif Round_Pre_Flop != 0 and hand3() :
                check_fold()
        
            elif Round_Pre_Flop == 0 and hand4() :
                Raise(2)
            elif Round_Pre_Flop != 0 and hand4() :
                check_fold()

            elif Round_Pre_Flop == 0 and hand5() :
                Raise(3)
            elif Round_Pre_Flop != 0 and hand5() :
                check_fold()

            else :
                check_fold()
                
        if Flop1_Deside == True and Turn1_Deside == False :

            if Round_Flop == 0 and hand1() :
                bet(5)
            elif Round_Flop != 0 and hand1() :
                check_fold()

            elif Round_Flop == 0 and hand2() :
                bet(4)
            elif Round_Flop != 0 and hand2() :
                check_fold()

            elif Round_Flop == 0 and hand3() :
                check_fold()
            elif Round_Pre_Flop != 0 and hand3() :
                check_fold()
        
            elif Round_Flop == 0 and hand4() :
                check_fold()
            elif Round_Flop != 0 and hand4() :
                check_fold()

            elif Round_Flop == 0 and hand5() :
                check_fold()
            elif Round_Flop != 0 and hand5() :
                check_fold()            

            else :
                check_fold()

        if Turn1_Deside == True and River1_Deside == False :

            if Round_Turn == 0 and hand1() :
                bet(5)
            elif Round_Turn != 0 and hand1() :
                check_fold()

            elif Round_Turn == 0 and hand2() :
                bet(4)
            elif Round_Turn != 0 and hand2() :
                check_fold()

            elif Round_Turn == 0 and hand3() :
                check_fold()
            elif Round_Turn != 0 and hand3() :
                check_fold()
        
            elif Round_Turn == 0 and hand4() :
                check_fold()
            elif Round_Turn != 0 and hand4() :
                check_fold()

            elif Round_Turn == 0 and hand5() :
                check_fold()
            elif Round_Turn != 0 and hand5() :
                check_fold()

            else :
                check_fold()            


        if River1_Deside == True :

            if Round_River == 0 and hand1() :
                bet(5)
            elif Round_River != 0 and hand1() :
                check_fold()

            elif Round_River == 0 and hand2() :
                bet(4)
            elif Round_River != 0 and hand2() :
                check_fold()

            elif Round_River == 0 and hand3() :
                check_fold()
            elif Round_River != 0 and hand3() :
                check_fold()
        
            elif Round_River == 0 and hand4() :
                check_fold()
            elif Round_River != 0 and hand4() :
                check_fold()

            elif Round_River == 0 and hand5() :
                check_fold()
            elif Round_River != 0 and hand5() :
                check_fold()            

            else :
                check_fold()




            
    time.sleep(1)



# first line values: ----------------------
My_Profile_Name = "Sepehr75"
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
        
            
    Round_Pre_Flop = 0
    if Light( My_Seat_Number ) == True and Gray1 == False and Hand_End_Cheker() == False and Flop1_Deside == False and Just_Seated == False :
        shout(paint.light_magenta.bold("light is founded"))
        Read_Bets() #
        Decide() # preflop
    elif Hand_End_Cheker() == False and Flop1_Deside == False and Just_Seated == False :
        Vital_Signs("4 Entering This section is not possible")
        Screenshot_Error("6.6 Entering This section is not possible")
        Read_Bets() #
        Decide() # preflop



# PreFlop: -------

        
    if Just_Seated == False :

        shout("Running PreFlop Section")
        time01 = time.time()
        time02 = time.time() - time01
        Round_Pre_Flop = 0
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
            



