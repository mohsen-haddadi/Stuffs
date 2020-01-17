# All functions in this file are cache
# All functions before and after 2018 should be checked and marked "tested ok" (All testing ok have done on 6 Agust 2018)
# Check_Mod_On() omit from these functions: 1.my_turn_by_seat_order() #ok  2.Players_turn_by_seat_order( Player_Seat ) #ok 3.Players_turn_from_me_by_seat_order( Player_Seat ) #ok 
# 4.next_playing_player_seat( forward_backward_number ) #ok 5. my_turn_from_last_raiser_sofar() #ok 6. am_i_last_player_from_last_raiser() #ok
# 7.am_i_last_player_by_seat_order() #ok 
# variables: Did_i_raised_at[...] (complete it later) from 2018-1 file(i can look for in reset_info read_bets call bet raise functions) it may be better to change dictionaries to functions too like def Did_i_raised_at(stage)
# For examination when everything is ready, creat a function which print every function returnings in this file and var like My_last_raise in Decition function if check mod is off. and Turn off the other prints and shouts by manipulating the shout function.
def Turn_Finder(Seat_Starter , Xth) : #tested ok
    """ Return The seat number;for instance;(4,1)returns seat 4! """
    Answer = (Seat_Starter - 1 + Xth ) % 5
    if Answer == 0 :
        return 5
    else :
        return Answer

def my_turn_by_seat_order() : #tested ok
    """
    The rules may differs on the other websites. (for 2 players) 
    At preflop last player is always big blind, At non preflop last player is always dealer
    """
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat, Last_Cards_cache , Pre_Flop1_Deside , Flop1_Deside #, Check_Mod

    #Pre_Flop1 = Pre_Flop()
    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        Pre_Flop1 = True
    else :
        Pre_Flop1 = False

    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( Big_Blind_Seat + 1 , i )
        elif Pre_Flop1 == False and Small_Blind_Seat != Dealer_Seat : 
            Seat = Turn_Finder( Small_Blind_Seat , i )
        elif Pre_Flop1 == False and Small_Blind_Seat == Dealer_Seat : #2 players # The rules may differs on the other websites. (for 2 players)
            Seat = Turn_Finder( Big_Blind_Seat , i )
            
        if Seat != My_Seat_Number :
            if Last_Cards_cache[Seat] == True :
                Total += 1
        elif Seat == My_Seat_Number :
            #if Last_Cards_cache[Seat] != True :  #not on main file anymore
                #Check_Mod_On("my_turn_by_seat_order()")
                #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            #else :
                #Total += 1
                #my_position = Total
            Total += 1 #this line is copy & pasted here new
            my_position = Total #this line is copy & pasted here new
    if Total < 2 :
        pass #not on main file anymore
        #Check_Mod_On("my_turn_by_seat_order()") 
        #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        pass
        #return ( my_position , Total )
    return ( my_position , Total ) #this line is copy & pasted here new

def Players_turn_by_seat_order( Player_Seat ) : # just for below function usage #tested ok
    """ 
    The rules may differs on the other websites. (for 2 players) 
    At preflop last player is always big blind, At non preflop last player is always dealer
    if Player_Seat Card is False it will assume Player_Seat Card is True 
    """
    global Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat,\
           Last_Cards_cache , Pre_Flop1_Deside , Flop1_Deside #, Check_Mod

    #Pre_Flop1 = Pre_Flop() 
    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        Pre_Flop1 = True
    else :
        Pre_Flop1 = False

    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( Big_Blind_Seat + 1 , i )
        elif Pre_Flop1 == False and Small_Blind_Seat != Dealer_Seat :
            Seat = Turn_Finder( Small_Blind_Seat , i )
        elif Pre_Flop1 == False and Small_Blind_Seat == Dealer_Seat : #2 players # The rules may differs on the other websites. (for 2 players)
            Seat = Turn_Finder( Big_Blind_Seat , i )
            
        if Seat != Player_Seat :
            if Last_Cards_cache[Seat] == True :
                Total += 1
        elif Seat == Player_Seat :
            #if Last_Cards_cache[Seat] != True :
                #Check_Mod_On("Players_turn_from_me_coins_cache()")
                #Screenshot_Error("Players_turn_from_me_coins_cache() (This case can not happen) Player Cards (seat %s) is not visible" %Player_Seat)
            #else :
                #Total += 1
                #Player_position = Total
            Total += 1 #this line is copy & pasted here new
            Player_position = Total #this line is copy & pasted here new
    if Total < 2 :
        pass #not on main file anymore
        #Check_Mod_On("Players_turn_from_me_coins_cache()")
        #Screenshot_Error("Players_turn_from_me_coins_cache() (This case can not happen) Total lower than 2 my seat %s" %Player_Seat)
    else :
        pass
        #return ( Player_position , Total )
    return ( Player_position , Total ) #this line is copy & pasted here new

