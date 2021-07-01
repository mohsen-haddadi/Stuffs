"""
Note 1: use c.new_hand = hand_is_ended() inside waiting functions.
Note 2: If I've resume the game, set 
        c.bot_status = 'WAITING_FOR_FIRST_HAND' inside resume function.
"""

import time, os
from datetime import datetime

import pygame, keyboard

import screen_monitoring.pixel_matching.pixel_matching as pm
import decision_making.decide
from decision_making.rules_and_info.starting_hands import group
from readability.read_cards import read_and_save_flop_cards,\
read_and_save_turn_card, read_and_save_river_card
from readability.ocr import ocr_my_bank
from readability.click import fold, check, call, all_in,\
raising, check_fold
from readability.fix_game_disruption import fix_game_disruption,\
set_just_do_check_fold_to_true, screenshot_error
#importing same level directory modules
import config as c
from iprint import shout
from set_variables import red_chips


def wait_celebration_ends(waiting_seconds = 10):
    t1 = time.time()
    while True:
        c.new_hand = hand_is_ended()
        if not c.new_hand:
            break
        if time.time() - t1 > waiting_seconds:
            fix_game_disruption('game is stuck at celebration')
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 
    # sleep time so buttons and cards are dealt properly
    time.sleep(1)

def wait_hand_ends(waiting_minutes = 5):
    t1 = time.time()
    while True:
        c.new_hand = hand_is_ended()
        if c.new_hand:
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
            break
        if time.time() - t1 > 60 * waiting_minutes :
            shout('This hand is played manually more than %s minutes' 
                  %waiting_minutes)
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def wait_for_my_new_hand(waiting_minutes = 10):
    shout("Looking for my cards in 'I_AM_PLAYING' Section..."
          , color = 'light_magenta')
    t1 = time.time()
    while True:
        if pm.player_cards_pixel(c.game_position, c.my_seat_number):
            shout("My cards are founded", color = 'light_magenta')
            c.preflop_stage = True
            break
        # 2021: It's not reasonable to break here at all. 
        # So I comment these 3 lines:
        #c.new_hand = hand_is_ended()
        #if not c.new_hand:
        #    break
        if time.time() - t1 > 60*waiting_minutes:
            fix_game_disruption('My cards are not founded for new hand '\
                                'after %s minutes wating'%waiting_minutes)
            if not pm.player_cards_pixel(c.game_position, 
                                         c.my_seat_number):
                c.bot_status = 'WAITING_FOR_FIRST_HAND'
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 
            
def wait_for_my_first_hand(waiting_minutes = 8):
    """Don't break this waiting function if c.new_hand is True, because 
    I'm waiting for first hand and maybe several hands are played without me.
    """
    shout("Looking for cards in 'WAITING_FOR_FIRST_HAND' Section..."
          , color = 'light_magenta')
    t1 = time.time()
    fixing_retry = 1
    while True:

        if pm.player_cards_pixel(c.game_position, c.my_seat_number):
            shout("My cards are founded", color = 'light_magenta')
            c.bot_status = 'I_AM_PLAYING'
            break
        if (time.time()-t1) > ((60*waiting_minutes)/3) and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()
        if time.time() - t1 > 60 * waiting_minutes :
            c.bot_status = 'ON_MAIN_MENU'
            shout("No one join the table, call operator to go to main menu")
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def first_round_at_preflop():
    """ 
    This function is created to help handling the bot after the game is
    unpaused in 'I_AM_PLAYING' bot status.
    If I've resume the game, set c.bot_status = 'WAITING_FOR_FIRST_HAND'
    inside resume function.
    Even at preflop (betting_round = 0) (first_round_at_preflop() is True) 
    I can resume the game without doing set_just_do_check_fold_to_true().
    """
    def is_there_any_raiser():
        """ Except me """
        for seat in range(1, c.TOTAL_SEATS+1):
            if seat == c.my_seat_number:
                continue
            elif red_chips(seat):
                return True
        return False

    if not pm.pre_flop_pixel(c.game_position):
        return False 
    if is_there_any_raiser():
        shout('doing some ocr to check if it is first_round_at_preflop or not')
        if c.my_seat_number in (c.big_blind_seat, c.big_blind_seat):
            if ocr_bet(c.my_seat_number) > c.BLIND_VALUE:
                return False
        else:
            if pm.player_chips_pixel(c.game_position, c.my_seat_number):
                return False
    return True

