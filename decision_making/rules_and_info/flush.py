#OK
from decision_making.rules_and_info.suit_and_value import s, n
#from suit_and_value import s, n
import configs # don't import as c while there is a variable named c.

"""
Functions with True or False return,are in 2 kind of categoreis: 1.Me_Flush_ Me_Flush_draw 2.Table_Flush Table_Flush_draw
If one of them is True the rest will be False. All functions can be False at the same time.

Ranking Functions are :1.Me_flush_Ranking 2.Me_flush_draw_Ranking .
Ranking Functions return 1.a Number or 
2.None value if their True or False Functions have not been True already or we are at pre flop stage.
Table functions has no rankings in Flush and Pair files. in Str file there are Table_.._Number functions. 
"""


def Me_Flush_by_3_table_cards(board_list=None) :
    """ ( ['6 c','8 c','10 c','K c','A d'] , '2 c' , '3 c' ) return False """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) :
        sign = 0
        for i in board_list :
            if s(configs.my_hole_cards[0]) == s(i) :
                sign += 1
        if sign == 3 :
            return True
    return False

def Me_Flush_by_4_table_cards(board_list=None) :
    """ ( ['6 c','8 c','10 c','K c','A c'] , 'Q c' , '3 c' ) return False """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    sign1 = 0
    sign2 = 0
    for i in board_list :
        if s(configs.my_hole_cards[0]) == s(i) :
            sign1 += 1
        if s(configs.my_hole_cards[1]) == s(i) :
            sign2 += 1
    if sign1 == 4 or sign2 == 4 :
        return True
    return False

def Me_Flush_by_5_table_cards(board_list=None) :
    """
    ( ['6 c','8 c','10 c','K c','A c'] , '2 c' , '3 c' ) return False
    ( ['6 c','8 c','10 c','K c','A c'] , 'Q c' , '7 c' ) return True
    """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    sign1 = 0
    sign2 = 0
    for i in board_list :
        if s(configs.my_hole_cards[0]) == s(i) :
            sign1 += 1
        if s(configs.my_hole_cards[1]) == s(i) :
            sign2 += 1

    if sign1 == 5 and sign2 == 5:
        My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
    elif sign1 == 5 :
        My_highest = n(configs.my_hole_cards[0])
    elif sign2 == 5 :
        My_highest = n(configs.my_hole_cards[1])
    sign_List = []
    for i in board_list :
        sign_List.append(n(i))
    if (sign1 == 5 or sign2 == 5) and My_highest > min(sign_List) :
        return True
    return False

def Me_Flush(board_list=None) :
    """ if Me_Flush_by_3_table_cards or Me_Flush_by_4_table_cards or Me_Flush_by_5_table_cards """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    if Me_Flush_by_3_table_cards( board_list ) or Me_Flush_by_4_table_cards( board_list ) or Me_Flush_by_5_table_cards( board_list ) :
        return True
    else:
        return False

def Me_Flush_Ranking(board_list=None) :
    """
    Rank 1,...,9
    Example: Rank 3: ( ['6 c','K c','5 c'] , 'J c' , '3 c' )
    return None if Me_Flush_ == False
    """    
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return None
        
    if Me_Flush( board_list ) == False :
        return None
    c = 0; d = 0; h = 0; sp = 0
    for i in board_list :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1
    sign_List = []
    
    if c >= 3 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) :
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "c" :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "c" :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
            if s(i) == "c" : sign_List.append(n(i))

    elif d >= 3 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) :
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "d" :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "d" :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
            if s(i) == "d" : sign_List.append(n(i))
            
    elif h >= 3 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) :
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "h" :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "h" :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
            if s(i) == "h" : sign_List.append(n(i))

    elif sp >= 3 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) :
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "s" :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "s" :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
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


def Me_Flush_draw_by_2_table_cards(board_list=None) :
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) and len(board_list) <= 4 :
        sign = 0
        for i in board_list :
            if s(configs.my_hole_cards[0]) == s(i) :
                sign += 1
        if sign == 2 :
            return True
    return False

def Me_Flush_draw_by_3_table_cards(board_list=None) :
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    sign1 = 0
    sign2 = 0
    if s(configs.my_hole_cards[0]) != s(configs.my_hole_cards[1]) and len(board_list) <= 4 : 
        for i in board_list :
            if s(configs.my_hole_cards[0]) == s(i) :
                sign1 += 1
            if s(configs.my_hole_cards[1]) == s(i) :
                sign2 += 1
        if sign1 == 3 or sign2 == 3 :
            return True
    return False    

def Me_Flush_draw_Ranking(board_list=None) :
    """
    Rank 1,...,10
    Example: Rank 2: ( ['6 c','K c','5 h'] , 'Q c' , '3 c' )
    return None if Me_Flush == True or on River or not Me_Flush_draw
    """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return None
        
    if Me_Flush( board_list ) == True or len(board_list) == 5 \
       or( Me_Flush_draw_by_2_table_cards( board_list ) == False and Me_Flush_draw_by_3_table_cards( board_list ) == False ) :
        return None
    c = 0; d = 0; h = 0; sp = 0
    for i in board_list :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1
    sign_List = []
    
    if c >= 2 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) and s(configs.my_hole_cards[0]) == "c" and c == 2:
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "c" and c == 3 :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "c" and c == 3 :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
            if s(i) == "c" : sign_List.append(n(i))

    elif d >= 2 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) and s(configs.my_hole_cards[0]) == "d" and d == 2:
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "d" and d == 3 :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "d" and d == 3 :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
            if s(i) == "d" : sign_List.append(n(i))

            
    elif h >= 2 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) and s(configs.my_hole_cards[0]) == "h" and h == 2:
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "h" and h == 3 :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "h" and h == 3 :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
            if s(i) == "h" : sign_List.append(n(i))

    elif sp >= 2 :
        if s(configs.my_hole_cards[0]) == s(configs.my_hole_cards[1]) and s(configs.my_hole_cards[0]) == "s" and sp == 2:
            My_highest = max(n(configs.my_hole_cards[0]),n(configs.my_hole_cards[1]))
        elif s(configs.my_hole_cards[0]) == "s" and sp == 3 :
            My_highest = n(configs.my_hole_cards[0])
        elif s(configs.my_hole_cards[1]) == "s" and sp == 3 :
            My_highest = n(configs.my_hole_cards[1])
        for i in board_list :
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


def Table_Flush_3_cards(board_list=None) :
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    c = 0; d = 0; h = 0; sp = 0
    for i in board_list :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 3 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_4_cards(board_list=None) :
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    c = 0; d = 0; h = 0; sp = 0
    for i in board_list :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 4 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_5_cards(board_list=None) :
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    c = 0; d = 0; h = 0; sp = 0
    for i in board_list :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 5 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_draw(board_list=None) :
    """
    True if 2 same sign card availabe on the table(not more or less than 2)
    returns False on River
    """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    if len(board_list) > 4 :
        return False
    
    c = 0; d = 0; h = 0; sp = 0
    for i in board_list :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 2 in (c,d,h,sp) :
        return True
    return False

def Table_Flush(board_list=None) :
    """ if Table_Flush_3_cards( board_list ) or Table_Flush_4_cards( board_list ) or Table_Flush_5_cards( board_list ) """
    
    if board_list == None :
        board_list = configs.board_cards[:]
    if board_list == []:
        return False
        
    if Table_Flush_3_cards( board_list ) or Table_Flush_4_cards( board_list ) or Table_Flush_5_cards( board_list ) :
        return True
    return False

