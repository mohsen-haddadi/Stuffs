import time, os
import numpy as np , cv2
import pyautogui
import match_card

def Coins_Founded():
    globalization()
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
    globalization()
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
    globalization()
    Flop = pixelMatchesColor( po[0]+136, po[1]+218, (237,237,237) ) #Flop
    return Flop 
def Turn():
    globalization()
    Turn = pixelMatchesColor( po[0]+196, po[1]+218, (237,237,237) ) #Turn
    return Turn 
def River():
    globalization()
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
    globalization()
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
    globalization()
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
    globalization()
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
    globalization()
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
    globalization()
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
    globalization()
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
    globalization()
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
    globalization()

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
    globalization()

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
    globalization()

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

