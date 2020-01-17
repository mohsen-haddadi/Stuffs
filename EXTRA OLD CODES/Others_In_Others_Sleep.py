import pyautogui
from pyautogui import pixelMatchesColor
from pyautogui import click

def getpo_for_starting(): #when i am watching the game myself, raise the Exeption 
    global po
    
    po=pyautogui.locateOnScreen('mainpic.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic.png')
        if po_new is None:
            Screenshot_Error("Could not find game on screen") #Type_of_Error in string
            raise Exception('Could not find game on screen. Is the game visible?')
        po=( po_new[0]+329 , po_new[1]-258 )


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

getpo_for_starting()




