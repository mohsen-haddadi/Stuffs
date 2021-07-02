#OK
from decision_making.rules_and_info.suit_and_value import s, n, board_cards_list
#from suit_and_value import s, n
import configs as c

"""
There are 4 Functions which returns a List in accordance with table cards.

Functions with True or False return,are in 2 kind of categoreis: 1.Table_ 2.Me_
If one of them is True the rest will be False. one Function is always True.

Ranking Functions return 1.a Number or 2.a tuple or 
3.None value if their True or False Functions have not been True already 
  or we are at pre flop stage.
"""

"""
In Python, List variables can be modified inside function's scopes which have 
came from other scopes even if they are assigned to the other variable names. 
To avoid this misbehavior, at the beginning of functions always copy lists 
by using List = List[:]  or by doing List = [...]. 
This way new List variables will have new separated IDs.
"""

def Table_Individual_Cards_List(board_list=None) :
    """ [7,7,5,10] returns [10, 5]"""
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return []

    board_list = [n(i) for i in board_list ] 
    Individual_Cards = [i for i in board_list if board_list.count(i) == 1]
    Individual_Cards.sort(reverse=True)
    return Individual_Cards

def Table_2_same_Cards_List(board_list=None) : 
    """ [7,7,5,5,6] returns [7, 5]"""
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return []

    board_list = [n(i) for i in board_list ]
    
    Table_2_same_Cards = []
    for i in board_list:
        if board_list.count(i) == 2 and i not in Table_2_same_Cards:
            Table_2_same_Cards.append( i )
    Table_2_same_Cards.sort(reverse=True)
    return Table_2_same_Cards

def Table_3_same_Cards_List(board_list=None) :
    """ [] or max one index"""
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return []

    board_list = [n(i) for i in board_list ]
    
    Table_3_same_Cards = []
    for i in board_list:
        if board_list.count(i) == 3 and i not in Table_3_same_Cards:
            Table_3_same_Cards.append( i )
    Table_3_same_Cards.sort(reverse=True)
    return Table_3_same_Cards

def Table_4_same_Cards_List(board_list=None) :
    """ [] or max one index"""
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return []

    board_list = [n(i) for i in board_list ]
    
    Table_4_same_Cards = []
    for i in board_list:
        if board_list.count(i) == 4 and i not in Table_4_same_Cards:
            Table_4_same_Cards.append( i )
    Table_4_same_Cards.sort(reverse=True)
    return Table_4_same_Cards

    
def Table_Individual(board_list=None) : 
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False

    board_list = [n(i) for i in board_list ]

    pair_list = []
    for i in range(2,15):
        if board_list.count(i) >= 2 :
            pair_list.append(board_list.count(i))
    if len(pair_list) == 0 :
        return True
    else :
        return False
    
def Table_1_pair(board_list=None) : 
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False

    board_list = [n(i) for i in board_list ]

    pair_list = []
    for i in range(2,15):
        if board_list.count(i) >= 2 :
            pair_list.append(board_list.count(i))

    if len(pair_list) == 1 and 2 in pair_list :
        return True
    else :
        return False


def Table_2_pair(board_list=None) : 
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False

    board_list = [n(i) for i in board_list ]

    pair_list = []
    for i in range(2,15):
        if board_list.count(i) >= 2 :
            pair_list.append(board_list.count(i))

    if len(pair_list) == 2 and 3 not in pair_list :
        return True
    else :
        return False
        
