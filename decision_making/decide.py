#OK
from decision_making.playpreflop import play_pre_flop
#from play import * 
from iprint import shout
import configs as c

def decide():

    if c.preflop_stage == True and c.flop_stage == False : # instead i can use FUNCTIONS_table_information.Pre_Flop_Deside() too
        shout("*Deciding on preflop*", color = 'light_cyan')
    elif c.flop_stage == True and c.turn_stage == False :
        shout("*Deciding on flop*", color = 'light_cyan')
    elif c.turn_stage == True and c.river_stage == False :
        shout("*Deciding on turn*", color = 'light_cyan')
    elif c.river_stage == True :
        shout("*Deciding on river*", color = 'light_cyan')
    else :
        shout("*Deciding on unknown*", color = 'light_cyan')
    
    if c.just_do_check_fold == True :
        return ("check_fold")

    else :

        if Pre_Flop_Deside():
            return play_pre_flop()


#        elif Flop_Deside():
#            return play_flop()
#
#        elif Turn_Deside():
#            return play_turn()
#
#        elif River_Deside():
#            return play_river()
#
        #uncomment lines, when play.py module is completed.
        else :
            return ("not defined")

