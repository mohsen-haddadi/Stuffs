from FUNCTIONS_Supporting_funcs_for_Play_funcs import *
#from str & flush & pair files import *
#from FUNCTIONS_hands_category import *
# Pre_Flop1_Deside = False ; Flop1_Deside = False ; Turn1_Deside = False ; River1_Deside = False 
"""
some Play functions are in calendare. add them here later
Me_str() or Me_Flush() can overlap lower than Me_full_house() (Except Me_str() and Me_2_pair() won't overlap) 
so for all functions lower than Me_full_house() like: 1. Play_hand5_no_raiser() and 2. Play_1_pair() .... , (Me_str() or Me_Flush()) are excluded.
"""
def globalization():
    """ variables order is important while loading """
    global po , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    po , file_name , Reports_directory ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Card_1th , Card_2th , Card_3th , Card_4th , Card_5th , My_1th_Card , My_2th_Card ,\
    Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated ,\
    Cards_cache , White_cache , Red_cache , Bet_cache ,\
    Last_White_cache , Last_Red_cache , Last_Cards_cache , Last_Bet_cache,\
    Did_i_raised_at  , My_last_raise ,Players_name_dic , Players_bank_dic ,\
    BLIND , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat = pickle.load( open( "variables.p", "rb" ) )

#def Play_Pre_Flop(): in the calendar i think

def Bluff_table_flush_4_cards(): #can i add it to Play_individual_cards() functions?! check it later # it has been used in Play_hand5_no_raiser() too
    globalization()

    if River_Deside() and Table_Flush_4_cards() and not Me_str() and not Me_Flush() and Me_Individual() \
    and ( Table_Individual() or Table_1_pair() ) and Table_str_1_cards_Number()\
    and last_raise_at("River") == 0 and last_raise_at("Turn") == 0 and last_raise_at("Flop") <= 4 * BLIND and last_raise_at("Pre_Flop") <= 4 * BLIND :
        shout("Bluff table flush 4 cards is True")
        return True
    else :
        return False

def Play_hand5_no_raiser(): # Check the logic
    """ 
    lower than or 1 pair, but overall full house or overall 4 of kind are possible 
    so if hand5() is True, Play_individual_cards() and Play_1_pair() should not run anyway.
    """
    globalization()

    if not hand5() or Any_raiser_sofar() or ( not Pre_Flop_Deside() and not Me_Individual() and not Me_1_pair() ) or \
    ( not Pre_Flop_Deside() and (Me_str() or Me_Flush()) ) :
        return False

    elif Pre_Flop_Deside() :

        return RAISE( 3 * BLIND )

    elif Flop_Deside() :

        if Bluff_hand5_flop_table_2_cards() :

            return RAISE( 4 * BLIND )

        elif Me_Individual() or Table_1_pair() or ( Me_1_pair() and Me_1_pair_Ranking()[0] > 1 ) :

            return check()

        elif Me_1_pair() and Me_1_pair_Ranking()[0] == 1 :

            return RAISE( 3 * BLIND )

        else :

            shout("Decide Bug")
            Screenshot_Error("Decide Bug")
            #Check_Mod_On("Decide Bug") #by Blocking this line,we let it countinue dicisions at next stage
            return check_fold()

    elif Turn_Deside() :

        if Me_Individual() or ( Table_1_pair() and not did_i_raise_at("Flop") ) or \
        ( Me_1_pair() and   ( Me_1_pair_Ranking()[0] > 2 or ( Me_1_pair_Ranking()[0] == 2 and Table_1_pair() ) )   )  or\
        Table_str_1_cards_Number() == 2 or Table_Flush_4_cards() :

            return check()

        else :

            return RAISE( 3 * BLIND )

    elif River_Deside() :

        if Bluff_table_flush_4_cards() :

            return RAISE( 2 * BLIND )

        elif am_i_last_player_by_seat_order() or Me_Individual() or ( Table_1_pair() and not did_i_raise_at("Turn") ) or\
        ( Me_1_pair() and Me_1_pair_Ranking()[0] != 1 and not did_i_raise_at("Turn") ) or\
        Table_str_1_cards_Number() == 2 or Table_Flush_4_cards() or Table_Flush_5_cards() :

            return check()

        else :

            return RAISE( 3 * BLIND )

    def Bluff_hand5_flop_table_2_cards(): # define it inside the function
        globalization()

        if Flop_Deside() and not Any_raiser_sofar() and hand5() and ( Table_1_pair() or Table_3_of_kinds() ) and Me_Individual() :
            shout("Bluffing hand5 flop table 2 cards")
            return True
        else :
            return False

def Play_hand4():

def Play_hand3():

def Play_hand2():

def Play_hand1():

