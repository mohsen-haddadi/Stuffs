"""
Note 1: use config.new_hand = hand_is_ended() inside waiting functions.
Note 2: If I've resume the game, set 
        config.bot_status = 'WAITING_FOR_FIRST_HAND' inside resume function.
"""

import time, os
from datetime import datetime

import pygame, keyboard

import screen_monitoring.pixel_matching.pixel_matching as pm
import decision_making.decide
import decision_making.rules_and_info.starting_hands as hand_ranking
from readability.read_cards import read_and_save_flop_cards,\
read_and_save_turn_card, read_and_save_river_card
from readability.ocr import ocr_my_bank
from readability.click import fold, check, call, all_in,\
raising, check_fold
from readability.fix_game_disruption import fix_game_disruption,\
set_just_do_check_fold_to_true, screenshot_error
#importing same level directory modules
import config
from iprint import shout
from set_variables import red_chips


def wait_celebration_ends(waiting_seconds = 10):
    t1 = time.time()
    while True:
        config.new_hand = hand_is_ended()
        if not config.new_hand:
            break
        if time.time() - t1 > waiting_seconds:
            fix_game_disruption('game is stuck at celebration')
            break
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 
    # sleep time so buttons and cards are dealt properly
    time.sleep(1)

def wait_hand_ends(waiting_minutes = 5):
    t1 = time.time()
    while True:
        config.new_hand = hand_is_ended()
        if config.new_hand:
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
            break
        if time.time() - t1 > 60 * waiting_minutes :
            shout('This hand is played manually more than %s minutes' 
                  %waiting_minutes)
            break
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 

def wait_for_my_new_hand(waiting_minutes = 10):
    shout("Looking for my cards in 'I_AM_PLAYING' Section..."
          , color = 'light_magenta')
    t1 = time.time()
    while True:
        if pm.player_cards_pixel(config.game_position, config.my_seat_number):
            shout("My cards are founded", color = 'light_magenta')
            config.preflop_stage = True
            break
        config.new_hand = hand_is_ended()
        if not config.new_hand:
            break
        if time.time() - t1 > 60*waiting_minutes:
            fix_game_disruption('My cards are not founded for new hand '\
                                'after %s minutes wating'%waiting_minutes)
            if not pm.player_cards_pixel(config.game_position, 
                                         config.my_seat_number):
                config.bot_status = 'WAITING_FOR_FIRST_HAND'
            break
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 
            
def wait_for_my_first_hand(waiting_minutes = 5):
    """Don't break this waiting function if config.new_hand is True, because 
    I'm waiting for first hand and maybe several hands are played without me.
    """
    shout("Looking for cards in 'WAITING_FOR_FIRST_HAND' Section..."
          , color = 'light_magenta')
    t1 = time.time()
    fixing_retry = 1
    while True:

        if pm.player_cards_pixel(config.game_position, config.my_seat_number):
            shout("My cards are founded", color = 'light_magenta')
            config.bot_status = 'I_AM_PLAYING'
            break
        if (time.time()-t1) > ((60*waiting_minutes)/3) and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()
        if time.time() - t1 > 60 * waiting_minutes :
            config.bot_status = 'ON_MAIN_MENU'
            shout("No one join the table, call operator to go to main menu")
            break
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 

def first_round_at_preflop():
    """ 
    This function is created to help handling the bot after the game is
    unpaused in 'I_AM_PLAYING' bot status.
    If I've resume the game, set config.bot_status = 'WAITING_FOR_FIRST_HAND'
    inside resume function.
    Even at preflop (betting_round = 0) (first_round_at_preflop() is True) 
    I can resume the game without doing set_just_do_check_fold_to_true().
    """
    def is_there_any_raiser():
        """ Except me """
        for seat in range(1, config.TOTAL_SEATS+1):
            if seat == config.my_seat_number:
                continue
            elif red_chips(seat):
                return True
        return False

    if not pm.pre_flop_pixel(config.game_position):
        return False 
    if is_there_any_raiser():
        shout('doing some ocr to check if it is first_round_at_preflop or not')
        if config.my_seat_number in (config.big_blind_seat, config.big_blind_seat):
            if ocr_bet(config.my_seat_number) > config.BLIND_VALUE:
                return False
        else:
            if pm.player_chips_pixel(config.game_position, config.my_seat_number):
                return False
    return True