def Players_turn_from_me_by_seat_order( Player_Seat ) : #tested ok
    """ if before me :-2, if after me: +4(+4 is max), no 0.if Player_Seat Card is False it will return something wrong like 0"""
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat,\
           Last_Cards_cache , Pre_Flop1_Deside , Flop1_Deside #, Check_Mod

    Answer = Players_turn_by_seat_order( Player_Seat )[0] - my_turn_by_seat_order()[0]
    return Answer
    
def is_there_any_raiser_now(): #tested ok
    """ Except me ,for current stage"""
    global My_Seat_Number , Last_Red_cache
    
    for Seat in range(1,6):
        if Seat == My_Seat_Number :
            continue
        elif Last_Red_cache[Seat] :
            return True
    return False
           
def my_turn_from_last_raiser_sofar(): #tested ok 
    """last raiser except me.(Min is 2. Max is 5). return None if there is no raisers so far """
    global My_Seat_Number , Last_Cards_cache , Bet_cache , Red_cache , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River #, Check_Mod

    Last_Red_Seat = last_raiser_seat_sofar()

    Total = 0
    for i in range(1,6):
        
        Seat = Turn_Finder( Last_Red_Seat , i )

        if Seat != My_Seat_Number :
            if Last_Cards_cache[Seat] == True :
                Total += 1
        elif Seat == My_Seat_Number :
            #if Last_Cards_cache[Seat] != True :   #not on main file anymore
                #Check_Mod_On("my_turn_from_last_raiser_cache()")
                #Screenshot_Error("my_turn_from_last_raiser_cache() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            #else :
                #Total += 1
                #my_position = Total
            Total += 1 #this line is copy & pasted here new
            my_position = Total #this line is copy & pasted here new           
    if Total < 2 :
        pass #not on main file anymore
        #Check_Mod_On("my_turn_from_last_raiser_cache()")
        #Screenshot_Error("my_turn_from_last_raiser_cache() (This case can not happen1) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        pass
        #return ( my_position , Total )
    return ( my_position , Total ) #this line is copy & pasted here new

def next_playing_player_seat( forward_backward_number ) : #tested ok
    """ forward_backward_number can be + or -
    if abs(forward_backward_number) > (4 or more than playing players) : return None """
    global Last_Cards_cache , My_Seat_Number #, Check_Mod

    if forward_backward_number > 0 :
        sign = +1
    elif forward_backward_number < 0 :
        sign = -1
    else :
        return None
    
    p = 0
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , sign * i )
        if Last_Cards_cache[Seat] == True :
            p += (sign * 1)
        if p == forward_backward_number :
            return Seat
    #Check_Mod_On("next_playing_player_seat()")
    #Screenshot_Error("next_playing_player at cache is None")

def last_raisers_list_seat_now() : #tested ok
    """ Except me. My_Seat_Number = 1, raisers seat: 3 , 5. returns : [5,3]. if no raisers: [] """
    global Last_Red_cache , My_Seat_Number

    last_raisers_list = []
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Last_Red_cache[Seat] :
            last_raisers_list.append(Seat)

    last_raisers_list.reverse()
    return last_raisers_list

def number_of_raisers() : # what about the other rounds? # a new and complete function ( number_of_raisers_now() ) has defined instead of this function. i can delete this function later
    """ Except me """
    global Last_Red_cache , My_Seat_Number
    
    return len(last_raisers_list_seat_now( My_Seat_Number ))

