"""
TODO:
Add 'fold' header with True or False values to csv too.
"""
import os
from datetime import datetime

import pandas as pd

import config as c
import decision_making.play
from readability.ocr import ocr_my_bank
from decision_making.rules_and_info.table_information import \
early_position, middle_position, late_position
import decision_making.rules_and_info.starting_hands as hand
def is_file_empty(csv_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # https://thispointer.com/python-three-ways-to-check-if-a-file-is-empty/
    # Create file if file does not exist
    if not os.path.exists(csv_path):
        open(csv_path, "w")
    return os.stat(csv_path).st_size == 0

def append_new_line_to_csv(csv_path):
    # https://www.w3resource.com/python-exercises/pandas/python-pandas-data-frame-exercise-26.php
    if c.scenario_list == []:
        c.scenario_list = [None]
    if is_file_empty(csv_path):
        new_line = {
            'Hand number': [c.hand_number],
            # If bank is in big blinds. Depends on the site.  
            'Winning bb': [won_money()], 
            'Cards': [hand.change_hand_format(c.my_1th_card, c.my_2th_card)], 
            'Hand category': [hand_category()], 
            'Starting hand ranking': [hand.holdem_starting_hand_ranking()],
            'Check fold': [c.just_do_check_fold], 
            # If bank is in big blinds. Depends on the site.
            'Money profit': [won_money() * c.BLIND_VALUE], 
            'Scenario list': [c.scenario_list],
            'First scenario': [c.scenario_list[0]], 
            'Last scenario': [c.scenario_list[-1]], 
            'Last 2 scenarios': [c.scenario_list[-2:]], 
            'play version': [decision_making.play.VERSION], 
            'Blind': [c.BLIND_VALUE], 
            'Seat position': [seat_position()], 
            'Small blind': [c.my_seat_number == c.small_blind_seat], 
            'Big blind': [c.my_seat_number == c.big_blind_seat], 
            'dealer': [c.my_seat_number == c.dealer_seat], 
            'Total players': [c.TOTAL_SEATS], 
            'Website': ['cheeta'], 
            'Game number': [1], 
            'Game time': [game_time()]
            }
        df = pd.DataFrame(new_line, index=[0])
        #df = df.astype(int)
        df.to_csv(csv_path, index = False)
    else:
        new_line = {
            'Hand number': c.hand_number,
            # If bank is in big blinds. Depends on the site.
            'Winning bb': won_money(), 
            'Cards': hand.change_hand_format(c.my_1th_card, c.my_2th_card), 
            'Hand category': hand_category(), 
            'Starting hand ranking': hand.holdem_starting_hand_ranking(),
            'Check fold': c.just_do_check_fold, 
            # If bank is in big blinds. Depends on the site.
            'Money profit': won_money() * c.BLIND_VALUE, 
            'Scenario list': c.scenario_list,
            'First scenario': [c.scenario_list[0]], 
            'Last scenario': [c.scenario_list[-1]], 
            'Last 2 scenarios': c.scenario_list[-2:],
            'play version': decision_making.play.VERSION, 
            'Blind': c.BLIND_VALUE, 
            'Seat position': seat_position(), 
            'Small blind': c.my_seat_number == c.small_blind_seat, 
            'Big blind': c.my_seat_number == c.big_blind_seat, 
            'dealer': c.my_seat_number == c.dealer_seat, 
            'Total players': c.TOTAL_SEATS, 
            'Website': 'cheeta', 
            'Game number': c.game_number, 
            'Game time': game_time()
            }
        df = pd.read_csv(csv_path)
        df = df.append(new_line, ignore_index=True)
        #df = df.astype(int)
        try:
            df.to_csv(csv_path, index = False)
        except PermissionError:
            print('close the csv file')
            pass

    #print(df)

def hand_category():
    overlap_hand = ''
    if hand.hand8() and  hand.hand9():
        overlap_hand = ' hand8 hand9'
    elif  hand.hand8():
        overlap_hand = ' hand8'
    elif  hand.hand9():
        overlap_hand = ' hand9'

    if  hand.hand1():
        return 'hand1%s' %overlap_hand
    elif  hand.hand2():
        return 'hand2%s' %overlap_hand
    elif  hand.hand3():
        return 'hand3%s' %overlap_hand
    elif  hand.hand4():
        return 'hand4%s' %overlap_hand
    elif  hand.hand5():
        return 'hand5%s' %overlap_hand
    elif  hand.hand6():
        return 'hand6%s' %overlap_hand
    elif  hand.hand7():
        return 'hand7%s' %overlap_hand
    else:
        return None

def seat_position():
    if early_position():
        return 'early_position'
    elif middle_position():
        return 'middle_position'
    elif late_position():
        return 'late_position'

def game_time():
    hour = datetime.now().strftime("%H")
    hour = int(hour)
    if 3 <= hour < 9:
        return '3-9'
    elif 9 <= hour < 15:
        return '9-15'
    elif 15 <= hour < 21:
        return '15-21'
    elif 21 <= hour <= 24 or hour < 3:
        return '21-3'

def won_money():
    my_old_bank = c.players_bank[c.my_seat_number]
    my_new_bank = ocr_my_bank()
    if None in (my_old_bank, my_new_bank):
        return None
    else:
        won = my_new_bank - my_old_bank
        return round(won, 2)

#append_new_line_to_csv('data w14.csv')
