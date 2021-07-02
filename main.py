"""
#Important#
When play.py module is completed, 
change these 2 functions by uncommenting some lines inside them:
1. click_decision() at main_assit.py
2. decide() at decide.py

delete lines with #❌⛏❌ comment at this file when play.py is completed.
"""
import time

import win32gui, win32con 
import pandas as pd

import screen_monitoring.find_game_position.find_game_position as find_game_position
import decision_making.play
from decision_making.rules_and_info.table_information import Flop_Deside #❌⛏❌
from readability.read_cards import read_and_save_my_cards
from readability.fix_game_disruption import fix_game_disruption,\
set_just_do_check_fold_to_true, screenshot_error
from hand_history_data_base.append_to_csv import append_new_line_to_csv
#importing same level directory modules
import configs as c
from iprint import shout
from set_variables import set_all_variables_to_none, read_and_save_bets,\
determine_small_big_dealer_seats, determine_playing_seats,\
reset_table_information, read_and_save_banks_and_names
from observing import bot_is_observing
from main_assist import *

def bot_is_on_main_menu():
    shout("* bot_status == 'ON_MAIN_MENU' *", color = 'on_green')
    raise Exception("5.This can not happen IN FUTURE because main "\
                    "menu automation is built " \
                    "( fix_game_disruption --> Sit_In --> "\
                    "table is full --> exit --> "\
                    "c.bot_status = 'ON_MAIN_MENU' --> main menu "\
                    "--> c.bot_status = 'WAITING_FOR_FIRST_HAND' )")

def bot_is_waiting_till_next_hand():
    """
    Bot is suspended automatically from decide.py module for a hand 
    so operator can play that hand manually.
    This situation should happen when decision_making package is 
    *under construction* and can not play some scenarios. 
    The bot_status is change to 'OPERATOR_IS_PLAYING_THE_HAND' in 
    decide.py module so that the operator plays the hand.
    In this bot_status, the bot will not look for buttons and will not run 
    fix_game_disruption() anymore. The bot just waits for the next hand.

    #IMPORTANT# 
    If this bot_status is added to decide function at decide.py, bot will 
    acts like a copilot and operator must always beware and plays some hands 
    beside the bot.
    """
    shout("* bot_status == 'OPERATOR_SHOULD_PLAY_THE_HAND' *",color ='on_green')
    sound('Play yourself')
    shout('OPERATOR MUST PLAY THIS HAND!', color = 'rainbow', save = False)
    wait_hand_ends(waiting_minutes = 5)  
    c.bot_status = 'WAITING_FOR_FIRST_HAND'
    fix_game_disruption("Game was played manually for a hand")

def bot_is_waiting_for_first_hand():
    """
    Why do we need to have 'WAITING_FOR_FIRST_HAND' status?
    Answer: Because we may need to wait for several hands before we start  
    our first hand and wait_for_my_first_hand() will not break by new hands.
    """ 
    shout("* bot_status == 'WAITING_FOR_FIRST_HAND' *",color = 'on_green')
    rebuy_if_bank_is_low(min_blinds = 15)
    wait_for_my_first_hand(waiting_minutes = 8)

