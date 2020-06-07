from FUNCTIONS_suit_and_value import s, n

"""
Functions with True or False return,are in 2 kind of categoreis: 1.Me_Flush_ Me_Flush_draw 2.Table_Flush Table_Flush_draw
If one of them is True the rest will be False. All functions can be False at the same time.

Ranking Functions are :1.Me_flush_Ranking 2.Me_flush_draw_Ranking .
Ranking Functions return 1.a Number or 2.None value if their True or False Functions have not been True already.
Table functions has no rankings in Flush and Pair files. in Str file there are Table_.._Number functions. 
"""


def globalization():
    """ variables order is important while loading """
    global GAME_POSITION , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    GAME_POSITION , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat = pickle.load( open( "variables.p", "rb" ) )



def Me_Flush_by_3_table_cards( List = None ) :
    """ ( ['6 c','8 c','10 c','K c','A d'] , '2 c' , '3 c' ) return False """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    if s(My_1th_Card) == s(My_2th_Card) :
        sign = 0
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign += 1
        if sign == 3 :
            return True
    return False

def Me_Flush_by_4_table_cards( List = None ) :
    """ ( ['6 c','8 c','10 c','K c','A c'] , 'Q c' , '3 c' ) return False """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

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

def Me_Flush_by_5_table_cards( List = None ) :
    """
    ( ['6 c','8 c','10 c','K c','A c'] , '2 c' , '3 c' ) return False
    ( ['6 c','8 c','10 c','K c','A c'] , 'Q c' , '7 c' ) return True
    """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

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

def Me_Flush( List = None ) :
    """ if Me_Flush_by_3_table_cards or Me_Flush_by_4_table_cards or Me_Flush_by_5_table_cards """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    
    if Me_Flush_by_3_table_cards( List ) or Me_Flush_by_4_table_cards( List ) or Me_Flush_by_5_table_cards( List ) :
        return True
    else:
        return False

def Me_Flush_Ranking( List = None ) :
    """
    Rank 1,...,9
    Example: Rank 3: ( ['6 c','K c','5 c'] , 'J c' , '3 c' )
    return None if Me_Flush_ == False
    """    
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    if Me_Flush( List ) == False :
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



def Me_Flush_draw_by_2_table_cards( List = None ) :
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    if s(My_1th_Card) == s(My_2th_Card) and len(List) <= 4 :
        sign = 0
        for i in List :
            if s(My_1th_Card) == s(i) :
                sign += 1
        if sign == 2 :
            return True
    return False

def Me_Flush_draw_by_3_table_cards( List = None ) :
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

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

def Me_Flush_draw_Ranking( List = None ) :
    """
    Rank 1,...,10
    Example: Rank 2: ( ['6 c','K c','5 h'] , 'Q c' , '3 c' )
    return None if Me_Flush == True or on River or not Me_Flush_draw
    """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    if Me_Flush( List ) == True or len(List) == 5 \
       or( Me_Flush_draw_by_2_table_cards( List ) == False and Me_Flush_draw_by_3_table_cards( List ) == False ) :
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


def Table_Flush_3_cards( List = None ) :
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th 
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 3 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_4_cards( List = None ) :
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th 
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 4 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_5_cards( List = None ) :
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th 
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    
    c = 0; d = 0; h = 0; sp = 0
    for i in List :
        if s(i) == "c" : c = c + 1
        if s(i) == "d" : d = d + 1
        if s(i) == "h" : h = h + 1
        if s(i) == "s" : sp = sp + 1

    if 5 in (c,d,h,sp) :
        return True
    return False

def Table_Flush_draw( List = None ) :
    """
    True if 2 same sign card availabe on the table(not more or less than 2)
    returns False on River
    """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th 
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

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

def Table_Flush( List = None ) :
    """ if Table_Flush_3_cards( List ) or Table_Flush_4_cards( List ) or Table_Flush_5_cards( List ) """
    global Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th 
    globalization()
    
    if List == None :
        if Flop1_Deside == True and Turn1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th ]
        elif Turn1_Deside == True and River1_Deside == False :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th ]
        elif River1_Deside == True :
            List = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]

    if Table_Flush_3_cards( List ) or Table_Flush_4_cards( List ) or Table_Flush_5_cards( List ) :
        return True
    return False

