#OK
from decision_making.rules_and_info.suit_and_value import s, n
#from suit_and_value import s, n
import configs as c

"""
Functions with True or False return,are in 2 kind of categoreis: 1.Me_str_ Me_Open_str_draw 2.Table_str 
If one of them is True the rest will be False. All functions can be False at the same time.
At Str file there is a Exeption for this: Only Table_str_1_cards and Table_str_2_cards Functions can be True at the same time

Ranking Functions are :1.Me_str_(1 or 2 cards) 2.Me_Open_str(1 or 2 cards)_draw .
Ranking Functions return 1.a Number or 
2.None value if their True or False Functions have not been True already or we are at pre flop stage.
Table functions has no rankings in Flush and Pair files. in Str file there are Table_.._Number functions. 
"""
"""
In Python, List variables can be modified inside function's 
scopes which have came from other scopes even if they are 
assigned to the other variable names. 
To avoid this misbehavior, at the beginning of functions 
always copy lists by using List = List[:]  or by doing List = [...]. 
This way new List variables will have new separated IDs.
"""

# Supporting Functions:-------------------------

def str_length(board_list):

    if board_list == []:
        return None
    List = board_list[:]
    #if 14 in List :
        #List.append(1)
    List = list(set(List))
    List.sort()
    
    length_list = []
    n = 1
    for i in range( 1,len(List) ):
        if List[i] - List[i-1] == 1 :
            n = n + 1
        if List[i] - List[i-1] != 1 or i == len(List) - 1 :
            length_list.append(n)
            n = 1
    return max(length_list)
            
def str_1_Cards_list(board_list) :

    if board_list == []:
        return []
    List = board_list[:]

    for i in range( len(List) ) :
        List[i] = n( List[i] )
    str_1_Cards_list = []
    for i in range(1,15):

        Loop_List = []
        for cards in List:
            Loop_List.append(cards)
        if 14 in Loop_List :
            Loop_List.append(1)
        if i in Loop_List :
            continue
        Loop_List.append(i)
        if str_length( Loop_List ) == 5 :
            if len(List) == 4 :
                str_1_Cards_list.append(i)
            if len(List) == 5 :
                Loop_List2 = []
                for cards in List:
                    Loop_List2.append(cards)
                if 14 in Loop_List2 :
                    Loop_List2.append(1)
                if str_length( Loop_List2 ) != 5 :
                    str_1_Cards_list.append(i)
        if str_length( Loop_List ) == 6 :
            if (1 not in Loop_List and min(Loop_List) != i) or (1 in Loop_List and abs(i-1) <= 5) or (1 in Loop_List and abs(i-14) <= 4) :
                str_1_Cards_list.append(i)

    str_1_Cards_list.sort(reverse=True)
    return str_1_Cards_list
                                    
