
def s(Card) :
    if Card in ('A c','2 c','3 c','4 c','5 c','6 c','7 c','8 c','9 c','10 c','J c','Q c','K c') :
        return "c"
    if Card in ('A d','2 d','3 d','4 d','5 d','6 d','7 d','8 d','9 d','10 d','J d','Q d','K d') :
        return "d"
    if Card in ('A h','2 h','3 h','4 h','5 h','6 h','7 h','8 h','9 h','10 h','J h','Q h','K h') :
        return "h"
    if Card in ('A s','2 s','3 s','4 s','5 s','6 s','7 s','8 s','9 s','10 s','J s','Q s','K s') :
        return "s"

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



def Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th ) : 
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th)
    Flop_str_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            Loop_List = [Card_1th, Card_2th, Card_3th]
            if 14 in Loop_List :
                Loop_List.append(1)
            if i == j or i in Loop_List or j in Loop_List :
                continue
            Loop_List.append(i)
            Loop_List.append(j)
            if str_length( Loop_List ) == 5 :
                Flop_str_2_Cards_list.append((i,j))
                
    for tuples in Flop_str_2_Cards_list :
        if (min(tuples),max(tuples)) in Flop_str_2_Cards_list and min(tuples) != max(tuples):
            Flop_str_2_Cards_list.remove( (min(tuples),max(tuples)) )
    Flop_str_2_Cards_list = list( set(Flop_str_2_Cards_list) )

    Flop_str_2_Cards_list.sort(reverse=True)
    
    return Flop_str_2_Cards_list


def Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th)
    Turn_str_1_Cards_list = []
    for i in range(1,15):
        Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th]
        if 14 in Loop_List :
            Loop_List.append(1)
        if i in Loop_List :
            continue        
        Loop_List.append(i)
        if str_length( Loop_List ) == 5 :
            Turn_str_1_Cards_list.append(i)

    Turn_str_1_Cards_list.sort(reverse=True)
    return Turn_str_1_Cards_list


def Turn_str_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th)    
    Turn_str_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th]
            if 14 in Loop_List :
                Loop_List.append(1)
            if i == j or i in Loop_List or j in Loop_List :
                continue
            Loop_List.append(i)
            Loop_List.append(j)
            if str_length( Loop_List ) == 5 \
            and i not in Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )\
            and j not in Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ) :
                Turn_str_2_Cards_list.append((i,j))
            if str_length( Loop_List ) == 6 \
            and min(Loop_List) not in (i,j) :
                    Turn_str_2_Cards_list.append((i,j))

    for tuples in Turn_str_2_Cards_list :
        if (min(tuples),max(tuples)) in Turn_str_2_Cards_list and min(tuples) != max(tuples):
            Turn_str_2_Cards_list.remove( (min(tuples),max(tuples)) )
    Turn_str_2_Cards_list = list( set(Turn_str_2_Cards_list) )

    Turn_str_2_Cards_list = list( set(Turn_str_2_Cards_list) -
                                  set(Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )) )
    
    Turn_str_2_Cards_list.sort(reverse=True)
    return Turn_str_2_Cards_list


def River_str( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th) ;Card_5th = n(Card_5th)  
    List = [Card_1th, Card_2th, Card_3th, Card_4th, Card_5th]
    if 14 in List :
        List.append(1)
    if str_length( List ) == 5 :
        return max(List)
    else :
        return None

def River_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th) ;Card_5th = n(Card_5th)  
    River_str_1_Cards_list = []
    for i in range(1,15):
        Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th, Card_5th]
        if 14 in Loop_List :
            Loop_List.append(1)
        if i in Loop_List :
            continue        
        Loop_List.append(i)
        if str_length( Loop_List ) == 5 \
        and River_str(Card_1th, Card_2th, Card_3th, Card_4th, Card_5th) == None :
            River_str_1_Cards_list.append(i)
        if str_length( Loop_List ) == 6 \
        and min(Loop_List) != i :
            River_str_1_Cards_list.append(i)
            
    River_str_1_Cards_list = list( set(River_str_1_Cards_list) -
                                  set(Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )) )
    
    River_str_1_Cards_list.sort(reverse=True)
    return River_str_1_Cards_list


