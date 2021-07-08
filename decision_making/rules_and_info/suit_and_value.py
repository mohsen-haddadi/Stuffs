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