def str_2_Cards_list(board_list) :

    if board_list == []:
        return []
    List = board_list[:]

    for i in range( len(List) ) :
        List[i] = n( List[i] )
    str_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            Loop_List = []
            for cards in List:
                Loop_List.append(cards)
            if 14 in Loop_List :
                Loop_List.append(1)
            if i == j or i in Loop_List or j in Loop_List :
                continue
            Loop_List.append(i)
            Loop_List.append(j)
            
            if len(List) == 3 :
                
                if str_length( Loop_List ) == 5 :
                    str_2_Cards_list.append((i,j))

            if len(List) == 4 :
                
                if str_length( Loop_List ) == 5 \
                and i not in str_1_Cards_list( List ) \
                and j not in str_1_Cards_list( List ) :
                    str_2_Cards_list.append((i,j))
                    
                if str_length( Loop_List ) == 6 :
                    Loop_List.sort()
                    if (1 in Loop_List and min(i,j) >= 3 and Loop_List[1] not in (i,j)) \
                    or (1 in Loop_List and min(i,j) == 2) \
                    or (1 not in Loop_List and Loop_List[0] not in (i,j)) :
                        str_2_Cards_list.append((i,j))

            if len(List) == 5 :
                
                Loop_List2 = []
                for cards in List:
                    Loop_List2.append(cards)
                if 14 in Loop_List2 :
                    Loop_List2.append(1)

                if str_length( Loop_List ) == 5 \
                and str_length( Loop_List2 ) != 5 \
                and i not in str_1_Cards_list( List ) \
                and j not in str_1_Cards_list( List ) :
                    str_2_Cards_list.append((i,j))

                if str_length( Loop_List ) == 6 :
                    Loop_List.sort()
                    if ( (1 not in Loop_List and str_length( list( set(Loop_List) - set([min(Loop_List2)]) ) ) != 6 and Loop_List[0] not in (i,j)) \
                         or (1 not in Loop_List and str_length( list( set(Loop_List) - set([min(Loop_List2)]) ) ) == 6 and Loop_List[1] not in (i,j)) \
                         or (1 in Loop_List and max(i,j) <= 6) \
                         or (1 in Loop_List and max(i,j) > 6 and str_length( list( set(Loop_List) - set( [min(list(set(Loop_List2)-set([1])))] ) ) ) != 6 and Loop_List[1] not in (i,j)) \
                         or (1 in Loop_List and max(i,j) > 6 and str_length( list( set(Loop_List) - set( [min(list(set(Loop_List2)-set([1])))] ) ) ) == 6 and Loop_List[2] not in (i,j)) )\
                    and str_length( list( set(Loop_List2) | set([i]) ) ) !=6 \
                    and str_length( list( set(Loop_List2) | set([j]) ) ) !=6 :
                        str_2_Cards_list.append((i,j))

                if str_length( Loop_List ) == 7 :
                    Loop_List.sort()
                    if ( 1 in Loop_List and min(i,j)>7 and Loop_List[1] not in (i,j) and Loop_List[2] not in (i,j) ) \
                    or ( 1 in Loop_List and max(i,j)<=7 and Loop_List[0] not in (i,j) and Loop_List[1] not in (i,j) ) \
                    or ( 1 not in Loop_List and Loop_List[0] not in (i,j) and Loop_List[1] not in (i,j) ) :
                        str_2_Cards_list.append((i,j))

    for tuples in str_2_Cards_list :
        if (min(tuples),max(tuples)) in str_2_Cards_list and min(tuples) != max(tuples):
            str_2_Cards_list.remove( (min(tuples),max(tuples)) )
    str_2_Cards_list = list( set(str_2_Cards_list) )
    
    str_2_Cards_list.sort(reverse=True)
    return str_2_Cards_list

def open_str_draw_1_Cards_list(board_list) :

    if board_list == []:
        return []
    List = board_list[:]

    for i in range( len(List) ) :
        List[i] = n( List[i] )
    open_str_draw_1_Cards_list = []
    for i in range(1,15):

        Loop_List = []
        for cards in List:
            Loop_List.append(cards)
        if 14 in Loop_List :
            Loop_List.append(1)
        if i in Loop_List :
            continue
        Loop_List.append(i)
        
        if len(List) == 3 :
            if str_length( Loop_List ) == 4 and min(Loop_List) != 1 and max(Loop_List) != 14 :
                open_str_draw_1_Cards_list.append(i)

        if len(List) == 4 :
            if str_length( Loop_List ) == 4 :
                while 14 in Loop_List :
                    Loop_List.remove(14)
                while 1 in Loop_List :
                    Loop_List.remove(1)
                if str_length( Loop_List ) == 4 \
                and str_length( List ) != 4 :
                    open_str_draw_1_Cards_list.append(i)
                    
    open_str_draw_1_Cards_list.sort(reverse=True)
    
    return open_str_draw_1_Cards_list
            