def River_str_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th) ;Card_5th = n(Card_5th)      
    River_str_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th, Card_5th]
            if 14 in Loop_List :
                Loop_List.append(1)
            if i == j or i in Loop_List or j in Loop_List :
                continue
            Loop_List.append(i)
            Loop_List.append(j)
            
            if str_length( Loop_List ) == 5 \
            and River_str(Card_1th, Card_2th, Card_3th, Card_4th, Card_5th) == None \
            and i not in Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ) \
            and i not in River_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ) \
            and j not in Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ) \
            and j not in River_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ) :
                River_str_2_Cards_list.append((i,j))
            Loop_List2 = [Card_1th, Card_2th, Card_3th, Card_4th, Card_5th]
            if 14 in Loop_List2 :
                Loop_List2.append(1)
            if str_length( Loop_List ) == 6 and min(Loop_List) not in (i,j)\
            and str_length( list( set(Loop_List2) | set([i]) ) ) !=6 \
            and str_length( list( set(Loop_List2) | set([j]) ) ) !=6 :
                River_str_2_Cards_list.append((i,j))
            if str_length( Loop_List ) == 7 :
                Loop_List.sort()
                if Loop_List[0] not in (i,j) and Loop_List[1] not in (i,j) :
                    River_str_2_Cards_list.append((i,j))

    for tuples in River_str_2_Cards_list :
        if (min(tuples),max(tuples)) in River_str_2_Cards_list and min(tuples) != max(tuples):
            River_str_2_Cards_list.remove( (min(tuples),max(tuples)) )
    River_str_2_Cards_list = list( set(River_str_2_Cards_list) )


    River_str_2_Cards_list = list( set(River_str_2_Cards_list) -
                                  set(Turn_str_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )) )
    River_str_2_Cards_list = list( set(River_str_2_Cards_list) -
                                  set(Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )) )

    River_str_2_Cards_list.sort(reverse=True)
    return River_str_2_Cards_list


def Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th)
    Flop_open_str_draw_1_Cards_list = []
    for i in range(1,15):
        Loop_List = [Card_1th, Card_2th, Card_3th]      
        Loop_List.append(i)
        if str_length( Loop_List ) == 4 and min(Loop_List) != 1 and max(Loop_List) != 14 :
            Flop_open_str_draw_1_Cards_list.append(i)

    Flop_open_str_draw_1_Cards_list.sort(reverse=True)
    return Flop_open_str_draw_1_Cards_list    


def Flop_open_str_draw_2_Cards_list( Card_1th, Card_2th, Card_3th ):
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) 
    Flop_open_str_draw_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            Loop_List = [Card_1th, Card_2th, Card_3th]
            if i == j or i in Loop_List or j in Loop_List :
                continue
            while 14 in Loop_List :
                Loop_List.remove(14)
            while 1 in Loop_List :
                Loop_List.remove(1)
            Loop_List.append(i)
            Loop_List.append(j)
            if str_length( Loop_List ) == 4 \
            and i not in Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th )\
            and j not in Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th ) :
                Flop_open_str_draw_2_Cards_list.append((i,j))
                
    for tuples in Flop_open_str_draw_2_Cards_list :
        if (min(tuples),max(tuples)) in Flop_open_str_draw_2_Cards_list and min(tuples) != max(tuples):
            Flop_open_str_draw_2_Cards_list.remove( (min(tuples),max(tuples)) )
    Flop_open_str_draw_2_Cards_list = list( set(Flop_open_str_draw_2_Cards_list) )
    
    Flop_open_str_draw_2_Cards_list.sort(reverse=True)
    return Flop_open_str_draw_2_Cards_list


def Turn_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ): 
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th)
    Turn_open_str_draw_1_Cards_list = []
    for i in range(1,15):
        Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th]
        if 14 in Loop_List :
            Loop_List.append(1)
        if i in Loop_List :
            continue        
        Loop_List.append(i)
        if str_length( Loop_List ) == 4 :
            while 14 in Loop_List :
                Loop_List.remove(14)
            while 1 in Loop_List :
                Loop_List.remove(1)
            if str_length( Loop_List ) == 4 \
            and str_length( [Card_1th, Card_2th, Card_3th, Card_4th] ) !=4 :
                Turn_open_str_draw_1_Cards_list.append(i)

    Turn_open_str_draw_1_Cards_list = list( set(Turn_open_str_draw_1_Cards_list) -
                                  set(Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th )) )

    Turn_open_str_draw_1_Cards_list.sort(reverse=True)
    return Turn_open_str_draw_1_Cards_list


