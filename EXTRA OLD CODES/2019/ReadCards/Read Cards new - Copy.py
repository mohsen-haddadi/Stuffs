import pyautogui , time

po=pyautogui.locateOnScreen('mainpic.png')

Cards_names=['A c','2 c','3 c','4 c','5 c','6 c','7 c','8 c','9 c','10 c','J c','Q c','K c',
             'A d','2 d','3 d','4 d','5 d','6 d','7 d','8 d','9 d','10 d','J d','Q d','K d',
             'A h','2 h','3 h','4 h','5 h','6 h','7 h','8 h','9 h','10 h','J h','Q h','K h',
             'A s','2 s','3 s','4 s','5 s','6 s','7 s','8 s','9 s','10 s','J s','Q s','K s']

pyautogui.locateOnScreen('%s_1th Card on Table.png' %'6 d' )

def Read_Flop_Cards():
    global Card_1th , Card_2th , Card_3th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    time0 = time.time()
    for x in Cards_names :
        i= pyautogui.locateOnScreen('%s_1th Card on Table.png' %x )
        if i != None :
            print("1th card is: %s" %x)
            Card_1th = x
            break

    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen('%s_2th Card on Table.png' %x )
        if i != None :
            print("2th card is: %s" %x)
            Card_2th = x
            break



    for x in Cards_names:
        i= pyautogui.locateOnScreen('%s_3th Card on Table.png' %x )
        if i != None :
            print("3th card is: %s" %x)
            Card_3th = x
            break