def Table_3_of_kinds(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False

    board_list = [n(i) for i in board_list ]

    pair_list = []
    for i in range(2,15):
        if board_list.count(i) >= 2 :
            pair_list.append(board_list.count(i))

    if len(pair_list) == 1 and 3 in pair_list :
        return True
    else :
        return False


def Table_full_house(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    pair_list = []
    for i in range(2,15):
        if board_list.count(i) >= 2 :
            pair_list.append(board_list.count(i))

    if len(pair_list) == 2 and 3 in pair_list :
        return True
    else :
        return False


def Table_4_of_kinds(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ] 

    pair_list = []
    for i in range(2,15):
        if board_list.count(i) >= 2 :
            pair_list.append(board_list.count(i))

    if len(pair_list) == 1 and 4 in pair_list :
        return True
    else :
        return False




def Me_Individual(board_list=None):
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 0 and board_list.count( n(c.my_2th_card) ) == 0 and n(c.my_1th_card) != n(c.my_2th_card) :
        return True
    else :
        return False

def Me_pocket_pair(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 0 and board_list.count( n(c.my_2th_card) ) == 0 and n(c.my_1th_card) == n(c.my_2th_card) :
        return True
    else :
        return False


def Me_1_pair(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if (board_list.count( n(c.my_1th_card) ) == 1 and board_list.count( n(c.my_2th_card) ) == 0) \
       or (board_list.count( n(c.my_1th_card) ) == 0 and board_list.count( n(c.my_2th_card) ) == 1):
        return True
    else :
        return False

def Me_2_pair(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 1 and board_list.count( n(c.my_2th_card) ) == 1 and n(c.my_1th_card) != n(c.my_2th_card) :
        return True
    else :
        return False
    
def Me_3_of_kinds(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if (board_list.count( n(c.my_1th_card) ) == 2 and board_list.count( n(c.my_2th_card) ) == 0) \
       or (board_list.count( n(c.my_1th_card) ) == 0 and board_list.count( n(c.my_2th_card) ) == 2):
        return True
    else :
        return False

def Me_pocket_3_of_kinds(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 1 and board_list.count( n(c.my_2th_card) ) == 1 and n(c.my_1th_card) == n(c.my_2th_card) and ( Table_Individual( board_list ) or Table_4_of_kinds( board_list ) ) :
        return True
    else :
        return False

def Me_full_house(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if ( (board_list.count( n(c.my_1th_card) ) == 2 and 1 <= board_list.count( n(c.my_2th_card) ) <= 2)\
       or (1 <= board_list.count( n(c.my_1th_card) ) <= 2 and board_list.count( n(c.my_2th_card) ) == 2) ) and n(c.my_1th_card) != n(c.my_2th_card) :
        return True
    else :
        return False

def Me_pocket_full_house(board_list=None) :
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False

    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 1 and board_list.count( n(c.my_2th_card) ) == 1 and n(c.my_1th_card) == n(c.my_2th_card) \
       and ( Table_1_pair( board_list ) or Table_2_pair( board_list ) or Table_3_of_kinds( board_list ) ):
        return True
    else :
        return False

def Me_4_of_kinds(board_list=None) : 
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 3 or board_list.count( n(c.my_2th_card) ) == 3 :
        return True
    else :
        return False

def Me_pocket_4_of_kinds(board_list=None) : 
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return False
        
    board_list = [n(i) for i in board_list ]

    if board_list.count( n(c.my_1th_card) ) == 2 and board_list.count( n(c.my_2th_card) ) == 2 and n(c.my_1th_card) == n(c.my_2th_card) :
        return True
    else :
        return False

def Cards_Matching(board_list, My_Card) : 

    if board_list == []:
        return None
    board_list = [n(i) for i in board_list ]
    My_Card = n( My_Card )
    
    board_list = list(set(board_list))
    board_list.sort(reverse=True)
    if My_Card in board_list :
        for i in range( len(board_list) ) :
            if My_Card == board_list[i] :
                return i+1
    else :
        return None

def cards_ranking(My_Card, board_list=None) : # screenshot va be cheat sheet e pair functions ezafe shavad
    """
    Ranks: 1,...,6
    It does not return None at all. 
    This is an independant function and it does not have any True or False function
    1: (12, [9,8,5]). 1: (12, [12,11,10]). 1: (12, [12,12,10]). 1: (5, []) 
    2: (10, [12,10,7]). 4: (5, [12,10,7]). 6: (3, [12,11,7,6,5])
    """
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return 1

    board_list = [n(i) for i in board_list ]

    My_Card = n( My_Card )
    
    board_list = list(set(board_list))
    board_list.sort(reverse=True)
    Cards_Ranking = 1
    for i in range( len(board_list) ) :
        if My_Card >= board_list[i] :
            return Cards_Ranking
        else :
            Cards_Ranking = Cards_Ranking + 1
    return Cards_Ranking


def Me_Individual_Ranking(board_list=None) : 
    """
    Ranks :1,...,9
    1: ([14,13,5,4,3],12,8).  2: ([14,14,5,4,3],12,8)
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_Individual(board_list) == True :

        board_list = [n(i) for i in board_list ]        
        board_list.sort(reverse=True)

        My_Card = max(c.my_1th_card,c.my_2th_card)
        rank = 1
        for i in range(14,1,-1):
            if i == My_Card :
                break
            elif i in board_list :
                continue
            rank += 1

        return rank    

def Me_pocket_pair_Ranking(board_list=None) : 
    """
    Ranks :1,2,3,4,5,6
    1 :([14,14,6,5,4],9,9) or ([14,14,14,5,4],9,9)
    6 :([14,13,9,8,7],4,4)
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_pocket_pair(board_list) == True :

        board_list = [n(i) for i in board_list ]        
        board_list.sort(reverse=True)
        
        board_list = [i for i in board_list if board_list.count( i ) == 1]
        My_Card = c.my_1th_card
        rank = 1
        for i in range(14,1,-1):
            if i == My_Card :
                break
            elif i in board_list :
                rank += 1

        return rank  

def Me_1_pair_Ranking(board_list=None) : 
    """
    Best Rank: (1, 14) Example: ([10,8,2,5],14,10)
    second index is my Kicker card
    ([14,14,10,8,5],10,11): (1, 11)
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_1_pair(board_list) == True :

        board_list = [n(i) for i in board_list ]        
        board_list.sort(reverse=True)

        board_list = [i for i in board_list if board_list.count( i ) == 1]
        if board_list.count( n(c.my_1th_card) ) == 1 :
            My_Card = c.my_1th_card
            My_Kicker = c.my_2th_card
        elif board_list.count( n(c.my_2th_card) ) == 1 :
            My_Card = c.my_2th_card
            My_Kicker = c.my_1th_card

        return ( Cards_Matching ( board_list , My_Card ) , n(My_Kicker) )

def Me_2_pair_Ranking(board_list=None) : 
    """
    Best Rank: (1, 2) Example: ([6,2,2,10,8],10,8)
    note: first index is always lower like 1 in (1, 2)
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_2_pair(board_list) == True :

        board_list = [n(i) for i in board_list ]        
        board_list.sort(reverse=True)

        return ( Cards_Matching( board_list , max(c.my_1th_card,c.my_2th_card) ) , Cards_Matching( board_list , min(c.my_1th_card,c.my_2th_card) ) )

def Me_3_of_kinds_Ranking(board_list=None) : 
    """
    Best Rank: (1, 14) Example: ([5,6,6,8],6 ,14 )
    second index is my Kicker card
    First index rank: 1,2
    First index at Table_full_house or Table_1_pair is: Always 1
    First index at Table_2_pair first index is: 1,2. At Table_2_pair second index will be returned but not usable.
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_3_of_kinds( board_list) == True :

        board_list = [n(i) for i in board_list ]        
        board_list.sort(reverse=True)

        if board_list.count( n(c.my_1th_card) ) == 2 :
            My_Card = c.my_1th_card
            My_Kicker = c.my_2th_card
        elif board_list.count( n(c.my_2th_card) ) == 2 :
            My_Card = c.my_2th_card
            My_Kicker = c.my_2th_card

        Card = []
        for i in range( len(board_list) ) :
            if board_list.count( board_list[i] ) == 2 and board_list[i] not in Card :
                Card.append( board_list[i] )
        Card.sort(reverse=True)
        
        return ( Cards_Matching( Card , My_Card ) , n(My_Kicker) )

def Me_pocket_3_of_kinds_Ranking(board_list=None) :
    """
    Ranks: 1,2,3,4,5,6
    6: if Table_4_of_kinds : ([4,4,4,4,10],10,10)
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_pocket_3_of_kinds(board_list) == True :

        if Table_4_of_kinds(board_list) == True :
            return 6
        board_list = [n(i) for i in board_list ]        
        board_list.sort(reverse=True)

        My_Card = c.my_1th_card
        return Cards_Matching( board_list , My_Card )

def Me_full_house_Ranking(board_list=None) : 
    """
    Ranks: 1,2,3,4
    Table_2_pair : 1 ([4,4,10,7,7],10,7) or ([4,10,10,7,7],10,4).  2 ([7,10,10,4,4],10,4).  4 ([4,4,10,7,7],4,10).
    Table_1_pair : depends on 2 same cards Ranking not 3 same cards ranking.
    Table_1_pair : 1 ( [2,3,5,5,6] , 5 , 6 ) .  2 ( [2,3,5,5,6] , 5 , 3 ).  3 ( [2,3,5,5,6] , 5 , 2 )
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_full_house(board_list) == True :

        board_list = [n(i) for i in board_list ]       
        board_list.sort(reverse=True)

        if Table_2_pair( board_list ) :
            
            Card = []
            for i in range( len(board_list) ) :
                if board_list.count( board_list[i] ) == 2 and board_list[i] not in Card:
                    Card.append( board_list[i] )
            Card.sort(reverse=True)

            if Card[0] not in ( n(c.my_1th_card) ,n(c.my_2th_card) ) :
                return 4 # very rare
            else :
                if Card[1] not in ( n(c.my_1th_card) ,n(c.my_2th_card) ) and Card[1] != min(board_list) :
                    return 1
                if ( n(c.my_1th_card) ) != Card[0] : My_Card = c.my_1th_card
                if ( n(c.my_2th_card) ) != Card[0] : My_Card = c.my_2th_card
                Card2 = []
                for i in (board_list) :
                    if Card[0] == i or i in Card2:
                        continue
                    else :
                        Card2.append(i)
                return Cards_Matching( Card2 , My_Card )

        if board_list.count( n(c.my_1th_card) ) == 1 :
            My_Card = c.my_1th_card
        elif board_list.count( n(c.my_2th_card) ) == 1 :
            My_Card = c.my_2th_card
            
        Card = []
        for i in range( len(board_list) ) :
            if board_list.count( board_list[i] ) == 1 :
                Card.append( board_list[i] )
        Card.sort(reverse=True)
        
        return Cards_Matching( Card , My_Card )

def Me_pocket_full_house_Ranking(board_list=None) :
    """
    Ranks: 1,2,3
    Table_1_pair: 1 ([2,5,5,7,9], 7,7).  2 ([2,5,5,7,9], 2,2).
    Table_2_pair: 1 ([2,2,5,5,7], 7,7).  3 ([2,2,5,7,7], 5,5).  4 ([2,5,5,7,7], 2,2).
    Table_3_of_kinds: 3 ([5,5,5,7,8], 8,8).
    """
    
    if board_list == None :
        board_list = board_cards_list()[:]
    if board_list == []:
        return None

    if Me_pocket_full_house( board_list ) == True :

        board_list = [n(i) for i in board_list ]         
        board_list.sort(reverse=True)

        if Table_1_pair( board_list ) == True :
            for i in range( len(board_list) ) :
                if board_list.count( board_list[i] ) == 2 :
                    Card = board_list[i]
                    break
            if Card < c.my_1th_card :
                return 1
            elif Card > c.my_1th_card :
                return 2
            
        elif Table_2_pair( board_list ) == True :
            Card = []
            for i in range( len(board_list) ) :
                if board_list.count( board_list[i] ) == 2 and board_list[i] not in Card:
                    Card.append( board_list[i] )
            
            if max(Card) < c.my_1th_card :
                return 1
            elif min(Card) < c.my_1th_card < max(Card) :
                return 3
            elif min(Card) > c.my_1th_card :
                return 4

        elif Table_3_of_kinds( board_list ) == True :
            return 3