def wait_for_sb_b_d_buttons(waiting_seconds = 5):
    """5 seconds waiting does not need c.new_hand to break it"""
    t1 = time.time()
    while True:
        if dealer_button_is_founded():  #💊
            break
        if time.time() - t1 > waiting_seconds:
            fix_game_disruption('sb b d buttons are not founded')
            if not dealer_button_is_founded():  #💊
                set_just_do_check_fold_to_true('sb b d buttons are not founded')
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def game_is_paused():
    """Hold 'end' button to pause the bot.
    game_is_paused() is used in main.py and main_assist.py and 
    observing.py modules.
    It is used at the end of waiting functions or functions which contains 
    'while True:' statement.
    After game is paused, bot should redirect to 'WAITING_FOR_FIRST_HAND' 
    status immediately.
    """
    if keyboard.is_pressed("end"): 
        shout("game is paused", color = 'on_yellow')
        answer = input("Press 'Enter' to start the bot playing. "\
                       "\nPress '1' then 'Enter' to start the bot observing.")
        if answer == '1':
            c.bot_status = 'OBSERVING'
        else:
            c.bot_status = 'WAITING_FOR_FIRST_HAND'
        # DON'T use set_just_do_check_fold_to_true() here.
        # we use it at *if not first_round_at_preflop():* statement.
        # this statement will checks if the hand is just started or not 
        # and won't waste just started hands by doing just check_fold.
        return True
    return False



def dealer_button_is_founded(): #💊
    """For cheet there is no small or big blind buttons"""
    dealer_button_founded = False
    for seat in range(1, c.TOTAL_SEATS+1):
        if pm.dealer_pixel(c.game_position, seat) == True:
            dealer_button_founded = True
            break
    return dealer_button_founded

def shifted_to_next_stage():
    if (not c.flop_stage and pm.flop_pixel(c.game_position) 
        and not pm.turn_pixel(c.game_position) 
        and not pm.river_pixel(c.game_position)):
        c.flop_stage = True
        if c.bot_status != 'OBSERVING':
            shout("Waiting for my turn at flop_stage...", 'light_magenta') 
        return True
    if (not c.turn_stage and pm.turn_pixel(c.game_position) 
        and not pm.river_pixel(c.game_position) ):
        c.turn_stage = True
        if c.bot_status != 'OBSERVING':
            shout("Waiting for my turn at turn_stage...", 'light_magenta') 
        return True
    if not c.river_stage and pm.river_pixel(c.game_position):
        c.river_stage = True
        if c.bot_status != 'OBSERVING':
            shout("Waiting for my turn at river_stage...", 'light_magenta')
        return True
    return False

def read_board_cards():
    if c.flop_stage and not c.turn_stage and not c.river_stage:
        read_and_save_flop_cards()
    if c.turn_stage and not c.river_stage:
        read_and_save_turn_card()
    if c.river_stage:
        read_and_save_river_card()

def stages_are_sequenced(): 
    if pm.flop_pixel(c.game_position) and c.preflop_stage == False:
        return False
    if pm.turn_pixel(c.game_position) and False in (c.preflop_stage,
                                                         c.flop_stage):
        return False
    if (pm.river_pixel(c.game_position) and
        False in (c.preflop_stage, c.flop_stage, c.turn_stage)):
        return False
    return True