def Read_Turn_Cards():
    global Card_4th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    time0 = time.time()
    for x in Cards_names:
        i= pyautogui.locateOnScreen('%s_4th Card on Table.png' %x,  region=(po[0]+150, po[1]+215, 20, 40) )
        if i != None :
            print("4th card is: %s" %x)
            Card_4th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names:
            i= pyautogui.locateOnScreen('%s_4th Card on Table.png' %x,  region=(po[0]+150, po[1]+215, 20, 40) )
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
        i= pyautogui.locateOnScreen('%s_5th Card on Table.png' %x,  region=(po[0]+212, po[1]+215, 20, 40) )
        if i != None :
            print("5th card is: %s" %x)
            Card_5th = x
            break
    if i == None :
        Vital_Signs()
        for x in Cards_names:
            i= pyautogui.locateOnScreen('%s_5th Card on Table.png' %x,  region=(po[0]+212, po[1]+215, 20, 40) )
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
            i= pyautogui.locateOnScreen('%s_Seat1 1th Card.png' %x,  region=(po[0]+369, po[1]+391, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat1 1th Card.png' %x,  region=(po[0]+369, po[1]+391, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat1 2th Card.png' %x,  region=(po[0]+388, po[1]+391, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat1 2th Card.png' %x,  region=(po[0]+388, po[1]+391, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat2 1th Card.png' %x,  region=(po[0]+115, po[1]+393, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat2 1th Card.png' %x,  region=(po[0]+115, po[1]+393, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat2 2th Card.png' %x,  region=(po[0]+133, po[1]+393, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat2 2th Card.png' %x,  region=(po[0]+133, po[1]+393, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat3 1th Card.png' %x )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break


        for x in Cards_names:
            i= pyautogui.locateOnScreen('%s_Seat3 2th Card.png' %x )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break



    if My_Seat_Number == 4 :
        for x in Cards_names:
            i= pyautogui.locateOnScreen('%s_Seat4 1th Card.png' %x,  region=(po[0]-171, po[1]+85, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat4 1th Card.png' %x,  region=(po[0]-171, po[1]+85, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %x,  region=(po[0]-152, po[1]+85, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %x,  region=(po[0]-152, po[1]+85, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat5 1th Card.png' %x,  region=(po[0]+399, po[1]+85, 10, 30) )
            if i != None :
                print("My first Card is: %s" %x)
                My_1th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat5 1th Card.png' %x,  region=(po[0]+399, po[1]+85, 10, 30) )
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
            i= pyautogui.locateOnScreen('%s_Seat5 2th Card.png' %x,  region=(po[0]+418, po[1]+85, 10, 30) )
            if i != None :
                print("My second Card is: %s" %x)
                My_2th_Card = x
                break
        if i == None :
            Vital_Signs()
            for x in Cards_names:
                i= pyautogui.locateOnScreen('%s_Seat5 2th Card.png' %x,  region=(po[0]+418, po[1]+85, 10, 30) )
                if i != None :
                    print("My My second Card is: %s" %x)
                    My_2th_Card = x
                    break
            time1 = time.time() - time0
            if (i == None or Flop() or time1 > 20 ) :
                print("My second card on seat 5 is not founded!")
                Screenshot_Error("My second card on seat 5 is not founded!") #Type_of_Error in string
                Check_Mod = True



def Flop():
    Flop= pixelMatchesColor( po[0]+136, po[1]+218, (237,237,237) ) #Flop
    return Flop 
def Turn():
    Turn= pixelMatchesColor( po[0]+196, po[1]+218, (237,237,237) ) #Turn
    return Turn 
def River():
    River= pixelMatchesColor( po[0]+261, po[1]+218, (237,237,237) ) #River
    return River

#------------------------------------------------------------------------------------


########### from def Buttons new

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


def OCR_My_Name_String(Seat_Num):
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

def OCR_My_Name(Seat_Num):
    x1 = Win_Finish_Me(Seat_Num)
    y1 = Gray_Sign_Seat(Seat_Num)
    string = OCR_My_Name_String(Seat_Num)
    x2 = Win_Finish_Me(Seat_Num)
    y2 = Gray_Sign_Seat(Seat_Num)
    if ( x1 or y1 or x2 or y2 ):
        while ( x1 or y1 or x2 or y2 ):
            x1 = Win_Finish_Me(Seat_Num)
            y1 = Gray_Sign_Seat(Seat_Num)
            x2 = Win_Finish_Me(Seat_Num)
            y2 = Gray_Sign_Seat(Seat_Num)
        return OCR_My_Name_String(Seat_Num)
    else :
        return string

#############

def getpo_for_starting(): #when i am watching the game myself, raise the Exeption 
    global po
    
    po=pyautogui.locateOnScreen('mainpic.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic.png')
        if po_new is None:
            Screenshot_Error("Could not find game on screen") #Type_of_Error in string
            raise Exception('Could not find game on screen. Is the game visible?')
        po=( po_new[0]+329 , po_new[1]-258 )


def getpo():
    global po
    
    po=pyautogui.locateOnScreen('mainpic.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic.png')
        if po_new == None:
            return None

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
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5

def Click_on_Exit_Button(): #this should be compeleted at futurefor Sit_In!!!!!!!!!!!!!!!!!!!!!  (maybe should be compeleted, maybe not)
    pyautogui.click( po[0]+378, po[1]+21 )

def Sit_In(Chips): # "Min buy in" or "Max buy in"
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    My_Seat_Number = None
    for i in range(1 ,6 ):
        if Available_Seat(i) == True :
            Click_on_Available_Seat(i)
            My_Seat_Number = i
            break
    if My_Seat_Number == None :
        Click_on_Exit_Button()
    else :
        x1 = time.time()
        time1 = 0
        Buy_In = None
        while ( (time1 < 5) and Buy_In !=True ):
            Buy_In = Buy_In_Button()
            x2 = time.time()
            time1 = x2-x1
        if Buy_In != True :
            Raise_What_is_Problem("Sit_In Buy_In_Button")
        if (Chips == "Min buy in" and My_Seat_Number != None) :
            Hold_Click_Buy_In_Minus_Button()
        if (Chips == "Max buy in" and My_Seat_Number != None):
            Hold_Click_on_Buy_In_Plus_Button()
        if My_Seat_Number != None :
            Click_on_Buy_In_Button()
            Just_Seated = True


def I_am_back_Button():
    x1 = pixelMatchesColor( po[0]+137, po[1]+608, (1,80,165) ) #I_am_back_Button
    x2 = pixelMatchesColor( po[0]+137, po[1]+608, (1,91,188) ) #I_am_back_Button_Light
    return (x1 or x2)

def Click_on_I_am_back_Button():
    pyautogui.click( po[0]+137, po[1]+608 )

def Check_I_am_In_or_Out():
    global My_Seat_Number , My_Profile_Name
    if I_am_back_Button() == True :
        Click_on_I_am_back_Button()
    if OCR_My_Name(My_Seat_Number) == My_Profile_Name :
        return ("In")
    else :
        return ("Out")
        
   
def Vital_Signs(): #if getpo() == None or ...
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
    if Lost_Connection == True :
        x1 = time.time()
        while ( Lost_Connection == True  ):
            Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
        x2 = time.time()
        Lost_Connection_Time[x1]= x2-x1 

    pyautogui.click(0, 720) # click to Exit probable Advertisement

    getpo_for_starting() #if None,it will raise the Exeption 
    if I_am_back_Button() == True :
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

def Cards(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+330, po[1]+331, (154,7,13) ) #Cards_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+74, po[1]+332, (154,7,13) ) #Cards_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-181, po[1]+331, (154,7,13) ) #Cards_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-140, po[1]+212, (154,7,13) ) #Cards_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+359, po[1]+212, (154,7,13) ) #Cards_seat_5  


"""
t0 = time.time()
i=pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %'J h' )
t1 = time.time()
print(t1-t0)
print(i)



t0 = time.time()
i=pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %'J h' , region=(po[0]-200, po[1]+135, 340, 40) )
t1 = time.time()
print(t1-t0)
print(i)



t0 = time.time()
i=pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %'J h' , region=(po[0]-352, po[1]+80, 340, 40) )
t1 = time.time()
print(t1-t0)
print(i)

t0 = time.time()
i=pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %'J h',  region=(po[0]-152, po[1]+85, 10, 30) )
t1 = time.time()
print(t1-t0)
print(i)


"""
t0 = time.time()
i=pyautogui.locateOnScreen('%s_Seat4 2th Card.png' %'Q c' , region=(po[0]-50, po[1]+210, 340, 50) )
t1 = time.time()
print(t1-t0)
print(i)

t0 = time.time()
i=pyautogui.locateOnScreen('%s_4th Card on Table.png' %'Q c',  region=(po[0]+150, po[1]+215, 20, 40) )
t1 = time.time()
print(t1-t0)
print(i)

