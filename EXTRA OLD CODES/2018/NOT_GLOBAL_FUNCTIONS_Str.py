"""
Functions with True or False return,are in 2 kind of categoreis: 1.Me_str_ Me_Open_str_draw 2.Table_str 
If one of them is True the rest will be False. All functions can be False at the same time.
At Str file there is a Exeption for this: Only Table_str_1_cards and Table_str_2_cards Functions can be True at the same time

Ranking Functions are :1.Me_str_(1 or 2 cards) 2.Me_Open_str(1 or 2 cards)_draw .
Ranking Functions return 1.a Number or 2.None value if their True or False Functions have not been True already.
Table functions has no rankings in Flush and Pair files. in Str file there are Table_.._Number functions. 
"""

# Supporting Functions:-------------------------


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


def str_length( List ):
    
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
            

def str_1_Cards_list( List ) :
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    str_2_Cards_list( [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """

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
            if (1 not in Loop_List and min(Loop_List) != i) or (1 in Loop_List and abs(i-1) <= 5) :
                str_1_Cards_list.append(i)

    str_1_Cards_list.sort(reverse=True)
    return str_1_Cards_list
                
                    
def str_2_Cards_list( List ) :
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    str_2_Cards_list( [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """

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


def open_str_draw_1_Cards_list( List ) :
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    str_2_Cards_list( [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """

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
            

def open_str_draw_2_Cards_list( List ) :
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    str_2_Cards_list( [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """

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



def Table_str_1_cards( table_cards_list ) :                                                           #b1
    """
    Only Table_str_1_cards and Table_str_2_cards Functions can be True at the same time
    At River just 30% it happens to be False for both Table_str_1_ and Table_str_2 at the same time.
    """
    if len(str_1_Cards_list( table_cards_list )) == 0 :
        return False
    else :
        return True

def Table_str_2_cards( table_cards_list ) :                                                       #b3
    """ Only Table_str_1_cards and Table_str_2_cards Functions can be True at the same time """    
    if len(str_2_Cards_list( table_cards_list )) == 0 :
        return False
    else :
        return True

def Table_str_1_cards_Number( table_cards_list ) :                                                        #b2
    """ Min Number is 0 if Table_str_1_cards == Flase, Max Number is 2 """
    return len(str_1_Cards_list( table_cards_list )) 

def Table_str_2_cards_Number( table_cards_list ) :                                                     #b4
    """
    Min Number is 0 if Table_str_2_cards== False, Max Number is 3 .
    At River just 30% it happens to be 0 for both Table_str_1_ and Table_str_2 at the same time.
    """
    return len(str_2_Cards_list( table_cards_list )) 

def Table_str_5_cards( List ):                               #b5
    """ At River happens. returns True or False """
    if 14 in List :
        List.append(1)
    if str_length( List ) == 5:
        return True
    else :
        return False

def Me_str_1_cards( table_cards_list , My_1th_Card , My_2th_Card ) :#2
    """ if Me_str_2_cards == True : return False """
    if Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True :
        return False
    
    for i in str_1_Cards_list( table_cards_list ) :
        if n(My_1th_Card) == i or n(My_2th_Card) == i :
            return True
        if n(My_1th_Card) == 14 :
            if 1 == i or n(My_2th_Card) == i :
                return True
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) == i or 1 == i :
                return True   
     
    return False

def Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) :#3
    """ if Me_str_1_cards == True : return False """
    if n(My_1th_Card) == n(My_2th_Card):
        return False
    for i in str_2_Cards_list( table_cards_list ) :
        if n(My_1th_Card) in i and n(My_2th_Card) in i :
            return True
        if n(My_1th_Card) == 14 :
            if 1 in i and n(My_2th_Card) in i :
                return True
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) in i and 1 in i :
                return True   
    return False



def Me_str_1_cards_Ranking( table_cards_list , My_1th_Card , My_2th_Card ) :       #4
    """
    Rank 1,2 & None
    None if Me_str_2_cards == True
    1 ( [7,8,9,11] , 10, 2 ) or ([7, 8, 9, 11], 10, 6).  2 ( [7,8,9,10] , 6, 2 )
    """
    if Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True :
        return None
    
    rank = 0
    for i in str_1_Cards_list( table_cards_list ) :
        rank += 1
        if n(My_1th_Card) == i or n(My_2th_Card) == i :
            return rank
        if n(My_1th_Card) == 14 :
            if 1 == i or n(My_2th_Card) == i :
                return rank
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) == i or 1 == i :
                return rank    

      
