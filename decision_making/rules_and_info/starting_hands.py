import pickle, os
from pathlib import PurePath
from decision_making.rules_and_info.suit_and_value import s, n
#from suit_and_value import s, n 

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
    pickle_path = PurePath(current_path).parent.parent / 'pickled variables.p'

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

#----

def hand1() :
    """ AA,KK """
    global  my_1th_card , my_2th_card 
    load_variables()
    if  n( my_1th_card ) == n( my_2th_card )  and 13 <= n( my_1th_card ) <= 14 :
        #shout("hand1 is True")
        return True
    else :
        return None

def hand2() :
    """ QQ,JJ """
    global  my_1th_card , my_2th_card 
    load_variables()
    if  n( my_1th_card ) == n( my_2th_card )  and 11 <= n( my_1th_card ) <= 12 :
        #shout("hand2 is True")
        return True
    else :
        return None

def hand3() :
    """ 1010,99 """
    global  my_1th_card , my_2th_card 
    load_variables()
    if  n( my_1th_card ) == n( my_2th_card )  and 9 <= n( my_1th_card ) <= 10 :
        #shout("hand3 is True")
        return True
    else :
        return None

def hand4() :
    """ 88,77,...,22 """
    global  my_1th_card , my_2th_card 
    load_variables()
    if  n( my_1th_card ) == n( my_2th_card )  and 2 <= n( my_1th_card ) <= 8 :
        #shout("hand4 is True")
        return True
    else :
        return None

def hand5() :
    """ A10,...,KQ  3 Blind raise """
    global  my_1th_card , my_2th_card 
    load_variables()
    if  n( my_1th_card ) != n( my_2th_card ) :
        if ( 12 <= n( my_1th_card ) <= 13 and 12 <= n( my_2th_card ) <= 13 ) \
        or ( 14 in [ n( my_1th_card ) , n( my_2th_card ) ] and n( my_1th_card ) >= 10 and n( my_2th_card ) >= 10 ) :
            #shout("hand5 is True")
            return True
    else :
        return None

def hand6() :
    """ KJ,QJ,,...,A2,...,(108,98 rang),109  1 Blind call """
    global  my_1th_card , my_2th_card 
    load_variables()
    if  n( my_1th_card ) != n( my_2th_card ) :
        if hand5() != True :
            if 14 in [ n( my_1th_card ) , n( my_2th_card ) ] \
            or ( n( my_1th_card ) >= 8 and n( my_2th_card ) >= 8 and s( my_1th_card ) == s( my_2th_card ) ) \
            or ( n( my_1th_card ) >= 9 and n( my_2th_card ) >= 9 ) :
                #shout("hand6 is True")
                return True
    else :
        return None

def hand7() :
    """ 72,73,...,96,107 (gheir rang)  Fold small blind position (otherwise Small always call Blind) """
    global  my_1th_card , my_2th_card 
    load_variables()
    if not( hand1() or hand2() or hand3() or \
            hand4() or hand5() or hand6() \
            or s( my_1th_card ) == s( my_2th_card ) ) :
        for i in range(2,8) :
            if i in ( n( my_1th_card ) , n( my_2th_card ) )  and abs( n( my_2th_card ) - n( my_1th_card ) ) >= 3 \
            and n( my_1th_card ) <= 10 and n( my_2th_card ) <= 10 :
                #shout("hand7 is True")
                return True
    else :
        return None


#--------------------------------------------


def hand8() :
    """ AK,...,1010,...22,...,(65 rang) Blind position call 2 blind raise, otherwise fold that """
    global  my_1th_card , my_2th_card 
    load_variables()
    if not( hand1() or hand2() ) :
        if hand3() or hand4() \
        or hand5() or hand6() \
        or ( n( my_1th_card ) >= 5 and n( my_2th_card ) >= 5 and \
             s( my_1th_card ) == s( my_2th_card ) and abs( n( my_2th_card ) - n( my_1th_card ) ) == 1 ) :
            #shout("hand8 is True")
            return True
    else :
        return None

def hand9() :
    """ AK,...,1010,...,(98 rang) Small position call 2 blind raise, otherwise fold that """
    global  my_1th_card , my_2th_card 
    load_variables()
    if not( hand1() or hand2() ) :
        if hand3() or hand4() \
        or hand5() or hand6() :
            #shout("hand9 is True")
            return True
    else :
        return None    


