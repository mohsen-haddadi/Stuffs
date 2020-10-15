#OK
"""The variables which may change in this module are:
    1. config.game_position
    2. config.my_seat_number
    3. config.waiting_for_first_hand
    4. config.just_do_check_fold
"""
import socket, wmi, time

import pyautogui

import screen_monitoring.pixel_matching.pixel_matching as pm
import config
from iprint import shout
from readability_then_click import click, click_on_button, hold_click_on_button
from readability_then_ocr import ocr_my_name


def sit_in(chips): # "Min buy in" or "Max buy in"
    #global game_position, my_seat_number , waiting_for_first_hand

    shout("Searching for a seat to sit in", color = 'yellow')
    config.my_seat_number = None
    for i in range(1 ,6 ):
        if pm.available_seat_pixel(config.game_position,i) == True :
            click('available_seat_%s' %i)
            config.my_seat_number = i
            config.waiting_for_first_hand = True
            shout("Sit_In() --> waiting_for_first_hand is True."
                  , color = 'yellow')
            break
    if config.my_seat_number == None :
        click_on_button('exit')
        
        raise Exception("Sit_In(chips):This can not happen IN FUTURE becuase main menu automation is built")
    else :
        x1 = time.time()
        time1 = 0
        Buy_In = None 
        while ( (time1 < 5) and Buy_In !=True ):
            Buy_In = pm.button_pixel(config.game_position, 'buy_in')
            x2 = time.time()
            time1 = x2-x1
        if Buy_In != True :
            fix_game_disruption("Sit_In(chips):Buy_In != True")
        if (chips == "Min buy in" and config.my_seat_number != None) :
            hold_click_on_button('buy_in_minus', seconds = 10)
        if (chips == "Max buy in" and config.my_seat_number != None):
            hold_click_on_button('buy_in_plus', seconds = 10)
        if config.my_seat_number != None :
            click_on_button('buy_in')
            screenshot_error("Rebuyed")
#
#def pm.i_am_back_button_pixel(game_position):

#def click_on_i_am_back_button(): # we can use click('i_am_back') directly

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
    #global game_position, my_seat_number , MY_PROFILE_NAME , just_do_check_fold

    if pm.button_pixel(config.game_position, 'i_am_back') == True :
        click('i_am_back')
    if ocr_my_name() == config.MY_PROFILE_NAME or ocr_my_name() == True :
        shout("I am In", color = 'yellow')
        return ("In")

    for i in range(1,6):
        if pm.i_am_seated_pixel(config.game_position, i) :
            if is_internet_disconnected() == False and find_and_click_on_reconnect_button() == None :
                if config.my_seat_number == i :
                    shout("I am In not by OCR")
                    return ("In")
                else :
                    config.my_seat_number = i
                    shout('I AM IN,BUT MY SEAT IS MANUALLY CHANGED TO: %s' %config.my_seat_number)
                    set_just_do_check_fold_to_true("My seat is manually changed!")
                    return ("In")
                
    shout("I am Out", color = 'yellow')
    return ("Out")

def find_and_click_on_reconnect_button():
    #global game_position

    shout('looking for reconnect button')
    x1 = pyautogui.locateCenterOnScreen('screen_monitoring/game_position/reconnect button.png')
    if x1 != None :
        pyautogui.click(x1)
        shout('reconnect button founded and clicked', color = 'yellow')
        time.sleep(5)
        if pm.button_pixel(config.game_position, 'i_am_back') == True :
            click('i_am_back')
        return x1
    
    x2 = pyautogui.locateCenterOnScreen('screen_monitoring/game_position/reconnect button.png')
    if x2 != None :
        pyautogui.click(x2)
        shout('reconnect button founded and clicked', color = 'yellow')
        time.sleep(5)
        if pm.button_pixel(config.game_position, 'i_am_back') == True :
            click('i_am_back')
        return x1

    else :
        return None

def fix_game_disruption(String = None): #if find_game_reference_point() == None or ...
    #global game_position , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand , just_do_check_fold

    shout( 7*"-" , color = 'yellow')
    if String == None :
        shout("fix_game_disruption() is running....", color = 'yellow')
    elif type(String) == str :
        shout("fix_game_disruption() <-- %s is running...." %String
              , color = 'yellow')

    if is_internet_disconnected() :
        shout('Internet is Disconnected, waiting to reconect...')
        while is_internet_disconnected() :
            continue
        shout('Internet is Connected Back!')
        time.sleep(15)
        if find_and_click_on_reconnect_button() == None :
            screenshot_error('No reconnect button founded')

    click('exit_probable_advertisement') # click to Exit probable Advertisement
    shout("Position (0,720) is clicked", color = 'yellow')
    pyautogui.press('esc')
    
    config.game_position = pyautogui.locateOnScreen(
                    'screen_monitoring/find_game_position/reference image.png')
    if config.game_position == None:
        config.alternative_game_position = pyautogui.locateOnScreen(
                    'screen_monitoring/find_game_position/alternative reference image.png')   
        if config.alternative_game_position != None:
            config.game_position = ( alternative_game_position[0]+328 , alternative_game_position[1]-245 ) 
    if config.game_position != None :
        config.game_position = (int(config.game_position[0]),int(config.game_position[1]))
    else:
        for process in wmi.WMI().Win32_Process ():
            if process.Name == 'SystemSettings.exe' :
                shout("SystemSettings Update is on desktop")
                shout("closing Windows Update program")
                screenshot_error('right before closing windows update program')
                click('close_update_window')
                break        

    if config.game_position == None :
        config.game_position = find_game_position.find_game_reference_point()
    if config.game_position != None :
        shout("Game region refounded after fix_game_disruption()"
              , color = 'yellow')
    
    if pm.button_pixel(config.game_position, 'i_am_back') == True :
        click('i_am_back')
        if pm.player_cards_pixel(config.game_position,  config.my_seat_number ) == True :
            config.just_do_check_fold = True
            shout("After fix_game_disruption() --> just_do_check_fold is True."
                  , color = 'yellow')
        else :
            config.waiting_for_first_hand = True
            shout("After fix_game_disruption() --> waiting_for_first_hand is True."
                  , color = 'on_yellow')

    if check_i_am_in_or_out() == "Out":
        sit_in("Min buy in")

    shout( 7*"-" , color = 'yellow')

#if (buttoms are still not visible after vital signs).... : #My pixel matching were wrong somewhere
#    t = time.time()
#    pyautogui.screenshot( 'Error %s.png' %t )
#    raise Exception('what was the probelm on %s?' %t ) 
        
def set_just_do_check_fold_to_true(string = None) :
    #global just_do_check_fold

    config.just_do_check_fold = True
    if string == None :
        shout("just_do_check_fold is On", color = 'on_yellow')
    elif type(string) == str :
        shout("just_do_check_fold is On: %s" %string, color = 'on_yellow')

def screenshot_error(type_of_error): #type_of_error in string
    #global REPORTS_DIRECTORY

    t = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
    t = t[:-4]
    shout("Screenshot Error: %s" %type_of_error, color = 'on_light_blue')
    pyautogui.screenshot( '%s/Error %s %s.png' %(config.REPORTS_DIRECTORY, t, type_of_error) )

def raise_exception_the_problem(string):
    screenshot_error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')