def Play_1_pair():
    """
    Only with Rank == 1 will be bet. if Kicker card was good bet 2*BLIND if not bet 1*BLIND
    Easily in case of danger like Table flush 4 or 5 cards ,or str 1 cards == 2  ;it will be checked 
    """
    globalization()

    if Pre_Flop_Deside() or Any_raiser_sofar() or hand5() or ( Me_str() or Me_Flush() ) :
        return False
    elif (Flop_Deside() and not Me_1_pair() ) or (Turn_Deside() and not Me_1_pair()) or (River_Deside() and not Me_1_pair()) :
        return False

    elif Flop_Deside() :

        if Table_1_pair() :

            return check()

        elif Me_1_pair_Ranking()[1] >= 10 and Me_1_pair_Ranking()[0] == 1 :

            return RAISE( 2 * BLIND )

        elif Me_1_pair_Ranking()[0] == 1 :

            return RAISE( 1 * BLIND )

        else :

            return check()

    elif Turn_Deside() :

        if Table_1_pair() or Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 :

            return check()

        elif Me_1_pair_Ranking()[1] >= 10 and Me_1_pair_Ranking()[0] == 1 :

            return RAISE( 2 * BLIND )

        elif Me_1_pair_Ranking()[0] == 1 :

            return RAISE( 1 * BLIND )

        else :

            return check()

    elif River_Deside() :

        if Table_1_pair() or Table_2_pair() or Me_1_pair_Ranking()[0] != 1 or\
        Table_Flush_4_cards() or Table_Flush_5_cards() or Table_str_1_cards_Number() == 2 or\
        ( am_i_last_player_by_seat_order() and did_i_raise_sofar() ) :

            return check()

        elif Me_1_pair_Ranking()[1] >= 10 :

            return RAISE( 2 * BLIND )

        else :

            return RAISE( 1 * BLIND )

def Play_2_pair():

    globalization()

    if Pre_Flop_Deside() or Any_raiser_sofar() or ( Me_str() or Me_Flush() ) :
        return False
    elif (Flop_Deside() and not Me_2_pair() ) or (Turn_Deside() and not Me_2_pair()) or (River_Deside() and not Me_2_pair()) :
        return False

    elif Flop_Deside() :

        return RAISE( 3 * BLIND )

    elif Turn_Deside() :

        if Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 or\
        ( Table_1_pair() and ( not did_i_raise_sofar() or Me_2_pair_Ranking()[0] > 1 ) ) :

            return check()

        else :

            return RAISE( 3 * BLIND )

    elif River_Deside() :

        if Table_Flush_4_cards() or Table_Flush_5_cards() or Table_str_1_cards_Number() == 2 or\
        ( Table_1_pair() and ( not did_i_raise_sofar() or Me_2_pair_Ranking()[0] > 1 or am_i_last_player_by_seat_order() ) ) :

            return check()

        elif not Table_str_1_cards() and not Table_str_2_cards() and not Table_Flush() and not Table_1_pair() and\
        not Table_3_of_kinds() and Me_2_pair_Ranking() in [(1,2),(1,3),(1,4)] :

            return RAISE( 9 * BLIND )

        else :

            return RAISE( 3 * BLIND )


def Play_3_of_kind():

    globalization()

    if Pre_Flop_Deside() or Any_raiser_sofar() or ( Me_str() or Me_Flush() ) :
        return False
    elif (Flop_Deside() and not Me_3_of_kinds() ) or (Turn_Deside() and not Me_3_of_kinds()) or (River_Deside() and not Me_3_of_kinds()) :
        return False

    elif Flop_Deside() :

        if did_i_raise_at("Pre_Flop") :
            return RAISE( 3 * BLIND )

        else :

            shout("Check and Raise Strategy")
            return check()

    elif Turn_Deside() :

        if Me_3_of_kinds_Ranking()[0] == 2 and not did_i_raise_at("Flop") :

            return check()

        elif Me_3_of_kinds_Ranking()[0] == 2 :

            shout("Anti Bluff bet")
            return RAISE( 3 * BLIND )

        elif Me_3_of_kinds_Ranking()[0] == 1 and not Me_3_of_kinds([Card_1th , Card_2th , Card_3th]) and not did_i_raise_sofar() :

            shout("Check and Raise Strategy")
            return check()

        elif Me_3_of_kinds_Ranking()[0] == 1 :

            return  RAISE( 3 * BLIND )

        else :

            shout("Decide Bug")
            Screenshot_Error("Decide Bug")
            return check_fold()            

    elif River_Deside() :

        if ( Me_3_of_kinds_Ranking()[0] == 2 or Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 ) and\
        ( am_i_last_player_by_seat_order() or ( not am_i_last_player_by_seat_order() and not did_i_raise_at("Flop") ) ) :

            shout("Check Weak Me_3_of_kinds")
            return check()

        elif Me_3_of_kinds_Ranking()[0] == 2 or Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 :

            shout("Anti Bluff bet")
            return RAISE( 3 * BLIND )

        #Rank == 2 finished.
        elif Table_2_pair() and Me_3_of_kinds_Ranking()[0] == 1 and\
        ( Table_Individual_Cards_List()[0] < min( Table_2_same_Cards_List()[0] and Table_2_same_Cards_List()[1] ) ) :

            shout("Best hand of full house")
            return RAISE( 6 * BLIND )

        else : 

            shout("Bet Normal Me_3_of_kinds hand")
            return RAISE( 3 * BLIND ) #Table_full_house is possible too

