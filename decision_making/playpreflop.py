VERSION = 1

import configs as c
from decision_making.rules_and_info.starting_hands import group, holdem_starting_hand_ranking
from decision_making.rules_and_info.table_information import *

def scenario(number):
    c.scenario_list.append(number)

def play_pre_flop():

    # At current stage, Everybody acting before or after you has either Checked or Called the pre flop Big Blind
    if not raised():

        if c.my_seat_number == c.small_blind_seat:
            if not group('ABCD'): # pdf recommendation is group('ABCDEF')
                if holdem_starting_hand_ranking() > 145:
                    scenario(1)
                    return 'fold'
                else:
                    scenario(2)
                    return 'call'
            else:
                scenario(3)
                return 'raise', 3.5

        elif c.my_seat_number == c.big_blind_seat:
            if early_position():
                if group('ABCD'): # pdf recommendation is group('ABCDEF')
                    scenario(4)
                    return 'raise', 3.5
                else:
                    scenario(5)
                    return 'check'
            elif middle_position():
                if group('ABCDE'): # pdf recommendation is group('ABCDEF')
                    scenario(6)
                    return 'raise', 3.5
                else:
                    scenario(7)
                    return 'check'
            elif late_position():
                if group('ABCDEF'):
                    scenario(8)
                    return 'raise', 3.5
                else:
                    scenario(9)
                    return 'check'

        else:
            if early_position():
                if group('ABCD'):
                    scenario(10)
                    return 'raise', 3.5
                else:
                    scenario(11)
                    return 'fold'
            elif middle_position():
                if group('ABCDE'):
                    scenario(12)
                    return 'raise', 3.5
                elif group('FG'):
                    scenario(13)
                    return 'call'
                else:
                    scenario(14)
                    return 'fold'
            elif late_position():
                if group('ABCDEF'):
                    scenario(15)
                    return 'raise', 3.5
                elif group('GH'):
                    scenario(16)
                    return 'call'
                else:
                    scenario(17)
                    return 'fold' 



    # At current stage, Someone acting before or after you has Raised already
    elif raised():

        if c.my_seat_number in (c.small_blind_seat, c.big_blind_seat) and Max_raise_sofar() / c.BLIND_VALUE < 5:

            if group('ABC'): # pdf recommendation is group('ABCD')
                scenario(18)
                return 'raise', 'pot'
            elif group('DEF'): # pdf recommendation is group('EF')
                scenario(19)
                return 'call'
            else:
                scenario(20)
                return 'fold'

        elif Max_raise_sofar() / c.BLIND_VALUE < 5:
            if early_position():
                if group('AB'):
                    scenario(21)
                    return 'raise', 'pot'
                elif group('C'):
                    scenario(22)
                    return 'call'
                else:
                    scenario(23)
                    return 'fold'
            elif middle_position():
                if group('AB'):
                    scenario(24)
                    return 'raise', 'pot'
                elif group('C'): # my recommendation is group('CD')
                    scenario(25)
                    return 'call'
                else:
                    scenario(26)
                    return 'fold'
            elif late_position():
                if group('AB'):
                    scenario(27)
                    return 'raise', 'pot'
                elif group('CD'):
                    scenario(28)
                    return 'call'
                else:
                    scenario(29)
                    return 'fold'

        elif 5 <= Max_raise_sofar() / c.BLIND_VALUE < 10:
            if early_position():
                if group('A'):
                    scenario(30)
                    return 'raise', 'pot'
                elif group('BC'):
                    scenario(31)
                    return 'call'
                elif call_low_re_raise(1.99):
                    scenario(32)
                    return 'call'
                else:
                    scenario(33)
                    return 'fold'
            elif middle_position():
                if group('AB'):
                    scenario(34)
                    return 'raise', 'pot'
                elif group('C'): # my recommendation is group('CD')
                    scenario(35)
                    return 'call'
                elif call_low_re_raise(1.99):
                    scenario(36)
                    return 'call'
                else:
                    scenario(37)
                    return 'fold'
            elif late_position():
                if group('AB'):
                    scenario(38)
                    return 'raise', 'pot'
                elif group('CD'):
                    scenario(39)
                    return 'call'
                elif call_low_re_raise(1.99):
                    scenario(40)
                    return 'call'
                else:
                    scenario(41)
                    return 'fold'

        elif 10 <= Max_raise_sofar() / c.BLIND_VALUE < 20:

            if group('A'):
                scenario(42)
                return 'raise', 'pot'
            elif group('B'): # for low stack tables can be group('BC')
                scenario(43)
                return 'call'
            elif call_low_re_raise(1.99):
                scenario(44)
                return 'call'
            else:
                scenario(45)
                return 'fold'


        elif 20 <= Max_raise_sofar() / c.BLIND_VALUE:

            if group('A'): # for low stack tables can be group('AB')
                scenario(46)
                return 'all_in'
            elif group('B') and call_low_re_raise():
                scenario(47)
                return 'call'
            else:
                scenario(48)
                return 'fold'











































































