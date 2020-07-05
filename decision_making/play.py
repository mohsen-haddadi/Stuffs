import pickle, os
from pathlib import PurePath

from decision_making.rules_and_info.table_information import *
from decision_making.rules_and_info.straight import *
from decision_making.rules_and_info.flush import *
from decision_making.rules_and_info.non_straight_and_flush import *
from decision_making.rules_and_info.suit_and_value import *
from decision_making.rules_and_info.starting_hands import *

#from rules_and_info.table_information import *
#from rules_and_info.straight import *
#from rules_and_info.flush import *
#from rules_and_info.non_straight_and_flush import *
#from rules_and_info.suit_and_value import *
#from rules_and_info.starting_hands import *


"""
some Play functions are in calendare. add them here later
Me_str() or Me_Flush() can overlap lower than Me_full_house() (Except Me_str() and Me_2_pair() won't overlap) 
so for all functions lower than Me_full_house() like: 1. Play_hand5_no_raiser() and 2. Play_1_pair() .... , (Me_str() or Me_Flush()) are excluded.
"""

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


def bluff_table_flush_4_cards():
    load_variables()

    if River_Deside() and Table_Flush_4_cards() and not Me_str() and not Me_Flush() and Me_Individual() \
    and ( Table_Individual() or Table_1_pair() ) and Table_str_1_cards_Number()\
    and last_raise_at("River") == 0 and last_raise_at("Turn") == 0 and last_raise_at("Flop") <= 4 * BLIND_VALUE and last_raise_at("Pre_Flop") <= 4 * BLIND_VALUE :
        shout("Bluffing table flush 4 cards")
        return True
    else :
        return False

def play_hand5_no_raiser(): # Check the logic
    """ 
    lower than or 1 pair, but overall full house or overall 4 of kind are possible 
    so if hand5() is True, Play_individual_cards() and Play_1_pair() should not run anyway.
    """
    load_variables()

    if not hand5() or Any_raiser_sofar() or ( not Pre_Flop_Deside() and not Me_Individual() and not Me_1_pair() ) or \
    ( not Pre_Flop_Deside() and (Me_str() or Me_Flush()) ) :
        return False

    elif Pre_Flop_Deside() :

        return ("raise", 3)

    elif Flop_Deside() :

        if bluff_hand5_flop_table_2_cards() :

            return ("raise", 4)

        elif Me_Individual() or Table_1_pair() or ( Me_1_pair() and Me_1_pair_Ranking()[0] > 1 ) :

            return ("check")

        elif Me_1_pair() and Me_1_pair_Ranking()[0] == 1 :

            return ("raise", 3)

    elif Turn_Deside() :

        if Me_Individual() or ( Table_1_pair() and not did_i_raise_at("Flop") ) or \
        ( Me_1_pair() and   ( Me_1_pair_Ranking()[0] > 2 or ( Me_1_pair_Ranking()[0] == 2 and Table_1_pair() ) )   )  or\
        Table_str_1_cards_Number() == 2 or Table_Flush_4_cards() :

            return ("check")

        else :

            return ("raise", 3)

    elif River_Deside() :

        if bluff_table_flush_4_cards() :

            return ("raise", 2)

        elif am_i_last_player_by_seat_order() or Me_Individual() or ( Table_1_pair() and not did_i_raise_at("Turn") ) or\
        ( Me_1_pair() and Me_1_pair_Ranking()[0] != 1 and not did_i_raise_at("Turn") ) or\
        Table_str_1_cards_Number() == 2 or Table_Flush_4_cards() or Table_Flush_5_cards() :

            return ("check")

        else :

            return ("raise", 3)

    def bluff_hand5_flop_table_2_cards(): # define it inside the function
        load_variables()

        if Flop_Deside() and not Any_raiser_sofar() and hand5() and ( Table_1_pair() or Table_3_of_kinds() ) and Me_Individual() :
            shout("Bluffing hand5 flop table 2 cards")
            return True
        else :
            return False

#def play_hand4():
#
#def play_hand3():
#
#def play_hand2():
#
#def play_hand1():

