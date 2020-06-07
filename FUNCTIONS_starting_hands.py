from FUNCTIONS_suit_and_value import s, n 


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

#----

def hand1() :
    """ AA,KK """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if  n( My_1th_Card ) == n( My_2th_Card )  and 13 <= n( My_1th_Card ) <= 14 :
        #shout("hand1 is True")
        return True
    else :
        return None

def hand2() :
    """ QQ,JJ """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if  n( My_1th_Card ) == n( My_2th_Card )  and 11 <= n( My_1th_Card ) <= 12 :
        #shout("hand2 is True")
        return True
    else :
        return None

def hand3() :
    """ 1010,99 """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if  n( My_1th_Card ) == n( My_2th_Card )  and 9 <= n( My_1th_Card ) <= 10 :
        #shout("hand3 is True")
        return True
    else :
        return None

def hand4() :
    """ 88,77,...,22 """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if  n( My_1th_Card ) == n( My_2th_Card )  and 2 <= n( My_1th_Card ) <= 8 :
        #shout("hand4 is True")
        return True
    else :
        return None

def hand5() :
    """ A10,...,KQ  3 Blind raise """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if  n( My_1th_Card ) != n( My_2th_Card ) :
        if ( 12 <= n( My_1th_Card ) <= 13 and 12 <= n( My_2th_Card ) <= 13 ) \
        or ( 14 in [ n( My_1th_Card ) , n( My_2th_Card ) ] and n( My_1th_Card ) >= 10 and n( My_2th_Card ) >= 10 ) :
            #shout("hand5 is True")
            return True
    else :
        return None

def hand6() :
    """ KJ,QJ,,...,A2,...,(108,98 rang),109  1 Blind call """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if  n( My_1th_Card ) != n( My_2th_Card ) :
        if hand5() != True :
            if 14 in [ n( My_1th_Card ) , n( My_2th_Card ) ] \
            or ( n( My_1th_Card ) >= 8 and n( My_2th_Card ) >= 8 and s( My_1th_Card ) == s( My_2th_Card ) ) \
            or ( n( My_1th_Card ) >= 9 and n( My_2th_Card ) >= 9 ) :
                #shout("hand6 is True")
                return True
    else :
        return None

def hand7() :
    """ 72,73,...,96,107 (gheir rang)  Fold small blind position (otherwise Small always call Blind) """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if not( hand1() or hand2() or hand3() or \
            hand4() or hand5() or hand6() \
            or s( My_1th_Card ) == s( My_2th_Card ) ) :
        for i in range(2,8) :
            if i in ( n( My_1th_Card ) , n( My_2th_Card ) )  and abs( n( My_2th_Card ) - n( My_1th_Card ) ) >= 3 \
            and n( My_1th_Card ) <= 10 and n( My_2th_Card ) <= 10 :
                #shout("hand7 is True")
                return True
    else :
        return None


#--------------------------------------------


def hand8() :
    """ AK,...,1010,...22,...,(65 rang) Blind position call 2 blind raise, otherwise fold that """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if not( hand1() or hand2() ) :
        if hand3() or hand4() \
        or hand5() or hand6() \
        or ( n( My_1th_Card ) >= 5 and n( My_2th_Card ) >= 5 and \
             s( My_1th_Card ) == s( My_2th_Card ) and abs( n( My_2th_Card ) - n( My_1th_Card ) ) == 1 ) :
            #shout("hand8 is True")
            return True
    else :
        return None

def hand9() :
    """ AK,...,1010,...,(98 rang) Small position call 2 blind raise, otherwise fold that """
    global  My_1th_Card , My_2th_Card 
    globalization()
    if not( hand1() or hand2() ) :
        if hand3() or hand4() \
        or hand5() or hand6() :
            #shout("hand9 is True")
            return True
    else :
        return None    


