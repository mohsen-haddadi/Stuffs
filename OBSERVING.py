"""
'OBSERVING' status can be used to test screen monitoring or to
get opponents playing styles or to gather statistical data.
"""
import time

import screen_monitoring.pixel_matching.pixel_matching as pm
from readability.ocr import ocr_bet
from readability.read_cards import read_and_save_my_cards
from readability.fix_game_disruption import fix_game_disruption, screenshot_error
#importing same level directory modules
import config as c
from iprint import shout
from set_variables import determine_small_big_dealer_seats,\
reset_table_information, read_and_save_banks_and_names
from main_assist import *

def wait_hand_ends_when_observing(waiting_minutes = 5):
    shout('waiting till current hand ends...')
    t1 = time.time()
    fixing_retry = 1
    while True:
        c.new_hand = hand_is_ended()
        if c.new_hand:
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
            shout ("-------- Hand ended --------", color = 'on_green')
            break
        if (time.time()-t1) > ((60*waiting_minutes)/4) and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()
        if time.time() - t1 > 60 * waiting_minutes :
            c.bot_status = 'ON_MAIN_MENU'
            shout("No hand ending after %s minutes, "\
            	  "call operator to go to main menu" %waiting_minutes)
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def wait_new_hand_starts_when_observing(waiting_minutes = 30):
    shout('waiting new hand starts by looking for dealer button...')
    t1 = time.time()
    fixing_retry = 1
    while True:
        if sb_b_d_buttons_are_founded():
            break
        if (time.time()-t1) > ((60*waiting_minutes)/4) and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()
        if time.time() - t1 > 60 * waiting_minutes :
            c.bot_status = 'ON_MAIN_MENU'
            shout("No one join the table after %s minutes, "\
                  "call operator to go to main menu" %waiting_minutes)
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 


def am_i_in_or_not():

    for i in range(1, config.TOTAL_SEATS+1):
        if pm.i_am_seated_pixel(c.game_position, i) :
            c.my_seat_number = i
            return True
    c.my_seat_number = None
    return False

def set_seats_not_folded_dictionary():
    #global seats_not_folded
    c.seats_not_folded = {}
    for seat in range(1, c.TOTAL_SEATS+1):
        c.seats_not_folded[seat] = pm.player_cards_pixel(c.game_position, seat)

def first_player_seat(): 

    if c.preflop_stage == True and c.flop_stage == False :
        on_preflop = True
    else :
        on_preflop = False

    if on_preflop == True :
        return c.big_blind_seat + 1
    elif on_preflop == False and c.small_blind_seat != c.dealer_seat : 
        return c.small_blind_seat 
    #2 players # The rules may differs on the other websites for 2 players.
    elif on_preflop == False and c.small_blind_seat == c.dealer_seat : 
        return c.big_blind_seat

def turn_finder(starter_seat , xth) :
    """Returns the seat number; for instance; (4,1) returns seat 4!"""
    answer = (starter_seat - 1 + xth ) % 5
    if answer == 0 :
        return 5
    else :
        return answer

def find_seat_to_report(acted_players):

    i = not_folded_count = 0
    while True:
        i += 1
        seat_to_report = turn_finder(first_player_seat(), i)
        if c.seats_not_folded[seat_to_report]:
            not_folded_count += 1
        if not_folded_count == acted_players + 1:
            return seat_to_report
        # To make sure while True does not loop infinitively.
        if acted_players < 0:
            shout('A mistake must have happened')
            break

def ready_to_report(seat_to_report):
    """Target player is ready to report when he is not deciding"""
    return not pm.active_player_pixel(c.game_position, seat_to_report)

def report_the_player(seat_to_report):
    #global seats_not_folded
    if not pm.player_cards_pixel(c.game_position, seat_to_report):
        c.seats_not_folded[seat] = False
        shout('Seat %s has folded' %seat_to_report, color = 'light_cyan')
    elif not pm.player_chips_pixel(c.game_position, seat_to_report):
        shout('Seat %s has checked' %seat_to_report, color = 'light_cyan')
    # It happens for big blind seat at preflop stage.
    elif (not pm.are_chips_white_or_red_pixel(c.game_position, seat_to_report) 
          and seat_to_report == c.big_blind_seat ):
        shout('Seat %s has checked' %seat_to_report, color = 'light_cyan')
    elif not pm.are_chips_white_or_red_pixel(c.game_position, seat_to_report):
        shout('Seat %s has called' %seat_to_report, color = 'light_cyan')
    elif pm.are_chips_white_or_red_pixel(c.game_position, seat_to_report):
        bet = ocr_bet(seat_to_report)
        shout('Seat %s has raised %s' %(seat_to_report, bet), color = 'light_cyan')






def bot_is_observing():
    wait_hand_ends_when_observing(waiting_minutes = 30)
    while True:
        if c.bot_status != 'OBSERVING': 
            break
        shout("* bot_status == 'OBSERVING' *",color = 'on_green')
        reset_table_information()
        wait_new_hand_starts_when_observing(waiting_minutes = 30)
        shout ("-------- New Hand Started --------", color = 'on_green')
        if c.bot_status != 'OBSERVING':
            break
        # use this statement after waiting functions 
        # which uses c.new_hand = hand_is_ended()
        if c.new_hand: 
            continue
        determine_small_big_dealer_seats()
        if am_i_in_or_not():
            if pm.player_cards_pixel(c.game_position
                                     , c.my_seat_number):
                read_and_save_my_cards()
                play_sound_for_good_starting_hands()
        read_and_save_banks_and_names()

        # Playing a whole hand in this loop
        observing_a_hand()
        if c.bot_status != 'OBSERVING':
            break
        if c.new_hand: 
            continue
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def observing_a_hand():
    """Use wait_hand_ends_when_observing() before all breaks, 
    except one which ended without any problem.
    """

    set_seats_not_folded_dictionary()
    acted_players = 0
    t1 = time.time()
    while True:
        if shifted_to_next_stage():
            acted_players = 0
            read_board_cards()
            if not stages_are_sequenced():
                shout("Stages are not sequenced",color = 'on_light_red')
                screenshot_error('stages are not sequenced')
                wait_hand_ends_when_observing(waiting_minutes = 30)
                break # new line
        seat_to_report = find_seat_to_report(acted_players)
        if ready_to_report(seat_to_report):
            acted_players += 1
            report_the_player(seat_to_report) #🗺️ 💎♣💎♠💎♦💎♥💎 🗺️ 
            #update_betting_rounds()
            #read_and_save_bets()
        if t1 - time.time() > 5 * 60:
            c.bot_status = 'WAITING_FOR_FIRST_HAND'
            fix_game_disruption('This hand last more than 5 minutes')
            wait_hand_ends_when_observing(waiting_minutes = 30)
            break # new line
        c.new_hand = hand_is_ended()
        if c.new_hand:
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
            # Hand is ended without any problem. Save statistical data here.
            shout('I should save statistical data here later.', 'rainbow')
            shout ("-------- Hand ended --------", color = 'on_green')
            break
        if c.bot_status != 'OBSERVING': # will not be used
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            if c.bot_status == 'OBSERVING':
                wait_hand_ends_when_observing(waiting_minutes = 30)
            break 

