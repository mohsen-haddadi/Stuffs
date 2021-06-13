#OK
import time

import pyautogui

import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.click_coordinates.click_coordinates as click_coordinates
import config
from iprint import shout
from readability.fix_game_disruption import fix_game_disruption, set_just_do_check_fold_to_true, screenshot_error, raise_exception_the_problem

def click(name):
    x, y = click_coordinates.click_coordinates(config.game_position, name)
    pyautogui.click(x, y)
    if name in ('available_seat_1', 'available_seat_2', 'available_seat_3',
                'available_seat_4', 'available_seat_5', 'exit_probable_advertisement',
                'close_update_window'):
        shout("%s is clicked" %name, color = 'light_cyan')
    else:
        shout("%s button is clicked" %name, color = 'light_cyan')

def hold_click(name ,seconds = 10):
    x, y = click_coordinates.click_coordinates(config.game_position, name)
    pyautogui.mouseDown(x=x, y=y)
    time.sleep(seconds)
    pyautogui.mouseUp()
    shout("%s button is hold for %s seconds" %(name, seconds), color = 'light_cyan')

def click_on_button(button_name): 
    # for call, check, fold, bet, raise,
    # exit, menu, rebuy_menu,
    # exit_yes, leave_next_hand_ok, buy_in, and re_buy buttons.
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status 

    if pm.button_pixel(config.game_position, button_name) : 
        click(button_name) 
        if button_name == 'exit':
            config.bot_status = 'ON_MAIN_MENU'

    else :

        if button_name in ('call', 'check', 'fold', 'bet', 'raise') :

            time0 = time.time()
            fix_game_disruption("button %s is not visible" %button_name )
            time1 = time.time() - time0
            if config.bot_status == 'WAITING_FOR_FIRST_HAND':
                return None
            elif config.just_do_check_fold == True:
                if pm.button_pixel(config.game_position, 'check') :
                    click('check')
                elif pm.button_pixel(config.game_position, 'fold') :
                    click('fold') 
                else:
                    screenshot_error("check and fold buttons are not visible")  
            elif pm.player_cards_pixel(config.game_position, config.my_seat_number ) \
            and pm.button_pixel(config.game_position, button_name) and time1 <= 10 :
                click(button_name) #new function
            else :
                set_just_do_check_fold_to_true("There is problem on clicking on button %s" %button_name)

        elif button_name in ('exit', 'menu', 'rebuy_menu'):

            fix_game_disruption("button %s is not visible" %button_name )
            if pm.button_pixel(config.game_position, button_name):
                click(button_name)
                if button_name == 'exit':
                    config.bot_status = 'ON_MAIN_MENU'
            else:
                raise_exception_the_problem("button %s is not visible" %button_name)

        elif button_name in ('exit_yes', 'leave_next_hand_ok', 'buy_in', 're_buy'):

            raise_exception_the_problem("button %s is not visible" %button_name)

def number_of_clicks_on_button(button_name, number): # Number of clicks 
    # for plus and minus buttons
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    number = int(number)
    if pm.button_pixel(config.game_position, button_name) :
        for i in range (number):
            click(button_name)
    else :
        time0 = time.time()
        fix_game_disruption("button %s is not visible" %button_name)
        time1 = time.time() - time0
        if config.bot_status == 'WAITING_FOR_FIRST_HAND':
            return None
        elif config.just_do_check_fold == True:
            if pm.button_pixel(config.game_position, 'check') :
                click('check')
            elif pm.button_pixel(config.game_position, 'fold') :
                click('fold') 
            else:
                screenshot_error("check and fold buttons are not visible") 
        if pm.player_cards_pixel(config.game_position,  config.my_seat_number ) \
        and pm.button_pixel(config.game_position, button_name) and time1 <= 10 :
            for i in range (number):
                click(button_name)
        else :
            set_just_do_check_fold_to_true("There is problem on clicking on button %s" %button_name)

def hold_click_on_button(button_name, seconds = 10): 
    # for buy_in_plus and buy_in_minus and re_buy_plus and re_buy_minus buttons
    # It holds left click for 10s
    #global game_position

    if pm.button_pixel(config.game_position, button_name) :
        hold_click(button_name ,seconds = seconds)

    else :
        time.sleep(2)
        if pm.button_pixel(config.game_position, button_name) :
            hold_click(button_name ,seconds = seconds)
        else :
            raise_exception_the_problem("button %s is not visible" %button_name) 