def Turn_open_str_draw_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th ): 
    
    Card_1th = n(Card_1th) ;Card_2th = n(Card_2th) ;Card_3th = n(Card_3th) ;Card_4th = n(Card_4th)    
    Turn_open_str_draw_2_Cards_list = []
    for i in range(1,15):
        for j in range(1,15):
            Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th]
            if 14 in Loop_List :
                Loop_List.append(1)
            if i == j or i in Loop_List or j in Loop_List :
                continue
            Loop_List.append(i)
            Loop_List.append(j)
            if str_length( Loop_List ) == 4 :
                while 14 in Loop_List :
                    Loop_List.remove(14)
                while 1 in Loop_List :
                    Loop_List.remove(1)
                if str_length( Loop_List ) == 4  \
                and i not in Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th )\
                and i not in Turn_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )\
                and j not in Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th )\
                and j not in Turn_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )\
                and str_length( [Card_1th, Card_2th, Card_3th, Card_4th] ) !=4 :
                    Turn_open_str_draw_2_Cards_list.append((i,j))
            if str_length( Loop_List ) == 2 :
                p = 0
                for k in range(1,15) :
                    Loop_List = [Card_1th, Card_2th, Card_3th, Card_4th] 
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
                        Turn_open_str_draw_2_Cards_list.append((i,j))
                        break

    for tuples in Turn_open_str_draw_2_Cards_list :
        if (min(tuples),max(tuples)) in Turn_open_str_draw_2_Cards_list and min(tuples) != max(tuples):
            Turn_open_str_draw_2_Cards_list.remove( (min(tuples),max(tuples)) )
    Turn_open_str_draw_2_Cards_list = list( set(Turn_open_str_draw_2_Cards_list) )

    Turn_open_str_draw_2_Cards_list = list( set(Turn_open_str_draw_2_Cards_list) -
                                  set(Flop_open_str_draw_2_Cards_list( Card_1th, Card_2th, Card_3th )) )

    Turn_open_str_draw_2_Cards_list.sort(reverse=True)
    return Turn_open_str_draw_2_Cards_list













#------------------------------------------------------------------


def Flop_flush_3_Cards( Card_1th, Card_2th, Card_3th ):
    
    if s(Card_1th) == s(Card_2th) == s(Card_3th) :
        
        max2 = 14
        while True :
            if max2 not in ( n(Card_1th), n(Card_2th), n(Card_3th) ) :
                break
            else :
                max2 = max2 - 1

        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,s(Card_1th)) )


def Flop_flush_draw( Card_1th, Card_2th, Card_3th ):
    
    if Flop_flush_3_Cards( Card_1th, Card_2th, Card_3th ) == None :
        c = 0; d = 0; h = 0; sp = 0
        for i in [ Card_1th, Card_2th, Card_3th ] :
            if s(i) == "c" : c = c + 1
            if s(i) == "d" : d = d + 1
            if s(i) == "h" : h = h + 1
            if s(i) == "s" : sp = sp + 1

        List = []
        if c == 2 :
            sign = "c"
            for i in [ Card_1th, Card_2th, Card_3th ] :
                if s(i) == "c" : List.append(n(i))
        elif d == 2 :
            sign = "d"
            for i in [ Card_1th, Card_2th, Card_3th ] :
                if s(i) == "d" : List.append(n(i))
        elif h == 2 :
            sign = "h"
            for i in [ Card_1th, Card_2th, Card_3th ] :
                if s(i) == "h" : List.append(n(i))
        elif sp == 2 :
            sign = "s"
            for i in [ Card_1th, Card_2th, Card_3th ] :
                if s(i) == "s" : List.append(n(i))
        else :
            return None
                    
        max2 = 14
        while True :
            if max2 not in ( List ) :
                break
            else :
                max2 = max2 - 1
                
        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,sign) )



#
def Flush_3_cards( List , My_1th_Card , My_2th_Card ) :

    if s(My_1th_Card) == s(My_2th_Card) :
        sign = 0
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign += 1
        if sign == 3 :
            return True
    return False

def Flush_4_cards( List , My_1th_Card , My_2th_Card ) :

    sign1 = 0
    sign2 = 0
    for i in List :
        if s(My_1th_Card) == s(i) :
            sign1 += 1
        if s(My_2th_Card) == s(i) :
            sign2 += 1
    if sign1 == 4 or sign2 == 4 :
        return True
    return False

