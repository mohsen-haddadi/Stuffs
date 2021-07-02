import configs as c

def s(card) :
    """ returns suit of a card in string format"""
    if card[1] == 'Spade':
        return 's'
    elif card[1] == 'Heart':
        return 'h'
    elif card[1] == 'Club':
        return 'c'
    elif card[1] == 'Diamond':
        return 'd'

def n(card) :
    """ returns value of a card by numbering them from 2 to 14"""
    if isinstance(card, int) and 2 <= card <= 14:
        return card 
    else:
        if card[0] == 'Two':
            return 2
        elif card[0] == 'Three':
            return 3
        elif card[0] == 'Four':
            return 4
        elif card[0] == 'Five':
            return 5
        elif card[0] == 'Six':
            return 6
        elif card[0] == 'Seven':
            return 7
        elif card[0] == 'Eight':
            return 8
        elif card[0] == 'Nine':
            return 9
        elif card[0] == 'Ten':
            return 10
        elif card[0] == 'Jack':
            return 11
        elif card[0] == 'Queen':
            return 12
        elif card[0] == 'King':
            return 13
        elif card[0] == 'Ace':
            return 14

def board_cards_list():
    if c.preflop_stage and not c.flop_stage :
        board_list = []
    elif c.flop_stage and not c.turn_stage :
        board_list = [ c.board_card_1th, c.board_card_2th, c.board_card_3th ]
    elif c.turn_stage and not c.river_stage :
        board_list = [ c.board_card_1th , c.board_card_2th , c.board_card_3th,
                       c.board_card_4th ]
    elif c.river_stage :
        board_list = [ c.board_card_1th, c.board_card_2th, c.board_card_3th,
                       c.board_card_4th , c.board_card_5th ]

    return board_list