def Overall_full_house(): # define it 1.here or 2.at supporting function(need to import FUNCTIONS_Pair file) or 3.define at FUNCTIONS_Pair file. NUMBER 3 IS THE BEST ANSWER

def Overall_4_of_kind(): # define it 1.here or 2.at supporting function(need to import FUNCTIONS_Pair file) or 3.define at FUNCTIONS_Pair file. NUMBER 3 IS THE BEST ANSWER

def Play_str():
    """
    If Me_str() is True, functions lower than Me_full_house() like : 1. Play_hand5_no_raiser() and 2. Play_1_pair()... should return False
    """
    globalization()

    if Pre_Flop_Deside() or Any_raiser_sofar() or Me_Flush() or not Me_str() :
        return False

    elif Flop_Deside() :

        shout("Low bet and Raise Strategy")
        return RAISE( 3 * BLIND )

    elif Turn_Deside() :

        if Table_Flush_4_cards() or ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 2 ) or ( Me_str_2_cards() and Is_above_str_1_card() ) :

            shout("Check Weak Me_str hand")
            return check()

        elif not Table_Individual() or Table_Flush_3_cards() or\
        ( Me_str_2_cards() and Me_str_2_cards_Ranking() != 1 and not Is_above_str_1_card() ) or\
        ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 and \
        Table_str_2_cards() and str_2_Cards_list([Card_1th , Card_2th , Card_3th , Card_4th])[0][0] > \
        str_1_Cards_list([Card_1th , Card_2th , Card_3th , Card_4th])[0] ) : #Avoid Me_str_1_cards 10 to Ace

            shout("Bet Normal Me_str hand")
            if Max_raise_sofar() <= 3 * BLIND :

                return RAISE( 3 * BLIND )

            else :

                return RAISE( Max_raise_sofar() )

        elif Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_1_cards hand, 10 to Ace")
            if not did_i_raise_sofar() :

                return RAISE( 2 * BLIND ) 

            else :

                shout("I can Bet more and better at the other sites")
                return RAISE( Max_raise_sofar() )

        elif Me_str_2_cards() and Me_str_2_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_2_cards hand")
            if not did_i_raise_sofar() :

                return RAISE( 4 * BLIND )

            elif Max_raise_sofar() <=  3 * BLIND :

                return RAISE( 6 * BLIND )

            else :

                return RAISE( 2 * Max_raise_sofar() )

        else :

            shout("Decide Bug")
            Screenshot_Error("Decide Bug")
            return check_fold()                

    elif River_Deside() :

        if Table_Flush_4_cards() or Table_Flush_5_cards() or Table_2_pair() or Table_3_of_kinds() or\
        ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 2 ) or\
        ( Me_str_2_cards() and Is_above_str_1_card() ) :

            shout("Check or Anti Bluff Bet Weak Me_str hand")
            if Max_raise_sofar() >=  6 * BLIND or am_i_last_player_by_seat_order() :

                return check()

            else :

                shout("Anti Bluff Bet")
                return RAISE( Max_raise_sofar() )

        elif Table_Flush_3_cards() or Table_1_pair() or\
        ( Me_str_2_cards() and Me_str_2_cards_Ranking() =! 1 and not Is_above_str_1_card() ) or\
        ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 and \
        Table_str_2_cards() and str_2_Cards_list([Card_1th , Card_2th , Card_3th , Card_4th , Card_5th])[0][0] > \
        str_1_Cards_list([Card_1th , Card_2th , Card_3th , Card_4th ,Card_5th])[0] ) : #Avoid Me_str_1_cards 10 to Ace

            shout("Normal Me_str hand")
            if not did_i_raise_at("Turn") :

                return RAISE( 3 * BLIND )

            elif did_i_raise_at("Turn") and am_i_last_player_by_seat_order() :

                shout("I can Bet it at the other sites")
                return check()

            elif did_i_raise_at("Turn") and not am_i_last_player_by_seat_order() :

                if Max_raise_sofar() <=  3 * BLIND :
                    return RAISE( 3 * BLIND )
                else :
                    return RAISE( Max_raise_sofar() )

        elif Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 :

            shout("Awesome Me_str_1_cards hand, 10 to Ace, Bet")
            if not did_i_raise_sofar() :

                return RAISE( 2 * BLIND ) 

            else :

                shout("I can Bet more and better at the other sites")
                return RAISE( Max_raise_sofar() )

        elif Me_str_2_cards() and Me_str_2_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_2_cards hand")
            if not did_i_raise_sofar() :
                return RAISE( 4 * BLIND )
            elif am_i_last_player_by_seat_order() :
                if Max_raise_sofar() <= 3 * BLIND :
                    return RAISE( 6 * BLIND )
                else :
                    return RAISE( 2 * Max_raise_sofar() )
            else :
                if Max_raise_sofar() <= 3 * BLIND :
                    return RAISE( 9 * BLIND )
                else : 
                    return RAISE( 4 * Max_raise_sofar() )

        else :

            shout("Decide Bug")
            Screenshot_Error("Decide Bug")
            return check_fold()  