def open_str_draw_2_Cards_list(board_list) :

    if board_list == []:
        return []
    List = board_list[:]

    for i in range( len(List) ) :
        List[i] = n( List[i] )
    open_str_draw_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            

            if len(List) == 3 :
                
                Loop_List = []
                for cards in List:
                    Loop_List.append(cards)

                if i == j or i in Loop_List or j in Loop_List or i in(1,14) or j in (1,14):
                    continue
                while 14 in Loop_List :
                    Loop_List.remove(14)
                while 1 in Loop_List :
                    Loop_List.remove(1)
                Loop_List.append(i)
                Loop_List.append(j)
                if str_length( Loop_List ) == 4 \
                and i not in open_str_draw_1_Cards_list( List ) \
                and j not in open_str_draw_1_Cards_list( List ) :
                    open_str_draw_2_Cards_list.append((i,j))

            if len(List) == 4 :

                Loop_List = []
                for cards in List:
                    Loop_List.append(cards)

                if 14 in Loop_List :
                    Loop_List.append(1)
                if i == j or i in Loop_List or j in Loop_List or i in(1,14) or j in (1,14):
                    continue
                Loop_List.append(i)
                Loop_List.append(j)
                if str_length( Loop_List ) == 4 :
                    while 14 in Loop_List :
                        Loop_List.remove(14)
                    while 1 in Loop_List :
                        Loop_List.remove(1)
                    if str_length( Loop_List ) == 4  \
                    and i not in open_str_draw_1_Cards_list( List ) \
                    and j not in open_str_draw_1_Cards_list( List ) \
                    and str_length( List ) !=4 :
                        open_str_draw_2_Cards_list.append((i,j))
                if str_length( Loop_List ) == 2 :
                    p = 0
                    for k in range(1,15) :
                        
                        Loop_List = []
                        for cards in List:
                            Loop_List.append(cards)

                        if 14 in Loop_List : 
                            Loop_List.append(1)
                        Loop_List.append(i)
                        Loop_List.append(j)
                        if k in Loop_List : 
                            continue
                        Loop_List.append(k) 
                        if str_length( Loop_List ) == 5 : 
                            p = p + 1
                        if p == 2 :
                            open_str_draw_2_Cards_list.append((i,j))
                            break

    for tuples in open_str_draw_2_Cards_list :
        if (min(tuples),max(tuples)) in open_str_draw_2_Cards_list and min(tuples) != max(tuples):
            open_str_draw_2_Cards_list.remove( (min(tuples),max(tuples)) )
    open_str_draw_2_Cards_list = list( set(open_str_draw_2_Cards_list) )

    open_str_draw_2_Cards_list.sort(reverse=True)
                    
    return open_str_draw_2_Cards_list

# Supporting Functions Ended--------------------


def Table_str_1_cards(board_list=None) :
    """
    Only Table_str_1_cards and Table_str_2_cards Functions can be True at the same time
    At River just 30% it happens to be False for both Table_str_1_ and Table_str_2 at the same time.
    """

    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False

    if len(str_1_Cards_list( board_list )) == 0 :
        return False
    else :
        return True

def Table_str_2_cards(board_list=None) :
    """ Only Table_str_1_cards and Table_str_2_cards Functions can be True at the same time """    
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False

    if len(str_2_Cards_list( board_list )) == 0 :
        return False
    else :
        return True

def Table_str_1_cards_Number(board_list=None) :
    """ Min Number is 0 if Table_str_1_cards == Flase, Max Number is 2 """
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return 0

    return len(str_1_Cards_list( board_list )) 

def Table_str_2_cards_Number(board_list=None) : 
    """
    Min Number is 0 if Table_str_2_cards== False, Max Number is 3 .
    At River just 30% it happens to be 0 for both Table_str_1_ and Table_str_2 at the same time.
    """
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return 0

    return len(str_2_Cards_list( board_list )) 

def Table_str_5_cards(board_list=None):
    """ At River happens. returns True or False """
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False

    if 14 in board_list :
        board_list.append(1)
    if str_length( board_list ) == 5:
        return True
    else :
        return False


