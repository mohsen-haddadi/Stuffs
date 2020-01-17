"""
There are 4 Functions which returns a List in accordance with table cards

Functions with True or False return,are in 2 kind of categoreis: 1.Table_ 2.Me_
If one of them is True the rest will be False. one Function is always True.

Ranking Functions return 1.a Number or 2.a tuple or 3.None value if their True or False Functions have not been True already.
"""

def n(Card) :
    if Card in ('2 c','2 d','2 h','2 s',2):
        return 2
    if Card in ('3 c','3 d','3 h','3 s',3):
        return 3
    if Card in ('4 c','4 d','4 h','4 s',4):
        return 4
    if Card in ('5 c','5 d','5 h','5 s',5):
        return 5
    if Card in ('6 c','6 d','6 h','6 s',6):
        return 6
    if Card in ('7 c','7 d','7 h','7 s',7):
        return 7
    if Card in ('8 c','8 d','8 h','8 s',8):
        return 8
    if Card in ('9 c','9 d','9 h','9 s',9):
        return 9
    if Card in ('10 c','10 d','10 h','10 s',10):
        return 10
    if Card in ('J c','J d','J h','J s',11):
        return 11
    if Card in ('Q c','Q d','Q h','Q s',12):
        return 12
    if Card in ('K c','K d','K h','K s',13):
        return 13
    if Card in ('A c','A d','A h','A s',14):
        return 14

def Table_Individual_Cards_List( List ) :
    """ [7,7,5,10] returns [10, 5]"""
    List = [n(i) for i in List ] 
    Individual_Cards = [i for i in List if List.count(i) == 1]
    Individual_Cards.sort(reverse=True)
    return Individual_Cards

def Table_2_same_Cards_List( List ) : 
    """ [7,7,5,5,6] returns [7, 5]"""
    List = [n(i) for i in List ]
    
    Table_2_same_Cards = []
    for i in List:
        if List.count(i) == 2 and i not in Table_2_same_Cards:
            Table_2_same_Cards.append( i )
    Table_2_same_Cards.sort(reverse=True)
    return Table_2_same_Cards

def Table_3_same_Cards_List( List ) :
    """ [] or max one index"""
    List = [n(i) for i in List ]
    
    Table_3_same_Cards = []
    for i in List:
        if List.count(i) == 3 and i not in Table_3_same_Cards:
            Table_3_same_Cards.append( i )
    Table_3_same_Cards.sort(reverse=True)
    return Table_3_same_Cards

def Table_4_same_Cards_List( List ) :
    """ [] or max one index"""
    List = [n(i) for i in List ] 
    
    Table_4_same_Cards = []
    for i in List:
        if List.count(i) == 4 and i not in Table_4_same_Cards:
            Table_4_same_Cards.append( i )
    Table_4_same_Cards.sort(reverse=True)
    return Table_4_same_Cards

    
def Table_Individual( List ) : 

    List = [n(i) for i in List ] 

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))
    if len(pair_list) == 0 :
        return True
    else :
        return False
    
def Table_1_pair( List ) : 

    List = [n(i) for i in List ] 

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 1 and 2 in pair_list :
        return True
    else :
        return False


def Table_2_pair( List ) : 

    List = [n(i) for i in List ] 

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 2 and 3 not in pair_list :
        return True
    else :
        return False
        
def Table_3_of_kinds( List ) :

    List = [n(i) for i in List ] 

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 1 and 3 in pair_list :
        return True
    else :
        return False


def Table_full_house( List ) :

    List = [n(i) for i in List ] 

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 2 and 3 in pair_list :
        return True
    else :
        return False


def Table_4_of_kinds( List ) :

    List = [n(i) for i in List ] 

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 1 and 4 in pair_list :
        return True
    else :
        return False




