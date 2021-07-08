#💊 : means edited
import configs as c

def s(card): #💊
    """ returns suit of a card in string format"""
    if card == 'Unknown':
        return 'Unknown'
    else:
        return card[1]

def n(card): #💊
    """ returns value of a card by numbering them from 2 to 14"""
    if isinstance(card, int) and 2 <= card <= 14:
        return card 
    elif card == 'Unknown':
        return 'Unknown'
    elif card[0] == 'T':
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    else:
        return int(card[0])

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