def Me_str_1_cards(board_list=None) :
    """ if Me_str_2_cards == True : return False """
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False

    if Me_str_2_cards( board_list ) == True :
        return False
    
    for i in str_1_Cards_list( board_list ) :
        if n(c.my_hole_cards[0]) == i or n(c.my_hole_cards[1]) == i :
            return True
        if n(c.my_hole_cards[0]) == 14 :
            if 1 == i or n(c.my_hole_cards[1]) == i :
                return True
        if n(c.my_hole_cards[1]) == 14 :
            if n(c.my_hole_cards[0]) == i or 1 == i :
                return True   
     
    return False

def Me_str_2_cards(board_list=None) :
    """ if Me_str_1_cards == True : return False """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False

    if n(c.my_hole_cards[0]) == n(c.my_hole_cards[1]):
        return False
    for i in str_2_Cards_list( board_list ) :
        if n(c.my_hole_cards[0]) in i and n(c.my_hole_cards[1]) in i :
            return True
        if n(c.my_hole_cards[0]) == 14 :
            if 1 in i and n(c.my_hole_cards[1]) in i :
                return True
        if n(c.my_hole_cards[1]) == 14 :
            if n(c.my_hole_cards[0]) in i and 1 in i :
                return True   
    return False

def Me_str_1_cards_Ranking(board_list=None) :
    """
    Rank 1,2 & None
    None if Me_str_2_cards == True or Me_str == False
    1 ( [7,8,9,11] , 10, 2 ) or ([7, 8, 9, 11], 10, 6).  2 ( [7,8,9,10] , 6, 2 )
    """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return None

    if Me_str_2_cards( board_list ) == True :
        return None
    
    rank = 0
    for i in str_1_Cards_list( board_list ) :
        rank += 1
        if n(c.my_hole_cards[0]) == i or n(c.my_hole_cards[1]) == i :
            return rank
        if n(c.my_hole_cards[0]) == 14 :
            if 1 == i or n(c.my_hole_cards[1]) == i :
                return rank
        if n(c.my_hole_cards[1]) == 14 :
            if n(c.my_hole_cards[0]) == i or 1 == i :
                return rank    

def Me_str_2_cards_Ranking(board_list=None) :
    """
    Rank 1,2,3 & None
    1 ([7, 8, 9, 11], 10, 12).  2 ([7, 8, 9], 10, 6).  3 ([7, 8, 9], 5, 6)
    """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return None

    if n(c.my_hole_cards[0]) == n(c.my_hole_cards[1]):
        return None
    rank = 0
    for i in str_2_Cards_list( board_list ) :
        rank += 1
        if n(c.my_hole_cards[0]) in i and n(c.my_hole_cards[1]) in i :
            return rank
        if n(c.my_hole_cards[0]) == 14 :
            if 1 in i and n(c.my_hole_cards[1]) in i :
                return rank
        if n(c.my_hole_cards[1]) == 14 :
            if n(c.my_hole_cards[0]) in i and 1 in i :
                return rank

def Me_str(board_list=None) : 
    """ if Me_str_2_cards or Me_str_1_cards """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False
        
    if Me_str_2_cards( board_list ) == True or Me_str_1_cards( board_list ) == True :
        return True
    else:
        return False