### new functions: *****************
def last_raise_now() : #tested ok
    """
    Except me (I can't be included after ocr bets on my turn).
    for current stage, returns 0 if it's only blinds at pre flop or no raises at the other stages
    """
    global Last_Bet_cache , My_Seat_Number , Last_Red_cache

    a = []
    for Seat in range(1,6) :
        if type(Last_Bet_cache[Seat]) == int :
            a.append( Last_Bet_cache[Seat] )
    if len(a) != 0 and is_there_any_raiser_now() ==  True :
        return max(a)
    a = []
    return 0

def last_raiser_seat_now() :#Not usable because of below function. after finishing Play File delete this function.
    global Last_Red_cache , My_Seat_Number , Last_Bet_cache

    last_raiser = None
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        
        if Last_Bet_cache[Seat] == last_raise_now() :
            last_raiser = Seat
            
    return last_raiser 

def last_raiser_seat_sofar() : #tested ok
    """ Except me (because after ocr, max of Bet_cache at any stage and round is not me for sure), if no raising is found: returns None """
    global Bet_cache , Red_cache , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River # if an stage is not reached, its Round is 0

    Seat = None
    for Stage in [ ("Pre_Flop",Round_Pre_Flop ) , ("Flop",Round_Flop) , ("Turn",Round_Turn) , ("River",Round_River) ] : 
        try :            
            List = Bet_cache["%s %s" %Stage] # Error Line
            List = list( List.items() )
            second_indexes = []
            for i in List :
                if type(i[1]) == int : 
                    second_indexes.append( i[1] ) 
            for Seat_count , Item in List :
                if Red_cache["%s %s" %Stage][Seat_count] == True and Item == max( second_indexes ) : # Red_cache to avoid pre_flop blinds or calls as raises 
                    Seat = Seat_count
        except :
            pass    

    return Seat

    