def Flush_5_cards( List , My_1th_Card , My_2th_Card ) :

    sign1 = 0
    sign2 = 0
    for i in List :
        if s(My_1th_Card) == s(i) :
            sign1 += 1
        if s(My_2th_Card) == s(i) :
            sign2 += 1

    if sign1 == 5 and sign2 == 5:
        My_highest = max(n(My_1th_Card),n(My_2th_Card))
    elif sign1 == 5 :
        My_highest = n(My_1th_Card)
    elif sign2 == 5 :
        My_highest = n(My_2th_Card)
    sign_List = []
    for i in List :
        sign_List.append(n(i))
    if (sign1 == 5 or sign2 == 5) and My_highest > min(sign_List) :
        return True
    return False

def Flush( List , My_1th_Card , My_2th_Card ) :

    if Flush_3_cards( List , My_1th_Card , My_2th_Card ) or Flush_4_cards( List , My_1th_Card , My_2th_Card ) or Flush_5_cards( List , My_1th_Card , My_2th_Card ) :
        return True
    else:
        return False

def Flush_Ranking( List , My_1th_Card , My_2th_Card ) :
    
    if Flush( List , My_1th_Card , My_2th_Card ) == False :
        return None
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1
    sign_List = []
    
    if c >= 3 :
        if s(My_1th_Card) == s(My_2th_Card) :
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "c" :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "c" :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "c" : sign_List.append(n(i))

    elif d >= 3 :
        if s(My_1th_Card) == s(My_2th_Card) :
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "d" :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "d" :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "d" : sign_List.append(n(i))
            
    elif h >= 3 :
        if s(My_1th_Card) == s(My_2th_Card) :
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "h" :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "h" :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "h" : sign_List.append(n(i))

    elif sp >= 3 :
        if s(My_1th_Card) == s(My_2th_Card) :
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "s" :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "s" :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "s" : sign_List.append(n(i))

    sign_List.sort(reverse=True)
    rank = 1
    for i in range(14,1,-1):
        if i == My_highest :
            break
        elif i in sign_List :
            continue
        rank += 1

    return rank



def Flush_draw_2_cards( List , My_1th_Card , My_2th_Card ) :

    if s(My_1th_Card) == s(My_2th_Card) and len(List) <= 4 :
        sign = 0
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign += 1
        if sign == 2 :
            return True
    return False

def Flush_draw_3_cards( List , My_1th_Card , My_2th_Card ) :

    sign1 = 0
    sign2 = 0
    if s(My_1th_Card) != s(My_2th_Card) and len(List) <= 4 : 
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign1 += 1
            if s(My_2th_Card) == s(i) :
                sign2 += 1
        if sign1 == 3 or sign2 == 3 :
            return True
    return False    

def Flush_draw_Ranking( List , My_1th_Card , My_2th_Card ) :
    
    if Flush( List , My_1th_Card , My_2th_Card ) == True or len(List) == 5 \
       or( Flush_draw_2_cards( List , My_1th_Card , My_2th_Card ) == False and Flush_draw_3_cards( List , My_1th_Card , My_2th_Card ) == False ) :
        return None
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1
    sign_List = []
    
    if c >= 2 :
        if s(My_1th_Card) == s(My_2th_Card) and s(My_1th_Card) == "c" and c == 2:
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "c" and c == 3 :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "c" and c == 3 :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "c" : sign_List.append(n(i))

    elif d >= 2 :
        if s(My_1th_Card) == s(My_2th_Card) and s(My_1th_Card) == "d" and d == 2:
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "d" and d == 3 :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "d" and d == 3 :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "d" : sign_List.append(n(i))

            
    elif h >= 2 :
        if s(My_1th_Card) == s(My_2th_Card) and s(My_1th_Card) == "h" and h == 2:
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "h" and h == 3 :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "h" and h == 3 :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "h" : sign_List.append(n(i))

    elif sp >= 2 :
        if s(My_1th_Card) == s(My_2th_Card) and s(My_1th_Card) == "s" and sp == 2:
            My_highest = max(n(My_1th_Card),n(My_2th_Card))
        elif s(My_1th_Card) == "s" and sp == 3 :
            My_highest = n(My_1th_Card)
        elif s(My_2th_Card) == "s" and sp == 3 :
            My_highest = n(My_2th_Card)
        for i in List :
            if s(i) == "s" : sign_List.append(n(i))


    sign_List.sort(reverse=True)
    rank = 1
    for i in range(14,1,-1):
        if i == My_highest :
            break
        elif i in sign_List :
            continue
        rank += 1

    return rank