def is_there_any_better_possible_1_card_straight_on_table(board_list=None) : # screen shot again with these new Edition and discriptoins
    """
    returns True or False only.
    Table_str_1_cards must be True to return True.

    is_there_any_better_possible_1_card_straight_on_table() == True ;Me_str_2_cards_Ranking == 2 :
    ([7, 8, 9,  11, 12], 5, 6) ; ([5, 8, 9,  11, 12], 6, 7) ; ([6, 8, 9,  11, 12], 5, 7) 
    ([7, 8, 9,  11], 5, 6)
    is_there_any_better_possible_1_card_straight_on_table() == True ;Me_str_2_cards_Ranking == 1 :
    ([9, 10, 11,  13, 14], 7, 8) ; ([7, 10, 11,  13, 14], 8, 9) ; ([8, 10, 11,  13, 14], 7, 9)
    ([10, 11, 12,  14], 8, 9)
    if Table_str_1_cards() is True, Me_str_2_cards_Ranking == 3 is not possible 
    if Me_str_2_cards == True and Table_str_1_cards == True, automatically my higher card get lower or higher than str_1_Cards_list()[0]

    if Me_str_1_cards_Ranking == 2 or i'm not straight ,it will return True :
    False: ([7, 8, 9, 10], 2, 11). True: ([7, 8, 9, 10], 2, 6). True: ([7, 8, 9, 10], 2, 3). 

    This function common usage is: (Me_str_2_cards() and is_there_any_better_possible_1_card_straight_on_table()) means my 2 cards straight is not good.
    """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False
        
    if Table_str_1_cards( board_list ) == False :
        return False
    elif Me_str_1_cards_Ranking( board_list , c.my_hole_cards[0] , c.my_hole_cards[1] ) == 1 : 
        return False 
    elif Me_str_2_cards( board_list , c.my_hole_cards[0] , c.my_hole_cards[1] ) == False :
        return True
    elif max(c.my_hole_cards[0],c.my_hole_cards[1]) < str_1_Cards_list( board_list )[0] : #equal is not possible
        return True
    else :
        return False


def Me_Open_str_draw_1_cards(board_list=None) :
    """
    if Me_str == True: retun False
    ( [7,8,9] ,2 ,10 ): True.  ( [6,7,8,9] ,2 ,10 ): False
    """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False
        
    if Me_Open_str_draw_2_cards( board_list ) == True \
       or Me_str_2_cards( board_list ) == True :
        return False
    
    for i in open_str_draw_1_Cards_list( board_list ) :
        if n(c.my_hole_cards[0]) == i or n(c.my_hole_cards[1]) == i :
            return True
    return False    

def Me_Open_str_draw_2_cards(board_list=None) :
    """ if Me_str == True: retun False """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return False
        
    if n(c.my_hole_cards[0]) == n(c.my_hole_cards[1]):
        return False
    for i in open_str_draw_2_Cards_list( board_list ) :
        if n(c.my_hole_cards[0]) in i and n(c.my_hole_cards[1]) in i :
            return True
        if n(c.my_hole_cards[0]) == 14 :
            if 1 in i and n(c.my_hole_cards[1]) in i :
                return True
        if n(c.my_hole_cards[1]) == 14 :
            if n(c.my_hole_cards[0]) in i and 1 in i :
                return True   
    return False

def Me_Open_str_draw_1_cards_Ranking(board_list=None) :
    """ Rank 1,2 & None """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return None
        
    if Me_Open_str_draw_2_cards( board_list ) == True \
       or Me_str_2_cards( board_list ) == True :
        return None
    
    rank = 0
    for i in open_str_draw_1_Cards_list( board_list ) :
        rank += 1
        if n(c.my_hole_cards[0]) == i or n(c.my_hole_cards[1]) == i :
            return rank

def Me_Open_str_draw_2_cards_Ranking(board_list=None) :
    """ Rank 1,2,3 & None """
    
    if board_list == None :
        board_list = c.board_cards[:]
    if board_list == []:
        return None
        
    if n(c.my_hole_cards[0]) == n(c.my_hole_cards[1]):
        return None
    
    rank = 0
    for i in open_str_draw_2_Cards_list( board_list ) :
        rank += 1
        if n(c.my_hole_cards[0]) in i and n(c.my_hole_cards[1]) in i :
            return rank
        if n(c.my_hole_cards[0]) == 14 :
            if 1 in i and n(c.my_hole_cards[1]) in i :
                return rank
        if n(c.my_hole_cards[1]) == 14 :
            if n(c.my_hole_cards[0]) in i and 1 in i :
                return rank
    

