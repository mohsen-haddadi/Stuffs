import eval7, time, itertools

from decision_making.rules_and_info.starting_hands import holdem_starting_hand_ranking

def create_all_1326_hole_cards_list():
   SUITS = ['s', 'd', 'c', 'h']
   RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
   DECK = [''.join(item) for item in itertools.product(RANKS, SUITS)]
   ALL_1326_HOLE_CARDS_LIST = [list(hole_Cards) for hole_Cards in itertools.combinations(DECK, 2)]
   return ALL_1326_HOLE_CARDS_LIST
#    SUITS = ['s', 'd', 'c', 'h']
#    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#    ALL_1326_HOLE_CARDS_LIST = []
#    for rank1 in RANKS:
#        for suit1 in SUITS:
#            hole_card_1 = '%s%s' %(rank1, suit1)
#            for rank2 in RANKS:
#                for suit2 in SUITS:
#                    hole_card_2 = '%s%s' %(rank2, suit2)
#                    if hole_card_1 == hole_card_2:
#                        continue
#                    if not [hole_card_1, hole_card_2] in ALL_1326_HOLE_CARDS_LIST\
#                    and not [hole_card_2, hole_card_1] in ALL_1326_HOLE_CARDS_LIST:
#                        ALL_1326_HOLE_CARDS_LIST.append([hole_card_1, hole_card_2])
#    return ALL_1326_HOLE_CARDS_LIST

ALL_1326_HOLE_CARDS_LIST = create_all_1326_hole_cards_list()

def cards_weight(cards_weight_range = 1.5):
    """ Best cards_weight_range can be 1.5
    If cards_weight_range is equal to 0.5:
    cards_weight for 'AA': 1.25
    cards_weight for '72o': 0.75
    cards_weight determines with which hole cards opponents will 
    call more often.
    If small and big blinds seats are on the game don't weight cards
    by setting cards_weight_range to 0
    Using cards_weight function is very time consuming. 
    """
    hole_cards_weight_dic = {}
    for hole_cards in ALL_1326_HOLE_CARDS_LIST:
        ranking = holdem_starting_hand_ranking(hole_cards) # returns 1 to 169
        ranking_in_cent = (169 - ranking) / 168 # ranking_in_cent is 0 to 1
        # y = A + B x
        cards_weight = (1 - cards_weight_range / 2) + cards_weight_range * ranking_in_cent
        hole_cards_weight_dic[f'{hole_cards}'] = cards_weight
    return hole_cards_weight_dic

hole_cards_weight_dic = cards_weight(1.5)

def win_odds(board_cards, my_hole_cards, cards_weight = True):
    """ Due to computing speed issues, only at River change 
    cards_weight_range default value from 0 to 1.5 to use win_odds function.  
    """
    cards = board_cards + my_hole_cards
    hand = [eval7.Card(s) for s in cards]
    my_score = eval7.evaluate(hand)

    weaker_hands_count, stronger_hands_count, equal_hands_count = (0, 0, 0)

    for hole_cards in ALL_1326_HOLE_CARDS_LIST:
        if hole_cards[0] in board_cards or hole_cards[0] in my_hole_cards\
        or hole_cards[1] in board_cards or hole_cards[1] in my_hole_cards:
            continue
        cards = board_cards + hole_cards
        hand = [eval7.Card(s) for s in cards]
        score = eval7.evaluate(hand)
        if not cards_weight: # using if statement to boost speed up.
            weight = 1
        else:
            weight = hole_cards_weight_dic[f'{hole_cards}']
        if score < my_score:
            weaker_hands_count += 1 * weight
        elif score > my_score:
            stronger_hands_count += 1 * weight
        elif score == my_score:
            equal_hands_count += 1 * weight
            #print(hole_cards)

    #my_hand_name_ranking = eval7.handtype(my_score)
    #print('my hand ranking name is: %s' %my_hand_name_ranking)

    #print('number of weaker hands than mine: %s' %weaker_hands_count)
    #print('number of stronger hands than mine: %s' %stronger_hands_count)
    #print('number of equal hands to mine: %s' %equal_hands_count)
    total_hands = weaker_hands_count + stronger_hands_count + equal_hands_count
    #print('total hands: %s' %total_hands)
    return round( 100 * (total_hands - stronger_hands_count) / total_hands, 2)

def all_possible_win_odds(board_cards, my_hole_cards):
    """ 
    returns a list of win odds (0 to 1) by calculating all possible next remaining board cards.
    It is a time consuming function. 
    It may take 7 seconds to return the list. 
    """
    all_possible_new_board_cards = []

    SUITS = ['s', 'd', 'c', 'h']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    if len(board_cards) == 5:
        return None

    if len(board_cards) == 4:
        for rank in RANKS:
            for suit in SUITS:
                board_card_5th = '%s%s' %(rank, suit)
                if board_card_5th in my_hole_cards or board_card_5th in board_cards:
                    continue
                all_possible_new_board_cards.append([board_card_5th])

    if len(board_cards) == 3:
        for rank1 in RANKS:
            for suit1 in SUITS:
                board_card_4th = '%s%s' %(rank1, suit1)
                if board_card_4th in my_hole_cards \
                or board_card_4th in board_cards :
                    continue
                for rank2 in RANKS:
                    for suit2 in SUITS:
                        board_card_5th = '%s%s' %(rank2, suit2)
                        if board_card_5th in my_hole_cards \
                        or board_card_5th in board_cards \
                        or board_card_5th == board_card_4th:
                            continue
                        if [board_card_4th, board_card_5th] in all_possible_new_board_cards \
                        or [board_card_5th, board_card_4th] in all_possible_new_board_cards :
                            continue
                        all_possible_new_board_cards.extend([[board_card_4th, board_card_5th]])

    all_possible_win_odds_list = []
    # Time consuming loop of this module:
    for new_board_cards in all_possible_new_board_cards:
        possible_board_on_river = board_cards + new_board_cards
        all_possible_win_odds_list.append(win_odds(possible_board_on_river, my_hole_cards))

        #if all_possible_win_odds_list[-1] >= 95: #awesome_odds
        #    print(possible_board_on_river)
    return all_possible_win_odds_list

def draw_odds(all_possible_win_odds_list, awesome_odds = 95):
    """return draw odds by calculating all possible next remaining board cards. """
    if all_possible_win_odds_list == None:
        return None
    awesome_boards_count = len([i for i in all_possible_win_odds_list if i>= awesome_odds])
    # length all_possible_new_board_cards is equal to length all_possible_win_odds_list
    #print(all_possible_win_odds_list)
    future_awesome_boards_odds = awesome_boards_count / len(all_possible_win_odds_list)
    #print('all possible new board cards count is: %s' % len(all_possible_win_odds_list))
    return round( 100 * future_awesome_boards_odds, 1 )

def next_win_odds_average(all_possible_win_odds_list):

    if all_possible_win_odds_list == None:
        return None 
    future_win_odds_average = sum(all_possible_win_odds_list) / len(all_possible_win_odds_list)
    return round( future_win_odds_average, 1 )
