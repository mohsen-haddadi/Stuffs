import pyautogui, time, os
from PIL import Image
from pyautogui import pixelMatchesColor
from pytesseract import image_to_string
from FUNCTIONS_hand import *


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
        return print("I won the game!")
    if( other1==True ):
        return print("Seat 1 won the game!")
    if( other2==True ):
        return print("Seat 2 won the game!")
    if( other3==True ):
        return print("Seat 3 won the game!")
    if( other4==True ):
        return print("Seat 4 won the game!")
    if( other5==True ):
        return print("Seat 5 won the game!")

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

    
def Players_In_dic_Engine(Five_Seats_CardsX):  #(print who Folds and Update players_In dictionary)
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
            return print("seat",k+1,"Folded!")    
      

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
        print("Seat 1 is at Small Blind Seat")
    elif Small_seat_2 == True :
        Small_Blind_Seat = 2
        print("Seat 2 is at Small Blind Seat")
    elif Small_seat_3 == True :
        Small_Blind_Seat = 3
        print("Seat 3 is at Small Blind Seat")
    elif Small_seat_4 == True :
        Small_Blind_Seat = 4
        print("Seat 4 is at Small Blind Seat")
    elif Small_seat_5 == True :
        Small_Blind_Seat = 5
        print("Seat 5 is at Small Blind Seat")


def Determine_Big_Blind_Seat():
    global Big_Blind_Seat
    
    Big_seat_1= pixelMatchesColor( po[0]+367, po[1]+329, (180,180,180) ) #Big_seat_1
    Big_seat_2= pixelMatchesColor( po[0]+111, po[1]+332, (200,200,200) ) #Big_seat_2
    Big_seat_3= pixelMatchesColor( po[0]-145, po[1]+329, (185,185,185) ) #Big_seat_3
    Big_seat_4= pixelMatchesColor( po[0]-174, po[1]+212, (185,185,185) ) #Big_seat_4
    Big_seat_5= pixelMatchesColor( po[0]+400, po[1]+212, (185,185,185) ) #Big_seat_5

    if Big_seat_1 == True :
        Big_Blind_Seat = 1
        print("Seat 1 is at Big Blind Seat")
    elif Big_seat_2 == True :
        Big_Blind_Seat = 2
        print("Seat 2 is at Big Blind Seat")
    elif Big_seat_3 == True :
        Big_Blind_Seat = 3
        print("Seat 3 is at Big Blind Seat")
    elif Big_seat_4 == True :
        Big_Blind_Seat = 4
        print("Seat 4 is at Big Blind Seat")
    elif Big_seat_5 == True :
        Big_Blind_Seat = 5
        print("Seat 5 is at Big Blind Seat") 


def Determine_Dealer_Seat():
    global Dealer_Seat
    
    Dealer_seat_1= pixelMatchesColor( po[0]+397, po[1]+330, (255,155,0) ) #Dealer_seat_1
    Dealer_seat_2= pixelMatchesColor( po[0]+144, po[1]+333, (254,193,0) ) #Dealer_seat_2
    Dealer_seat_3= pixelMatchesColor( po[0]-116, po[1]+330, (255,154,0) ) #Dealer_seat_3
    Dealer_seat_4= pixelMatchesColor( po[0]-202, po[1]+212, (255,160,0) ) #Dealer_seat_4
    Dealer_seat_5= pixelMatchesColor( po[0]+429, po[1]+212, (255,160,0) ) #Dealer_seat_5 

    if Dealer_seat_1 == True :
        Dealer_Seat = 1
        print("Seat 1 is at Dealer Seat")
    elif Dealer_seat_2 == True :
        Dealer_Seat = 2
        print("Seat 2 is at Dealer Seat")
    elif Dealer_seat_3 == True :
        Dealer_Seat = 3
        print("Seat 3 is at Dealer Seat")
    elif Dealer_seat_4 == True :
        Dealer_Seat = 4
        print("Seat 4 is at Dealer Seat")
    elif Dealer_seat_5 == True :
        Dealer_Seat = 5
        print("Seat 5 is at Dealer Seat")


