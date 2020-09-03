#OK
from decision_making.rules_and_info.suit_and_value import s, n
#from suit_and_value import s, n
import config as c

def holdem_starting_hand_ranking():
    """ 
    returns 1 to 169
    1 represent the most powerful hand and 169 represent the weakest hand.
    Hands order source:
    https://caniwin.com/poker/texas-holdem/pre-flop/10-player-odds/# 
    """

    HOLDEM_169_HOLE_CARDS_RANKING_LIST = [
    'AA', 'KK', 'QQ', 'AKs', 'JJ', 'AQs', 'KQs', 'AJs', 'KJs', 'ATs',
    'QJs', 'AKo', 'TT', 'KTs', 'QTs', 'JTs', '99', 'AQo', 'A9s', 'KQo', 
    'K9s', 'T9s', 'A8s', 'J9s', 'Q9s', '88', 'A5s', 'AJo', 'A7s', 'A4s',
    'A3s', 'KJo', 'A6s', 'QJo', '77', 'A2s', 'K8s', 'T8s', '98s', 'ATo',
    'J8s', 'Q8s', 'K7s', 'KTo', 'JTo', '66', 'QTo', 'K6s', '87s', 'K5s',
    '97s', '55', 'T7s', 'K4s', '76s', '44', 'K3s', 'Q7s', 'J7s', '33',
    'K2s', '22', '65s', '86s', 'Q6s', '54s', 'Q5s', '75s', '96s', 'T9o',
    'Q4s', 'T6s', 'A9o', 'Q3s', '64s', 'J6s', 'Q2s', 'J9o', '85s', '53s',
    'K9o', 'J5s', 'Q9o', 'J4s', 'A8o', '74s', 'J3s', '43s', '95s', 'J2s',
    'T5s', 'A5o', '63s', 'T4s', 'A7o', 'T8o', 'T3s', 'A4o', '52s', '98o',
    '84s', 'T2s', 'A3o', '42s', 'A6o', 'K8o', '94s', 'J8o', '73s', '93s',
    'Q8o', '87o', 'A2o', '32s', '92s', '62s', 'K7o', '83s', '97o', '76o',
    '82s', 'T7o', 'K6o', '72s', '65o', '86o', 'K5o', '54o', 'J7o', 'K4o',
    'Q7o', '75o', 'K3o', '96o', 'K2o', 'Q6o', '64o', 'Q5o', 'T6o', '53o',
    '85o', 'Q4o', 'J6o', 'Q3o', '43o', '74o', 'Q2o', 'J5o', '95o', 'J4o',
    '63o', 'J3o', 'T5o', '52o', 'J2o', 'T4o', '84o', '42o', 'T3o', 'T2o',
    '73o', '94o', '32o', '62o', '93o', '92o', '83o', '82o', '72o',
    ]

    def change_hand_format(my_1th_card, my_2th_card):
        """
        This function change the given hand format 
        to the format used in the HOLDEM_169_HOLE_CARDS_RANKING_LIST
        Example: c.my_1th_card = ('Seven', 'Spade') ; c.my_2th_card = ('Ace', 'Heart')
        returns 'A7o'
        """
        if n(c.my_1th_card) == 14:
            my_1th_card_value = 'A'
        elif n(c.my_1th_card) == 13:
            my_1th_card_value = 'K'
        elif n(c.my_1th_card) == 12:
            my_1th_card_value = 'Q'
        elif n(c.my_1th_card) == 11:
            my_1th_card_value = 'J'
        elif n(c.my_1th_card) == 10:
            my_1th_card_value = 'T'
        else:
            my_1th_card_value = str(n(c.my_1th_card))

        if n(c.my_2th_card) == 14:
            my_2th_card_value = 'A'
        elif n(c.my_2th_card) == 13:
            my_2th_card_value = 'K'
        elif n(c.my_2th_card) == 12:
            my_2th_card_value = 'Q'
        elif n(c.my_2th_card) == 11:
            my_2th_card_value = 'J'
        elif n(c.my_2th_card) == 10:
            my_2th_card_value = 'T'
        else:
            my_2th_card_value = str(n(c.my_2th_card))

        if n(c.my_1th_card) > n(c.my_2th_card):
            high_card = my_1th_card_value
            low_card = my_2th_card_value
        else:
            high_card = my_2th_card_value
            low_card = my_1th_card_value

        if n(c.my_1th_card) == n(c.my_2th_card):
            return '%s%s' %(my_1th_card_value, my_2th_card_value)
        elif s(c.my_1th_card) == s(c.my_2th_card):
            return '%s%ss' %(high_card, low_card)
        elif s(c.my_1th_card) != s(c.my_2th_card):
            return '%s%so' %(high_card, low_card)

    my_cards = change_hand_format(c.my_1th_card, c.my_2th_card)
    #print(my_cards)
    # hand_ranking from 1 to 169
    hand_ranking = HOLDEM_169_HOLE_CARDS_RANKING_LIST.index(my_cards) + 1
    return hand_ranking

