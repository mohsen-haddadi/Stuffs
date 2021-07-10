VERSION = 1

import configs as c
from iprint import shout
from hand_history_data_base.append_to_csv import scenario
import decision_making.rules_and_info.odds as odds
from decision_making.rules_and_info.starting_hands import group, holdem_starting_hand_ranking
from decision_making.rules_and_info.table_information import *


def play_river():

    win_odds = c.win_odds

    if early_position():
        saftey = 0.9 #1
    elif middle_position():
        saftey = 0.85 #0.95
    elif late_position():
        saftey = 0.8 #0.9

    # At current stage, Everybody acting before or after you has either Checked or Called the pre flop Big Blind
    if not raised():

        if late_position():
            if win_odds > 92 * saftey:
                scenario(81)
                return 'raise', 'half_pot'
            else:
                scenario(82)
                return 'check'
        else:
            if win_odds > 90 * saftey:
                
                scenario(83)
                return 'raise', 'half_pot'
            else:
                
                scenario(84)
                return 'check'

    # At current stage, Someone acting before or after you has Raised already
    elif raised():

        if Max_raise_sofar() / c.BLIND_VALUE < 5:

            if win_odds > 92 * saftey:
                
                scenario(85)
                return 'raise', 'pot'
            elif win_odds > 80 * saftey:
                
                scenario(86)
                return 'call'
            else:
                
                scenario(87)
                return 'fold'

        elif 5 <= Max_raise_sofar() / c.BLIND_VALUE < 10:

            if win_odds > 94 * saftey:
                
                scenario(88)
                return 'raise', 'half_pot'
            elif win_odds > 82 * saftey:
                
                scenario(89)
                return 'call'
            elif win_odds > 70 * saftey and call_low_re_raise(1.99):
                
                scenario(90)
                return 'call'
            else:
                
                scenario(91)
                return 'fold'

        elif 10 <= Max_raise_sofar() / c.BLIND_VALUE < 20:

            if win_odds > 95 :
                
                scenario(92)
                return 'raise', 'half_pot'
            elif win_odds > 84:
                
                scenario(93)
                return 'call'
            elif win_odds > 72 and call_low_re_raise(1.99):
                
                scenario(94)
                return 'call'
            else:
                
                scenario(95)
                return 'fold'


        elif 20 <= Max_raise_sofar() / c.BLIND_VALUE:

            if win_odds > 96 :
                
                scenario(96)
                return 'all_in'
            elif win_odds > 86 and call_low_re_raise():
                
                scenario(97)
                return 'call'
            else:
                
                scenario(98)
                return 'fold'