def Table_flush_3_cards( List ) :
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 3 in (c,d,h,sp) :
        return True
    return False

def Table_flush_4_cards( List ) :
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 4 in (c,d,h,sp) :
        return True
    return False

def Table_flush_5_cards( List ) :
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 5 in (c,d,h,sp) :
        return True
    return False

def Table_flush_draw( List ) :

    if len(List) > 4 :
        return False
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 2 in (c,d,h,sp) :
        return True
    return False

def Table_flush( List ) :
    
    if Table_flush_3_cards( List ) or Table_flush_4_cards( List ) or Table_flush_5_cards( List ) :
        return True
    return False

#

def Turn_flush_3_Cards( Card_1th, Card_2th, Card_3th, Card_4th ):
    
    if Flop_flush_3_Cards( Card_1th, Card_2th, Card_3th ) == None :
        c = 0; d = 0; h = 0; sp = 0
        for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
            if s(i) == "c" : c = c + 1
            if s(i) == "d" : d = d + 1
            if s(i) == "h" : h = h + 1
            if s(i) == "s" : sp = sp + 1

        List = []
        if c == 3 :
            sign = "c"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "c" : List.append(n(i))
        elif d == 3 :
            sign = "d"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "d" : List.append(n(i))
        elif h == 3 :
            sign = "h"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "h" : List.append(n(i))
        elif sp == 3 :
            sign = "s"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "s" : List.append(n(i))
        else :
            return None
                    
        max2 = 14
        while True :
            if max2 not in ( List ) :
                break
            else :
                max2 = max2 - 1
                
        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,sign) )


def Turn_flush_4_Cards( Card_1th, Card_2th, Card_3th, Card_4th ):
    
    if s(Card_1th) == s(Card_2th) == s(Card_3th) == s(Card_4th) :
        
        max2 = 14
        while True :
            if max2 not in ( n(Card_1th), n(Card_2th), n(Card_3th), n(Card_4th) ) :
                break
            else :
                max2 = max2 - 1

        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,s(Card_1th)) )

    

def Turn_flush_draw( Card_1th, Card_2th, Card_3th, Card_4th ):
    
    if Flop_flush_3_Cards( Card_1th, Card_2th, Card_3th ) == None \
    and Turn_flush_3_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) == None \
    and Trun_flush_4_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) == None :
        c = 0; d = 0; h = 0; sp = 0
        for i in [ Card_1th, Card_2th, Card_3th, Card_4th  ] :
            if s(i) == "c" : c = c + 1
            if s(i) == "d" : d = d + 1
            if s(i) == "h" : h = h + 1
            if s(i) == "s" : sp = sp + 1

        List = []
        if c == 2 and s( Flop_flush_draw( Card_1th, Card_2th, Card_3th ) ) != "c" :
            sign = "c"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "c" : List.append(n(i))
        elif d == 2 and s( Flop_flush_draw( Card_1th, Card_2th, Card_3th ) ) != "d"  :
            sign = "d"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "d" : List.append(n(i))
        elif h == 2 and s( Flop_flush_draw( Card_1th, Card_2th, Card_3th ) ) != "h"  :
            sign = "h"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "h" : List.append(n(i))
        elif sp == 2 and s( Flop_flush_draw( Card_1th, Card_2th, Card_3th ) ) != "s"  :
            sign = "s"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th ] :
                if s(i) == "s" : List.append(n(i))
        else :
            return None
                    
        max2 = 14
        while True :
            if max2 not in ( List ) :
                break
            else :
                max2 = max2 - 1
                
        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,sign) )


def River_flush_3_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ):
    
    if Flop_flush_3_Cards( Card_1th, Card_2th, Card_3th ) == None \
    and Turn_flush_3_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) == None \
    and Trun_flush_4_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) ==None :
        c = 0; d = 0; h = 0; sp = 0
        for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
            if s(i) == "c" : c = c + 1
            if s(i) == "d" : d = d + 1
            if s(i) == "h" : h = h + 1
            if s(i) == "s" : sp = sp + 1

        List = []
        if c == 3 :
            sign = "c"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "c" : List.append(n(i))
        elif d == 3 :
            sign = "d"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "d" : List.append(n(i))
        elif h == 3 :
            sign = "h"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "h" : List.append(n(i))
        elif sp == 3 :
            sign = "s"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "s" : List.append(n(i))
        else :
            return None
                    
        max2 = 14
        while True :
            if max2 not in ( List ) :
                break
            else :
                max2 = max2 - 1
                
        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,sign) )


