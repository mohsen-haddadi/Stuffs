from PIL import Image
from pytesseract import image_to_string
import pyautogui , time 
from pyautogui import pixelMatchesColor

Repeated_OCR_Others_Bank_Number = 0 # First line of code
My_Profile_Name = "Canary7"
My_Seat_Number = 1 #None
Lost_Connection_Time = {} #at the first line of the code!!

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

def OCR_My_Name(Seat_Num): #this OCR should be compeleted at future!!!!!!!!!!!!!!!!!!!!!
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
    global My_Seat_Number
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
            Vital_Signs()
        if (Chips == "Min buy in" and My_Seat_Number != None) :
            Hold_Click_Buy_In_Minus_Button()
        if (Chips == "Max buy in" and My_Seat_Number != None):
            Hold_Click_on_Buy_In_Plus_Button()
        if My_Seat_Number != None :
            Click_on_Buy_In_Button()


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
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name
    
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

def Screenshot_Error(Type_of_Error): #Type_of_Error in string
    t = time.time()
    pyautogui.screenshot( 'Error %s %s.png' %(Type_of_Error,t) )

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

def Others_Sleep(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+321, po[1]+403, (10,13,15) ) #Others_Sleep_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+161, po[1]+398, (11,15,17) ) #Others_Sleep_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-94, po[1]+403, (10,13,15) ) #Others_Sleep_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-124, po[1]+163, (10,13,15) ) #Others_Sleep_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+431, po[1]+183, (9,11,13) ) #Others_Sleep_seat_5


po=pyautogui.locateOnScreen('mainpic.png')

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
    global Lost_Connection_Time , My_Seat_Number
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
            print( "OCR_Others_Bank_Number(Error Not Digit!!) Seat %s" %Seat_Num )
            return None
        elif not(x1==False and x2==False) :
            print("OCR_Others_Bank_Number(this can not happen1) Seat %s" %Seat_Num )
            Screenshot_Error( "OCR_Others_Bank_Number(this can not happen1) Seat %s" %Seat_Num  ) #Type_of_Error in string
            return None 
        elif ( y1 and y2 and not( string1.count("$")==1 and string1.find('$')==0 ) ) :
            print("OCR_Others_Bank_Number(A Gift Over Bank Number) Seat %s " %Seat_Num )
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
                    print( "OCR_Others_Bank_Number(Error Not Digit!!2) Seat %s" %Seat_Num )
                    return None
                elif not(x1==False and x2==False) :
                    print("OCR_Others_Bank_Number(this can not happen2) Seat %s" %Seat_Num )
                    Screenshot_Error( "OCR_Others_Bank_Number(this can not happen2) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None 
                elif ( y1 and y2 and not( string1.count("$")==1 and string1.find('$')==0 ) ) :
                    print("OCR_Others_Bank_Number(A Gift Over Seat %s Bank Number2) " %Seat_Num )
                    return None

                else : # if not(y1 or y2) :
                    print("OCR_Others_Bank_Number(Unknown Error) Seat %s" %Seat_Num )
                    Screenshot_Error( "OCR_Others_Bank_Number(Unknown Error) Seat %s" %Seat_Num  ) #Type_of_Error in string
                    return None
            else:
                string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
                print ("Seat's %s Bank: " %Seat_Num , eval( string1 ) )
                Screenshot_Error( "OCR_Others_Bank_Number (Bank True after Vital sign) Seat %s" %Seat_Num  ) #Type_of_Error in string
                return eval( string1 )

    else:
        string1 = Replace_Comma_VoidSpace_Dollar_M_K( string1 )
        return eval( string1 )


def Click_on_Leave_Next_Hand_OK_Button():
    pyautogui.click( po[0]+108, po[1]+342 )

def Buy_In_Button():
    x1 = pixelMatchesColor( po[0]+71, po[1]+448, (26,123,0) ) #Buy_In_Button
    x2 = pixelMatchesColor( po[0]+71, po[1]+448, (32,149,0) ) #Buy_In_Button_Light
    return (x1 or x2)


