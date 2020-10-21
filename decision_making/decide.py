#OK
from decision_making.play import *
#from play import * 
from iprint import shout
import config

def decide():

    if config.preflop_stage == True and config.flop_stage == False : # instead i can use FUNCTIONS_table_information.Pre_Flop_Deside() too
        shout("*Deciding on preflop*", color = 'light_cyan')
    elif config.flop_stage == True and config.turn_stage == False :
        shout("*Deciding on flop*", color = 'light_cyan')
    elif config.turn_stage == True and config.river_stage == False :
        shout("*Deciding on turn*", color = 'light_cyan')
    elif config.river_stage == True :
        shout("*Deciding on river*", color = 'light_cyan')
    else :
        shout("*Deciding on unknown*", color = 'light_cyan')
    
    if config.just_do_check_fold == True :
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
            return play_pre_flop()

        else :
            return ("not defined")
        #uncomment these lines, when play.py module is completed.
#        elif play_flop() != False :
#            return play_flop()
#
#        elif play_turn() != False :
#            return play_turn()
#
#        elif play_river() != False :
#            return play_river()
#
#        else :
#            return ("not defined")