def River_flush_4_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ):
    
    if Trun_flush_4_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) ==None :
        c = 0; d = 0; h = 0; sp = 0
        for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
            if s(i) == "c" : c = c + 1
            if s(i) == "d" : d = d + 1
            if s(i) == "h" : h = h + 1
            if s(i) == "s" : sp = sp + 1

        List = []
        if c == 4 :
            sign = "c"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "c" : List.append(n(i))
        elif d == 4 :
            sign = "d"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "d" : List.append(n(i))
        elif h == 4 :
            sign = "h"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "h" : List.append(n(i))
        elif sp == 4 :
            sign = "s"
            for i in [ Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ] :
                if s(i) == "s" : List.append(n(i))
        else :
            return None
                    
        max2 = 14
        while True :
            if max2 not in ( List ) :
                break
            else :
                max2 = max2 - 1
                
        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,sign) )


def River_flush_5_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ):
    
    if s(Card_1th) == s(Card_2th) == s(Card_3th) == s(Card_4th) == s(Card_5th) :
        
        max2 = 14
        while True :
            if max2 not in ( n(Card_1th), n(Card_2th), n(Card_3th), n(Card_4th), n(Card_5th) ) :
                break
            else :
                max2 = max2 - 1

        if max2 == 14 : max2='A'
        if max2 == 13 : max2='K'
        if max2 == 12 : max2='Q'
        if max2 == 11 : max2='J'
        return ("%s %s" %(max2,s(Card_1th)) )




#------------------------------------------------------------------



def Cards_Matching( My_Card , List ) : 
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    Cards_Matching( My_Card , [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """

    for i in range( len(List) ) :
        List[i] = n( List[i] )
    My_Card = n( My_Card )
    
    List = list(set(List))
    List.sort(reverse=True)
    if My_Card in List :
        for i in range( len(List) ) :
            if My_Card == List[i] :
                return i+1
    else :
        return None

def Cards_Ranking( My_Card , List ) : 
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    Cards_Ranking( My_Card , [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """    
    
    for i in range( len(List) ) :
        List[i] = n( List[i] )
    My_Card = n( My_Card )
    
    List = list(set(List))
    List.sort(reverse=True)
    Cards_Ranking = 1
    for i in range( len(List) ) :
        if My_Card >= List[i] :
            return Cards_Ranking
        else :
            Cards_Ranking = Cards_Ranking + 1
    return Cards_Ranking



def Flop_Individual_Cards( Card_1th, Card_2th, Card_3th  ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th)]
    List = list(set(List))
    List.sort(reverse=True)
    if len( List ) == 3 :
        return List
    else :
        return None


def Flop_1_pair_Cards( Card_1th, Card_2th, Card_3th  ) :
    
    List = [ n(Card_1th) , n(Card_2th), n(Card_3th)]
    List = list(set(List))
    List.sort()
    if len( List ) == 2 :
        for i in range(len(List)):
            if [ n(Card_1th) , n(Card_2th), n(Card_3th) ].count(List[i]) == 2 :
                pair = List[i]
                pair = [pair]
                List.remove(List[i])
                pair.extend(List)
                return pair
    else :
        return None

def Flop_3_of_kinds_Cards( Card_1th, Card_2th, Card_3th  ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th)]
    List = list(set(List))
    if len( List ) == 1 :
        return List
    else :
        return None



###