def Me_str_2_cards_Ranking( table_cards_list , My_1th_Card , My_2th_Card ) :#5
    """
    Rank 1,2,3 & None
    1 ([7, 8, 9, 11], 10, 12).  2 ([7, 8, 9], 10, 6).  3 ([7, 8, 9], 5, 6)
    """
    if n(My_1th_Card) == n(My_2th_Card):
        return None
    rank = 0
    for i in str_2_Cards_list( table_cards_list ) :
        rank += 1
        if n(My_1th_Card) in i and n(My_2th_Card) in i :
            return rank
        if n(My_1th_Card) == 14 :
            if 1 in i and n(My_2th_Card) in i :
                return rank
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) in i and 1 in i :
                return rank


def Me_str( table_cards_list , My_1th_Card , My_2th_Card ) : #1
    """ if Me_str_2_cards or Me_str_1_cards """
    if Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True or Me_str_1_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True :
        return True
    else:
        return False


def Is_above_str_1_card( table_cards_list , My_1th_Card , My_2th_Card ) :#6 # screen shot again with these new Edition and discriptoins
    """
    Above , equal is not possible
    if Me_str_2_cards_Ranking > 1 or None
    if i'm not str or i'm Me_str_1_cards ,it will return True. so use both (Me_str_2_cards() and Is_above_str_1_card()) at the same time
    """

    if Table_str_1_cards( table_cards_list ) == False :
        return False
    elif Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == False :
        return True
    elif max(My_1th_Card,My_2th_Card) < str_1_Cards_list( table_cards_list )[0] : #equal is not possible
        return True
    else :
        return False




def Me_Open_str_draw_1_cards( table_cards_list , My_1th_Card , My_2th_Card  ) : #7
    """
    if Me_str == True: retun False
    ( [7,8,9] ,2 ,10 ): True.  ( [6,7,8,9] ,2 ,10 ): False
    """

    if Me_Open_str_draw_2_cards( table_cards_list , My_1th_Card , My_2th_Card  ) == True \
       or Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True :
        return False
    
    for i in open_str_draw_1_Cards_list( table_cards_list ) :
        if n(My_1th_Card) == i or n(My_2th_Card) == i :
            return True
    return False    


def Me_Open_str_draw_2_cards( table_cards_list , My_1th_Card , My_2th_Card  ) : #9
    """ if Me_str == True: retun False """
    if n(My_1th_Card) == n(My_2th_Card):
        return False
    for i in open_str_draw_2_Cards_list( table_cards_list ) :
        if n(My_1th_Card) in i and n(My_2th_Card) in i :
            return True
        if n(My_1th_Card) == 14 :
            if 1 in i and n(My_2th_Card) in i :
                return True
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) in i and 1 in i :
                return True   
    return False


def Me_Open_str_draw_1_cards_Ranking( table_cards_list , My_1th_Card , My_2th_Card ) : #8
    """ Rank 1,2 & None """
    if Me_Open_str_draw_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True \
       or Me_str_2_cards( table_cards_list , My_1th_Card , My_2th_Card ) == True :
        return None
    
    rank = 0
    for i in open_str_draw_1_Cards_list( table_cards_list ) :
        rank += 1
        if n(My_1th_Card) == i or n(My_2th_Card) == i :
            return rank

def Me_Open_str_draw_2_cards_Ranking( table_cards_list , My_1th_Card , My_2th_Card ) : #10
    """ Rank 1,2,3 & None """
    if n(My_1th_Card) == n(My_2th_Card):
        return None
    
    rank = 0
    for i in open_str_draw_2_Cards_list( table_cards_list ) :
        rank += 1
        if n(My_1th_Card) in i and n(My_2th_Card) in i :
            return rank
        if n(My_1th_Card) == 14 :
            if 1 in i and n(My_2th_Card) in i :
                return rank
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) in i and 1 in i :
                return rank
    




    
    