### 2018: ************** # There is no function in NOTEBOOK from before 2018 at all
def number_of_raisers_sofar() : #tested ok #check if Rounds are started from 0 at all stages. otherwise this function will not work properly.
    """ 
    Except me 
    Max number can be 4
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , My_Seat_Number , Red_cache


    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage) #starting back from current stage will work but i have find out no reason to do above lines instead of iritating all stages simply
    Raisers = [ My_Seat_Number ]

    count = 0
    for i in range( start , len(List) ) : #loop for stages

        stage = List[i]
        for Seat in range(1,6): #loop for seats

            if Seat in Raisers : #Except me and avoid repetitive player
                continue 

            Round = 0
            while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
                try:
                    if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                        count += 1 
                        Raisers.append(Seat)
                        break
                except:
                    break
                Round += 1

    return count

def number_of_raisers_at( stage ) : #tested ok
    """
    Except me 
    stage variable should be written in string format : "Pre_Flop" ; "Flop"  ; "Turn" ; "River" otherwise it will return 0.
    """
    global Red_cache , My_Seat_Number

    Players_count = 0
    for Seat in range(1,6): 
        if Seat == My_Seat_Number : #Except me
            continue 
        Round = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                    Players_count += 1 ; break
            except:
                break
            Round += 1

    return Players_count

def number_of_raisers_now() :#0 NOT IN NOTEBOOK # use this instead of number_of_raisers() function #tested ok
    """Except me """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , My_Seat_Number , Red_cache


    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    return number_of_raisers_at( stage )

def number_of_players_more_than_once_raised_at( stage ) : #tested ok
    """
    Except me 
    stage variable should be written in string format : "Pre_Flop" ; "Flop"  ; "Turn" ; "River" otherwise it will return 0.
    """
    global Red_cache , My_Seat_Number

    Players_count = 0
    for Seat in range(1,6):
        if Seat == My_Seat_Number : #Except me
            continue 
        Round = 0 ; count = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                    count += 1 
            except:
                break
            if count >= 2 :
                Players_count += 1
                break
            Round += 1

    return Players_count

def number_of_players_in() : #tested ok
    """ Included me"""
    global Last_Cards_cache

    count = 0
    for Seat in range(1,6) :
        if Last_Cards_cache[Seat] == True :
            count += 1
    return count

def Max_raise_sofar(): #tested ok, i forgot to append my bets too # delete this function. a better one is written below.
    """ Included me """
    global Bet_cache , Red_cache 

    if Any_raiser_sofar( Red_cache ) :
        a = []
        for i in range(len(list( Bet_cache.items() ))) :
            for Seat in range ( len( list(list( Bet_cache.items() )[i][1].items()) ) ) :
                bet = ( list(list(Bet_cache.items())[i][1].items()) )[Seat][1] 
                
                if type( bet ) == int :
                    a.append( bet )

        return max(a)

def Max_raise_sofar(): #tested ok
    """ 
    Included me 
    calls blinds at pre_flop are not counted as raises. so if no raises it will return 0.
    """
    global Bet_cache , Red_cache , My_last_raise , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River

    return max( last_raise_at("Pre_Flop") , last_raise_at("Flop") , last_raise_at("Turn") , last_raise_at("River") )

def Any_raiser_sofar() : #tested ok
    """ Except me (Automatically it's Except me when scaning Red_cache in a Round) """
    global Red_cache

    for i in range(len(list( Red_cache.items() ))) :
        for Seat in range ( len( list(list( Red_cache.items() )[i][1].items()) ) ) :
            if ( list(list(Red_cache.items())[i][1].items()) )[Seat][1] == True :
                return True
    return False

def am_i_last_player_by_seat_order():# tested ok
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat, Last_Cards_cache , Pre_Flop1_Deside , Flop1_Deside #, Check_Mod

    my_position = my_turn_by_seat_order()

    if my_position[1] - my_position[0] == 0 :
        return True
    else :
        return False

def am_i_last_player_from_last_raiser() :#1 NOT IN NOTEBOOK #tested ok
    """ Last raiser can be at any stages """
    global My_Seat_Number , Last_Cards_cache , Bet_cache , Red_cache , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River #, Check_Mod

    my_position = my_turn_from_last_raiser_sofar()
    if my_position[1] - my_position[0] == 0 :
        return True
    else :
        return False 

def last_raise_at(stage) : #tested ok
    """ 
    Included me 
    stage argument should be written in These string formats: "Pre_Flop" "Flop" "Turn" "River" 
    It i will returns 0 by mistake if stage string format is wrong. not reached stages or no raises returns 0.calls blinds at pre_flop returns 0.
    """
    global Bet_cache , Red_cache , My_last_raise , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River

    if stage == "Pre_Flop" : Round = Round_Pre_Flop
    elif stage == "Flop" : Round = Round_Flop
    elif stage == "Turn" : Round = Round_Turn
    elif stage == "River" : Round = Round_River
    try :
        Bets = [ Bet_cache["%s %s" %(stage,Round)][Seat] for Seat in range(1,6) if Red_cache["%s %s" %(stage,Round)][Seat] and Bet_cache["%s %s" %(stage,Round)][Seat] != None ] 
    except :
        Bets = [0] # means it is a not reached stage or stage format is wrong.
    if Bets == [] :
        Bets = [0]
    try :
        Mine = My_last_raise[stage]
    except :
        Mine = 0 # means i have not raised or stage format is wrong.
    return max( max(Bets) , Mine )

def did_i_raise_sofar(): #look ok
    global Did_i_raised_at

    return Did_i_raised_at["Pre_Flop"] or Did_i_raised_at["Flop"] or Did_i_raised_at["Turn"] or Did_i_raised_at["River"]

def am_i_last_raiser_at(stage) : #tested ok
    """ 
    stage argument should be written in These string formats: "Pre_Flop" "Flop" "Turn" "River" otherwise it will error
    if any stage is True or False the next stages are set to True or False too(even not reached stages), so It is counted as so far. 
    If no raising at all returns True
    """
    global Bet_cache , Red_cache , My_last_raise , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage)
    for i in range( start , len(List) ) :
        stage = List[i]

        try :
            Mine = My_last_raise[stage]
        except :
            Mine = 0  # means i have not raised

        if last_raise_at(stage) == 0 and Mine == 0 and stage != "Pre_Flop" :
            continue # continue to former stage in the list
        elif last_raise_at(stage) <= Mine :
            return True
        elif last_raise_at(stage) > Mine :
            return False

