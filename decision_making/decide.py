import pickle
from pathlib import Path
from decision_making.play import *
#from play import * 

def load_variables():
    """ variables order is important while loading """
    global game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    pickle_path = Path().absolute().parent / 'pickled variables.p'

    game_position , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat = pickle.load( open( str(pickle_path), "rb" ) )


def decide():
    load_variables()

    if Pre_Flop1_Deside == True and Flop1_Deside == False : # instead i can use FUNCTIONS_table_information.Pre_Flop_Deside() too
        shout(paint.light_cyan.bold("*Deciding on Preflop*"))
    elif Flop1_Deside == True and Turn1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Flop*"))
    elif Turn1_Deside == True and River1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Turn*"))
    elif River1_Deside == True :
        shout(paint.light_cyan.bold("*Deciding on River*"))
    else :
        shout(paint.light_cyan.bold("*Deciding on Unknown*"))
    
    if Check_Mod == True :
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