def Table_Individual( List ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 0 :
        return True
    else :
        return False
    
def Table_1_pair( List ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 1 and 2 in pair_list :
        return True
    else :
        return False


def Table_2_pair( List ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 2 and 3 not in pair_list :
        return True
    else :
        return False
        
def Table_3_of_kinds( List ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 1 and 3 in pair_list :
        return True
    else :
        return False


def Table_full_house( List ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 2 and 3 in pair_list :
        return True
    else :
        return False


def Table_4_of_kinds( List ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    pair_list = []
    for i in range(2,15):
        if List.count(i) >= 2 :
            pair_list.append(List.count(i))

    if len(pair_list) == 1 and 4 in pair_list :
        return True
    else :
        return False




def Me_Individual( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 0 and n(My_1th_Card) != n(My_2th_Card) :
        return True
    else :
        return False

def Me_pocket_pair( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 0 and n(My_1th_Card) == n(My_2th_Card) :
        return True
    else :
        return False


def Me_1_pair( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if (List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 0) \
       or (List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 1):
        return True
    else :
        return False

def Me_2_pair( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 1 and n(My_1th_Card) != n(My_2th_Card) :
        return True
    else :
        return False
    
def Me_3_of_kinds( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if (List.count( n(My_1th_Card) ) == 2 and List.count( n(My_2th_Card) ) == 0) \
       or (List.count( n(My_1th_Card) ) == 0 and List.count( n(My_2th_Card) ) == 2):
        return True
    else :
        return False

def Me_pocket_3_of_kinds( List , My_1th_Card , My_2th_Card ) :#test shavad

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 1 and n(My_1th_Card) == n(My_2th_Card) and Table_Individual( List ) :
        return True
    else :
        return False

def Me_full_house( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if (List.count( n(My_1th_Card) ) == 2 and 1 <= List.count( n(My_2th_Card) ) <= 2)\
       or (1 <= List.count( n(My_1th_Card) ) <= 2 and List.count( n(My_2th_Card) ) == 2) :
        return True
    else :
        return False

def Me_pocket_full_house( List , My_1th_Card , My_2th_Card ) :#test shavad

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 1 and List.count( n(My_2th_Card) ) == 1 and n(My_1th_Card) == n(My_2th_Card) \
       and ( Table_1_pair( List ) or Table_2_pair( List ) or Table_3_of_kinds( List ) ):
        return True
    else :
        return False

def Me_4_of_kinds( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 3 or List.count( n(My_2th_Card) ) == 3 :
        return True
    else :
        return False

def Me_pocket_4_of_kinds( List , My_1th_Card , My_2th_Card ) :

    for i in range( len(List) ) :
        List[i] = n( List[i] )

    if List.count( n(My_1th_Card) ) == 2 and List.count( n(My_2th_Card) ) == 2 and n(My_1th_Card) == n(My_2th_Card) :
        return True
    else :
        return False

def Cards_Matching( List , My_Card ) :
    """
    Lists var act like global in python functions. so List should be written like this
    to avoid manipulation in Lists var to furthermore usage in the other functions:
    Cards_Matching( My_Card , [ Card_1th, Card_2th, Card_3th, Card_4th ] )
    """

    for i in range( len(List) ) :
        List[i] = n( List[i] )
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

    if Me_Individual( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
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

def Me_pocket_pair_Ranking( List , My_1th_Card , My_2th_Card ) : #test shavad bana bar neveshte ro kaghaz 2018

    if Me_pocket_pair( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
        List.sort(reverse=True)

        My_Card = My_1th_Card
        rank = 1
        for i in range(14,1,-1):
            if i == My_Card :
                break
            elif i in List :
                rank += 1

        return rank  

def Me_1_pair_Ranking( List , My_1th_Card , My_2th_Card ) :

    if Me_1_pair( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
        List.sort(reverse=True)

        if List.count( n(My_1th_Card) ) == 1 :
            My_Card = My_1th_Card
        elif List.count( n(My_2th_Card) ) == 1 :
            My_Card = My_2th_Card

        return Cards_Matching( List , My_Card )

def Me_2_pair_Ranking( List , My_1th_Card , My_2th_Card ) :

    if Me_2_pair( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
        List.sort(reverse=True)

        return ( Cards_Matching( List , max(My_1th_Card,My_2th_Card) ) , Cards_Matching( List , min(My_1th_Card,My_2th_Card) ) )

def Me_3_of_kinds_Ranking( List , My_1th_Card , My_2th_Card ) : #newwww defined 2018!!!!! test shavad
    """Ranks: 1,2 """
    
    if Me_3_of_kinds( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
        List.sort(reverse=True)

        if List.count( n(My_1th_Card) ) == 2 :
            My_Card = My_1th_Card
        elif List.count( n(My_2th_Card) ) == 2 :
            My_Card = My_2th_Card

        Card = []
        for i in range( len(List) ) :
            if List.count( List[i] ) == 2 :
                Card.append( List[i] )
        Card.sort(reverse=True)
        
        return Cards_Matching( Card , My_Card )


def Me_pocket_3_of_kinds_Ranking( List , My_1th_Card , My_2th_Card ) :

    if Me_pocket_3_of_kinds( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
        List.sort(reverse=True)

        My_Card = My_1th_Card

        return Cards_Matching( List , My_Card )

def Me_full_house_Ranking( List , My_1th_Card , My_2th_Card ) : #newwww defined 2018!!!!! test shavad
    """Ranks: 1,2,3 """
    
    if Me_full_house( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
        List.sort(reverse=True)

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


def Me_pocket_full_house_Ranking( List , My_1th_Card , My_2th_Card ) :#test shavad

    if Me_pocket_full_house( List , My_1th_Card , My_2th_Card ) == True :

        for i in range( len(List) ) :
            List[i] = n( List[i] )        
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
                if List.count( List[i] ) == 2 :
                    Card.append( List[i] )
            if max(Card) < My_1th_Card :
                return 1
            elif min(Card) < My_1th_Card < max(Card) :
                return 2
            elif min(Card) > My_1th_Card :
                return 3

        elif Table_3_of_kinds( List ) == True :
            return 3



###


def Turn_Individual_Cards( Card_1th, Card_2th, Card_3th, Card_4th  ) :
    
    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th)]
    List = list(set(List))
    List.sort(reverse=True)
    if len( List ) == 4 :
        return List
    else :
        return None


def Turn_1_pair_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) :
    
    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th) ]
    if List.count(n(Card_4th)) == 2 :
        List = list(set(List))
        List.sort(reverse=True)
        List.remove(n(Card_4th))
        pair = [ n(Card_4th) ]
        pair.extend(List)
        return pair
    else:
        return None
        
        
def Turn_3_of_kinds_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th) ]
    if List.count(n(Card_4th)) == 3 :
        List = list(set(List))
        List.sort(reverse=True)
        List.remove(n(Card_4th))
        pair3 = [ n(Card_4th) ]
        pair3.extend(List)
        return pair3
    else:
        return None

def Turn_4_of_kinds_Cards( Card_1th, Card_2th, Card_3th, Card_4th ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th)]
    List = list(set(List))
    if len( List ) == 1 :
        return List
    else :
        return None          


def River_Individual_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th  ) :
    
    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th), n(Card_5th) ]
    List = list(set(List))
    List.sort(reverse=True)
    if len( List ) == 5 :
        return List
    else :
        return None


def River_1_pair_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ) :
    
    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th), n(Card_5th) ]
    if List.count(n(Card_5th)) == 2 and len(list(set(List))) == 4 :
        List = list(set(List))
        List.sort(reverse=True)
        List.remove(n(Card_5th))
        pair = [ n(Card_5th) ]
        pair.extend(List)
        return pair
    elif List.count(n(Card_5th)) == 2 and len(list(set(List))) == 3 :
        Turn_List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th) ]
        for i in range(len(Turn_List)):
            if Turn_List.count(List[i]) == 2 :
                pair = List[i]
                List = list(set(List))
                List.remove(pair)
                List.remove(n(Card_5th))
                pair = [ n(Card_5th) , pair ]
                pair.extend(List)
                return pair
    else:
        return None


def River_3_of_kinds_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th), n(Card_5th) ]
    if List.count(n(Card_5th)) == 3 and len(list(set(List))) == 3 :
        List = list(set(List))
        List.sort(reverse=True)
        List.remove(n(Card_5th))
        pair3 = [ n(Card_5th) ]
        pair3.extend(List)
        return pair3
    else:
        return None


def River_full_house_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th), n(Card_5th) ]
    if len(list(set(List))) == 2 and List.count(n(Card_1th)) in (2,3) :
        for i in range(len(List)) :
            if List.count(List[i]) == 2 :
                Card2 = List[i]
            if List.count(List[i]) == 3 :
                Card3 = List[i]                
        return [Card3 , Card2]
    else:
        return None


def River_4_of_kinds_Cards( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th ) :

    List = [ n(Card_1th) , n(Card_2th), n(Card_3th), n(Card_4th), n(Card_5th) ]
    if List.count(n(Card_5th)) == 4 :
        List = list(set(List))
        List.sort(reverse=True)
        List.remove(n(Card_5th))
        pair4 = [ n(Card_5th) ]
        pair4.extend(List)
        return pair4
    else:
        return None