def Me_Individual( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 0 and n(My_1th_Card) != n(My_2th_Card) :
        return True
    else :
        return False

def Me_pocket_pair( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 0 and n(My_1th_Card) == n(My_2th_Card) :
        return True
    else :
        return False


def Me_1_pair( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if (List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 0) \
       or (List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 1):
        return True
    else :
        return False

def Me_2_pair( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 1 and n(My_1th_Card) != n(My_2th_Card) :
        return True
    else :
        return False
    
def Me_3_of_kinds( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if (List.count( n(My_1th_Card) ) == 2 and List.count( n(My_2th_Card) ) == 0) \
       or (List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 2):
        return True
    else :
        return False

def Me_pocket_3_of_kinds( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 1 and n(My_1th_Card) == n(My_2th_Card) and ( Table_Individual( List ) or Table_4_of_kinds( List ) ) :
        return True
    else :
        return False

def Me_full_house( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if ( (List.count( n(My_1th_Card) ) == 2 and 1 <= List.count( n(My_2th_Card) ) <= 2)\
       or (1 <= List.count( n(My_1th_Card) ) <= 2 and List.count( n(My_2th_Card) ) == 2) ) and n(My_1th_Card) != n(My_2th_Card) :
        return True
    else :
        return False

def Me_pocket_full_house( List , My_1th_Card , My_2th_Card ) :

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 1 and n(My_1th_Card) == n(My_2th_Card) \
       and ( Table_1_pair( List ) or Table_2_pair( List ) or Table_3_of_kinds( List ) ):
        return True
    else :
        return False

def Me_4_of_kinds( List , My_1th_Card , My_2th_Card ) : 

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 3 or List.count( n(My_2th_Card) ) == 3 :
        return True
    else :
        return False

def Me_pocket_4_of_kinds( List , My_1th_Card , My_2th_Card ) : 

    List = [n(i) for i in List ] 

    if List.count( n(My_1th_Card) ) == 2 and List.count( n(My_2th_Card) ) == 2 and n(My_1th_Card) == n(My_2th_Card) :
        return True
    else :
        return False

def Cards_Matching( List , My_Card ) : 
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    Cards_Matching( [ Card_1th, Card_2th, Card_3th, Card_4th ] , My_Card )
    """

    List = [n(i) for i in List ] 
    My_Card = n( My_Card )
    
    List = list(set(List))
    List.sort(reverse=True)
    if My_Card in List :
        for i in range( len(List) ) :
            if My_Card == List[i] :
                return i+1
    else :
        return None

def Me_Individual_Ranking( List , My_1th_Card , My_2th_Card ) : 
    """
    Ranks :1,...,9
    1: ([14,13,5,4,3],12,8).  2: ([14,14,5,4,3],12,8)
    """
    if Me_Individual( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]        
        List.sort(reverse=True)

        My_Card = max(My_1th_Card,My_2th_Card)
        rank = 1
        for i in range(14,1,-1):
            if i == My_Card :
                break
            elif i in List :
                continue
            rank += 1

        return rank    

def Me_pocket_pair_Ranking( List , My_1th_Card , My_2th_Card ) : 
    """
    Ranks :1,2,3,4,5,6
    1 :([14,14,6,5,4],9,9) or ([14,14,14,5,4],9,9)
    6 :([14,13,9,8,7],4,4)
    """
    if Me_pocket_pair( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]        
        List.sort(reverse=True)
        
        List = [i for i in List if List.count( i ) == 1]
        My_Card = My_1th_Card
        rank = 1
        for i in range(14,1,-1):
            if i == My_Card :
                break
            elif i in List :
                rank += 1

        return rank  

def Me_1_pair_Ranking( List , My_1th_Card , My_2th_Card ) : 
    """
    Best Rank: (1, 14) Example: ([10,8,2,5],14,10)
    second index is my Kicker card
    ([14,14,10,8,5],10,11): (1, 11)
    """
    if Me_1_pair( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]        
        List.sort(reverse=True)

        List = [i for i in List if List.count( i ) == 1]
        if List.count( n(My_1th_Card) ) == 1 :
            My_Card = My_1th_Card
            My_Kicker = My_2th_Card
        elif List.count( n(My_2th_Card) ) == 1 :
            My_Card = My_2th_Card
            My_Kicker = My_1th_Card

        return ( Cards_Matching ( List , My_Card ) , n(My_Kicker) )

def Me_2_pair_Ranking( List , My_1th_Card , My_2th_Card ) : 
    """
    Best Rank: (1, 2) Example: ([6,2,2,10,8],10,8)
    note: first index is always lower like 1 in (1, 2)
    """

    if Me_2_pair( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]        
        List.sort(reverse=True)

        return ( Cards_Matching( List , max(My_1th_Card,My_2th_Card) ) , Cards_Matching( List , min(My_1th_Card,My_2th_Card) ) )

def Me_3_of_kinds_Ranking( List , My_1th_Card , My_2th_Card ) : 
    """
    Best Rank: (1, 14) Example: ([5,6,6,8],6 ,14 )
    second index is my Kicker card
    First index rank: 1,2
    First index at Table_full_house or Table_1_pair is: Always 1
    First index at Table_2_pair first index is: 1,2. At Table_2_pair second index will be returned but not usable.
    """
    
    if Me_3_of_kinds( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]        
        List.sort(reverse=True)

        if List.count( n(My_1th_Card) ) == 2 :
            My_Card = My_1th_Card
            My_Kicker = My_2th_Card
        elif List.count( n(My_2th_Card) ) == 2 :
            My_Card = My_2th_Card
            My_Kicker = My_2th_Card

        Card = []
        for i in range( len(List) ) :
            if List.count( List[i] ) == 2 and List[i] not in Card :
                Card.append( List[i] )
        Card.sort(reverse=True)
        
        return ( Cards_Matching( Card , My_Card ) , n(My_Kicker) )


def Me_pocket_3_of_kinds_Ranking( List , My_1th_Card , My_2th_Card ) :
    """
    Ranks: 1,2,3,4,5,6
    6: if Table_4_of_kinds : ([4,4,4,4,10],10,10)
    """
    if Me_pocket_3_of_kinds( List , My_1th_Card , My_2th_Card ) == True :

        if Table_4_of_kinds( List ) == True :
            return 6
        List = [n(i) for i in List ]        
        List.sort(reverse=True)

        My_Card = My_1th_Card
        return Cards_Matching( List , My_Card )

def Me_full_house_Ranking( List , My_1th_Card , My_2th_Card ) : 
    """
    Ranks: 1,2,3,4
    Table_2_pair : 1 ([4,4,10,7,7],10,7) or ([4,10,10,7,7],10,4).  2 ([7,10,10,4,4],10,4).  4 ([4,4,10,7,7],4,10).
    Table_1_pair : depends on 2 same cards Ranking not 3 same cards ranking.
    Table_1_pair : 1 ( [2,3,5,5,6] , 5 , 6 ) .  2 ( [2,3,5,5,6] , 5 , 3 ).  3 ( [2,3,5,5,6] , 5 , 2 )
    """
    
    if Me_full_house( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]       
        List.sort(reverse=True)

        if Table_2_pair( List ) :
            
            Card = []
            for i in range( len(List) ) :
                if List.count( List[i] ) == 2 and List[i] not in Card:
                    Card.append( List[i] )
            Card.sort(reverse=True)

            if Card[0] not in ( n(My_1th_Card) ,n(My_2th_Card) ) :
                return 4 # very rare
            else :
                if Card[1] not in ( n(My_1th_Card) ,n(My_2th_Card) ) and Card[1] != min(List) :
                    return 1
                if ( n(My_1th_Card) ) != Card[0] : My_Card = My_1th_Card
                if ( n(My_2th_Card) ) != Card[0] : My_Card = My_2th_Card
                Card2 = []
                for i in (List) :
                    if Card[0] == i or i in Card2:
                        continue
                    else :
                        Card2.append(i)
                return Cards_Matching( Card2 , My_Card )

        if List.count( n(My_1th_Card) ) == 1 :
            My_Card = My_1th_Card
        elif List.count( n(My_2th_Card) ) == 1 :
            My_Card = My_2th_Card
            
        Card = []
        for i in range( len(List) ) :
            if List.count( List[i] ) == 1 :
                Card.append( List[i] )
        Card.sort(reverse=True)
        
        return Cards_Matching( Card , My_Card )


def Me_pocket_full_house_Ranking( List , My_1th_Card , My_2th_Card ) :
    """
    Ranks: 1,2,3
    Table_1_pair: 1 ([2,5,5,7,9], 7,7).  2 ([2,5,5,7,9], 2,2).
    Table_2_pair: 1 ([2,2,5,5,7], 7,7).  2 ([2,2,5,7,7], 5,5).  3 ([2,5,5,7,7], 2,2).
    Table_3_of_kinds: 3 ([5,5,5,7,8], 8,8).
    """
    if Me_pocket_full_house( List , My_1th_Card , My_2th_Card ) == True :

        List = [n(i) for i in List ]         
        List.sort(reverse=True)

        if Table_1_pair( List ) == True :
            for i in range( len(List) ) :
                if List.count( List[i] ) == 2 :
                    Card = List[i]
                    break
            if Card < My_1th_Card :
                return 1
            elif Card > My_1th_Card :
                return 2
            
        elif Table_2_pair( List ) == True :
            Card = []
            for i in range( len(List) ) :
                if List.count( List[i] ) == 2 and List[i] not in Card:
                    Card.append( List[i] )
            
            if max(Card) < My_1th_Card :
                return 1
            elif min(Card) < My_1th_Card < max(Card) :
                return 2
            elif min(Card) > My_1th_Card :
                return 3

        elif Table_3_of_kinds( List ) == True :
            return 3