def am_i_last_raiser() : #tested ok
    """ As same as am_i_last_raiser_at(stage) for current stage. It is counted as so far """
    global Bet_cache , Red_cache , My_last_raise , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
    Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    return am_i_last_raiser_at(stage)

def am_i_after_last_raiser_by_seat_order() : #tested ok
    """
    The rules may differs on the other websites. (for 2 players)
    In this function, even at preflop the last player is counted the dealer.
    It is counted as so far. If no raiser at all it will return True.
    """
    global Bet_cache , Red_cache , Round_Pre_Flop , Round_Flop , Round_Turn , Round_River ,\
            My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat

    last_raiser_seat = last_raiser_seat_sofar() 

    if last_raiser_seat == None :
        return True

    if Small_Blind_Seat != Dealer_Seat : #small bllind is the first player
        first_player = Small_Blind_Seat
    elif Small_Blind_Seat == Dealer_Seat : #big bllind is the first player #2 players # The rules may differs on the other websites. (for 2 players)
        first_player = Big_Blind_Seat 

    for i in range(1,6):
        Seat = Turn_Finder( first_player , i )
        if Seat == My_Seat_Number :
            return False
        elif Seat == last_raiser_seat :
            return True
        else :
            continue

def did_i_checked() :#2 NOT IN NOTEBOOK #tested ok
    """ 
    It depends on my last action, so if stage round is 0 it will look at the former stage.
    if no action at Pre_Flop it returns True.
    calling Blinds at Pre_Flop will counted as checking and returns True.
    Among 1.did_i_checked() 2.did_i_called() 3.did_i_raised() one of them is always True and the other two is False.
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River, BLIND , My_Seat_Number , Last_Bet_cache , My_last_raise , Bet_cache , Red_cache 

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" ; Round = Round_Pre_Flop
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop" ; former_stage = "Pre_Flop" ; Round = Round_Flop
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" ; former_stage = "Flop" ; Round = Round_Turn
    elif River1_Deside == True :
        stage = "River" ; former_stage = "Turn" ; Round = Round_River   

    if stage == "Pre_Flop" and ( Last_Bet_cache[My_Seat_Number] == None or Last_Bet_cache[My_Seat_Number] <= BLIND ) :
        return True
    elif stage == "Pre_Flop" :
        return False
    # other stages except Pre_Flop: 
    elif Round == 0 :
        if last_raise_at(former_stage) == 0 : return True
        else : return False 
    elif Last_Bet_cache[My_Seat_Number] == None :
        return True
    elif Last_Bet_cache[My_Seat_Number] != None :
        return False

def did_i_called() :#3 NOT IN NOTEBOOK #tested ok
    """ 
    calling Blinds at Pre_Flop will counted as checking and returns False.
    It depends on my last action, so if stage round is 0 it will look at the former stage.
    Among 1.did_i_checked() 2.did_i_called() 3.did_i_raised() one of them is always True and the other two is False.
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River, BLIND , My_Seat_Number , Last_Bet_cache , Last_White_cache , My_last_raise , Bet_cache , Red_cache 

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" ; Round = Round_Pre_Flop
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop" ; former_stage = "Pre_Flop" ; Round = Round_Flop
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" ; former_stage = "Flop" ; Round = Round_Turn
    elif River1_Deside == True :
        stage = "River" ; former_stage = "Turn" ; Round = Round_River  

    if stage == "Pre_Flop" and Last_White_cache[My_Seat_Number] == True and Last_Bet_cache[My_Seat_Number] > BLIND :
        return True
    elif stage == "Pre_Flop" :
        return False
    # other stages except Pre_Flop:
    elif Round == 0 :
        try :
            Mine = My_last_raise[former_stage]
        except :
            Mine = 0  # means i have not raised    
        if Mine == last_raise_at(former_stage) :
            return False
        else :
            return True
    elif Last_White_cache[My_Seat_Number] == True :
        return True
    elif Last_White_cache[My_Seat_Number] == False :
        return False

