VERSION = 1

import configs as c
from iprint import shout
from hand_history_data_base.append_to_csv import scenario
import decision_making.rules_and_info.odds as odds
from decision_making.rules_and_info.starting_hands import group, holdem_starting_hand_ranking
from decision_making.rules_and_info.table_information import *



def play_turn():

    win_odds = c.win_odds
    next_win_odds_average = c.next_win_odds_average
    draw_odds = c.draw_odds

    if early_position():
        saftey = 0.9 #1
    elif middle_position():
        saftey = 0.85 #0.95
    elif late_position():
        saftey = 0.8 #0.9

    # At current stage, Everybody acting before or after you has either Checked or Called the pre flop Big Blind
    if not raised():

        if win_odds > 90 * saftey and next_win_odds_average > 75 * saftey:
            
            scenario(65)
            return 'raise', 'half_pot'
        else:
            
            scenario(66)
            return 'check'

    # At current stage, Someone acting before or after you has Raised already
    elif raised():

        if Max_raise_sofar() / c.BLIND_VALUE < 5:

            if win_odds > 92 * saftey and next_win_odds_average > 77 * saftey:
                
                scenario(67)
                return 'raise', 'pot'
            elif (win_odds > 80 * saftey and next_win_odds_average > 68 * saftey) or draw_odds > 26:
                
                scenario(68)
                return 'call'
            else:
                
                scenario(69)
                return 'fold'

        elif 5 <= Max_raise_sofar() / c.BLIND_VALUE < 10:

            if win_odds > 94 * saftey and next_win_odds_average > 78 * saftey:
                
                scenario(70)
                return 'raise', 'half_pot'
            elif (win_odds > 82 * saftey and next_win_odds_average > 77 * saftey) or draw_odds > 26:
                
                scenario(71)
                return 'call'
            elif ((win_odds > 70 * saftey and next_win_odds_average > 65 * saftey) or draw_odds > 26) and call_low_re_raise(1.99):
                
                scenario(72)
                return 'call'
            else:
                
                scenario(73)
                return 'fold'

        elif 10 <= Max_raise_sofar() / c.BLIND_VALUE < 20:

            if win_odds > 95 and next_win_odds_average > 79:
                
                scenario(74)
                return 'raise', 'half_pot'
            elif (win_odds > 84 and next_win_odds_average > 79) or draw_odds > 29:
                
                scenario(75)
                return 'call'
            elif ((win_odds > 72 and next_win_odds_average > 67) or draw_odds > 29) and call_low_re_raise(1.99):
                
                scenario(76)
                return 'call'
            else:
                
                scenario(77)
                return 'fold'


        elif 20 <= Max_raise_sofar() / c.BLIND_VALUE:

            if win_odds > 96 and next_win_odds_average > 80:
                
                scenario(78)
                return 'all_in'
            elif ((win_odds > 86 and next_win_odds_average > 80) or draw_odds > 70) and call_low_re_raise():
                
                scenario(79)
                return 'call'
            else:
                
                scenario(80)
                return 'fold'


