from FUNCTIONS_hands_category import * # this line is not usable at this file. it will be use in def play functions file instead

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


def decide():
    globalization()

    if Pre_Flop1_Deside == True and Flop1_Deside == False : # instead i can use FUNCTIONS_Supporting_funcs_for_Play_funcs.Pre_Flop_Deside() too
        shout(paint.light_cyan.bold("*Deciding on Preflop*"))
    elif Flop1_Deside == True and Turn1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Flop*"))
    elif Turn1_Deside == True and River1_Deside == False :
        shout(paint.light_cyan.bold("*Deciding on Turn*"))
    elif River1_Deside == True :
        shout(paint.light_cyan.bold("*Deciding on River*"))
    else :
        shout(paint.light_cyan.bold("*Deciding on Unknown*"))
    
    if Check_Mod == True :
        check_fold()

    else :
        
        if Pre_Flop1_Deside == True and Flop1_Deside == False :

            if Round_Pre_Flop == 0 and hand1( My_1th_Card , My_2th_Card ) :
                Raise(5)
            elif Round_Pre_Flop != 0 and hand1( My_1th_Card , My_2th_Card ) :
                all_in()

            elif Round_Pre_Flop == 0 and hand2( My_1th_Card , My_2th_Card ) :
                Raise(4)
            elif Round_Pre_Flop != 0 and hand2( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Pre_Flop == 0 and hand3( My_1th_Card , My_2th_Card ) :
                Raise(3)
            elif Round_Pre_Flop != 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
        
            elif Round_Pre_Flop == 0 and hand4( My_1th_Card , My_2th_Card ) :
                Raise(2)
            elif Round_Pre_Flop != 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Pre_Flop == 0 and hand5( My_1th_Card , My_2th_Card ) :
                Raise(3)
            elif Round_Pre_Flop != 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()

            else :
                check_fold()
                
        if Flop1_Deside == True and Turn1_Deside == False :

            if Round_Flop == 0 and hand1( My_1th_Card , My_2th_Card ) :
                bet(5)
            elif Round_Flop != 0 and hand1( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Flop == 0 and hand2( My_1th_Card , My_2th_Card ) :
                bet(4)
            elif Round_Flop != 0 and hand2( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Flop == 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_Pre_Flop != 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
        
            elif Round_Flop == 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_Flop != 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Flop == 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_Flop != 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()            

            else :
                check_fold()

        if Turn1_Deside == True and River1_Deside == False :

            if Round_Turn == 0 and hand1( My_1th_Card , My_2th_Card ) :
                bet(5)
            elif Round_Turn != 0 and hand1( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Turn == 0 and hand2( My_1th_Card , My_2th_Card ) :
                bet(4)
            elif Round_Turn != 0 and hand2( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Turn == 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_Turn != 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
        
            elif Round_Turn == 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_Turn != 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_Turn == 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_Turn != 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()

            else :
                check_fold()            


        if River1_Deside == True :

            if Round_River == 0 and hand1( My_1th_Card , My_2th_Card ) :
                bet(5)
            elif Round_River != 0 and hand1( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_River == 0 and hand2( My_1th_Card , My_2th_Card ) :
                bet(4)
            elif Round_River != 0 and hand2( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_River == 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_River != 0 and hand3( My_1th_Card , My_2th_Card ) :
                check_fold()
        
            elif Round_River == 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_River != 0 and hand4( My_1th_Card , My_2th_Card ) :
                check_fold()

            elif Round_River == 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()
            elif Round_River != 0 and hand5( My_1th_Card , My_2th_Card ) :
                check_fold()            

            else :
                check_fold()




            
    time.sleep(1)