def did_i_raised() :#4 NOT IN NOTEBOOK #tested ok
    """ 
    It depends on my last action, so if stage round is 0 it will look at the former stage.
    Among 1.did_i_checked() 2.did_i_called() 3.did_i_raised() one of them is always True and the other two is False.
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River, BLIND , My_Seat_Number , Last_Red_cache , My_last_raise , Bet_cache , Red_cache 

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" ; Round = Round_Pre_Flop
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop" ; former_stage = "Pre_Flop" ; Round = Round_Flop
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" ; former_stage = "Flop" ; Round = Round_Turn
    elif River1_Deside == True :
        stage = "River" ; former_stage = "Turn" ; Round = Round_River  

    if stage == "Pre_Flop" and Last_Red_cache[My_Seat_Number] == True :
        return True
    elif stage == "Pre_Flop" :
        return False
    # other stages except Pre_Flop: 
    elif Round == 0 : 
        try :
            Mine = My_last_raise[former_stage]
        except :
            Mine = 0  # means i have not raised    
        if Mine != 0 and Mine == last_raise_at(former_stage) :
            return True
        else :
            return False
    elif Last_Red_cache[My_Seat_Number] == True :
        return True
    elif Last_Red_cache[My_Seat_Number] == False :
        return False

def is_it_first_round() :#5 NOT IN NOTEBOOK #tested ok
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
    Round_Pre_Flop , Round_Flop , Round_Turn , Round_River

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        Round = Round_Pre_Flop
    elif Flop1_Deside == True and Turn1_Deside == False :
        Round = Round_Flop
    elif Turn1_Deside == True and River1_Deside == False :
        Round = Round_Turn
    elif River1_Deside == True :
        Round = Round_River  

    if Round == 0 :
        return True
    else :
        return False

def any_double_raiser_now() :#6 NOT IN NOTEBOOK #tested ok
    """
    Except me
    returns True or False only. if a raiser has raised triple it returns True too.
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , My_Seat_Number , Red_cache

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    for Seat in range(1,6): 
        count = 0
        if Seat == My_Seat_Number : #Except me
            continue 
        Round = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                    count += 1 
            except:
                break
            Round += 1

            if count >= 2 : # double raise
                return True

    return False

def any_triple_raiser_now() :#7 NOT IN NOTEBOOK #tested ok
    """
    Except me
    returns True or False only. if a raiser has more raised than triple it returns True too.
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , My_Seat_Number , Red_cache

    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    for Seat in range(1,6): 
        count = 0
        if Seat == My_Seat_Number : #Except me
            continue 
        Round = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                    count += 1 
            except:
                break
            Round += 1

            if count >= 3 : # triple raise
                return True

    return False

def any_double_raiser_sofar() :#8 NOT IN NOTEBOOK #tested ok
    """
    Except me
    returns True or False only. if a raiser has raised triple it returns True too.
    """  
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , My_Seat_Number , Red_cache


    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage) #starting back from current stage will work but i have find out no reason to do above lines instead of iritating all stages simply

    for i in range( start , len(List) ) : #loop for stages

        stage = List[i]
        
        for Seat in range(1,6): #loop for seats
            count = 0
            if Seat == My_Seat_Number : #Except me
                continue 

            Round = 0
            while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
                try:
                    if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                        count += 1 
                except:
                    break
                Round += 1
                if count >= 2 : # double raise
                    return True

    return False

def any_triple_raiser_sofar() :#9 NOT IN NOTEBOOK #tested ok
    """
    Except me
    returns True or False only. if a raiser has more raised than triple it returns True too.
    """
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside , My_Seat_Number , Red_cache


    if Pre_Flop1_Deside == True and Flop1_Deside == False :
        stage = "Pre_Flop" 
    elif Flop1_Deside == True and Turn1_Deside == False :
        stage = "Flop"  
    elif Turn1_Deside == True and River1_Deside == False :
        stage = "Turn" 
    elif River1_Deside == True :
        stage = "River" 

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage)#starting back from current stage will work but i have find out no reason to do above lines instead of iritating all stages simply

    for i in range( start , len(List) ) : #loop for stages

        stage = List[i]
        
        for Seat in range(1,6): #loop for seats
            count = 0
            if Seat == My_Seat_Number : #Except me
                continue 

            Round = 0
            while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
                try:
                    if Red_cache["%s %s" %(stage,Round)][Seat] == True : 
                        count += 1 
                except:
                    break
                Round += 1
                if count >= 3 : # triple raise
                    return True

    return False