def my_turn_from_coins() :
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

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
                Screenshot_Error("my_turn_from_coins() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
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
    global My_Seat_Number 

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
                Screenshot_Error("my_turn_from_last_raiser() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Screenshot_Error("my_turn_from_last_raiser() (This case can not happen1) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )



def next_playing_player_seat( My_Seat_Number , forward_backward_number ) :
    """ forward_backward_number can be + or -
    if abs(forward_backward_number) > (4 or more than playing players) : return None """

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


# FUNCTIONS_Decide_and_Pixel-Maching Ended ---------------------------------------------------------------------------------------







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
        print("Available_Seat 1 is clicked")
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
        print("Available_Seat 2 is clicked")
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
        print("Available_Seat 3 is clicked")
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
        print("Available_Seat 4 is clicked")
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5
        print("Available_Seat 5 is clicked")

def Fold_Button():
    x1 = pixelMatchesColor( po[0]+51, po[1]+581, (190,22,28) ) #Fold
    x2 = pixelMatchesColor( po[0]+51, po[1]+581, (220,27,33) ) #Fold_Light
    return (x1 or x2)

def Click_on_Fold_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Fold_Button() :
        pyautogui.click( po[0]+51, po[1]+581 )
        print("Fold_Button is clicked")
    else :
        Vital_Signs()
        if Cards( My_Seat_Number ) and Fold_Button() :
            pyautogui.click( po[0]+51, po[1]+581 )
            print("Fold_Button is clicked")

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
        print("Check_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Check_Button1 = Check_Button()
        if Cards( My_Seat_Number ) and Check_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+246, po[1]+578 )
            print("Check_Button is clicked")
        else :
            Check_Mod = True
            
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
        print("Call_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Call_Button1 = Call_Button()
        if Cards( My_Seat_Number ) and Call_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+261, po[1]+575 )
            print("Call_Button is clicked")
        else :
            Check_Mod = True

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
        print("Bet_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Bet_Button1 = Bet_Button()
        if Cards( My_Seat_Number ) and Bet_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+461, po[1]+576 )
            print("Bet_Button is clicked")
        else :
            Check_Mod = True

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
        print("Raise_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Raise_Button1 = Raise_Button()
        if Cards( My_Seat_Number ) and Raise_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+461, po[1]+576 )
            print("Raise_Button is clicked")
        else :
            Check_Mod = True

def Plus_Button():
    x1 = pixelMatchesColor( po[0]+246, po[1]+648, (58,68,83) ) #Plus_Button
    x2 = pixelMatchesColor( po[0]+246, po[1]+648, (77,88,105) ) #Plus_Button_Light
    return (x1 or x2)

def Number_of_Clicks_on_Plus_Button(Number): #Number of clicks
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Plus_Button() :
        for i in range (Number):
            pyautogui.click( po[0]+246, po[1]+648 )
        print("Plus_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Plus_Button1 = Plus_Button()
        if Cards( My_Seat_Number ) and Plus_Button1 and time1 <= 10 :
            for i in range (Number):
                pyautogui.click( po[0]+246, po[1]+648 )
            print("Plus_Button is clicked")
        else :
            Check_Mod = True

def Minus_Button():
    x1 = pixelMatchesColor( po[0]-9, po[1]+648, (58,68,83) ) #Minus_Button
    x2 = pixelMatchesColor( po[0]-9, po[1]+648, (77,88,105) ) #Minus_Button_Light
    return (x1 or x2)

def Number_of_Click_on_Minus_Button(Number): #Number of clicks
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Minus_Button() :
        for i in range (Number):
            pyautogui.click( po[0]-9, po[1]+648 )
        print("Minus_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Minus_Button1 = Minus_Button()
        if Cards( My_Seat_Number ) and Minus_Button1 and time1 <= 10 :
            for i in range (Number):
                pyautogui.click( po[0]-9, po[1]+648 )
            print("Minus_Button is clicked")
        else :
            Check_Mod = True

def All_In_Button():
    x1 = pixelMatchesColor( po[0]+531, po[1]+648, (207,90,6) ) #All_In_Button
    x2 = pixelMatchesColor( po[0]+531, po[1]+648, (235,98,0) ) #All_In_Button_Light
    return (x1 or x2)

def Click_on_All_In_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if All_In_Button() :
        pyautogui.click( po[0]+531, po[1]+648 )
        print("All_In_Button is clicked")
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        All_In_Button1 = All_In_Button()
        if Cards( My_Seat_Number ) and All_In_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+531, po[1]+648 )
            print("All_In_Button is clicked")
        else :
            Check_Mod = True

def Exit_Button():
    x1 = pixelMatchesColor( po[0]+378, po[1]+21, (130,135,146) ) #Exit_Button
    x2 = pixelMatchesColor( po[0]+378, po[1]+21, (156,160,168) ) #Exit_Button_Light
    return (x1 or x2)

def Click_on_Exit_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Exit_Button():
        pyautogui.click( po[0]+378, po[1]+21 )
        print("Exit_Button is clicked")
    else :
        Vital_Signs()
        if Exit_Button():
            pyautogui.click( po[0]+378, po[1]+21 )
            print("Exit_Button is clicked")
        else : #can't proceed to here
            Raise_What_is_Problem("Click_on_Exit_Button")
            
def Exit_Yes_Button():
    x1 = pixelMatchesColor( po[0]+47, po[1]+355, (168,11,16) ) #Exit_Yes_Button
    x2 = pixelMatchesColor( po[0]+47, po[1]+355, (177,13,19) ) #Exit_Yes_Button_Light
    return (x1 or x2)

def Click_on_Exit_Yes_Button():
    if Exit_Yes_Button():
        pyautogui.click( po[0]+47, po[1]+355 )
        print("Exit_Yes_Button is clicked")
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
        print("Menu_Button is clicked")
    else :
        Vital_Signs()
        if Exit_Button():
            pyautogui.click( po[0]-399, po[1]-66 )
            print("Menu_Button is clicked")
        else :
            Raise_What_is_Problem("Click_on_Exit_Button")

def Rebuy_Menu_Button():
    x1 = pixelMatchesColor( po[0]+513, po[1]+14, (203,0,6) ) #Rebuy_Menu_Button
    return (x1)

def Click_on_Rebuy_Menu_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Rebuy_Menu_Button():
        pyautogui.click( po[0]+513, po[1]+14 )
        print("Rebuy_Menu_Button is clicked")
    else :
        Vital_Signs()
        if Rebuy_Menu_Button():
            pyautogui.click( po[0]+513, po[1]+14 )
            print("Rebuy_Menu_Button is clicked")
        else :
            Raise_What_is_Problem("Click_on_Rebuy_Menu_Button")

def Leave_Next_Hand_OK_Button():
    x1 = pixelMatchesColor( po[0]+108, po[1]+342, (0,83,171) ) #Leave_Next_Hand_OK_Button
    x2 = pixelMatchesColor( po[0]+108, po[1]+342, (0,95,193) ) #Leave_Next_Hand_OK_Button_Light
    return (x1 or x2)

def Click_on_Leave_Next_Hand_OK_Button():
    if Leave_Next_Hand_OK_Button() :
        pyautogui.click( po[0]+108, po[1]+342 )
        print("Leave_Next_Hand_OK_Button is clicked")
    else :
        Raise_What_is_Problem("Click_on_Leave_Next_Hand_OK_Button")
    
def Buy_In_Button():
    x1 = pixelMatchesColor( po[0]+71, po[1]+448, (26,123,0) ) #Buy_In_Button
    x2 = pixelMatchesColor( po[0]+71, po[1]+448, (32,149,0) ) #Buy_In_Button_Light
    return (x1 or x2)

def Click_on_Buy_In_Button():
    if Buy_In_Button() :
        pyautogui.click( po[0]+71, po[1]+448 )
        print("Buy_In_Button is clicked")
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
        print("Re_Buy_Button is clicked")
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
    print("I_am_back_Button is clicked")
    Check_Mod = True
    


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

def all_in( Minus_Blinds ):
    """ if 0 : all_in everything """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
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
        Check_Mod = True #It's already True
        Vital_Signs()
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
            print("1th card is: %s" %x)
            Card_1th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names :
            i= pyautogui.locateOnScreen(imPath('%s_1th Card on Table.png' %x),  region=(po[0]-38, po[1]+215, 20, 40) )
            if i != None :
                print("1th card is: %s" %x)
                Card_1th = x
                break
        time1 = time.time() - time0
        if (i == None or not Flop() or Turn() or time1 > 20 ) :
            print("Flop 1th card not founded!")
            Screenshot_Error("Flop 1th card not founded!") #Type_of_Error in string
            Check_Mod = True

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_2th Card on Table.png' %x),  region=(po[0]+25, po[1]+215, 20, 40) )
        if i != None :
            print("2th card is: %s" %x)
            Card_2th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names :
            i= pyautogui.locateOnScreen(imPath('%s_2th Card on Table.png' %x),  region=(po[0]+25, po[1]+215, 20, 40) )
            if i != None :
                print("2th card is: %s" %x)
                Card_2th = x
                break
        time1 = time.time() - time0
        if (i == None or not Flop() or Turn() or time1 > 20 ) :
            print("Flop 2th card not founded!")
            Screenshot_Error("Flop 2th card not founded!") #Type_of_Error in string            
            Check_Mod = True

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_3th Card on Table.png' %x),  region=(po[0]+87, po[1]+215, 20, 40) )
        if i != None :
            print("3th card is: %s" %x)
            Card_3th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names :
            i= pyautogui.locateOnScreen(imPath('%s_3th Card on Table.png' %x),  region=(po[0]+87, po[1]+215, 20, 40) )
            if i != None :
                print("3th card is: %s" %x)
                Card_3th = x
                break
        time1 = time.time() - time0
        if (i == None or not Flop() or Turn() or time1 > 20 ) :
            print("Flop 3th card not founded!")
            Screenshot_Error("Flop 3th card not founded!") #Type_of_Error in string
            Check_Mod = True


def Read_Turn_Cards():
    global Card_4th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_4th Card on Table.png' %x),  region=(po[0]+150, po[1]+215, 20, 40) )
        if i != None :
            print("4th card is: %s" %x)
            Card_4th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_4th Card on Table.png' %x),  region=(po[0]+150, po[1]+215, 20, 40) )
            if i != None :
                print("4th card is: %s" %x)
                Card_4th = x
                break
        time1 = time.time() - time0
        if (i == None or not Turn() or River() or time1 > 20 ) :
            print("Trun 4th card not founded!")
            Screenshot_Error("Turn 4th card not founded!") #Type_of_Error in string
            Check_Mod = True

def Read_River_Cards():
    global Card_5th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen(imPath('%s_5th Card on Table.png' %x),  region=(po[0]+212, po[1]+215, 20, 40) )
        if i != None :
            print("5th card is: %s" %x)
            Card_5th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_5th Card on Table.png' %x),  region=(po[0]+212, po[1]+215, 20, 40) )
            if i != None :
                print("5th card is: %s" %x)
                Card_5th = x
                break        
        time1 = time.time() - time0
        if (i == None or not River() or time1 > 20 ) :
            print("River 5th card not founded!")
            Screenshot_Error("River 5th card not founded!") #Type_of_Error in string
            Check_Mod = True

def Read_My_Cards():
    global My_1th_Card , My_2th_Card  , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    if My_Seat_Number == 1 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat1 1th Card.png' %x),  region=(po[0]+369, po[1]+391, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat1 1th Card.png' %x),  region=(po[0]+369, po[1]+391, 10, 30) )
                if i != None :
                    print("My first Card is: %s" %x)
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My first card on seat 1 is not founded!")
                Screenshot_Error("My first card on seat 1 is not founded!") #Type_of_Error in string
                Check_Mod = True
                
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat1 2th Card.png' %x),  region=(po[0]+388, po[1]+391, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat1 2th Card.png' %x),  region=(po[0]+388, po[1]+391, 10, 30) )
                if i != None :
                    print("My second Card is: %s" %x)
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My second card on seat 1 is not founded!")
                Screenshot_Error("My second card on seat 1 is not founded!") #Type_of_Error in string
                Check_Mod = True        


    
    if My_Seat_Number == 2 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat2 1th Card.png' %x),  region=(po[0]+115, po[1]+393, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat2 1th Card.png' %x),  region=(po[0]+115, po[1]+393, 10, 30) )
                if i != None :
                    print("My first Card is: %s" %x)
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My first card on seat 2 is not founded!")
                Screenshot_Error("My first card on seat 2 is not founded!") #Type_of_Error in string
                Check_Mod = True


        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat2 2th Card.png' %x),  region=(po[0]+133, po[1]+393, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat2 2th Card.png' %x),  region=(po[0]+133, po[1]+393, 10, 30) )
                if i != None :
                    print("My My second Card is: %s" %x)
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My second card on seat 2 is not founded!")
                Screenshot_Error("My second card on seat 2 is not founded!") #Type_of_Error in string
                Check_Mod = True


    if My_Seat_Number == 3 :
        time0 = time.time()
        
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat3 1th Card.png' %x),  region=(po[0]-140, po[1]+390, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat3 1th Card.png' %x),  region=(po[0]-140, po[1]+390, 10, 30) )
                if i != None :
                    print("My first Card is: %s" %x)
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My first card on seat 3 is not founded!")
                Screenshot_Error("My first card on seat 3 is not founded!") #Type_of_Error in string
                Check_Mod = True

        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat3 2th Card.png' %x),  region=(po[0]-122, po[1]+390, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat3 2th Card.png' %x),  region=(po[0]-122, po[1]+390, 10, 30) )
                if i != None :
                    print("My My second Card is: %s" %x)
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My second card on seat 3 is not founded!")
                Screenshot_Error("My second card on seat 3 is not founded!") #Type_of_Error in string
                Check_Mod = True


    if My_Seat_Number == 4 :
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat4 1th Card.png' %x),  region=(po[0]-171, po[1]+85, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat4 1th Card.png' %x),  region=(po[0]-171, po[1]+85, 10, 30) )
                if i != None :
                    print("My first Card is: %s" %x)
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My first card on seat 4 is not founded!")
                Screenshot_Error("My first card on seat 4 is not founded!") #Type_of_Error in string
                Check_Mod = True

        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat4 2th Card.png' %x),  region=(po[0]-152, po[1]+85, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat4 2th Card.png' %x),  region=(po[0]-152, po[1]+85, 10, 30) )
                if i != None :
                    print("My My second Card is: %s" %x)
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My second card on seat 4 is not founded!")
                Screenshot_Error("My second card on seat 4 is not founded!") #Type_of_Error in string
                Check_Mod = True

    
    if My_Seat_Number == 5 :
        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat5 1th Card.png' %x),  region=(po[0]+399, po[1]+85, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat5 1th Card.png' %x),  region=(po[0]+399, po[1]+85, 10, 30) )
                if i != None :
                    print("My first Card is: %s" %x)
                    My_1th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My first card on seat 5 is not founded!")
                Screenshot_Error("My first card on seat 5 is not founded!") #Type_of_Error in string
                Check_Mod = True

        for x in Cards_names:
            i= pyautogui.locateOnScreen(imPath('%s_Seat5 2th Card.png' %x),  region=(po[0]+418, po[1]+85, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen(imPath('%s_Seat5 2th Card.png' %x),  region=(po[0]+418, po[1]+85, 10, 30) )
                if i != None :
                    print("My My second Card is: %s" %x)
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My second card on seat 5 is not founded!")
                Screenshot_Error("My second card on seat 5 is not founded!") #Type_of_Error in string
                Check_Mod = True




# Read Cards Ended ---------------------------------------------------------------------------------------------------------------



# Vital_signs: -------------------------------------------------------------------------------------------------------------------




def getpo_for_starting(): #when i am watching the game myself, raise the Exeption 
    global po

    print("Looking for game on screen...")
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
            if po_new == None:
                print("Could not find game on screen,program will use old position")
                Screenshot_Error("Could not find game on screen, Program will use former position")
                po = po_old # vital signs --> getpo_for_starting() will compensate
            else :
                po=( po_new[0]+329 , po_new[1]-258 )
        if po == None and fo == 1 :
            print("Adjust the game screen! Researching will be started again in 10s....")
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
        print("Available_Seat 1 is clicked")
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
        print("Available_Seat 2 is clicked")
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
        print("Available_Seat 3 is clicked")
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
        print("Available_Seat 4 is clicked")
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5
        print("Available_Seat 5 is clicked")

def Click_on_Exit_Button(): #this should be compeleted at future for Sit_In!!!!!!!!!!!!!!!!!!!!!  (maybe should be compeleted, maybe not)
    pyautogui.click( po[0]+378, po[1]+21 )
    print("Exit_Button is clicked")

def Sit_In(Chips): # "Min buy in" or "Max buy in"
    global My_Seat_Number , Just_Seated 
    My_Seat_Number = None
    for i in range(1 ,6 ):
        if Available_Seat(i) == True :
            Click_on_Available_Seat(i)
            My_Seat_Number = i
            Just_Seated = True
            print("Sit_In() --> Just_Seated is True.")
            break
    if My_Seat_Number == None :
        Click_on_Exit_Button()
        Just_Seated = None
        print("Sit_In() --> Just_Seated is None.")
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
            Vital_Signs()
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
    print("I_am_back_Button is clicked")
    Check_Mod = True

def Check_I_am_In_or_Out():
    global My_Seat_Number , My_Profile_Name
    if I_am_back_Button() == True :
        Click_on_I_am_back_Button()
    if OCR_My_Name(My_Seat_Number) == My_Profile_Name or OCR_My_Name(My_Seat_Number) == True :
        print("I am In")
        return ("In")
    #elif Me_In( My_Seat_Number ) tabe bayad dar ayande sakhte shavad :
        #print("I am In not by OCR")
        #return ("In")
    else :
        print("I am Out")
        return ("Out")
        
   
def Vital_Signs(): #if getpo() == None or ...
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    print("Vital_Signs() is running....")
    Lost_Connection = pyautogui.locateOnScreen('Lost_Connection.png')
    if Lost_Connection != None :
        print("Lost_Connection is Visible...")
        x1 = time.time()
        while ( Lost_Connection != None  ):
            Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
        print("Connection is Back again")
        x2 = time.time()
        Lost_Connection_Time[x1]= x2-x1 

    pyautogui.click(0, 720) # click to Exit probable Advertisement
    print("Position (0,720) is clicked")

    getpo_for_starting() #if None,it will raise the Exeption
    if po != None :
        print("Game region refounded after Vital_Signs()")
    
    if I_am_back_Button() == True :
        if Cards( My_Seat_Number ) == True :
            Check_Mod = True
            print("Vital_Signs() --> Check_Mod is True.")
        else :
            Just_Seated = True
            print("Vital_Signs() --> Just_Seated is True.")
        Click_on_I_am_back_Button()

    if Check_I_am_In_or_Out() == "Out":
        Sit_In("Min buy in")

#if (buttoms are still not visible after vital signs).... : #My pixel matching were wrong somewhere
#    t = time.time()
#    pyautogui.screenshot( 'Error %s.png' %t )
#    raise Exception('what was the probelm on %s?' %t ) 
        
def Screenshot_Error(Type_of_Error): #Type_of_Error in string
    t = time.time()
    pyautogui.screenshot( 'Error %s %s.png' %(Type_of_Error,t) )

def Raise_What_is_Problem(string):
    Screenshot_Error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')


# Vital_signs Ended --------------------------------------------------------------------------------------------------------------



def Decide():
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
           Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated 

    if Check_Mod == True :
        check_fold()

    else :
        check_fold()
        
    time.sleep(1)



# first line values: ----------------------
My_Profile_Name = "Sepehr75"
My_Seat_Number = 2
Just_Seated = True # will be omitted (None,True,False)
Lost_Connection_Time = {} 
# first line values Ended -----------------


getpo_for_starting()



while True :

    Pre_Flop1_Deside = False ; Flop1_Deside = False ; Turn1_Deside = False ; River1_Deside = False 

    if Just_Seated == True :

        print("Running Just_Seated == True Section")
        Check_Mod = False
        
        time1 = time.time()
        Hand_End_Cheker1 = False
        while Hand_End_Cheker1 == False :
            Hand_End_Cheker1 = Hand_End_Cheker()
            if time.time() - time1 > 5 * 60 :
                raise Exception('1.I should work on main menu automation later!')
                Vital_Signs()
            
        time1 = time.time()
        while Hand_End_Cheker1 == True :
            Hand_End_Cheker1 = Hand_End_Cheker()
            if time.time() - time1 > 5 * 60 :
                raise Exception('2.I should work on main menu automation later!')
                Vital_Signs()

        Light1 = False
        Gray1 = True
        while Light1 == False or Gray1 == True :
            Light1 = Light( My_Seat_Number )
            Gray1 = Gray_Sign_Seat( My_Seat_Number )
            if time.time() - time1 > 5 * 60 :
                raise Exception('3.I should work on main menu automation later!')
                Vital_Signs()

        if Pre_Flop() == False :
            Raise_What_is_Problem('4.I have just seated')

        Just_Seated = False
        print ("****** First hand Started ******")
    
    elif Just_Seated == None :
        raise Exception("5.This can not happen IN FUTURE becuase main menu automation is built\
                        ( vital_signs --> Sit_In --> table is full --> exit -->\
                        Just_Seated = None --> main menu --> Just_Seated = True )")


    

    if Pre_Flop() == False :
        Vital_Signs()
        Check_Mod = True
        Screenshot_Error('6.Pre_Flop() == False')
    else :
        Pre_Flop1 = True
        Pre_Flop1_Deside = True
        
    Read_My_Cards() #

    if Light( My_Seat_Number ) == True :        
        Decide() # preflop
    else :
        Vital_Signs()
        Decide() # preflop



# PreFlop: -------

        
    if Just_Seated == False :

        print("Running PreFlop Section")
        time01 = time.time()
        time02 = time.time() - time1
        while Hand_End_Cheker1 == False and Flop1_Deside == False and time02 < 5 * 60 and Just_Seated == False : 
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; Flop1 = False ; fo = 0
            while Hand_End_Cheker1 == False and Light1 == False and Flop1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    print("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                Flop1 = Flop()
                time2 = time.time() - time1
                    
            if not time2 < 1 * 60 :
                Vital_Signs()

            if Hand_End_Cheker1 == False :

                if Light1 == True and Pre_Flop() == True :
                    if is_there_any_raiser() == True :
                        Decide() # preflop
                    else :
                        Check_Mod = True
                        Screenshot_Error("7.Red should be True here")
                        Decide() # preflop
                        
                if Flop1 == True :            
                    Flop1_Deside = True
                    Read_Flop_Cards() #

        if not time02 < 5 * 60 :
            raise Exception("8.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated != False mishavad")
            Vital_Signs()


# Flop: -------


    if Just_Seated == False :

        print("Running Flop Section")
        time01 = time.time()
        time02 = time.time() - time1
        Red_Flop = 0
        while Hand_End_Cheker1 == False and Turn1_Deside == False and time02 < 5 * 60 and Just_Seated == False : 
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; Turn1 = False ; fo = 0
            while Hand_End_Cheker1 == False and Light1 == False and Turn1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    print("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                Turn1 = Turn()
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                Vital_Signs()
                
            if Hand_End_Cheker1 == False :

                if Light1 == True and Flop() == True :
                    if is_there_any_raiser() == True :
                        Decide() # Flop
                        Red_Flop += 1
                    elif Red_Flop > 0 :
                        Check_Mod = True
                        Screenshot_Error("9.Red should be True here")
                        Decide() # Flop
                    else :
                        Decide() # Flop
                        
                if Turn1 == True :            
                    Turn1_Deside = True
                    Read_Turn_Cards() #        
            
        if not time02 < 5 * 60 :
            raise Exception("10.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated != False mishavad")
            Vital_Signs()    



# Turn: -------

    
    if Just_Seated == False :

        print("Running Turn Section")
        time01 = time.time()
        time02 = time.time() - time1
        Red_Turn = 0
        while Hand_End_Cheker1 == False and River1_Deside == False and time02 < 5 * 60 and Just_Seated == False : 
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; River1 = False ; fo = 0
            while Hand_End_Cheker1 == False and Light1 == False and River1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    print("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                River1 = River()
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                Vital_Signs()
                
            if Hand_End_Cheker1 == False :

                if Light1 == True and Turn() == True :
                    if is_there_any_raiser() == True :
                        Decide() # Turn
                        Red_Turn += 1
                    elif Red_Turn > 0 :
                        Check_Mod = True
                        Screenshot_Error("11.Red should be True here")
                        Decide() # Turn
                    else :
                        Decide() # Turn
                        
                if River1 == True :            
                    River1_Deside = True
                    Read_River_Cards() #        
            
        if not time02 < 5 * 60 :
            raise Exception("12.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated != False mishavad")
            Vital_Signs()            
            

# River: -------


    if Just_Seated == False :

        print("Running River Section")
        time01 = time.time()
        time02 = time.time() - time1
        Red_River = 0
        while Hand_End_Cheker1 == False and time02 < 5 * 60 and Just_Seated == False : 
                
            time1 = time.time()
            time2 = time.time() - time1
            Light1 = False ; fo = 0
            while Hand_End_Cheker1 == False and Light1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    print("Looking for game on screen after 30s of idle...")
                    getpo()
                    fo = 1
                Hand_End_Cheker1 = Hand_End_Cheker()
                Light1 = Light( My_Seat_Number )
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                Vital_Signs()
                
            if Hand_End_Cheker1 == False :

                if Light1 == True and River() == True :
                    if is_there_any_raiser() == True :
                        Decide() # River
                        Red_Turn += 1
                    elif Red_Turn > 0 :
                        Check_Mod = True
                        Screenshot_Error("13.Red should be True here")
                        Decide() # River
                    else :
                        Decide() # River


                               
            
        if not time02 < 5 * 60 :
            raise Exception("14.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated != False mishavad")
            Vital_Signs()            
            


#-------


    if Hand_End_Cheker1 == True and Just_Seated != True :

        Declare_The_Winners()
        print ("-------- Hand Ended --------")
        Check_Mod = False
        
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Hand_End_Cheker1 == True and time02 < 1.5 * 60 :
            Hand_End_Cheker1 = Hand_End_Cheker()
            time2 = time.time() - time1
            if not time2 < 2 * 60 :
                if fo == 0 :
                    Vital_Signs()
                    fo = 1
                time01 = time.time()
                time02 = time.time() - time1                

        if not time02 < 1.5 * 60 :
            raise Exception("15.Game is locked, force to restart")
            


    if Hand_End_Cheker1 == False and Just_Seated != True :    

        Coins_Appeared = False
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Coins_Appeared == False and time02 < 1.5 * 60 :
            Coins_Appeared = Coins_Founded()
            time2 = time.time() - time1
            if not time2 < 8 and fo == 0 :
                getpo()
                fo = 1
            if not time2 < 2 * 60 :
                if fo == 1 :
                    Vital_Signs()
                    fo = 2
                time01 = time.time()
                time02 = time.time() - time1                

        if not time02 < 1.5 * 60 :
            raise Exception("16.Game is locked, force to restart")

        elif Just_Seated != True :
            print ("-------- New Hand Started --------")
            print ("Coins are Founded")
            Determine_Small_Blind_Seat()
            Determine_Big_Blind_Seat()
            Determine_Dealer_Seat()       


            Light1 = False
            Gray1 = True ; fo = 0
            time1 = time.time()
            while (Light1 == False or Gray1 == True) and Just_Seated == True :
                Light1 = Light( My_Seat_Number )
                Gray1 = Gray_Sign_Seat( My_Seat_Number )
                if time.time() - time1 > 1 * 60 :
                    Vital_Signs()