def play_individual_cards():

    load_variables()

    if Any_raiser_sofar() or Pre_Flop_Deside() or hand5() or not Me_Individual() or\
    ( Me_str() or Me_Flush() ) :
        return False

    elif Flop_Deside() or Turn_Deside() :

        if bluff_table_1_pair() and not did_i_raise_sofar() :
            return ("raise", 2)
        else :
            return ("check")

    elif River_Deside() :

        if bluff_table_flush_4_cards() :
            return ("raise", 2)
        if bluff_table_1_pair() and not did_i_raise_sofar() :
            return ("raise", 2)
        elif ( Table_4_of_kinds() and max( n(my_1th_card) , n(my_2th_card) ) in (14,13) ) :
            return ("raise", 1)
        else :
            return ("check")



    def bluff_table_1_pair() :
        load_variables()

        if not Pre_Flop_Deside() and Me_Individual() and Table_1_pair() and not Any_raiser_sofar() :
            shout("Bluffing table 1 pair")
            return True
        else :
            return False

def play_1_pair():
    """
    Only with Rank == 1 will be bet. if Kicker card was good bet 2*BLIND_VALUE if not bet 1*BLIND_VALUE
    Easily in case of danger like Table flush 4 or 5 cards ,or str 1 cards == 2  ;it will be checked 
    """
    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or hand5() or ( Me_str() or Me_Flush() ) :
        return False
    elif not Me_1_pair() : 
        return False

    elif Flop_Deside() :

        if Table_1_pair() :

            return ("check")

        elif Me_1_pair_Ranking()[1] >= 10 and Me_1_pair_Ranking()[0] == 1 :

            return ("raise", 2)

        elif Me_1_pair_Ranking()[0] == 1 :

            return ("raise", 1)

        else :

            return ("check")

    elif Turn_Deside() :

        if Table_1_pair() or Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 :

            return ("check")

        elif Me_1_pair_Ranking()[1] >= 10 and Me_1_pair_Ranking()[0] == 1 :

            return ("raise", 2)

        elif Me_1_pair_Ranking()[0] == 1 :

            return ("raise", 1)

        else :

            return ("check")

    elif River_Deside() :

        if Table_1_pair() or Table_2_pair() or Me_1_pair_Ranking()[0] != 1 or\
        Table_Flush_4_cards() or Table_Flush_5_cards() or Table_str_1_cards_Number() == 2 or\
        ( am_i_last_player_by_seat_order() and did_i_raise_sofar() ) :

            return ("check")

        elif Me_1_pair_Ranking()[1] >= 10 :

            return ("raise", 2)

        else :

            return ("raise", 1)

def play_2_pair():

    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or ( Me_str() or Me_Flush() ) :
        return False
    elif not Me_2_pair() : 
        return False

    elif Flop_Deside() :

        return ("raise", 3)

    elif Turn_Deside() :

        if Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 or\
        ( Table_1_pair() and ( not did_i_raise_sofar() or Me_2_pair_Ranking()[0] > 1 ) ) :

            return ("check")

        else :

            return ("raise", 3)

    elif River_Deside() :

        if Table_Flush_4_cards() or Table_Flush_5_cards() or Table_str_1_cards_Number() == 2 or\
        ( Table_1_pair() and ( not did_i_raise_sofar() or Me_2_pair_Ranking()[0] > 1 or am_i_last_player_by_seat_order() ) ) :

            return ("check")

        elif not Table_str_1_cards() and not Table_str_2_cards() and not Table_Flush() and not Table_1_pair() and\
        not Table_3_of_kinds() and Me_2_pair_Ranking() in [(1,2),(1,3),(1,4)] :

            return ("raise", 9)

        else :

            return ("raise", 3)

