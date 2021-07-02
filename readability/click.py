#OK
import time

import pyautogui, keyboard

import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.click_coordinates.click_coordinates as click_coordinates
import configs as c
from iprint import shout
from readability.fix_game_disruption import fix_game_disruption, set_just_do_check_fold_to_true, screenshot_error, raise_exception_the_problem
from readability.ocr import ocr_my_bet

def click(name):
    x, y = click_coordinates.click_coordinates(c.game_position, name)
    pyautogui.click(x, y)
    if name in ('available_seat_1', 'available_seat_2', 'available_seat_3',
                'available_seat_4', 'available_seat_5'):
        shout("%s is clicked" %name, color = 'light_cyan')
    else:
        shout("%s button is clicked" %name, color = 'light_cyan')

def hold_click(name ,seconds = 10):
    x, y = click_coordinates.click_coordinates(c.game_position, name)
    pyautogui.mouseDown(x=x, y=y)
    time.sleep(seconds)
    pyautogui.mouseUp()
    shout("%s button is hold for %s seconds" %(name, seconds), color = 'light_cyan')

def click_on_button(button_name): 
    # for call, check, fold, bet, raise,
    # exit, menu, 
    # buy_in, and re_buy buttons.
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status 

    if pm.button_pixel(c.game_position, button_name) : 
        click(button_name) 
        if button_name == 'exit':
            c.bot_status = 'ON_MAIN_MENU'

    else :

        if button_name in ('call', 'check', 'fold', 'bet', 'raise') :

            time0 = time.time()
            fix_game_disruption("button %s is not visible" %button_name )
            time1 = time.time() - time0
            if c.bot_status == 'WAITING_FOR_FIRST_HAND':
                return None
            elif c.just_do_check_fold == True:
                if pm.button_pixel(c.game_position, 'check') :
                    click('check')
                elif pm.button_pixel(c.game_position, 'fold') :
                    click('fold') 
                else:
                    screenshot_error("check and fold buttons are not visible")  
            elif pm.player_cards_pixel(c.game_position, c.my_seat_number ) \
            and pm.button_pixel(c.game_position, button_name) and time1 <= 10 :
                click(button_name) #new function
            else :
                set_just_do_check_fold_to_true("There is problem on clicking on button %s" %button_name)

        elif button_name in ('exit', 'menu'):

            fix_game_disruption("button %s is not visible" %button_name )
            if pm.button_pixel(c.game_position, button_name):
                click(button_name)
                if button_name == 'exit':
                    c.bot_status = 'ON_MAIN_MENU'
            else:
                raise_exception_the_problem("button %s is not visible" %button_name)

        elif button_name in ('buy_in', 're_buy', 'max_buy_in', 'min_buy_in'):

            raise_exception_the_problem("button %s is not visible" %button_name)

def type_blinds(blinds):
    click('type_blinds')
    click('type_blinds')
    keyboard.write(str(blinds))


# 2017: -----------------------------

def fold():
    return click_on_button('fold')

def check():
    return click_on_button('check')

def call():
    return click_on_button('call')

def all_in():
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    if pm.button_pixel(c.game_position, 'all_in') == False and pm.button_pixel(c.game_position, 'call') == True \
    and pm.button_pixel(c.game_position, 'bet') == False and pm.button_pixel(c.game_position, 'raise') == False :
        return click('call')
    
    click_on_button('all_in')
    if pm.button_pixel(c.game_position, 'bet') == True :
        return click('bet')
    else :
        return click_on_button('raise')

def raising(Blinds):
    """ 
    Act for both raising and betting 
    Blinds is the number of blinds ; not the amount of money like in ocr
    if Blinds == 1 (or less): won't click on plus button
    """
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status,\
    #did_i_raised_at , my_last_raise_at , BLIND_VALUE
    if Blinds == 'half_pot':
        click('half_pot')
    elif Blinds == 'pot':
        click('pot')
    else:
        type_blinds(Blinds)

#    Blinds = Blinds * c.BLIND_VALUE
#    c.did_i_raised_at[stage] = True
#    Bets = [c.last_bets_cache[Seat] for Seat in range(1, c.TOTAL_SEATS+1) if c.last_red_chips_cache[Seat] and c.last_bets_cache[Seat] != None ]     
#    if c.preflop_stage and not c.flop_stage :
#        Bets.append(c.BLIND_VALUE)
#    else :
#        Bets.append(0) #That's why raising() algorithm can be use and act for betting too.
#    Bets.sort(reverse = True )
#    Raise_base = max(Bets)
#    Bets_difference = [ Bets[i] - Bets[i+1] for i in range(len(Bets)-1) ]
#    if Bets_difference == []:
#        Raise_add = c.BLIND_VALUE
#    elif max(Bets_difference) <= c.BLIND_VALUE :
#        Raise_add = c.BLIND_VALUE
#    else :
#        Raise_add = max(Bets_difference)
#    if Blinds > Raise_base + Raise_add :
#        c.my_last_raise_at[stage] = Blinds
#    else :
#        c.my_last_raise_at[stage] = Raise_base + Raise_add
    c.my_last_raise_at[stage] = ocr_my_bet()

    if pm.button_pixel(c.game_position, 'raise'):
        click('raise')
    elif pm.button_pixel(c.game_position, 'bet'):
        click('bet')
    elif pm.button_pixel(c.game_position, 'call'):
        shout('some one must have gone all in')
        click('call')    
    else :

        fix_game_disruption("RAISE() Button, No Raise nor Bet Button nor call founded")
        if pm.button_pixel(c.game_position, 'raise') :
            click('raise')
        elif pm.button_pixel(c.game_position, 'bet') :
            click('bet')
        elif pm.button_pixel(c.game_position, 'call'):
            shout('some one must have gone all in')
            click('call')  
        else :
            set_just_do_check_fold_to_true("No raise nor bet button nor call founded")

def check_fold():
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status
    if pm.button_pixel(c.game_position, 'check') :
        click('check')
    elif pm.button_pixel(c.game_position, 'fold') :
        click('fold') 
    else :

        fix_game_disruption("check_fold()")
        if c.bot_status != 'I_AM_PLAYING':
            return None
        elif pm.button_pixel(c.game_position, 'check') :
            click('check')
        elif pm.button_pixel(c.game_position, 'fold') :
            click('fold') 
        else:
            set_just_do_check_fold_to_true("check_fold()(It's already True)") 
            screenshot_error("check and fold buttons are not visible")      


