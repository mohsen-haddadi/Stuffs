import time

import win32gui, win32con 

import screen_monitoring.find_game_position.find_game_position as find_game_position
from readability.read_cards import read_and_save_my_cards
from readability.fix_game_disruption import fix_game_disruption,\
set_just_do_check_fold_to_true, screenshot_error
#importing same level directory modules
import config
from iprint import shout
from set_variables import set_all_variables_to_none, read_and_save_bets,\
determine_small_big_dealer_seats, reset_table_information,\
read_and_save_banks_and_names
from main_assist import *

def bot_is_on_main_menu():
    shout("* bot_status == 'ON_MAIN_MENU' *", color = 'on_green')
    raise Exception("5.This can not happen IN FUTURE because main "\
                    "menu automation is built " \
                    "( fix_game_disruption --> Sit_In --> "\
                    "table is full --> exit --> "\
                    "config.bot_status = 'ON_MAIN_MENU' --> main menu "\
                    "--> config.bot_status = 'WAITING_FOR_FIRST_HAND' )")

def bot_is_waiting_for_first_hand():
    """
    Why do we need to have 'WAITING_FOR_FIRST_HAND' status?
    Answer: Because we may need to wait for several hands before we start  
    our first hand and wait_for_my_first_hand() will not break by new hands.
    """ 
    shout("* bot_status == 'WAITING_FOR_FIRST_HAND' *",color = 'on_green')
    rebuy_if_bank_is_low(min_blinds = 15)
    wait_for_my_first_hand(waiting_minutes = 5)

def bot_is_playing():
    while True:
        config.new_hand = hand_is_ended()
        if config.new_hand: 
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
        reset_table_information()
        shout("* bot_status == 'I_AM_PLAYING' *",color = 'on_green')
        wait_for_my_new_hand(waiting_minutes = 10)
        # use this statement after functions which use fix_game_disruption()
        if config.bot_status != 'I_AM_PLAYING': 
            break
        # use this statement after waiting functions 
        # which uses config.new_hand = hand_is_ended()
        if config.new_hand: 
            continue
        shout ("-------- New Hand Started --------", color = 'on_green')
        wait_for_sb_b_d_buttons(waiting_seconds = 5) 
        if config.bot_status != 'I_AM_PLAYING':
            break
        determine_small_big_dealer_seats()
        # In case bot is resumed:
        if not first_round_at_preflop():
            set_just_do_check_fold_to_true("program must've started "\
                                           "again from middle of the game")
        read_and_save_my_cards()
        rebuy_if_bank_is_low(min_blinds = 15)
        read_and_save_banks_and_names()
        if config.bot_status != 'I_AM_PLAYING': 
            break
        play_sound_for_good_starting_hands()
        shout("Waiting for my turn at preflop_stage...", 'light_magenta') 
        # Playing a whole hand in this loop
        play_a_hand()
        if config.bot_status != 'I_AM_PLAYING':
            break
        if config.new_hand: 
            continue
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 

def play_a_hand():
    t1 = time.time()
    while True:
        if shifted_to_next_stage(): 
            read_board_cards()
            if not stages_are_sequenced():
                set_just_do_check_fold_to_true('stages are not sequenced')
                screenshot_error('stages are not sequenced')
        if its_my_turn():
            update_betting_rounds()
            read_and_save_bets()
            if config.bot_status == 'I_AM_PLAYING':
                click_decision() #🌏🌱♣♠♦♥🌱🌏
        if t1 - time.time() > 5 * 60:
            fix_game_disruption('This hand last more than 5 minutes')
        config.new_hand = hand_is_ended()
        if config.new_hand:
            shout ("-------- Hand ended --------", color = 'on_green')
            break
        if config.bot_status != 'I_AM_PLAYING':
            break
        if game_is_paused():
            input("press Enter to start again...") 
            fix_game_disruption('game is unpaused')
            break 

def start_the_bot():
    while True:

        if config.bot_status == 'ON_MAIN_MENU':
            bot_is_on_main_menu()
        elif config.bot_status == 'WAITING_FOR_FIRST_HAND':
            bot_is_waiting_for_first_hand()
        elif config.bot_status == 'I_AM_PLAYING':
            bot_is_playing()
        else:
            # Develop 'OBSERVING' status for bot_status later.
            # 'OBSERVING' status can be used to test screen monitoring or to
            # get opponents playing styles or to gather statistical data.
            raise Exception("bot_status can be only 'ON_MAIN_MENU' or "\
                            "'WAITING_FOR_FIRST_HAND' or 'I_AM_PLAYING'")

def main():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)
    # Cleaning variables off the last run by set them all to None.
    set_all_variables_to_none()
    create_report_folder()
    # Initial values:
    config.MY_PROFILE_NAME = "XOwl"
    if input("Is my name: %s ?(Enter:yes/any keyword:no)"%config.MY_PROFILE_NAME) != "" :
        config.MY_PROFILE_NAME = input("Enter profile name: ")
    config.my_seat_number = 2 #int( input("My seat number? ") )
    config.TOTAL_SEATS = 5
    config.BLIND_VALUE = 100000000
    config.bot_status = 'WAITING_FOR_FIRST_HAND'
    config.game_position = find_game_position.find_game_reference_point()

    start_the_bot()

if __name__ == '__main__':
    main()