def play_3_of_kind():

    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or ( Me_str() or Me_Flush() ) :
        return False
    elif not Me_3_of_kinds() : 
        return False

    elif Flop_Deside() :

        if did_i_raise_at("Pre_Flop") :
            return ("raise", 3)

        else :

            shout("Check and Raise Strategy")
            return ("check")

    elif Turn_Deside() :

        if Me_3_of_kinds_Ranking()[0] == 2 and not did_i_raise_at("Flop") :

            return ("check")

        elif Me_3_of_kinds_Ranking()[0] == 2 :

            shout("Anti Bluff bet")
            return ("raise", 3)

        elif Me_3_of_kinds_Ranking()[0] == 1 and not Me_3_of_kinds([board_card_1th , board_card_2th , board_card_3th]) and not did_i_raise_sofar() :

            shout("Check and Raise Strategy")
            return ("check")

        elif Me_3_of_kinds_Ranking()[0] == 1 :

            return  ("raise", 3)
       

    elif River_Deside() :

        if ( Me_3_of_kinds_Ranking()[0] == 2 or Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 ) and\
        ( am_i_last_player_by_seat_order() or ( not am_i_last_player_by_seat_order() and not did_i_raise_at("Flop") ) ) :

            shout("Check Weak Me_3_of_kinds")
            return ("check")

        elif Me_3_of_kinds_Ranking()[0] == 2 or Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 :

            shout("Anti Bluff bet")
            return ("raise", 3)

        #Rank == 2 finished.
        elif Table_2_pair() and Me_3_of_kinds_Ranking()[0] == 1 and\
        ( Table_Individual_Cards_List()[0] < min( Table_2_same_Cards_List()[0] and Table_2_same_Cards_List()[1] ) ) :

            shout("Best hand of full house")
            return ("raise", 6)

        else : 

            shout("Bet Normal Me_3_of_kinds hand")
            return ("raise", 3) #Table_full_house is possible too

