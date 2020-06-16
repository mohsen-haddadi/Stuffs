"""
Functions with True or False return,are in 2 kind of categoreis: 1.Me_Flush_ Me_Flush_draw 2.Table_Flush Table_Flush_draw
If one of them is True the rest will be False. All functions can be False at the same time.

Ranking Functions are :1.Me_flush_Ranking 2.Me_flush_draw_Ranking .
Ranking Functions return 1.a Number or 2.None value if their True or False Functions have not been True already.
Table functions has no rankings in Flush and Pair files. in Str file there are Table_.._Number functions. 
"""


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


def Me_Flush_by_3_table_cards( List , My_1th_Card , My_2th_Card ) :
    """ ( ['6 c','8 c','10 c','K c','A d'] , '2 c' , '3 c' ) return False """

    if s(My_1th_Card) == s(My_2th_Card) :
        sign = 0
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign += 1
        if sign == 3 :
            return True
    return False

def Me_Flush_by_4_table_cards( List , My_1th_Card , My_2th_Card ) :
    """ ( ['6 c','8 c','10 c','K c','A c'] , 'Q c' , '3 c' ) return False """
    
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

def Me_Flush_by_5_table_cards( List , My_1th_Card , My_2th_Card ) :
    """
    ( ['6 c','8 c','10 c','K c','A c'] , '2 c' , '3 c' ) return False
    ( ['6 c','8 c','10 c','K c','A c'] , 'Q c' , '7 c' ) return True
    """

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

def Me_Flush( List , My_1th_Card , My_2th_Card ) :
    """ if Me_Flush_by_3_table_cards or Me_Flush_by_4_table_cards or Me_Flush_by_5_table_cards """
    
    if Me_Flush_by_3_table_cards( List , My_1th_Card , My_2th_Card ) or Me_Flush_by_4_table_cards( List , My_1th_Card , My_2th_Card ) or Me_Flush_by_5_table_cards( List , My_1th_Card , My_2th_Card ) :
        return True
    else:
        return False

def Me_Flush_Ranking( List , My_1th_Card , My_2th_Card ) :
    """
    Rank 1,...,9
    Example: Rank 3: ( ['6 c','K c','5 c'] , 'J c' , '3 c' )
    return None if Me_Flush_ == False
    """    
    if Me_Flush( List , My_1th_Card , My_2th_Card ) == False :
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



def Me_Flush_draw_by_2_table_cards( List , My_1th_Card , My_2th_Card ) :

    if s(My_1th_Card) == s(My_2th_Card) and len(List) <= 4 :
        sign = 0
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign += 1
        if sign == 2 :
            return True
    return False

def Me_Flush_draw_by_3_table_cards( List , My_1th_Card , My_2th_Card ) :

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

def Me_Flush_draw_Ranking( List , My_1th_Card , My_2th_Card ) :
    """
    Rank 1,...,10
    Example: Rank 2: ( ['6 c','K c','5 h'] , 'Q c' , '3 c' )
    return None if Me_Flush == True or on River or not Me_Flush_draw
    """
    if Me_Flush( List , My_1th_Card , My_2th_Card ) == True or len(List) == 5 \
       or( Me_Flush_draw_by_2_table_cards( List , My_1th_Card , My_2th_Card ) == False and Me_Flush_draw_by_3_table_cards( List , My_1th_Card , My_2th_Card ) == False ) :
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


def Table_Flush_3_cards( List ) :
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 3 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_4_cards( List ) :
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 4 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_5_cards( List ) :
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 5 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_draw( List ) :
    """
    True if 2 same sign card availabe on the table(not more or less than 2)
    returns False on River
    """
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

def Table_Flush( List ) :
    """ if Table_Flush_3_cards( List ) or Table_Flush_4_cards( List ) or Table_Flush_5_cards( List ) """
    
    if Table_Flush_3_cards( List ) or Table_Flush_4_cards( List ) or Table_Flush_5_cards( List ) :
        return True
    return False