"""
        elif 10 <= Max_raise_sofar() / c.BLIND_VALUE < 20:
            raiser_bank = c.players_bank[last_raiser_seat_sofar()]
            if raiser_bank == None or raiser_bank / c.BLIND_VALUE > 40 :
                if group('A'):
                    scenario(49)
                    return 'raise', 'pot')
                elif group('B'): # for low stack tables can be group('BC')
                    scenario(50)
                    return 'call')
                else:
                    scenario(51)
                    return 'fold')
            else:
                if number_of_raisers_now() == 1:
                    if group('AB'):
                        scenario(52)
                        return 'raise', 'all in')
                    elif group('C'): # Separated 'elif' just for statistical conclusions.
                        scenario(53)
                        return 'raise', 'all in')
                    else:
                        scenario(54)
                        return 'fold')
                else:
                    if group('A'):
                        scenario(55)
                        return 'raise', 'all in')
                    elif group('B'): # Separated 'elif' just for statistical conclusions.
                        scenario(56)
                        return 'raise', 'all in')
                    elif group('C'): 
                        scenario(57)
                        return 'call')
                    else:
                        scenario(58)
                        return 'fold')

        elif 20 <= Max_raise_sofar() / c.BLIND_VALUE:
            raiser_bank = c.players_bank[last_raiser_seat_sofar()]

            if raiser_bank == None or raiser_bank / c.BLIND_VALUE > 40 :
                if group('A'): # for low stack tables can be group('AB')
                    scenario(59)
                    return 'raise', 'all in')
                elif group('B') and call_low_re_raise():
                    scenario(60)
                    return 'call')
                else:
                    scenario(61)
                    return 'fold')
            else:
                if number_of_raisers_now() == 1:
                    if group('AB'):
                        scenario(62)
                        return 'raise', 'all in')
                    elif group('C'): # Separated 'elif' just for statistical conclusions.
                        scenario(63)
                        return 'raise', 'all in')
                    else:
                        scenario(64)
                        return 'fold')
                else:
                    
                    if group('A'):
                        scenario(65)
                        return 'raise', 'all in')
                    elif group('B'): # Separated 'elif' just for statistical conclusions.
                        scenario(66)
                        return 'raise', 'all in')
                    elif group('C'): 
                        scenario(67)
                        return 'call')
                    else:
                        scenario(68)
                        return 'fold')
"""




        # the raiser has gone all in with lower than 20 BB bank. 
        # the raiser has gone all in with 20 BB to 40 BB bank.

        # the raiser has gone all in with more than 40 BB bank.
            # the all in raiser has raised with more than 10 BB at pre flop stage.
            # ................  has not ..........................................

        # the raiser is before me

            ### no re raises ###
            # i was the last raiser 2 stage ago and the raiser take advantage of my check at previous stage
            # the raiser has done continue bet.
            # i was last raiser and the raiser raised all of a sudden

            ### re raises ###
            # the raiser has raised and re raised  
            # the raiser has check and raised

        # the raiser is after me

            ### no re raises ###
            # i was the last raiser at previous stage and the raiser take advantage of my check
            # the raiser has done continue bet.

            ### re raises ###
            # the raiser has re raised
