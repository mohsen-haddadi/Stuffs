import pyautogui, time, os, pygame , win32gui , win32con , socket , wmi , cv2 , numpy , re , pickle
from PIL import Image
from datetime import datetime
#from pyautogui import pixelMatchesColor
#from pytesseract import image_to_string
from painter import paint
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.ocr.ocr as ocr
import screen_monitoring.read_cards.read_cards as read_cards
import screen_monitoring.click_coordinates.click_coordinates as click_coordinates
import decision_making.decide
import click_button 

if __name__ == '__main__':
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)


def Create_file_directories():
    global file_name , Reports_directory
    load_variables()
    
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

    save_variables()
"""
Using 'if' line at below is a MUST, bescause while importing main file from the other files,
2 diffrent file_name with diffrent times will be created for each file and therefore shoutings from each file will be save in seperated files. 
So i should put file_name variable in load_variables() and save_variables() too.
"""

if __name__ == '__main__': 
    set_all_variables_to_none()
    Create_file_directories()

def shout(String) :
    global file_name
    load_variables()

    text_file_name = os.path.join( "Reports/%s" %file_name , file_name )
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

if __name__ == '__main__':
    shout(paint.rainbow.bold("Hello Kitty"))


pygame.mixer.init() #Check later if i can move this line to first line of sound() function or not.
def sound(string_name) :
    try :
        pygame.mixer.music.load( os.path.join( 'Sounds' , "%s.wav" %string_name ) )
        return pygame.mixer.music.play()
    except :
        pass

# FUNCTIONS_Pixel-Maching ---------------------------------------------------------------------------------------------



def sb_b_d_buttons_are_founded():
    global game_position
    load_variables()

    small_blind_button_founded, big_blind_button_founded, dealer_button_founded = (False, False, False)
    for seat in [1,2,3,4,5]:
        if pm.small_blind_pixel(game_position, seat) == True:
            small_blind_button_founded = True
            break
    for seat in [1,2,3,4,5]:
        if pm.big_blind_pixel(game_position, seat) == True:
            big_blind_button_founded = True
            break
    for seat in [1,2,3,4,5]:
        if pm.dealer_pixel(game_position, seat) == True:
            dealer_button_founded = True
            break
    return small_blind_button_founded and big_blind_button_founded and dealer_button_founded

def declare_the_winners():
    global game_position
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.my_seat_won_pixel(game_position, seat) == True:
            shout(paint.on_light_magenta.bold("I won the game!"))
        if pm.other_seat_won_pixel(game_position, seat) == True :
            shout("Seat %s won the game!" %seat)

def white(game_position, seat):
    # It checks if there is a white color sign in front of a seat,
    # by returning True or False, to find out if a player has call or not

    if pm.player_chips_pixel(game_position, seat):
        return not pm.are_chips_white_or_red_pixel(game_position, seat)
    else :
        return False

def red(game_position, seat):
    # It checks if there is a red color sign in front of a seat,
    # by returning True or False, to find out if a player has bet/raised or not.
    # (In accordance to Google: 'A bet is the first wager of a round.')
    if pm.player_chips_pixel(game_position, seat):
        return pm.are_chips_white_or_red_pixel(game_position, seat)
    else :
        return False

def hand_is_ended():
    game_position
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.my_seat_won_pixel(game_position, seat):
            return True
        if pm.other_seat_won_pixel(game_position, seat):
            return True
    return False

# 2017 :------------------------------

###
def determine_small_blind_seat():
    global game_position, Small_Blind_Seat
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.small_blind_pixel(game_position, seat):
            Small_Blind_Seat = seat
            shout("Seat %s is at Small Blind Seat" %seat)
            break

### 
def determine_big_blind_seat():
    global game_position, Big_Blind_Seat
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.big_blind_pixel(game_position, seat):
            Big_Blind_Seat = seat
            shout("Seat %s is at Big Blind Seat" %seat)
            break

###
def determine_dealer_seat():
    global game_position, Dealer_Seat
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.dealer_pixel(game_position, seat):
            Dealer_Seat = seat
            shout("Seat %s is at Dealer Seat" %seat)
            break


# FUNCTIONS_Pixel-Maching Ended ---------------------------------------------------------------------------------------








# def_Buttons_new: ---------------------------------------------------------------------------------------------------------------


def click_on_available_seat(seat):
    global game_position
    load_variables()
    if seat == 1 :
        pyautogui.click( game_position[0]+362, game_position[1]+408 ) #Seat1
        shout(paint.light_cyan.bold("Available_Seat 1 is clicked"))
    if seat == 2 :
        pyautogui.click( game_position[0]+107, game_position[1]+411 ) #Seat2
        shout(paint.light_cyan.bold("Available_Seat 2 is clicked"))
    if seat == 3 :
        pyautogui.click( game_position[0]-148, game_position[1]+408 ) #Seat3
        shout(paint.light_cyan.bold("Available_Seat 3 is clicked"))
    if seat == 4 :
        pyautogui.click( game_position[0]-178, game_position[1]+103 ) #Seat4
        shout(paint.light_cyan.bold("Available_Seat 4 is clicked"))
    if seat == 5 :
        pyautogui.click( game_position[0]+392, game_position[1]+103 ) #Seat5
        shout(paint.light_cyan.bold("Available_Seat 5 is clicked"))

def click_on_fold_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.fold_button_pixel(game_position) :
        pyautogui.click( game_position[0]+51, game_position[1]+581 )
        shout(paint.light_cyan.bold("Fold_Button is clicked"))
    else :
        fix_game_disruption("Click_on_Fold_Button()")
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and pm.fold_button_pixel(game_position) :
            pyautogui.click( game_position[0]+51, game_position[1]+581 )
            shout(paint.light_cyan.bold("Fold_Button is clicked"))
        set_check_mode_to_true("Click_on_Fold_Button()")