def wait_for_sb_b_d_buttons(waiting_seconds = 5):
    """5 seconds waiting does not need config.new_hand to break it"""
    t1 = time.time()
    while True:
        if sb_b_d_buttons_are_founded():
            break
        if time.time() - t1 > waiting_seconds:
            fix_game_disruption('sb b d buttons are not founded')
            if not sb_b_d_buttons_are_founded():
                set_just_do_check_fold_to_true('sb b d buttons are not founded')
            break
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 

def game_is_paused():
    """Hold 'end' button to pause the bot.
    game_is_paused() is used in main.py and main_assist.py modules.
    It is used at the end waiting functions or functions which contains 
    'while True:' statement.
    After game is paused, bot should redirect to 'WAITING_FOR_FIRST_HAND' 
    status immediately.
    """
    if keyboard.is_pressed("end"): 
        print("game is paused")
        config.bot_status = 'WAITING_FOR_FIRST_HAND'
        # DON'T use set_just_do_check_fold_to_true() here.
        # we use it at wait_for_my_first_hand() function, this function will 
        # checks if the hand is just started or not and won't waste 
        # just started hands by doing just check_fold.
        return True
    return False



def sb_b_d_buttons_are_founded():
    """For cheet there is no small or big blind buttons"""
    small_blind_button_founded = False
    big_blind_button_founded = False 
    dealer_button_founded = False
    for seat in range(1, config.TOTAL_SEATS+1):
        if pm.small_blind_pixel(config.game_position, seat) == True:
            small_blind_button_founded = True
            break
    for seat in range(1, config.TOTAL_SEATS+1):
        if pm.big_blind_pixel(config.game_position, seat) == True:
            big_blind_button_founded = True
            break
    for seat in range(1, config.TOTAL_SEATS+1):
        if pm.dealer_pixel(config.game_position, seat) == True:
            dealer_button_founded = True
            break
    return small_blind_button_founded and big_blind_button_founded and dealer_button_founded

def shifted_to_next_stage():
    if (not config.flop_stage and pm.flop_pixel(config.game_position) 
        and not pm.turn_pixel(config.game_position) 
        and not pm.river_pixel(config.game_position)):
        config.flop_stage = True
        shout("Waiting for my turn at flop_stage...", 'light_magenta') 
        return True
    if (not config.turn_stage and pm.turn_pixel(config.game_position) 
        and not pm.river_pixel(config.game_position) ):
        config.turn_stage = True
        shout("Waiting for my turn at turn_stage...", 'light_magenta') 
        return True
    if not config.river_stage and pm.river_pixel(config.game_position):
        config.river_stage = True
        shout("Waiting for my turn at river_stage...", 'light_magenta')
        return True
    return False

def read_board_cards():
    if config.flop_stage and not config.turn_stage and not config.river_stage:
        read_and_save_flop_cards()
    if config.turn_stage and not config.river_stage:
        read_and_save_turn_card()
    if config.river_stage:
        read_and_save_river_card()
 
def stages_are_sequenced(): 
    if pm.flop_pixel(config.game_position) and config.preflop_stage == False:
        return False
    if pm.turn_pixel(config.game_position) and False in (config.preflop_stage, config.flop_stage):
        return False
    if (pm.river_pixel(config.game_position) and
        False in (config.preflop_stage, config.flop_stage, config.turn_stage)):
        return False
    return True