def play_straight():
    """
    If Me_str() is True, functions lower than Me_full_house() like : 1. Play_hand5_no_raiser() and 2. Play_1_pair()... should return False
    """
    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or Me_Flush() or not Me_str() :
        return False

    elif Flop_Deside() :

        shout("Low bet and Raise Strategy")
        return ("raise", 3)

    elif Turn_Deside() :

        if Table_Flush_4_cards() or ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 2 ) or\
        ( Me_str_2_cards() and is_there_any_better_possible_1_card_straight_on_table() ) :

            shout("Check Weak Me_str hand")
            return ("check")

        elif not Table_Individual() or Table_Flush_3_cards() or\
        ( Me_str_2_cards() and Me_str_2_cards_Ranking() != 1 and not is_there_any_better_possible_1_card_straight_on_table() ) or\
        ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 and \
        Table_str_2_cards() and str_2_Cards_list([board_card_1th , board_card_2th , board_card_3th , board_card_4th])[0][0] > \
        str_1_Cards_list([board_card_1th , board_card_2th , board_card_3th , board_card_4th])[0] ) : #Avoid Me_str_1_cards 10 to Ace

            shout("Bet Normal Me_str hand")
            if Max_raise_sofar() <= 3 * BLIND_VALUE :

                return ("raise", 3)

            else :

                return ("raise", Max_raise_sofar() // BLIND_VALUE)

        elif Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_1_cards hand, 10 to Ace")
            if not did_i_raise_sofar() :

                return ("raise", 2) 

            else :

                shout("I can Bet more and better at the other sites")
                return ("raise", Max_raise_sofar() // BLIND_VALUE)

        elif Me_str_2_cards() and Me_str_2_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_2_cards hand")
            if not did_i_raise_sofar() :

                return ("raise", 4) 

            elif Max_raise_sofar() <=  3 * BLIND_VALUE :

                return ("raise", 6) 

            else :

                return ("raise", (2 * Max_raise_sofar()) // BLIND_VALUE)        

    elif River_Deside() :

        if Table_Flush_4_cards() or Table_Flush_5_cards() or Table_2_pair() or Table_3_of_kinds() or\
        ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 2 ) or\
        ( Me_str_2_cards() and is_there_any_better_possible_1_card_straight_on_table() ) :

            shout("Check or Anti Bluff Bet Weak Me_str hand")
            if Max_raise_sofar() >=  6 * BLIND_VALUE or am_i_last_player_by_seat_order() :

                return ("check")

            else :

                shout("Anti Bluff Bet")
                return ("raise", Max_raise_sofar() // BLIND_VALUE)    

        elif Table_Flush_3_cards() or Table_1_pair() or\
        ( Me_str_2_cards() and Me_str_2_cards_Ranking() != 1 and not is_there_any_better_possible_1_card_straight_on_table() ) or\
        ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 and \
        Table_str_2_cards() and str_2_Cards_list([board_card_1th , board_card_2th , board_card_3th , board_card_4th , board_card_5th])[0][0] > \
        str_1_Cards_list([board_card_1th , board_card_2th , board_card_3th , board_card_4th ,board_card_5th])[0] ) : #Avoid Me_str_1_cards 10 to Ace

            shout("Normal Me_str hand")
            if not did_i_raise_at("Turn") :

                return ("raise", 3) 

            elif did_i_raise_at("Turn") and am_i_last_player_by_seat_order() :

                shout("I can Bet it at the other sites")
                return ("check")

            elif did_i_raise_at("Turn") and not am_i_last_player_by_seat_order() :

                if Max_raise_sofar() <=  3 * BLIND_VALUE :
                    return ("raise", 3) 
                else :
                    return ("raise", Max_raise_sofar() // BLIND_VALUE)

        elif Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 :

            shout("Awesome Me_str_1_cards hand, 10 to Ace, Bet")
            if not did_i_raise_sofar() :

                return ("raise", 2) 

            else :

                shout("I can Bet more and better at the other sites")
                return ("raise", Max_raise_sofar() // BLIND_VALUE)

        elif Me_str_2_cards() and Me_str_2_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_2_cards hand")
            if not did_i_raise_sofar() :
                return ("raise", 4) 
            elif am_i_last_player_by_seat_order() :
                if Max_raise_sofar() <= 3 * BLIND_VALUE :
                    return ("raise", 6) 
                else :
                    return ("raise", (2 * Max_raise_sofar()) // BLIND_VALUE)    
            else :
                if Max_raise_sofar() <= 3 * BLIND_VALUE :
                    return ("raise", 9) 
                else : 
                    return ("raise", (4 * Max_raise_sofar()) // BLIND_VALUE)    

def play_flush():
    """
    If Me_Flush() is True, functions lower than Me_full_house() like : 1. Play_hand5_no_raiser() and 2. Play_1_pair()... should return False
    """
    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or not Me_Flush() :
        return False

    elif Flop_Deside() :

        shout("Low bet and Raise Strategy")
        return ("raise", 3) 

    elif Turn_Deside() :

        if Me_Flush_by_4_table_cards() :

            if Me_Flush_Ranking() <= 4 :

                shout("Weak Me_Flush hand")
                return ("check")

            elif 2 <= Me_Flush_Ranking() <= 3 :

                shout("Good Me_Flush hand")

                if am_i_last_player_by_seat_order() :

                    shout("I can Bet with 2 <= Rank <= 3 at the other sites")
                    return ("check")

                else :

                    return ("raise", Max_raise_sofar() // BLIND_VALUE)

            elif Me_Flush_Ranking() == 1 :

                shout("Awesome Me_Flush hand")

                if not did_i_raise_sofar() :

                    return ("raise", 2) 

                elif did_i_raise_sofar() :

                    shout("Low bet and Raise Strategy")
                    return ("raise", Max_raise_sofar() // BLIND_VALUE)

        elif Me_Flush_by_3_table_cards() :

            shout("A Good or Awesome Me_Flush hand")

            if Max_raise_sofar() <= 2 * BLIND_VALUE :

                return ("raise", 3) 

            elif Max_raise_sofar() >= 3 * BLIND_VALUE :

                return ("raise", (2 * Max_raise_sofar()) // BLIND_VALUE)    

    elif River_Deside() :

        if Table_3_of_kinds() or Table_2_pair() :

            shout("Weak Me_Flush hand")
            return ("check")

        elif ( Me_Flush_by_4_table_cards() or Me_Flush_by_5_table_cards() ) :

            if Me_Flush_Ranking() != 1 :

                shout("Weak Me_Flush hand") 

                if did_i_raise_at("Turn") and not am_i_last_player_by_seat_order() :

                    shout("Anti Bluff bet")
                    return ("raise", Max_raise_sofar() // BLIND_VALUE)

                elif not did_i_raise_at("Turn") or am_i_last_player_by_seat_order() :

                    shout("I can Bet with 2 <= Rank <= 3 at the other sites")
                    return ("check")

            if Me_Flush_Ranking() == 1 :

                if Table_1_pair() :

                    shout("Good Me_Flush hand")

                    if not did_i_raise_sofar() :
                        return ("raise", 2) 

                    elif did_i_raise_sofar() :
                        return ("raise", Max_raise_sofar() // BLIND_VALUE)

                elif not Table_1_pair() :

                    shout("Awesome Me_Flush hand")

                    if not did_i_raise_sofar() :
                        return ("raise", 2) 

                    elif did_i_raise_sofar() :
                        return ("raise", (2 * Max_raise_sofar()) // BLIND_VALUE)    

        elif Me_Flush_by_3_table_cards() :

            if Table_1_pair() :

                shout("Good Me_Flush hand")

                if not did_i_raise_sofar() :
                    return ("raise", 2) 

                elif did_i_raise_sofar() :
                    return ("raise", Max_raise_sofar() // BLIND_VALUE)

            elif not Table_1_pair() :

                shout("A Good or Awesome Me_Flush hand")

                if Me_Flush_Ranking() != 1 :
                    return ("raise", (2 * Max_raise_sofar()) // BLIND_VALUE)    

                elif Me_Flush_Ranking() == 1 :
                    return ("raise", (3 * Max_raise_sofar()) // BLIND_VALUE)    

def play_full_house():

    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or not Me_full_house() :
        return False

    elif Flop_Deside() :

        shout("check and raise strategy") # whether i've had raised at pre flop or not i check and raise
        return ("check")

    elif Turn_Deside() :

        if not did_i_raise_sofar() or Max_raise_sofar() <= 1 :
            return ("raise", 4)
        else :
            return ("raise", (3 * Max_raise_sofar()) // BLIND_VALUE)

    elif River_Deside() :

        if Me_full_house_Ranking() == 4 :
            if am_i_last_player_by_seat_order() or not did_i_raise_at("Turn") or Max_raise_sofar() >= 5 * BLIND_VALUE :
                return ("check")
            else :
                shout("Anti bluff raise")
                return ("raise", (Max_raise_sofar()) // BLIND_VALUE)
        elif not did_i_raise_sofar() or Max_raise_sofar() <= 3 * BLIND_VALUE :
            return ("raise", 9)
        else :
            return ("raise", (2 * Max_raise_sofar()) // BLIND_VALUE)

def play_4_of_kind():

    load_variables()

    if Pre_Flop_Deside() or Any_raiser_sofar() or not Me_4_of_kinds() :
        return False

    elif Flop_Deside() :

        if did_i_raise_sofar() :
            shout("Low bet and raise strategy")
            return ("raise", (Max_raise_sofar()) // BLIND_VALUE)   
        else :
            shout("check and raise strategy")
            return ("check")

    elif Turn_Deside():

        if did_i_raise_sofar() :
            shout("Low bet and raise strategy")
            return ("raise", (Max_raise_sofar()) // BLIND_VALUE)
        else :
            shout("Low bet and raise strategy")
            return ("raise", 2)

    elif River_Deside() :

        if did_i_raise_sofar() :
            return ("raise", (3 * Max_raise_sofar()) // BLIND_VALUE)
        else :
            return ("raise", 2)





#def play_pre_flop():
#
#def play_flop(): # write it in paper and then define it here
#
#def play_turn(): # write it in paper and then define it here
#
#def play_river(): # write it in paper and then define it here
#
#
#def overall_full_house(): # define it 1.here or 2.at supporting function(need to import FUNCTIONS_Pair file) or 3.define at FUNCTIONS_Pair file. NUMBER 3 IS THE BEST ANSWER
#
#def overall_4_of_kind(): # define it 1.here or 2.at supporting function(need to import FUNCTIONS_Pair file) or 3.define at FUNCTIONS_Pair file. NUMBER 3 IS THE BEST ANSWER
#it seemes there is no need to define functions overall_full_house() and overall_4_of_kind() at all (2019)
