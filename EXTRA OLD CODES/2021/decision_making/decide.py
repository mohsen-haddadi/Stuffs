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

        if to_play_pre_flop():
            return play_pre_flop()

        elif to_play_hand5_individual_or_1_pair(): 
            return play_hand5_individual_or_1_pair()

        elif to_play_individual_cards():
            return play_individual_cards()

        elif to_play_1_pair():
            return play_1_pair()

        elif to_play_2_pair():
            return play_2_pair()

        elif to_play_3_of_kind():
            return play_3_of_kind()

        elif to_play_straight():
            return play_straight()

        elif to_play_flush():
            return play_flush()

        elif to_play_full_house():
            return play_full_house()

        elif to_play_4_of_kind():
            return play_4_of_kind()

        elif to_play_pocket_pair():
            return play_pocket_pair()

        elif to_play_pocket_3_of_kinds():
            return play_pocket_3_of_kinds()

        elif to_play_pocket_full_house():
            return play_pocket_full_house()

        elif to_play_pocket_4_of_kinds():
            return play_pocket_4_of_kinds()



        elif to_play_pre_flop_raised():
            return play_pre_flop_raised()
        
#        elif to_play_flop_raised():
#            return play_flop_raised()
#
#        elif to_play_turn_raised():
#            return play_turn_raised()
#
#        elif to_play_river_raised():
#            return play_river_raised()
#
        #uncomment lines, when play.py module is completed.
        else :
            return ("not defined")