def update_betting_rounds():
    if config.preflop_stage and not config.flop_stage:
        config.preflop_betting_round += 1
        shout('TESTING. preflop_betting_round is:%s'
              %config.preflop_betting_round, color = 'on_light_red')
    if config.flop_stage and not config.turn_stage:
        config.flop_betting_round += 1
        shout('TESTING. flop_betting_round is:%s'
              %config.flop_betting_round, color = 'on_light_red')
    if config.turn_stage and not config.river_stage:
        config.turn_betting_round += 1
        shout('TESTING. turn_betting_round is:%s'
              %config.turn_betting_round, color = 'on_light_red')
    if config.river_stage:
        config.river_betting_round += 1
        shout('TESTING. river_betting_round is:%s'
              %config.river_betting_round, color = 'on_light_red')

def hand_is_ended():
    """
    This is an important function, because it determines
    when new hand will start.
    For cheet: 
    1.Yellow around winning cards 
    2.If everyone fold the somebodies raise, only one player have cards.
    """
    for seat in range(1, config.TOTAL_SEATS+1):
        if pm.my_seat_won_pixel(config.game_position, seat):
            return True
        if pm.other_seat_won_pixel(config.game_position, seat):
            return True
    return False

def declare_the_winners():
    """May differs for Cheet"""
    for seat in range(1, config.TOTAL_SEATS+1):
        if pm.my_seat_won_pixel(config.game_position, seat) == True:
            shout("I won the game!", color = 'on_light_magenta')
        if pm.other_seat_won_pixel(config.game_position, seat) == True :
            shout("Seat %s won the game!" %seat)

def rebuy_if_bank_is_low(min_blinds = 15):
    my_bank = ocr_my_bank()
    if my_bank == None :
        shout("My bank can't be read")
    elif my_bank != None :
        shout("My bank is:%s" %my_bank, color = 'light_green')
        if 0 < my_bank <= min_blinds * config.BLIND_VALUE:
            shout("Rebuying...")
            pass # Later i'll build

def its_my_turn():
    if pm.active_player_pixel(config.game_position, config.my_seat_number):
        shout("It is my turn now", color = 'light_magenta')
        return True
    return False

def sound(string_name) :
    try :
        pygame.mixer.init()
        pygame.mixer.music.load( os.path.join('Sounds' ,
                                              "%s.wav" %string_name ) )
        return pygame.mixer.music.play()
    except :
        pass

def play_sound_for_good_starting_hands() :
     
    if config.preflop_stage == True and config.flop_stage == False :
        if hand_ranking.hand1() :
            sound("Michel")
            shout("Playing Music: 'Michel'", color = 'light_cyan')
        elif hand_ranking.hand2() :
            sound("Alan Walker")
            shout("Playing Music: 'Alan Walker'", color = 'light_cyan')
        elif hand_ranking.hand3() :
            sound("Alan Walker")
            shout("Playing Music: 'Alan Walker'", color = 'light_cyan')
        elif hand_ranking.hand4() :
            sound("Pocket low pairs")
            shout("Playing Music: 'Pocket low pairs'", color = 'light_cyan')
        elif hand_ranking.hand5() :
            sound("Bob Marley")
            shout("Playing Music: 'Bob Marley'", color = 'light_cyan')

def click_decision():

    decision = decision_making.decide.decide()
    if decision[0] == "check" :
        check()
    elif decision[0] == "call" :
        call()
    elif decision[0] == "fold" :
        fold()
    elif decision[0] == "raise" :
        raising(decision[1] * BLIND_VALUE)
    elif decision[0] == "all_in" :
        all_in()
    elif decision[0] == "check_fold" :
        check_fold()
    elif decision[0] == "not defined" :
        pass
        # uncomment these 2 line, when play.py module is completed.
        #screenshot_error("decide function deficiency")
        #check_fold()
    elif decision == None:
        screenshot_error("A play function returned None")
        check_fold()
    else :
        screenshot_error("returned string is not in standard format")
        check_fold()
    time.sleep(1)

def create_report_folder():
    config.DATED_REPORT_FOLDER = datetime.now().strftime("%Y.%m.%d %A %H.%M.%S")
    config.REPORTS_DIRECTORY = "Reports/%s" %config.DATED_REPORT_FOLDER
    if not os.path.exists( config.REPORTS_DIRECTORY ):
        os.makedirs( config.REPORTS_DIRECTORY )

