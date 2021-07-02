#OK
from decision_making.rules_and_info.suit_and_value import s, n
#from suit_and_value import s, n
import configs as c

def group(string):
    GROUPS = {
        'A': ['AA', 'KK'],
        'B': ['AKs', 'QQ'],
        'C': ['AK', 'JJ','TT'],
        'D': ['AQs', 'AQ', 'AJs', '99', '88'],
        'E': ['AJ', 'ATs', 'KQs', '77', '66', '55'],
        'F': ['AT', 'KQ', 'KJs', 'QJs', '44', '33', '22'],
        'G': ['A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
              'KTs', 'QTs', 'JTs', 'J9s', 'T9s', '98s'],
        'H': ['KJ', 'KT', 'QJ', 'J8s', 'T8s', '87s', '76s']
        }
    # removing whitespaces
    string = ''.join(string.split())
    group_cards = []
    for char in string:
        group_cards = group_cards + GROUPS[char]
    return change_hand_format(c.my_1th_card, c.my_2th_card) in group_cards

def holdem_starting_hand_ranking():
    """ 
    returns 1 to 169
    1 represent the most powerful hand and 169 represent the weakest hand.
    Hands order source:
    https://caniwin.com/poker/texas-holdem/pre-flop/10-player-odds/# 
    """
    HOLDEM_169_HOLE_CARDS_RANKING_LIST = [
    'AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', 'AKs', '77', 'AQs',
    'AJs', 'AK', 'ATs', 'AQ', 'AJ', 'KQs', '66', 'A9s', 'AT', 'KJs', 
    'A8s', 'KTs', 'KQ', 'A7s', 'A9', 'KJ', '55', 'QJs', 'K9s', 'A5s',
    'A6s', 'A8', 'KT', 'QTs', 'A4s', 'A7', 'K8s', 'A3s', 'QJ', 'K9',
    'A5', 'A6', 'Q9s', 'K7s', 'JTs', 'A2s', 'QT', '44', 'A4', 'K6s',
    'K8', 'Q8s', 'A3', 'K5s', 'J9s', 'Q9', 'JT', 'K7', 'A2', 'K4s',
    'Q7s', 'K6', 'K3s', 'T9s', 'J8s', '33', 'Q6s', 'Q8', 'K5', 'J9',
    'K2s', 'Q5s', 'T8s', 'K4', 'J7s', 'Q4s', 'Q7', 'T9', 'J8', 'K3',
    'Q6', 'Q3s', '98s', 'T7s', 'J6s', 'K2', '22', 'Q2s', 'Q5', 'J5s',
    'T8', 'J7', 'Q4', '97s', 'J4s', 'T6s', 'J3s', 'Q3', '98', '87s',
    'T7', 'J6', '96s', 'J2s', 'Q2', 'T5s', 'J5', 'T4s', '97', '86s',
    'J4', 'T6', '95s', 'T3s', '76s', 'J3', '87', 'T2s', '85s', '96',
    'J2', 'T5', '94s', '75s', 'T4', '93s', '86', '65s', '84s', '95',
    'T3', '92s', '76', '74s', 'T2', '54s', '85', '64s', '83s', '94',
    '75', '82s', '73s', '93', '65', '53s', '63s', '84', '92', '43s',
    '74', '72s', '54', '64', '52s', '62s', '83', '42s', '82', '73',
    '53', '63', '32s', '43', '72', '52', '62', '42', '32',
    ]
#    HOLDEM_169_HOLE_CARDS_RANKING_LIST_non_heads_up = [
#    'AA', 'KK', 'QQ', 'AKs', 'JJ', 'AQs', 'KQs', 'AJs', 'KJs', 'ATs',
#    'QJs', 'AKo', 'TT', 'KTs', 'QTs', 'JTs', '99', 'AQo', 'A9s', 'KQo', 
#    'K9s', 'T9s', 'A8s', 'J9s', 'Q9s', '88', 'A5s', 'AJo', 'A7s', 'A4s',
#    'A3s', 'KJo', 'A6s', 'QJo', '77', 'A2s', 'K8s', 'T8s', '98s', 'ATo',
#    'J8s', 'Q8s', 'K7s', 'KTo', 'JTo', '66', 'QTo', 'K6s', '87s', 'K5s',
#    '97s', '55', 'T7s', 'K4s', '76s', '44', 'K3s', 'Q7s', 'J7s', '33',
#    'K2s', '22', '65s', '86s', 'Q6s', '54s', 'Q5s', '75s', '96s', 'T9o',
#    'Q4s', 'T6s', 'A9o', 'Q3s', '64s', 'J6s', 'Q2s', 'J9o', '85s', '53s',
#    'K9o', 'J5s', 'Q9o', 'J4s', 'A8o', '74s', 'J3s', '43s', '95s', 'J2s',
#    'T5s', 'A5o', '63s', 'T4s', 'A7o', 'T8o', 'T3s', 'A4o', '52s', '98o',
#    '84s', 'T2s', 'A3o', '42s', 'A6o', 'K8o', '94s', 'J8o', '73s', '93s',
#    'Q8o', '87o', 'A2o', '32s', '92s', '62s', 'K7o', '83s', '97o', '76o',
#    '82s', 'T7o', 'K6o', '72s', '65o', '86o', 'K5o', '54o', 'J7o', 'K4o',
#    'Q7o', '75o', 'K3o', '96o', 'K2o', 'Q6o', '64o', 'Q5o', 'T6o', '53o',
#    '85o', 'Q4o', 'J6o', 'Q3o', '43o', '74o', 'Q2o', 'J5o', '95o', 'J4o',
#    '63o', 'J3o', 'T5o', '52o', 'J2o', 'T4o', '84o', '42o', 'T3o', 'T2o',
#    '73o', '94o', '32o', '62o', '93o', '92o', '83o', '82o', '72o',
#    ]

    my_cards = change_hand_format(c.my_1th_card, c.my_2th_card)
    #print(my_cards)
    # hand_ranking from 1 to 169
    hand_ranking = HOLDEM_169_HOLE_CARDS_RANKING_LIST.index(my_cards) + 1
    return hand_ranking

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
        return '%s%s' %(high_card, low_card)
             