#----

def hand1() :
    """ AA,KK """
    if  n( c.my_1th_card ) == n( c.my_2th_card )  and 13 <= n( c.my_1th_card ) <= 14 :
        #shout("hand1 is True")
        return True
    else :
        return None

def hand2() :
    """ QQ,JJ """
    if  n( c.my_1th_card ) == n( c.my_2th_card )  and 11 <= n( c.my_1th_card ) <= 12 :
        #shout("hand2 is True")
        return True
    else :
        return None

def hand3() :
    """ 1010,99 """
    if  n( c.my_1th_card ) == n( c.my_2th_card )  and 9 <= n( c.my_1th_card ) <= 10 :
        #shout("hand3 is True")
        return True
    else :
        return None

def hand4() :
    """ 88,77,...,22 """
    if  n( c.my_1th_card ) == n( c.my_2th_card )  and 2 <= n( c.my_1th_card ) <= 8 :
        #shout("hand4 is True")
        return True
    else :
        return None

def hand5() :
    """ A10,...,KQ  3 Blind raise """
    if  n( c.my_1th_card ) != n( c.my_2th_card ) :
        if ( 12 <= n( c.my_1th_card ) <= 13 and 12 <= n( c.my_2th_card ) <= 13 ) \
        or ( 14 in [ n( c.my_1th_card ) , n( c.my_2th_card ) ] and n( c.my_1th_card ) >= 10 and n( c.my_2th_card ) >= 10 ) :
            #shout("hand5 is True")
            return True
    else :
        return None

def hand6() :
    """ KJ,QJ,,...,A2,...,(108,98 rang),109  1 Blind call """
    if  n( c.my_1th_card ) != n( c.my_2th_card ) :
        if hand5() != True :
            if 14 in [ n( c.my_1th_card ) , n( c.my_2th_card ) ] \
            or ( n( c.my_1th_card ) >= 8 and n( c.my_2th_card ) >= 8 and s( c.my_1th_card ) == s( c.my_2th_card ) ) \
            or ( n( c.my_1th_card ) >= 9 and n( c.my_2th_card ) >= 9 ) :
                #shout("hand6 is True")
                return True
    else :
        return None

def hand7() :
    """ 72,73,...,96,107 (gheir rang)  Fold small blind position (otherwise Small always call Blind) """
    if not( hand1() or hand2() or hand3() or \
            hand4() or hand5() or hand6() \
            or s( c.my_1th_card ) == s( c.my_2th_card ) ) :
        for i in range(2,8) :
            if i in ( n( c.my_1th_card ) , n( c.my_2th_card ) )  and abs( n( c.my_2th_card ) - n( c.my_1th_card ) ) >= 3 \
            and n( c.my_1th_card ) <= 10 and n( c.my_2th_card ) <= 10 :
                #shout("hand7 is True")
                return True
    else :
        return None


#--------------------------------------------


def hand8() :
    """ AK,...,1010,...22,...,(65 rang) Blind position call 2 blind raise, otherwise fold that """
    if not( hand1() or hand2() ) :
        if hand3() or hand4() \
        or hand5() or hand6() \
        or ( n( c.my_1th_card ) >= 5 and n( c.my_2th_card ) >= 5 and \
             s( c.my_1th_card ) == s( c.my_2th_card ) and abs( n( c.my_2th_card ) - n( c.my_1th_card ) ) == 1 ) :
            #shout("hand8 is True")
            return True
    else :
        return None

def hand9() :
    """ AK,...,1010,...,(98 rang) Small position call 2 blind raise, otherwise fold that """
    if not( hand1() or hand2() ) :
        if hand3() or hand4() \
        or hand5() or hand6() :
            #shout("hand9 is True")
            return True
    else :
        return None    


