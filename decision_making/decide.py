import pickle, os
from pathlib import PurePath
from decision_making.play import *
#from play import * 

def load_variables():
    """ variables order is important while loading """
    global game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat

    current_path = os.path.abspath(os.path.dirname(__file__)) 
    pickle_path = PurePath(current_path).parent / 'pickled variables.p'

    game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat = \
    pickle.load( open( str(pickle_path), "rb" ) )

def decide():
    load_variables()

    if preflop_stage == True and flop_stage == False : # instead i can use FUNCTIONS_table_information.Pre_Flop_Deside() too
        shout(paint.light_cyan.bold("*Deciding on preflop*"))
    elif flop_stage == True and turn_stage == False :
        shout(paint.light_cyan.bold("*Deciding on flop*"))
    elif turn_stage == True and river_stage == False :
        shout(paint.light_cyan.bold("*Deciding on turn*"))
    elif river_stage == True :
        shout(paint.light_cyan.bold("*Deciding on river*"))
    else :
        shout(paint.light_cyan.bold("*Deciding on unknown*"))
    
    if just_do_check_fold == True :
        return ("check_fold")

    else :


        if play_hand5_no_raiser() != False :
            return play_hand5_no_raiser()

        elif play_hand4() != False :
            return play_hand4()

        elif play_hand3() != False :
            return play_hand3()
            
        elif play_hand2() != False :
            return play_hand2()

        elif play_hand1() != False :
            return play_hand1()

        elif play_3_of_kind() != False :
            return play_3_of_kind()

        elif play_straight() != False :
            return play_straight()

        elif play_flush() != False :
            return play_flush()

        elif play_individual_cards() != False :
            return play_individual_cards()

        elif play_1_pair() != False :
            return play_1_pair()

        elif play_2_pair() != False :
            return play_2_pair()

        elif play_full_house() != False :
            return play_full_house()

        elif play_4_of_kind() != False :
            return play_4_of_kind()

        elif play_pre_flop() != False :
            return play_preflop()

        elif play_flop() != False :
            return play_flop()

        elif play_turn() != False :
            return play_turn()

        elif play_river() != False :
            return play_river()

        else :
            return ("not defined")