def bot_is_playing():
    while True:
        c.new_hand = hand_is_ended()
        if c.new_hand: 
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
        c.hand_number += 1
        reset_table_information()
        shout("* bot_status == 'I_AM_PLAYING' *",color = 'on_green')
        wait_for_my_new_hand(waiting_minutes = 10)
        # use this statement after functions which use fix_game_disruption()
        if c.bot_status != 'I_AM_PLAYING': 
            break
        # use this statement after waiting functions 
        # which uses c.new_hand = hand_is_ended()
        if c.new_hand: 
            continue
        shout ("-------- New Hand Started --------", color = 'on_green')
        wait_for_sb_b_d_buttons(waiting_seconds = 5) 
        if c.bot_status != 'I_AM_PLAYING':
            break
        determine_small_big_dealer_seats()
        determine_playing_seats()
        # In case bot is resumed:
        if not first_round_at_preflop():
            set_just_do_check_fold_to_true("program must've started "\
                                           "again from middle of the game")
        read_and_save_my_cards()
        rebuy_if_bank_is_low(min_blinds = 15)
        read_and_save_banks_and_names()
        if c.bot_status != 'I_AM_PLAYING': 
            break
        play_sound_for_good_starting_hands()
        shout("Waiting for my turn at preflop_stage...", 'light_magenta') 
        # Playing a whole hand in this loop
        play_a_hand()
        if c.bot_status != 'I_AM_PLAYING':
            break
        if c.new_hand: 
            continue
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def play_a_hand():
    t1 = time.time()
    while True:
        if shifted_to_next_stage():

            if Flop_Deside() and c.last_player_cards_cache[c.my_seat_number]: #❌⛏❌
                # I MUST PLAY SOUND #❌⛏❌
                sound('Schiller Nachtflug') #❌⛏❌

            read_board_cards()
            if not stages_are_sequenced():
                set_just_do_check_fold_to_true('stages are not sequenced')
                screenshot_error('stages are not sequenced')
        if its_my_turn():
            update_betting_rounds()
            read_and_save_bets()
            read_banks()
            if c.bot_status == 'I_AM_PLAYING':
                click_decision() #🌏🌱♣♠♦♥🌱🌏
        if t1 - time.time() > 5 * 60:
            c.bot_status = 'WAITING_FOR_FIRST_HAND'
            fix_game_disruption('This hand last more than 5 minutes')
        c.new_hand = hand_is_ended()
        if c.new_hand:
            shout ("appending hand data to csv file", color = 'on_green')
            append_new_line_to_csv(c.csv_path) 
            shout ("-------- Hand ended --------", color = 'on_green')
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 
        if c.bot_status != 'I_AM_PLAYING':
            break

def start_the_bot():
    while True:
        # Changes when time runs out or when doing some game fixing issues.
        if c.bot_status == 'ON_MAIN_MENU':
            bot_is_on_main_menu()
        # Changes when game is paused, and changes back 
        # to 'WAITING_FOR_FIRST_HAND' status only when game is unpaused.
        elif c.bot_status == 'OBSERVING':
            bot_is_observing()
        # Initial value. Changes when game is unpaused.
        # Also changes when time runs out or when doing some game fixing 
        # issues (In other cases than 'ON_MAIN_MENU' status) 
        elif c.bot_status == 'WAITING_FOR_FIRST_HAND':
            bot_is_waiting_for_first_hand()
        # Changes when my first hand by my cards pixels is appeared
        # after 'WAITING_FOR_FIRST_HAND' status.
        elif c.bot_status == 'I_AM_PLAYING':
            bot_is_playing()
        # Changes when decide function encountered deficiency. And then changes
        # back to 'WAITING_FOR_FIRST_HAND' status when hand is finished.
        # When ever i complete the play module, I won't use this status anymore.
        elif c.bot_status == 'OPERATOR_SHOULD_PLAY_THE_HAND':
            bot_is_waiting_till_next_hand()
        else:
            raise Exception("bot_status can be only 'ON_MAIN_MENU' or "\
                            "'OBSERVING' or 'OPERATOR_SHOULD_PLAY_THE_HAND' "\
                            "or 'WAITING_FOR_FIRST_HAND' or 'I_AM_PLAYING'")

def main():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)
    # Cleaning variables off the last run by set them all to None.
    set_all_variables_to_none()
    create_report_folder()
    # Initial values:
    c.MY_PROFILE_NAME = "XOwl"
    c.hand_number = 0
    c.csv_path = 'hand_history_data_base/hands history version %s.csv'\
                      %decision_making.play.VERSION
    try:
        df = pd.read_csv(c.csv_path)
        c.game_number = df.at[df.index[-1], 'Game number'] + 1
    except:
        c.game_number = 1
    if input("Is my name: %s ?(Enter:yes/any keyword:no)" 
             % c.MY_PROFILE_NAME) != "" :
        c.MY_PROFILE_NAME = input("Enter profile name: ")
    c.my_seat_number = 1 #int( input("My seat number? ") ) #💊
    c.TOTAL_SEATS = 5
    c.BLIND_VALUE = 100000000
    c.bot_status = 'WAITING_FOR_FIRST_HAND'
    c.game_position = find_game_position.find_game_reference_point()

    start_the_bot()

if __name__ == '__main__':
    main()