def update_betting_rounds():
    if c.preflop_stage and not c.flop_stage:
        c.preflop_betting_round += 1
        shout('TESTING. preflop_betting_round is:%s'
              %c.preflop_betting_round, color = 'on_light_red')
    if c.flop_stage and not c.turn_stage:
        c.flop_betting_round += 1
        shout('TESTING. flop_betting_round is:%s'
              %c.flop_betting_round, color = 'on_light_red')
    if c.turn_stage and not c.river_stage:
        c.turn_betting_round += 1
        shout('TESTING. turn_betting_round is:%s'
              %c.turn_betting_round, color = 'on_light_red')
    if c.river_stage:
        c.river_betting_round += 1
        shout('TESTING. river_betting_round is:%s'
              %c.river_betting_round, color = 'on_light_red')

def hand_is_ended(): #💊
    """
    This is an important function, because it determines
    when new hand will start.
    For cheet: 
    1.Yellow around winning cards 
    2.If everyone fold the somebodies raise, only one player have cards.
    """
    players_cards_count == 0
    for seat in range(1, c.TOTAL_SEATS+1):
        if pm.seat_won_pixel(c.game_position, seat):
            return True
        if pm.dealer_pixel(c.game_position, seat) and seat != c.dealer_seat:
            c.dealer_seat = seat
            return True
        if pm.player_cards_pixel(c.game_position, seat):
            players_cards_count += 1
    if players_cards_count == 1:
        return True
    return False

def declare_the_winners():
    """May differs for Cheet"""
    for seat in range(1, c.TOTAL_SEATS+1):
        if pm.seat_won_pixel(c.game_position, seat) == True:
            if c.my_seat_number == seat:
                shout("I won the game!", color = 'on_light_magenta')
            else:
                shout("Seat %s won the game!" %seat)

def rebuy_if_bank_is_low(min_blinds = 15):
    my_bank = ocr_my_bank()
    if my_bank == None :
        shout("My bank can't be read")
    elif my_bank != None :
        shout("My bank is:%s" %my_bank, color = 'light_green')
        if 0 < my_bank <= min_blinds * c.BLIND_VALUE:
            shout("Rebuying...")
            pass # Later i'll build

def its_my_turn():
    if pm.active_player_pixel(c.game_position, c.my_seat_number):
        shout("It is my turn now", color = 'light_magenta')
        return True
    return False

def sound(string_name) :
    try :
        pygame.mixer.init()
        pygame.mixer.music.load( os.path.join('Sounds' ,
                                              "%s.mp3" %string_name ) )
        return pygame.mixer.music.play()
    except :
        pass

def play_sound_for_good_starting_hands() :
     
    if c.preflop_stage == True and c.flop_stage == False :
        if group('A'):
            sound("Du Bist Erwacht")
            shout("Playing Music: 'Michel'", color = 'light_cyan')
        elif group('B'):
            sound("la isla bonita")
            shout("Playing Music: 'Alan Walker'", color = 'light_cyan')
        elif group('C'):
            sound("la isla bonita")
            shout("Playing Music: 'Alan Walker'", color = 'light_cyan')
        elif group('D'):
            sound("la isla bonita")
            shout("Playing Music: 'Pocket low pairs'", color = 'light_cyan')
        elif group('EFG'):
            sound("la isla bonita")
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
        raising(decision[1])
    elif decision[0] == "all_in" :
        all_in()
    elif decision[0] == "check_fold" :
        check_fold()
    elif decision[0] == "not defined" :
        c.bot_status = 'OPERATOR_SHOULD_PLAY_THE_HAND'
        # uncomment these 2 next lines and remove line above, 
        # when play.py module is completed.
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
    c.DATED_REPORT_FOLDER = datetime.now().strftime("%Y.%m.%d %A %H.%M.%S")
    c.REPORTS_DIRECTORY = "Reports/%s" %c.DATED_REPORT_FOLDER
    if not os.path.exists( c.REPORTS_DIRECTORY ):
        os.makedirs( c.REPORTS_DIRECTORY )