def click_on_check_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.check_button_pixel(game_position) :
        pyautogui.click( game_position[0]+246, game_position[1]+578 )
        shout(paint.light_cyan.bold("Check_Button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("Click_on_Check_Button()")
        time1 = time.time() - time0
        Check_Button1 = pm.check_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and Check_Button1 and time1 <= 10 :
            pyautogui.click( game_position[0]+246, game_position[1]+578 )
            shout(paint.light_cyan.bold("Check_Button is clicked"))
        else :
            set_check_mode_to_true("Click_on_Check_Button()")         

def click_on_call_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.call_button_pixel(game_position) :
        pyautogui.click( game_position[0]+261, game_position[1]+575 )
        shout(paint.light_cyan.bold("Call_Button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("Click_on_Call_Button()")
        time1 = time.time() - time0
        Call_Button1 = pm.call_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and Call_Button1 and time1 <= 10 :
            pyautogui.click( game_position[0]+261, game_position[1]+575 )
            shout(paint.light_cyan.bold("Call_Button is clicked"))
        else :
            set_check_mode_to_true("Click_on_Call_Button()")

def click_on_bet_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.bet_button_pixel(game_position) :
        pyautogui.click( game_position[0]+461, game_position[1]+576 )
        shout(paint.light_cyan.bold("Bet_Button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("Click_on_Bet_Button()")
        time1 = time.time() - time0
        Bet_Button1 = pm.bet_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and Bet_Button1 and time1 <= 10 :
            pyautogui.click( game_position[0]+461, game_position[1]+576 )
            shout(paint.light_cyan.bold("Bet_Button is clicked"))
        else :
            set_check_mode_to_true("Click_on_Bet_Button()")

def click_on_raise_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.raise_button_pixel(game_position) :
        pyautogui.click( game_position[0]+461, game_position[1]+576 )
        shout(paint.light_cyan.bold("Raise_Button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("Click_on_Raise_Button()")
        time1 = time.time() - time0
        Raise_Button1 = pm.raise_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and Raise_Button1 and time1 <= 10 :
            pyautogui.click( game_position[0]+461, game_position[1]+576 )
            shout(paint.light_cyan.bold("Raise_Button is clicked"))
        else :
            set_check_mode_to_true("Click_on_Raise_Button()")

def number_of_clicks_on_plus_button( number): # Number of clicks
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    number = int(number)
    if pm.plus_button_pixel(game_position) :
        for i in range (number):
            pyautogui.click( game_position[0]+246, game_position[1]+648 )
        shout(paint.light_cyan.bold("plus_button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("number_of_clicks_on_plus_button(number)")
        time1 = time.time() - time0
        Plus_Button1 = pm.plus_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and Plus_Button1 and time1 <= 10 :
            for i in range (number):
                pyautogui.click( game_position[0]+246, game_position[1]+648 )
            shout(paint.light_cyan.bold("plus_button is clicked"))
        else :
            set_check_mode_to_true("number_of_clicks_on_plus_button()")

def number_of_click_on_minus_button(number): # Number of clicks
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    number = int(number)
    if pm.minus_button_pixel(game_position) :
        for i in range (number):
            pyautogui.click( game_position[0]-9, game_position[1]+648 )
        shout(paint.light_cyan.bold("minus_button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("number_of_click_on_minus_button(number)")
        time1 = time.time() - time0
        Minus_Button1 = pm.minus_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and Minus_Button1 and time1 <= 10 :
            for i in range (number):
                pyautogui.click( game_position[0]-9, game_position[1]+648 )
            shout(paint.light_cyan.bold("Minus_Button is clicked"))
        else :
            set_check_mode_to_true("Number_of_Click_on_Minus_Button()")

def click_on_all_in_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.all_in_button_pixel(game_position) :
        pyautogui.click( game_position[0]+531, game_position[1]+648 )
        shout(paint.light_cyan.bold("All_In_Button is clicked"))
    else :
        time0 = time.time()
        fix_game_disruption("Click_on_All_In_Button()")
        time1 = time.time() - time0
        All_In_Button1 = pm.all_in_button_pixel(game_position)
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and All_In_Button1 and time1 <= 10 :
            pyautogui.click( game_position[0]+531, game_position[1]+648 )
            shout(paint.light_cyan.bold("All_In_Button is clicked"))
        else :
            set_check_mode_to_true("Click_on_All_In_Button()")


def click_on_exit_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.exit_button_pixel(game_position):
        pyautogui.click( game_position[0]+378, game_position[1]+21 )
        shout(paint.light_cyan.bold("Exit_Button is clicked"))
        Just_Seated = None
    else :
        fix_game_disruption("click_on_exit_button()")
        if pm.exit_button_pixel(game_position):
            pyautogui.click( game_position[0]+378, game_position[1]+21 )
            shout(paint.light_cyan.bold("Exit_Button is clicked"))
            Just_Seated = None
        else : #can't proceed to here
            raise_exception_the_problem("click_on_exit_button")         

def click_on_exit_yes_button():
    global game_position
    load_variables()
    if pm.exit_yes_button_pixel(game_position):
        pyautogui.click( game_position[0]+47, game_position[1]+355 )
        shout(paint.light_cyan.bold("exit_yes_button is clicked"))
    else :
        raise_exception_the_problem("click_on_exit_yes_button")

def click_on_menu_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.menu_button_pixel(game_position):
        pyautogui.click( game_position[0]-399, game_position[1]-66 )
        shout(paint.light_cyan.bold("Menu_Button is clicked"))
    else :
        fix_game_disruption("click_on_menu_button()")
        if pm.exit_button_pixel(game_position):
            pyautogui.click( game_position[0]-399, game_position[1]-66 )
            shout(paint.light_cyan.bold("Menu_Button is clicked"))
        else :
            raise_exception_the_problem("click_on_menu_button")

def click_on_rebuy_menu_button():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.rebuy_menu_button_pixel(game_position):
        pyautogui.click( game_position[0]+513, game_position[1]+14 )
        shout(paint.light_cyan.bold("Rebuy_Menu_Button is clicked"))
    else :
        fix_game_disruption("click_on_rebuy_menu_button()")
        if pm.rebuy_menu_button_pixel(game_position):
            pyautogui.click( game_position[0]+513, game_position[1]+14 )
            shout(paint.light_cyan.bold("Rebuy_Menu_Button is clicked"))
        else :
            raise_exception_the_problem("click_on_rebuy_menu_button")

def click_on_leave_next_hand_ok_button():
    global game_position
    load_variables()
    if pm.leave_next_hand_ok_button_pixel(game_position) :
        pyautogui.click( game_position[0]+108, game_position[1]+342 )
        shout(paint.light_cyan.bold("Leave_Next_Hand_OK_Button is clicked"))
    else :
        raise_exception_the_problem("click_on_leave_next_hand_ok_button")

def click_on_buy_in_button():
    global game_position
    load_variables()
    if pm.buy_in_button_pixel(game_position) :
        pyautogui.click( game_position[0]+71, game_position[1]+448 )
        shout(paint.light_cyan.bold("Buy_In_Button is clicked"))
    else :
        raise_exception_the_problem("click_on_buy_in_button")   

def hold_click_on_buy_in_plus_button(): 
    # It holds left click for 10s
    global game_position
    load_variables()
    if pm.buy_in_plus_button_pixel(game_position) :
        pyautogui.mouseDown(x=game_position[0]+264, y=game_position[1]+236)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if pm.buy_in_plus_button_pixel(game_position) :
            pyautogui.mouseDown(x=game_position[0]+264, y=game_position[1]+236)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            raise_exception_the_problem("hold_click_on_buy_in_plus_button") 

def hold_click_buy_in_minus_button(): #hold left click for 10s
    global game_position
    load_variables()
    if pm.buy_in_minus_button_pixel(game_position):
        pyautogui.mouseDown(x=game_position[0]-46, y=game_position[1]+244)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if pm.buy_in_minus_button_pixel(game_position):
            pyautogui.mouseDown(x=game_position[0]-46, y=game_position[1]+244)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            raise_exception_the_problem("Hold_Click_Buy_In_Minus_Button")

def click_on_re_buy_button():
    global game_position
    load_variables()
    if pm.re_buy_button_pixel(game_position):
        pyautogui.click( game_position[0]+91, game_position[1]+430 )
        shout(paint.light_cyan.bold("Re_Buy_Button is clicked"))
    else :
        raise_exception_the_problem("click_on_re_buy_button")

def hold_click_on_re_buy_plus_button(): 
    # It holds left click for 10s on re_buy_plus_button
    global game_position
    load_variables()
    if pm.re_buy_plus_button_pixel(game_position) :
        pyautogui.mouseDown(x=game_position[0]+264, y=game_position[1]+254)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if pm.re_buy_plus_button_pixel(game_position) :
            pyautogui.mouseDown(x=game_position[0]+264, y=game_position[1]+254)
            time.sleep(10)
            pyautogui.mouseUp()        
        else :
            raise_exception_the_problem("hold_click_on_re_buy_plus_button")

def hold_click_on_re_buy_minus_button():
    # It holds left click for 10s on re_buy_minus_button
    global game_position 
    load_variables()
    if pm.re_buy_minus_button_pixel(game_position) :
        pyautogui.mouseDown(x=game_position[0]-46, y=game_position[1]+261)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if pm.re_buy_minus_button_pixel(game_position) :
            pyautogui.mouseDown(x=game_position[0]-46, y=game_position[1]+261)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            raise_exception_the_problem("hold_click_on_re_buy_minus_button")

def click_on_i_am_back_button(): 
    global game_position, Check_Mod
    load_variables()
    pyautogui.click( game_position[0]+137, game_position[1]+608 )
    shout(paint.yellow.bold("I_am_back_Button is clicked"))
    set_check_mode_to_true("click_on_i_am_back_button()")

def click_on_reconnect_button():
    global game_position
    load_variables()

    shout('looking for reconnect button')
    x1=pyautogui.locateCenterOnScreen('reconnect button.png')
    if x1 != None :
        pyautogui.click(x1)
        shout(paint.yellow.bold('reconnect button founded and clicked'))
        time.sleep(5)
        if pm.i_am_back_button_pixel(game_position) == True :
            click_on_i_am_back_button()
        return x1
    
    x2=pyautogui.locateCenterOnScreen('reconnect button light.png')
    if x2 != None :
        pyautogui.click(x2)
        shout(paint.yellow.bold('reconnect button founded and clicked'))
        time.sleep(5)
        if pm.i_am_back_button_pixel(game_position) == True :
            click_on_i_am_back_button()
        return x1

    else :
        return None

# 2017: -----------------------------

def fold():
    global game_position, Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return click_on_fold_button()

def check():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return click_on_check_button()

def call():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return click_on_call_button()

def raising_old( Blinds ): # tested ok, not usable, new Raise() function work for it
    """ 
    Blinds is the amount of money like in ocr; not the number of blinds
    if Blinds == Raise_base + Raise_add (or less): won't click on plus button 
    raising_old() algorithm can be use and act for betting too. but bet() function can not be use for raising.
    """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , Did_i_raised_at , My_last_raise , BLIND
    load_variables()

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
        Bets.append(0) #That's why raising_old() algorithm can be use and act for betting too.

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

    number_of_clicks_on_plus_button( ( Blinds - (Raise_base + Raise_add) ) // BLIND )
    return  click_on_raise_button()

def bet( Blinds ): # not usable since there is raising() function act for both raising and betting for all stages
    """ 
    Blinds is the amount of money like in ocr; not the number of blinds
    if Blinds == BLIND (or less): won't click on plus button
    There can not be betting option on Pre_Flop stage.
    make sure is_there_any_raiser_now_cache is True, otherwise My_last_raise will be miscalculated. or use raising_old function easily instead.
    """
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Flop1_Deside , Turn1_Deside , River1_Deside , Did_i_raised_at , My_last_raise , BLIND
    load_variables()

    # There can not be betting option on Pre_Flop stage
    if Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    Did_i_raised_at[stage] = True
    My_last_raise[stage] = Blinds

    number_of_clicks_on_plus_button( ( Blinds // BLIND ) - 1 )
    return click_on_bet_button()

def all_in_old( Minus_Blinds = 0 ): #not completed on Did_i_raised_at and My_last_raise. i won't use this fuction anymore
    """ if 0 : all_in everything """
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    if pm.all_in_button_pixel(game_position) == False and pm.call_button_pixel(game_position) == True and pm.bet_button_pixel(game_position) == False and pm.raise_button_pixel(game_position) == False :
        return click_on_call_button()
    
    if Minus_Blinds == 0 :
        click_on_all_in_button()
        if pm.bet_button_pixel(game_position) == True :
            return click_on_bet_button()
        else :
            return click_on_raise_button()
    else :
        click_on_all_in_button()
        number_of_click_on_minus_button( Minus_Blinds )
        if pm.bet_button_pixel(game_position) == True :
            return click_on_bet_button()
        else :
            return click_on_raise_button()

def all_in():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    if pm.all_in_button_pixel(game_position) == False and pm.call_button_pixel(game_position) == True and pm.bet_button_pixel(game_position) == False and pm.raise_button_pixel(game_position) == False :
        return click_on_call_button()
    
    click_on_all_in_button()
    if pm.bet_button_pixel(game_position) == True :
        return click_on_bet_button()
    else :
        return click_on_raise_button()

def raising( Blinds ):
    """ 
    Act for both raising and betting 
    Blinds is the amount of money like in ocr; not the number of blinds
    if Blinds == BLIND (or less): won't click on plus button
    """
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , Did_i_raised_at , My_last_raise , BLIND
    load_variables()

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
        Bets.append(0) #That's why raising() algorithm can be use and act for betting too.

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

    number_of_clicks_on_plus_button( ( Blinds - (Raise_base + Raise_add) ) // BLIND )
    #Till here as same as raising()

    if pm.raise_button_pixel(game_position) :
        click_on_raise_button()
    elif pm.bet_button_pixel(game_position) :
        click_on_bet_button()
    else :

        fix_game_disruption("RAISE() Button, No Raise nor Bet Button founded")
        if pm.raise_button_pixel(game_position) :
            click_on_raise_button()
        elif pm.bet_button_pixel(game_position) :
            click_on_bet_button()  
        else :
            set_check_mode_to_true("No Raise nor Bet Button founded")

def check_fold():
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if pm.check_button_pixel(game_position) :
        click_on_check_button()
    elif pm.fold_button_pixel(game_position) :
        click_on_fold_button()
    else :

        set_check_mode_to_true("check_fold()(It's already True)") #It's already True
        fix_game_disruption("check_fold()")
        if pm.check_button_pixel(game_position) :
            click_on_check_button()
        elif pm.fold_button_pixel(game_position) :
            click_on_fold_button()        




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
    load_variables()

    region_table_card = { 1:(game_position[0]-38, game_position[1]+215, 20, 40) , 2:(game_position[0]+25, game_position[1]+215, 20, 40) , 3:(game_position[0]+87, game_position[1]+215, 20, 40) , 4:(game_position[0]+150, game_position[1]+215, 20, 40) , 5:(game_position[0]+212, game_position[1]+215, 20, 40) }

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
    global game_position, Card_1th , Card_2th , Card_3th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()

    Card_1th = Download_Table_Cards(1)

    if Card_1th == None :
        fix_game_disruption("Read_Flop_Cards():Card_1th")

        Card_1th = Download_Table_Cards(1)

        if Card_1th == None or not pm.flop_pixel(game_position) or pm.turn_pixel(game_position) :
            set_check_mode_to_true("Read_Flop_Cards():Card_1th")
            shout("Reading Flop cards is stoped")
            return None # to stop fix_game_disruption for 2 and 3 cards


    Card_2th = Download_Table_Cards(2)

    if Card_2th == None :
        fix_game_disruption("Read_Flop_Cards():Card_2th")

        Card_2th = Download_Table_Cards(2)

        if Card_2th == None or not pm.flop_pixel(game_position) or pm.turn_pixel(game_position) :
            set_check_mode_to_true("Read_Flop_Cards():Card_2th")
            shout("Reading Flop cards is stoped")
            return None # to stop fix_game_disruption for 3 card   


    Card_3th = Download_Table_Cards(3)

    time_str = "Reading Flop cards took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)

    if Card_3th == None :
        fix_game_disruption("Read_Flop_Cards():Card_3th")

        Card_3th = Download_Table_Cards(3)

        if Card_3th == None or not pm.flop_pixel(game_position) or pm.turn_pixel(game_position):
            set_check_mode_to_true("Read_Flop_Cards():Card_3th")
        

def Read_Turn_Cards(): 
    global game_position, Card_4th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()
   
    Card_4th = Download_Table_Cards(4)

    time_str = "Reading Turn card took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)

    if Card_4th == None :
        fix_game_disruption("Read_Flop_Cards():Card_4th")

        Card_4th = Download_Table_Cards(4)

        if Card_4th == None or not pm.turn_pixel(game_position) or pm.river_pixel(game_position) :
            set_check_mode_to_true("Read_Flop_Cards():Card_4th")


def Read_River_Cards(): 
    global game_position, Card_5th , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated

    t0 = time.time()
    
    Card_5th = Download_Table_Cards(5)
    
    time_str = "Reading River card took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)
    
    if Card_5th == None :
        fix_game_disruption("Read_Flop_Cards():Card_5th")

        Card_5th = Download_Table_Cards(5)

        if Card_5th == None or not pm.river_pixel(game_position):
            set_check_mode_to_true("Read_Flop_Cards():Card_5th")






def Download_My_Cards( My_Seat , Card_xth ) : 
    global Cards_names
    load_variables()

    region_1th_card = { 1:(game_position[0]+369, game_position[1]+391, 10, 30) , 2:(game_position[0]+115, game_position[1]+393, 10, 30) , 3:(game_position[0]-140, game_position[1]+390, 10, 30) , 4:(game_position[0]-171, game_position[1]+85, 10, 30) , 5:(game_position[0]+399, game_position[1]+85, 10, 30) }
    region_2th_card = { 1:(game_position[0]+388, game_position[1]+391, 10, 30) , 2:(game_position[0]+133, game_position[1]+393, 10, 30) , 3:(game_position[0]-122, game_position[1]+390, 10, 30) , 4:(game_position[0]-152, game_position[1]+85, 10, 30) , 5:(game_position[0]+418, game_position[1]+85, 10, 30) }

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




def read_my_cards(game_position, my_seat): 
    global game_position, My_1th_Card , My_2th_Card  , Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    t0 = time.time()
    
    My_1th_Card = Download_My_Cards(My_Seat_Number, 1)

    if My_1th_Card == None :
        fix_game_disruption("Read_My_Cards():My_1th_Card")

        My_1th_Card = Download_My_Cards(My_Seat_Number, 1)

        if My_1th_Card == None or pm.flop_pixel(game_position) :
            set_check_mode_to_true("Read_My_Cards():My_1th_Card")
            shout("Reading my 2th card is stoped")
            return None # to stop fix_game_disruption for my 2th card



    My_2th_Card = Download_My_Cards(My_Seat_Number, 2)
    time_str = "Reading my cards took:%s" %(time.time()-t0)
    time_str = time_str[:-15]
    shout(time_str)
    if My_2th_Card == None :
        fix_game_disruption("Read_My_Cards():My_2th_Card")

        My_2th_Card = Download_My_Cards(My_Seat_Number, 2)

        if My_2th_Card == None or pm.flop_pixel(game_position) :
            set_check_mode_to_true("Read_My_Cards():My_2th_Card")






# Read Cards Ended ---------------------------------------------------------------------------------------------------------------






# OCR Bet Number Positions new 2016: ---------------------------------------------------------------------------------------------
def replace_letters_comma_space_m_k(ocr_string):
    string = ocr_string
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("M","*1000000")
    string = string.replace("K","*1000")
    return string

def ocr_bet(game_position, seat):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod , Last_White_cache , Last_Red_cache
    load_variables()

    x1 = Last_White_cache[seat]
    y1 = Last_Red_cache[seat]
    string1 = ocr.ocr_bet_to_string(game_position,  seat)
    shout("string of bet OCR on seat%s is: %s" %(seat, string1) )
    x2 = white(seat)
    y2 = red(seat)
    string2 = replace_letters_comma_space_m_k(string1)
    string2 = string2.replace("*","")
    if not ( string2.isdigit() and (x1 or y1) and (x2 or y2) ) :
        if not ( (x1 or y1) and (x2 or y2) ) :
            set_check_mode_to_true("OCR Bet is None")            
            screenshot_error( "Easy_OCR_Bet_Number(This case can not happen1) Seat %s" %seat  ) #Type_of_Error in string
            fix_game_disruption("Easy_OCR_Bet_Number(%s)" %seat)
            return None
        else :
            fix_game_disruption("Easy_OCR_Bet_Number(%s)" %seat)
            x1 = white(seat)
            y1 = red(seat)
            string1 = ocr.ocr_bet_to_string(game_position, seat)
            shout("string of bet OCR on seat%s is: %s" %(seat, string1) )
            x2 = white(seat)
            y2 = red(seat)
            string2 = replace_letters_comma_space_m_k( string1 )
            string2 = string2.replace("*","")
            if not ( string2.isdigit() and (x1 or y1) and (x2 or y2) ) :
                if not ( (x1 or y1) and (x2 or y2) ) :
                    set_check_mode_to_true("OCR Bet is None") 
                    screenshot_error( "Easy_OCR_Bet_Number(This case can not happen2) Seat %s" %seat  ) #Type_of_Error in string
                    fix_game_disruption("Easy_OCR_Bet_Number(%s)" %seat)
                    return None
                else :
                    set_check_mode_to_true("OCR Bet is None") 
                    screenshot_error( "Easy_OCR_Bet_Number Seat(Not Digit!!) %s" %seat  ) #Type_of_Error in string
                    return None
            else :
                string1 = replace_letters_comma_space_m_k( string1 )
                return eval( string1 )
    
    else :
        string1 = replace_letters_comma_space_m_k( string1 )
        return eval( string1 )

def ocr_other_players_bank(game_position, seat):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod

    string1 = ocr.ocr_other_players_bank_to_string(game_position, seat)
    shout("string of other players bank OCR on seat%s is: %s" %(seat, string1) )

    string2 = replace_letters_comma_space_m_k(string1)
    string2 = string2.replace("*","")
    if not( string2.isdigit() ) :

        shout("Easy_OCR_Others_Bank_Number(A Gift Over Bank Number) Seat %s " %seat )
        return None

    else:
        string1 = replace_letters_comma_space_m_k( string1 )
        return eval( string1 )

def ocr_my_bank(game_position, seat):
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    load_variables()

    x1 = pm.my_seat_won_pixel(game_position, seat)
    string1 = ocr.ocr_my_bank_to_string(game_position, seat)
    shout("string of my bank OCR on seat%s is: %s" %(seat, string1) )
    x2 = pm.my_seat_won_pixel(game_position, seat)
    string2 = replace_letters_comma_space_m_k( string1 )
    string2 = string2.replace("*","")
    if not( string2.isdigit() and x1==False and x2==False ) :
        if not(x1==False and x2==False) :
            screenshot_error("OCR_My_Bank_Number(This case can not happen 1 ! My Bank can't be read, Becuase i'm in winning light) Seat %s" %seat) #Type_of_Error in string
            return None 
        if ( x1==False and x2==False ) :
            
            fix_game_disruption("OCR_My_Bank_Number(seat)")
            seat = My_Seat_Number
            x1 = pm.my_seat_won_pixel(game_position, seat)
            string1 = ocr.ocr_my_bank_to_string(game_position, seat)
            shout("string of my bank OCR on seat%s is: %s" %(seat, string1) )
            x2 = pm.my_seat_won_pixel(game_position, seat)
            string2 = replace_letters_comma_space_m_k( string1 )
            string2 = string2.replace("*","")
            if not( string2.isdigit() and x1==False and x2==False ) :
                if not(x1==False and x2==False) :
                    screenshot_error("OCR_My_Bank_Number(This case can not happen 2 ! My Bank can't be read, Becuase i'm in winning light) Seat %s" %seat) #Type_of_Error in string
                    return None 
                elif ( x1==False and x2==False ) :
                    screenshot_error( "OCR_My_Bank_Number(Error Not Digit!!2) Seat %s" %seat  ) #Type_of_Error in string
                    return None
                else :
                    screenshot_error( "OCR_My_Bank_Number(Unknown Error) Seat %s" %seat  ) #Type_of_Error in string
                    return None

            else:
                string1 = replace_letters_comma_space_m_k( string1 )
                return eval( string1 )

    else:
        string1 = replace_letters_comma_space_m_k( string1 )
        return eval( string1 )

def ocr_other_names(game_position, seat):
    x1 = pm.other_seat_won_pixel(game_position, seat)
    y1 = pm.notification_banner_pixel(game_position, seat)
    if x1 or y1 :
        return None
    else :
        string = ocr.ocr_other_names_to_string(game_position, seat)
        shout("string of other names OCR on seat%s is: %s" %(seat, string) )
        return string

def ocr_my_name(game_position, seat):

    if pm.my_seat_won_pixel(game_position, seat):
        return True
    if pm.notification_banner_pixel(game_position, seat):
        return None
    string = ocr.ocr_my_name_to_string(game_position, seat)
    shout("string of my bank OCR on seat%s is: %s" %(seat, string) )
    return string




# OCR Others Name Positions 2016 Ended -------------------------------------------------------------------------------------------





# fix_game_disruption: -------------------------------------------------------------------------------------------------------------------




def find_game_reference_point_for_starting(): #when i am watching the game myself, raise the Exeption 
    global game_position
    load_variables()

    shout(paint.yellow.bold("Looking for game on screen..."))
    game_position = pyautogui.locateOnScreen('mainpic celeb.png')
    if game_position == None:
        game_position_new = pyautogui.locateOnScreen('Alternative main pic celeb.png')
        if game_position_new is None:
            screenshot_error("Could not find game on screen") #Type_of_Error in string
            raise Exception('Could not find game on screen. Is the game visible?')
        game_position = ( game_position_new[0]+328 , game_position_new[1]-245 )
    if game_position != None :
        game_position = (int(game_position[0]),int(game_position[1]))
    save_variables()

def find_game_reference_point():
    global game_position
    load_variables()

    game_position_old = game_position
    game_position = None ; fo = 0
    while game_position == None and fo <= 2 :
        fo += 1
        game_position = pyautogui.locateOnScreen('mainpic celeb.png')
        if game_position == None:
            game_position_new = pyautogui.locateOnScreen('Alternative main pic celeb.png')
            if game_position_new == None and fo == 2 :
                shout(paint.yellow.bold("Could not find game on screen,program will use old position"))
                screenshot_error("Could not find game on screen, Program will use former position")
                game_position = game_position_old # vital signs --> find_game_reference_point_for_starting() will compensate
            elif game_position_new != None :
                game_position_new = ( game_position_new[0]+328 , game_position_new[1]-245 )
        if game_position == None and fo == 1 :
            shout(paint.yellow.bold("Adjust the game screen! Researching will be started again in 10s...."))
            time.sleep(10)
    if game_position != None :
        game_position = (int(game_position[0]),int(game_position[1]))
    save_variables()

#def ocr(x,y,h,w):


#def ocr_my_name(Seat_Num):

#
#def pm.i_am_seated_pixel(game_position, Number):


#
#def pm.available_seat_pixel(game_position, Number):


#def click_on_available_seat(seat):

#def click_on_exit_button(): 

def sit_in(chips): # "Min buy in" or "Max buy in"
    global game_position, My_Seat_Number , Just_Seated
    load_variables()

    shout(paint.yellow.bold("Searching for a seat to sit in"))
    My_Seat_Number = None
    for i in range(1 ,6 ):
        if pm.available_seat_pixel(game_position, i) == True :
            click_on_available_seat(i)
            My_Seat_Number = i
            Just_Seated = True
            shout(paint.yellow.bold("Sit_In() --> Just_Seated is True."))
            break
    if My_Seat_Number == None :
        click_on_exit_button()
        
        raise Exception("Sit_In(chips):This can not happen IN FUTURE becuase main menu automation is built")
    else :
        x1 = time.time()
        time1 = 0
        Buy_In = None 
        while ( (time1 < 5) and Buy_In !=True ):
            Buy_In = pm.buy_in_button_pixel(game_position)
            x2 = time.time()
            time1 = x2-x1
        if Buy_In != True :
            fix_game_disruption("Sit_In(chips):Buy_In != True")
        if (chips == "Min buy in" and My_Seat_Number != None) :
            hold_click_buy_in_minus_button()
        if (chips == "Max buy in" and My_Seat_Number != None):
            hold_click_on_buy_in_plus_button()
        if My_Seat_Number != None :
            click_on_buy_in_button()
            screenshot_error("Rebuyed")
#
#def pm.i_am_back_button_pixel(game_position):

#def click_on_i_am_back_button(): 

#def click_on_reconnect_button():


def is_internet_disconnected():
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


def check_i_am_in_or_out():
    global game_position, My_Seat_Number , My_Profile_Name , Check_Mod
    load_variables()

    if pm.i_am_back_button_pixel(game_position) == True :
        click_on_i_am_back_button()
    if ocr_my_name(My_Seat_Number) == My_Profile_Name or ocr_my_name(My_Seat_Number) == True :
        shout(paint.yellow.bold("I am In"))
        return ("In")

    for i in range(1,6):
        if pm.i_am_seated_pixel(game_position, i) :
            if is_internet_disconnected() == False and click_on_reconnect_button() == None :
                if My_Seat_Number == i :
                    shout("I am In not by OCR")
                    return ("In")
                else :
                    My_Seat_Number = i
                    shout('I AM IN,BUT MY SEAT IS MANUALLY CHANGED TO: %s' %My_Seat_Number)
                    set_check_mode_to_true("My seat is manually changed!")
                    return ("In")
                
    shout(paint.yellow.bold("I am Out"))
    return ("Out")

def fix_game_disruption(String = None): #if find_game_reference_point() == None or ...
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated , Check_Mod
    load_variables()

    shout(paint.yellow.bold( 7*"-" ))
    if String == None :
        shout(paint.yellow.bold("fix_game_disruption() is running...."))
    elif type(String) == str :
        shout(paint.yellow.bold("fix_game_disruption() <-- %s is running...." %String))

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

    if is_internet_disconnected() :
        shout('Internet is Disconnected, waiting to reconect...')
        while is_internet_disconnected() :
            continue
        shout('Internet is Connected Back!')
        time.sleep(15)
        if click_on_reconnect_button() == None :
            screenshot_error('No reconnect button founded')

    pyautogui.click(0, 720) # click to Exit probable Advertisement
    shout(paint.yellow.bold("Position (0,720) is clicked"))
    pyautogui.press('esc')
    
    game_position = pyautogui.locateOnScreen('mainpic celeb.png')
    if game_position == None:
        game_position_new =pyautogui.locateOnScreen('Alternative main pic celeb.png')    
    if game_position != None :
        game_position = (int(game_position[0]),int(game_position[1]))
    else:
        for process in wmi.WMI().Win32_Process ():
            if process.Name == 'SystemSettings.exe' :
                shout("SystemSettings Update is on desktop")
                shout("closing Windows Update program")
                screenshot_error('right before closing windows update program')
                pyautogui.click(1570, 10) 
                break        

    if game_position == None :
        find_game_reference_point_for_starting() #if None,it will raise the Exeption
    if game_position != None :
        shout(paint.yellow.bold("Game region refounded after fix_game_disruption()"))
    
    if pm.i_am_back_button_pixel(game_position) == True :
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) == True :
            Check_Mod = True
            shout(paint.yellow.bold("After fix_game_disruption() --> Check_Mod is True."))
        else :
            Just_Seated = True
            shout(paint.on_yellow.bold("After fix_game_disruption() --> Just_Seated is True."))
        click_on_i_am_back_button()

    if check_i_am_in_or_out() == "Out":
        sit_in("Min buy in")

    shout(paint.yellow.bold( 7*"-" ))
    save_variables()

#if (buttoms are still not visible after vital signs).... : #My pixel matching were wrong somewhere
#    t = time.time()
#    pyautogui.screenshot( 'Error %s.png' %t )
#    raise Exception('what was the probelm on %s?' %t ) 
        
def screenshot_error(type_of_error): #type_of_error in string
    global Reports_directory
    load_variables()
    t = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
    t = t[:-4]
    shout(paint.on_light_blue.bold("Screenshot Error: %s" %type_of_error))
    pyautogui.screenshot( '%s/Error %s %s.png' %(Reports_directory, t, type_of_error) )

def raise_exception_the_problem(string):
    screenshot_error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')


# fix_game_disruption Ended --------------------------------------------------------------------------------------------------------------

### Read_Bets & dinctionaries & Reset var funcs: ****************************************************************************************************************************


def read_and_save_players_banks_and_names() :
    global game_position, Players_name_dic , Players_bank_dic
    load_variables()

    for Seat in range(1,6):
        if pm.other_player_seated_pixel(game_position, Seat) == True :
            Players_bank_dic[Seat] = ocr_other_players_bank(game_position, Seat)
            Players_name_dic[Seat] = ocr_other_names(Seat)
            if red(Seat) :
                Players_bank_dic[Seat] = None
    shout(paint.on_light_red.bold("Players Bank dictionary is: %s" %Players_bank_dic ))
    shout(paint.on_light_red.bold("Players Name dictionary is: %s" %Players_name_dic ))

def reset_table_information() : # Round_Pre_Flop ,...,Round_River & Pre_Flop1_Deside ,...,River1_Deside dar loope while True baresi va be in func baraye reset shodan enteghal dade shavand
    global Players_name_dic , Players_bank_dic ,\
           Cards_cache , White_cache , Red_cache , Bet_cache ,\
           Last_Cards_cache , Last_White_cache , Last_Red_cache , Last_Bet_cache,\
           Did_i_raised_at , My_last_raise , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River
    load_variables()

    shout("Reseting table information")
    for Seat in range(1,6):
        Players_name_dic[Seat] = None
        Players_bank_dic[Seat] = None
    Cards_cache = {} ; White_cache = {}  ; Red_cache = {}  ; Bet_cache = {}
    Last_Cards_cache = {} ; Last_White_cache = {}  ; Last_Red_cache = {}  ; Last_Bet_cache = {}
    Did_i_raised_at = {"Pre_Flop": False , "Flop": False , "Turn": False , "River": False } ; My_last_raise = {} # make sure while starting the code Did_i_raised_at is defined by reset_table_information() before first deciding; otherwise did_i_raise_sofar() at supporting funcs file will error
    Round_Pre_Flop = 0; Round_Flop = 0 ; Round_Turn = 0 ; Round_River = 0 #(2018) Later make sure if all rounds are starting from 0 in main While True loop (Round_... = 0 should be implemented in read_and_save_bets() for all stages so for example Bet_cache dictionary surely will "have Round_... 0") #for testing i have put a shout(Bet_cache) at the end of read_and_save_bets() function 
    
    
def set_check_mode_to_true(string = None) :
    global Check_Mod
    load_variables()

    Check_Mod = True
    if string == None :
        shout(paint.on_yellow.bold("Check_Mod is On"))
    elif type(string) == str :
        shout(paint.on_yellow.bold("Check_Mod is On: %s" %string))
    save_variables()

def reset_check_mode_to_false() :
    global Check_Mod
    load_variables()

    if Check_Mod == True :
        shout("Check_Mod is reset to False")
        Check_Mod = False
    save_variables()


def read_and_save_bets() :
    global game_position, Cards_cache , White_cache , Red_cache , Bet_cache ,\
           Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
           Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
           Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside
    load_variables()

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
            Cards_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = pm.player_cards_pixel(game_position, Seat)
            White_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = white(Seat)
            Red_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]
            Last_White_cache[Seat] = White_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]
            Last_Red_cache[Seat] = Red_cache["Pre_Flop %s" %Round_Pre_Flop][Seat]

            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["Pre_Flop %s" %Round_Pre_Flop][Seat] = ocr_bet(Seat)
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
            Cards_cache["Flop %s" %Round_Flop][Seat] = pm.player_cards_pixel(game_position, Seat)
            White_cache["Flop %s" %Round_Flop][Seat] = white(Seat)
            Red_cache["Flop %s" %Round_Flop][Seat] = red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["Flop %s" %Round_Flop][Seat]
            Last_White_cache[Seat] = White_cache["Flop %s" %Round_Flop][Seat]
            Last_Red_cache[Seat] = Red_cache["Flop %s" %Round_Flop][Seat]

            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["Flop %s" %Round_Flop][Seat] = ocr_bet(Seat)
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
            Cards_cache["Turn %s" %Round_Turn][Seat] = pm.player_cards_pixel(game_position, Seat)
            White_cache["Turn %s" %Round_Turn][Seat] = white(Seat)
            Red_cache["Turn %s" %Round_Turn][Seat] = red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["Turn %s" %Round_Turn][Seat]
            Last_White_cache[Seat] = White_cache["Turn %s" %Round_Turn][Seat]
            Last_Red_cache[Seat] = Red_cache["Turn %s" %Round_Turn][Seat]
            
            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["Turn %s" %Round_Turn][Seat] = ocr_bet(Seat)
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
            Cards_cache["River %s" %Round_River][Seat] = pm.player_cards_pixel(game_position, Seat)
            White_cache["River %s" %Round_River][Seat] = white(Seat)
            Red_cache["River %s" %Round_River][Seat] = red(Seat)
            Last_Cards_cache[Seat] = Cards_cache["River %s" %Round_River][Seat]
            Last_White_cache[Seat] = White_cache["River %s" %Round_River][Seat]
            Last_Red_cache[Seat] = Red_cache["River %s" %Round_River][Seat]

            if Last_White_cache[Seat] == True or Last_Red_cache[Seat] == True :
                Bet_cache["River %s" %Round_River][Seat] = ocr_bet(Seat)
                if Last_White_cache[Seat] == True : 
                    shout(paint.light_green.bold("Seat%s Call: $%s" %(Seat,Bet_cache["River %s" %Round_River][Seat])))
                elif Last_Red_cache[Seat] == True :
                    shout(paint.light_green.bold("Seat%s Raise: $%s" %(Seat,Bet_cache["River %s" %Round_River][Seat])))
            else :
                Bet_cache["River %s" %Round_River][Seat] = None
            Last_Bet_cache[Seat] = Bet_cache["River %s" %Round_River][Seat]

    shout("shouting from read_and_save_bets(), Bet_cache is: %s"%Bet_cache) #(2018) delete this later. just for testing if rounds are started from 0, esp at preflop stage
    save_variables()


### Read_Bets & dinctionaries & Reset var funcs Ended ***********************************************************************************************************************
            
def play_sound() :
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside  , My_1th_Card , My_2th_Card
    load_variables()

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

def load_variables():
    """ variables order is important while loading """
    global game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat = pickle.load( open( "variables.p", "rb" ) )

def save_variables() :
    """
    functions i used save_variables() at: 1.click_decision() 2.fix_game_disruption() (containting funcs are not used anywhere else, so variables will overlap) 
    3.Check_Mod_On() 4.getpo() 5.getpo_for_starting() 6.Create_file_directories()
    Pickling at click_decision() will support Pickling variables at funcs like Read pm.player_cards_pixel(game_position, ), Determind small blind(), and.... because click_decision() is run after them.

    Where ever i use save_variables() at the end of a function i should Implement load_variables() at the first line of that function.
    To Pickle real updated variables.
    Becuase by running main file functions from the other files, the variables will update for that file but will not update for mian file. 
    like Check_Mod variable in fix_game_disruption() run from Buttons which is run from decide file.
    click_decision() should not use load_variables() because it's running at main file and it is a gate way. some varibiales may have changed in main while True.

    At gate way lines to the other files use save_variables() before and load_variables() after them. 
    The only gate way line is currently in click_decision() function now. By seperating read cards files, I can expand gate ways to lines like read pm.player_cards_pixel(game_position, ) 

    delete variables.p or set all variables to None at the beggining. (Done)
    By running main file if i have not assigned varibales from before, it will error. 
    By implementing load_variables() I can delete all global lines from supporting and... funcitons. 
    But I keep them to see the varibales I've used for that functions. 
    """
    global game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    pickle.dump( [game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat], open( "variables.p", "wb" ) )

def click_decision():

    decision = decision_making.decide.decide()
    if decision[0] == "check" :
        click_button.check()
    elif decision[0] == "call" :
        click_button.call()
    elif decision[0] == "fold" :
        click_button.fold()
    elif decision[0] == "raise" :
        click_button.raising(decision[1] * BLIND)
    elif decision[0] == "all_in" :
        click_button.all_in()
    elif decision[0] == "check_fold" :
        click_button.check_fold()
    elif decision[0] == "not defined" :
        screenshot_error("decide function deficiency")
        click_button.check_fold()
    elif decision == None:
        screenshot_error("A play function returned None")
        click_button.check_fold()
    else :
        screenshot_error("returned string is not in standard format")
        click_button.check_fold()
    time.sleep(1)

def set_all_variables_to_none():
    global game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat = (None,)*39
    save_variables()


if __name__ == '__main__':


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


    find_game_reference_point_for_starting()


while True :

    Pre_Flop1_Deside = False ; Flop1_Deside = False ; Turn1_Deside = False ; River1_Deside = False 

    if Just_Seated == True :

        shout(paint.on_green.bold("****** Running Just_Seated == True Section ******"))
        reset_check_mode_to_false() #

        reset_table_information() #

        if pm.my_seat_won_pixel(game_position,  My_Seat_Number ) == False :
            My_Bank = ocr_my_bank( My_Seat_Number )
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
        
        Hand_End_Cheker1 = hand_is_ended()
        while Hand_End_Cheker1 :
            Hand_End_Cheker1 = hand_is_ended()

        if pm.active_player_pixel(game_position, My_Seat_Number) != True or ( pm.active_player_pixel(game_position, My_Seat_Number) == True and pm.notification_banner_pixel(game_position, My_Seat_Number) == True ) :
            read_and_save_players_banks_and_names() #
        else :
            shout( paint.on_light_red.bold("Players Info is not Read") )

        time02 = 0 ; fo = 0 
        time1 = time.time()
        Cards1 = False
        shout(paint.light_magenta.bold("Looking for cards in Just_Seated == True Section..."))
        while Cards1 == False and time02 < 5 * 60 : #being alone time
            Cards1 = pm.player_cards_pixel(game_position,  My_Seat_Number )
            time2 = time.time() - time1
            n60 = ( time2 - 120 ) // 60
            if not time2 < 2 * 60 and n60 >= fo :
                fix_game_disruption("1")
                fo += 1
                time02 = time.time() - time1                

        if not time02 < 5 * 60 : #being alone time
            raise Exception("0.1.No one join, time to exit. Or Game is locked, force to restart(will be build in future), Just_Seated == None")

        if Cards1 == True :
            if pm.pre_flop_pixel(game_position) == False or ( pm.pre_flop_pixel(game_position) == True and is_there_any_raiser() == True) :
                set_check_mode_to_true("this is Ok! Becuase i may start program from middle of the game")

            Just_Seated = False
            shout(paint.light_magenta.bold("Cards are founded"))
            shout (paint.on_green.bold("****** First hand Started ******"))
    
    elif Just_Seated == None :
        raise Exception("5.This can not happen IN FUTURE becuase main menu automation is built\
                        ( fix_game_disruption --> Sit_In --> table is full --> exit -->\
                        Just_Seated = None --> main menu --> Just_Seated = True )")


#-------    

    if Hand_End_Cheker1 == False and pm.pre_flop_pixel(game_position) == False and Just_Seated == False and Check_Mod != True :
        fix_game_disruption("2")
        set_check_mode_to_true("2")
        screenshot_error('6.pre_flop_pixel() == False')
    elif Hand_End_Cheker1 == False and Just_Seated == False and Check_Mod != True :
        Pre_Flop1 = True
        Pre_Flop1_Deside = True

    if Hand_End_Cheker1 == False and pm.player_cards_pixel(game_position,  My_Seat_Number ) == True and Just_Seated == False :  
        Read_My_Cards() #
        play_sound() #


    its_my_turn = False
    Gray1 = True ; fo = 0 
    time1 = time.time()
    shout(paint.light_magenta.bold("Looking for light...")) 
    while Hand_End_Cheker1 == False and (its_my_turn == False or Gray1 == True) and Flop1_Deside == False and Just_Seated == False and time.time() - time1 < 5 * 60 :
        if pm.i_am_back_button_pixel(game_position) :
            fix_game_disruption("2.5 I am back Button is True")
        Hand_End_Cheker1 = hand_is_ended()
        its_my_turn = pm.active_player_pixel(game_position,  My_Seat_Number )
        Gray1 = pm.notification_banner_pixel(game_position,  My_Seat_Number )
        Flop1_Deside = pm.flop_pixel(game_position)
        n20 = (time.time() - time1 - 60 ) // 20
        if time.time() - time1 > 1 * 60 and n20 >= fo :
            fix_game_disruption("3")
            fo += 1
            
    if not time.time() - time1 < 5 * 60 :
        raise Exception("5.1.Game is locked, force to restart, Just_Seated == None")

    if Flop1_Deside == True :
        set_check_mode_to_true("1.5")
        screenshot_error("6.5 Pre Flop is Jumped, game must lagged")
        
         
    Round_Pre_Flop = 0 #(2018) shouldn't it be -1 ?! test it by printing for example Cards_cache dic which prints rounds too
    if pm.active_player_pixel(game_position,  My_Seat_Number ) == True and Gray1 == False and hand_is_ended() == False and Flop1_Deside == False and Just_Seated == False :
        Round_Pre_Flop += 1
        shout(paint.light_magenta.bold("light is founded"))
        read_and_save_bets() #
        click_decision() # preflop
    elif hand_is_ended() == False and Flop1_Deside == False and Just_Seated == False :
        fix_game_disruption("4 Entering This section is not possible")
        screenshot_error("6.6 Entering This section is not possible")
        #(2018) shouldn't Round_Pre_Flop += 1 line be here too ?!
        read_and_save_bets() #
        click_decision() # preflop



# PreFlop: -------

        
    if Just_Seated == False :

        shout("Running PreFlop Section")
        time01 = time.time()
        time02 = time.time() - time01
        
        while Hand_End_Cheker1 == False and Flop1_Deside == False and time02 < 5 * 60 and Just_Seated == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            its_my_turn = False ; Flop1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and its_my_turn == False and Flop1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    find_game_reference_point()
                    fo = 1
                if pm.i_am_back_button_pixel(game_position) :
                    fix_game_disruption("4.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  My_Seat_Number )
                Flop1 = pm.flop_pixel(game_position)
                time2 = time.time() - time1
                    
            if not time2 < 1 * 60 :
                fix_game_disruption("5")

            if Hand_End_Cheker1 == False :

                if its_my_turn == True and Flop1 == False :
                    Round_Pre_Flop += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # preflop
                    elif Check_Mod != True :
                        set_check_mode_to_true("3")
                        screenshot_error("7.Red should be True here, check later why this happens")
                        read_and_save_bets() #
                        click_decision() # preflop
                        
                if Flop1 == True :
                    Flop1_Deside = True
                    shout(paint.light_magenta.bold("Reading Flop Cards..."))
                    Read_Flop_Cards() #

        if not time02 < 5 * 60 :
            raise Exception("8.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            fix_game_disruption("6")


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
            its_my_turn = False ; Turn1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and its_my_turn == False and Turn1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    find_game_reference_point()
                    fo = 1
                if pm.i_am_back_button_pixel(game_position) :
                    fix_game_disruption("6.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  My_Seat_Number )
                Turn1 = pm.turn_pixel(game_position)
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                fix_game_disruption("7")
                
            if Hand_End_Cheker1 == False :

                if its_my_turn == True and Turn1 == False :
                    Round_Flop += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # Flop
                    elif Round_Flop > 0 :
                        set_check_mode_to_true("4")
                        screenshot_error("9.Red should be True here")
                        read_and_save_bets() #
                        click_decision() # Flop
                    else :
                        read_and_save_bets() #
                        click_decision() # Flop
                        
                if Turn1 == True :            
                    Turn1_Deside = True
                    shout(paint.light_magenta.bold("Reading Turn Card"))
                    Read_Turn_Cards() #        
            
        if not time02 < 5 * 60 :
            raise Exception("10.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            fix_game_disruption("8")    



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
            its_my_turn = False ; River1 = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and its_my_turn == False and River1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    find_game_reference_point()
                    fo = 1
                if pm.i_am_back_button_pixel(game_position) :
                    fix_game_disruption("8.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  My_Seat_Number )
                River1 = pm.river_pixel(game_position)
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                fix_game_disruption("9")
                
            if Hand_End_Cheker1 == False :

                if its_my_turn == True and River1 == False :
                    Round_Turn += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # Turn
                    elif Round_Turn > 0 :
                        set_check_mode_to_true("5")
                        screenshot_error("11.Red should be True here")
                        read_and_save_bets() #
                        click_decision() # Turn
                    else :
                        read_and_save_bets() #
                        click_decision() # Turn
                        
                if River1 == True :            
                    River1_Deside = True
                    shout(paint.light_magenta.bold("Reading River Card"))
                    Read_River_Cards() #        
            
        if not time02 < 5 * 60 :
            raise Exception("12.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            fix_game_disruption("10")            
            

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
            its_my_turn = False ; fo = 0
            shout(paint.light_magenta.bold("Looking for Next sign..."))
            while Hand_End_Cheker1 == False and its_my_turn == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    find_game_reference_point()
                    fo = 1
                if pm.i_am_back_button_pixel(game_position) :
                    fix_game_disruption("10.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  My_Seat_Number )
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                fix_game_disruption("11")
                
            if Hand_End_Cheker1 == False :

                if its_my_turn == True and pm.river_pixel(game_position) == True :
                    Round_River += 1
                    shout(paint.light_magenta.bold("light is founded"))
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # River
                    elif Round_River > 0 :
                        set_check_mode_to_true("6")
                        screenshot_error("13.Red should be True here")
                        read_and_save_bets() #
                        click_decision() # River
                    else :
                        read_and_save_bets() #
                        click_decision() # River


                               
            
        if not time02 < 5 * 60 :
            raise Exception("14.I should work on main menu automation later!(game is locked maybe, force to exit or restart),Just_Seated == None mishavad")
            fix_game_disruption("12")            
            


#-------
            
    if Hand_End_Cheker1 == True and Just_Seated == True :

        declare_the_winners()
        shout (paint.on_green.bold("-------- Hand Ended --------"))

    if Hand_End_Cheker1 == True and Just_Seated == False :

        declare_the_winners()
        shout (paint.on_green.bold("-------- Hand Ended --------"))
        
        reset_check_mode_to_false() #

        reset_table_information() #

        if pm.my_seat_won_pixel(game_position,  My_Seat_Number ) == False : 
            My_Bank = ocr_my_bank( My_Seat_Number )
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
            Hand_End_Cheker1 = hand_is_ended()
            time2 = time.time() - time1
            if not time2 < 2 * 60 :
                if fo == 0 :
                    fix_game_disruption("13")
                    fo = 1
                time02 = time.time() - time1                

        if not time02 < 1.5 * 60 :
            raise Exception("15.Game is locked, force to restart, Just_Seated == None")
            


    if Hand_End_Cheker1 == False and Just_Seated == False :

        if pm.active_player_pixel(game_position, My_Seat_Number) != True or ( pm.active_player_pixel(game_position, My_Seat_Number) == True and pm.notification_banner_pixel(game_position, My_Seat_Number) == True ) :
            read_and_save_players_banks_and_names() #
        else :
            shout( paint.on_light_red.bold("Players Info is not Read") )

        Coins_Appeared = False
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Coins_Appeared == False and time02 < 5 * 60 : #being alone time
            Coins_Appeared = sb_b_d_buttons_are_founded()
            time2 = time.time() - time1
            if not time2 < 8 and fo == 0 :
                find_game_reference_point()
                fo = 1
            if not time2 < 2 * 60 :
                if fo == 1 :
                    fix_game_disruption("14")
                    fo = 2
                time02 = time.time() - time1                

        if not time02 < 5 * 60 : #being alone time
            raise Exception("16.No one join, time to exit. Or Game is locked, force to restart, Just_Seated == None")

        elif Just_Seated == False :
            shout (paint.on_green.bold("-------- New Hand Started --------"))
            shout ("Coins are Founded")
            determine_small_blind_seat()
            determine_big_blind_seat()
            determine_dealer_seat()       


                    
            time02 = 0 ; fo = 0 
            time1 = time.time()
            Cards1 = False
            shout(paint.light_magenta.bold("Looking for cards..."))
            while Hand_End_Cheker1 == False and Cards1 == False and Just_Seated == False and time02 < 1.5 * 60 :
                if pm.i_am_back_button_pixel(game_position) :
                    fix_game_disruption("14.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                Cards1 = pm.player_cards_pixel(game_position,  My_Seat_Number )
                time2 = time.time() - time1
                if not time2 < 2 * 60 :
                    if fo == 0 :
                        fix_game_disruption("15")
                        fo = 1
                    time02 = time.time() - time1                

            if not time02 < 1.5 * 60 :
                raise Exception("17.Game is locked, force to restart, Just_Seated == None")

            if Cards1 == True :
                shout(paint.light_magenta.bold("Cards are founded"))

            elif not time02 < 1.5 * 60 :
                fix_game_disruption("15")

            if Hand_End_Cheker1 == True and Cards1 == False :
                fix_game_disruption("16. I am maybe out")
            