# 2017: -----------------------------

def fold():
    return click_on_button('fold')

def check():
    return click_on_button('check')

def call():
    return click_on_button('call')

def all_in_old(Minus_Blinds = 0): #not completed on did_i_raised_at and my_last_raise_at. i won't use this fuction anymore
    """ if 0 : all_in everything """
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    if pm.button_pixel(config.game_position, 'all_in') == False and pm.button_pixel(config.game_position, 'call') == True \
    and pm.button_pixel(config.game_position, 'bet') == False and pm.button_pixel(config.game_position, 'raise') == False :
        return click_on_button('call')
    
    if Minus_Blinds == 0 :
        click_on_button('all_in')
        if pm.button_pixel(config.game_position, 'bet') == True :
            return click_on_button('bet')
        else :
            return click_on_button('raise')
    else :
        click_on_button('all_in')
        number_of_clicks_on_button('minus', Minus_Blinds)
        if pm.button_pixel(config.game_position, 'bet') == True :
            return click_on_button('bet')
        else :
            return click_on_button('raise')

def all_in():
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    if pm.button_pixel(config.game_position, 'all_in') == False and pm.button_pixel(config.game_position, 'call') == True \
    and pm.button_pixel(config.game_position, 'bet') == False and pm.button_pixel(config.game_position, 'raise') == False :
        return click('call')
    
    click_on_button('all_in')
    if pm.button_pixel(config.game_position, 'bet') == True :
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
    #preflop_stage , flop_stage , turn_stage , river_stage , did_i_raised_at , my_last_raise_at , BLIND_VALUE

    if config.preflop_stage == True and config.flop_stage == False :
        stage = "Pre_Flop" 
    elif config.flop_stage == True and config.turn_stage == False :
        stage = "Flop"  
    elif config.turn_stage == True and config.river_stage == False :
        stage = "Turn" 
    elif config.river_stage == True :
        stage = "River" 

    if Blinds == 'pot':
        click('pot')
    else:
        Blinds = Blinds * c.BLIND_VALUE

        config.did_i_raised_at[stage] = True
        
        Bets = [config.last_bets_cache[Seat] for Seat in range(1, config.TOTAL_SEATS+1) if config.last_red_chips_cache[Seat] and config.last_bets_cache[Seat] != None ]     

        if config.preflop_stage and not config.flop_stage :
            Bets.append(config.BLIND_VALUE)
        else :
            Bets.append(0) #That's why raising() algorithm can be use and act for betting too.

        Bets.sort(reverse = True )

        Raise_base = max(Bets)

        Bets_difference = [ Bets[i] - Bets[i+1] for i in range(len(Bets)-1) ]

        if Bets_difference == []:
            Raise_add = config.BLIND_VALUE
        elif max(Bets_difference) <= config.BLIND_VALUE :
            Raise_add = config.BLIND_VALUE
        else :
            Raise_add = max(Bets_difference)

        if Blinds > Raise_base + Raise_add :
            config.my_last_raise_at[stage] = Blinds
        else :
            config.my_last_raise_at[stage] = Raise_base + Raise_add

        number_of_clicks_on_button('plus', ( Blinds - (Raise_base + Raise_add) ) // config.BLIND_VALUE)
    #Till here as same as raising()

    if pm.button_pixel(config.game_position, 'raise') :
        click('raise')
    elif pm.button_pixel(config.game_position, 'bet') :
        click('bet')
    else :

        fix_game_disruption("RAISE() Button, No Raise nor Bet Button founded")
        if pm.button_pixel(config.game_position, 'raise') :
            click('raise')
        elif pm.button_pixel(config.game_position, 'bet') :
            click('bet')
        else :
            set_just_do_check_fold_to_true("No raise nor bet button founded")

def check_fold():
    #global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status
    if pm.button_pixel(config.game_position, 'check') :
        click('check')
    elif pm.button_pixel(config.game_position, 'fold') :
        click('fold') 
    else :

        fix_game_disruption("check_fold()")
        if config.bot_status != 'I_AM_PLAYING':
            return None
        elif pm.button_pixel(config.game_position, 'check') :
            click('check')
        elif pm.button_pixel(config.game_position, 'fold') :
            click('fold') 
        else:
            set_just_do_check_fold_to_true("check_fold()(It's already True)") 
            screenshot_error("check and fold buttons are not visible")      