def Play_flush():
    """
    If Me_Flush() is True, functions lower than Me_full_house() like : 1. Play_hand5_no_raiser() and 2. Play_1_pair()... should return False
    """
    globalization()

    if Pre_Flop_Deside() or Any_raiser_sofar() or not Me_Flush() :
        return False

    elif Flop_Deside() :

        shout("Low bet and Raise Strategy")
        return RAISE( 3 * BLIND )

    elif Turn_Deside() :

        if Me_Flush_by_4_table_cards() :

            if Me_Flush_Ranking() <= 4 :

                shout("Weak Me_Flush hand")
                return check()

            elif 2 <= Me_Flush_Ranking() <= 3 :

                shout("Good Me_Flush hand")

                if am_i_last_player_by_seat_order() :

                    shout("I can Bet with 2 <= Rank <= 3 at the other sites")
                    return check()

                else :

                    return RAISE( Max_raise_sofar() )

            elif Me_Flush_Ranking() == 1 :

                shout("Awesome Me_Flush hand")

                if not did_i_raise_sofar() :

                    return RAISE( 2 * BLIND )

                elif did_i_raise_sofar() :

                    shout("Low bet and Raise Strategy")
                    return RAISE( Max_raise_sofar() )

        elif Me_Flush_by_3_table_cards() :

            shout("A Good or Awesome Me_Flush hand")

            if Max_raise_sofar() <= 2 * BLIND :

                return RAISE( 3 * BLIND )

            elif Max_raise_sofar() >= 3 * BLIND :

                return RAISE( 2 * Max_raise_sofar() )

    elif River_Deside() :

        if Table_3_of_kinds() or Table_2_pair() :

            shout("Weak Me_Flush hand")
            return check()

        elif ( Me_Flush_by_4_table_cards() or Me_Flush_by_5_table_cards() ) :

            if Me_Flush_Ranking() != 1 :

                shout("Weak Me_Flush hand") 

                if did_i_raise_at("Turn") and not am_i_last_player_by_seat_order() :

                    shout("Anti Bluff bet")
                    return RAISE( Max_raise_sofar() )

                elif not did_i_raise_at("Turn") or am_i_last_player_by_seat_order() :

                    shout("I can Bet with 2 <= Rank <= 3 at the other sites")
                    return check()

            if Me_Flush_Ranking() == 1 :

                if Table_1_pair() :

                    shout("Good Me_Flush hand")

                    if not did_i_raise_sofar() :
                        return RAISE( 2 * BLIND )

                    elif did_i_raise_sofar() :
                        return RAISE( Max_raise_sofar() )

                elif not Table_1_pair() :

                    shout("Awesome Me_Flush hand")

                    if not did_i_raise_sofar() :
                        return RAISE( 2 * BLIND )

                    elif did_i_raise_sofar() :
                        return RAISE( 2 * Max_raise_sofar() )

        elif Me_Flush_by_3_table_cards() :

            if Table_1_pair() :

                shout("Good Me_Flush hand")

                if not did_i_raise_sofar() :
                    return RAISE( 2 * BLIND )

                elif did_i_raise_sofar() :
                    return RAISE( Max_raise_sofar() )

            elif not Table_1_pair() :

                shout("A Good or Awesome Me_Flush hand")

                if Me_Flush_Ranking() != 1 :
                    return RAISE( 2 * Max_raise_sofar() )

                elif Me_Flush_Ranking() == 1 :
                    return RAISE( 3 * Max_raise_sofar() )

    else :

        shout("Decide Bug")
        Screenshot_Error("Decide Bug")
        return check_fold() 











def Play_full_house():

def Play_4_of_kind():

def Play_individual_cards():
