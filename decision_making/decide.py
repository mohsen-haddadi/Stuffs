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

        if play_pre_flop() != False :
            return play_pre_flop()

        elif play_hand5_individual_or_1_pair() != False : 
            return play_hand5_individual_or_1_pair()

        elif play_individual_cards() != False :
            return play_individual_cards()

        elif play_1_pair() != False :
            return play_1_pair()

        elif play_2_pair() != False :
            return play_2_pair()

        elif play_3_of_kind() != False :
            return play_3_of_kind()

        elif play_straight() != False :
            return play_straight()

        elif play_flush() != False :
            return play_flush()

        elif play_full_house() != False :
            return play_full_house()

        elif play_4_of_kind() != False :
            return play_4_of_kind()

        elif play_pocket_pair() != False :
            return play_pocket_pair()

        elif play_pocket_3_of_kinds() != False :
            return play_pocket_3_of_kinds()

        elif play_pocket_full_house() != False :
            return play_pocket_full_house()

        elif play_pocket_4_of_kinds() != False :
            return play_pocket_4_of_kinds()



        elif play_pre_flop_raised() != False :
            return play_pre_flop_raised()
        
#        elif play_flop_raised() != False :
#            return play_flop_raised()
#
#        elif play_turn_raised() != False :
#            return play_turn_raised()
#
#        elif play_river_raised() != False :
#            return play_river_raised()
#
        #uncomment lines, when play.py module is completed.
        else :
            return ("not defined")

