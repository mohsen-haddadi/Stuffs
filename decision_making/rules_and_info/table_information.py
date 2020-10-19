#OK
import config as c

"""
All functions in this file are cache.
All functions in this file with True or False returning won't return None at any case.
"""

# set_just_do_check_fold_to_true() omit from these functions: 1.my_turn_by_seat_order() #ok  2.Players_turn_by_seat_order( Player_Seat ) #ok 3.Players_turn_from_me_by_seat_order( Player_Seat ) #ok 
# 4.next_playing_player_seat( forward_backward_number ) #ok 5. my_turn_from_last_raiser_sofar() #ok 6. am_i_last_player_from_last_raiser() #ok
# 7.am_i_last_player_by_seat_order() #ok 8. am_i_first_player_by_seat_order() #ok 9.am_i_last_player_by_seat_order_at_non_preflop_stage #ok
# 10.am_i_first_player_from_last_raiser() #ok
# For examination when everything is ready, creat a function which print every function returnings in this file and var like c.my_last_raise_at in Decition function if check mod is off. and Turn off the other prints and shouts by manipulating the shout function.


def Pre_Flop_Deside() : #tested ok #screen shot and add to cheat sheet
    """
    Among functions: Pre_Flop_Deside() Flop_Deside() Turn_Deside() River_Deside()
    only one of them can be True at a certain time 
    """

    if c.preflop_stage and not c.flop_stage :
        return True
    else :
        return False

def Flop_Deside() : #tested ok #screen shot and add to cheat sheet

    if c.flop_stage and not c.turn_stage :
        return True
    else :
        return False
        
def Turn_Deside() : #tested ok #screen shot and add to cheat sheet

    if c.turn_stage and not c.river_stage :
        return True
    else :
        return False
        
def River_Deside() : #tested ok #screen shot and add to cheat sheet

    if c.river_stage :
        return True
    else :
        return False
        

def Max_raise_sofar(): 
    """ 
    Return 0 to anything
    Included me 
    calls blinds at pre_flop are not counted as raises. so if no raises it will return 0.
    """
    
    return max( last_raise_at("Pre_Flop") , last_raise_at("Flop") , last_raise_at("Turn") , last_raise_at("River") )

def last_raise_now() : 
    """
    Return 0 to anything
    Except me (I can't be included after ocr bets on my turn).
    for current stage
    returns 0 if it's only blinds at pre flop or no raise at current stage
    """
    
    a = []
    for Seat in range(1, config.TOTAL_SEATS+1):
        if type(c.last_bets_cache[Seat]) == int :
            a.append( c.last_bets_cache[Seat] )
    if len(a) != 0 and Any_raiser_now() ==  True :
        return max(a)
    a = []
    return 0

def last_raise_at(stage) : #screen shot again and add to cheat sheet with these new descriptions. 
    """ 
    Return 0 to anything
    Included me 
    stage argument should be written in These string formats: "Pre_Flop" "Flop" "Turn" "River" 
    It i will returns 0 by mistake if stage string format is wrong. 
    not reached stages or no raises at current stage returns 0.calls blinds at pre_flop returns 0.
    """
    
    if stage == "Pre_Flop" : Round = c.preflop_betting_round
    elif stage == "Flop" : Round = c.flop_betting_round
    elif stage == "Turn" : Round = c.turn_betting_round
    elif stage == "River" : Round = c.river_betting_round
    try :
        Bets = [ c.bets_cache["%s %s" %(stage,Round)][Seat] for Seat in range(1, config.TOTAL_SEATS+1) if c.red_chips_cache["%s %s" %(stage,Round)][Seat] and c.bets_cache["%s %s" %(stage,Round)][Seat] != None ] 
    except :
        Bets = [0] # means it is a not reached stage or stage format is wrong.
    if Bets == [] :
        Bets = [0]
    try :
        Mine = c.my_last_raise_at[stage]
    except :
        Mine = 0 # means i have not raised or stage format is wrong.
    return max( max(Bets) , Mine )


def Any_raiser_sofar() : 
    """ 
    Return True or False
    Except me (Automatically it's Except me when scaning c.red_chips_cache in a Round) 
    """
    
    for i in range(len(list( c.red_chips_cache.items() ))) :
        for Seat in range ( len( list(list( red_chips_cache.items() )[i][1].items()) ) ) :
            if ( list(list(red_chips_cache.items())[i][1].items()) )[Seat][1] == True :
                return True
    return False

def Any_raiser_now():
    """ 
    Return True or False
    Except me ,for current stage
    """
    
    for Seat in range(1, config.TOTAL_SEATS+1):
        if Seat == c.my_seat_number :
            continue
        elif c.last_red_chips_cache[Seat] :
            return True
    return False


def number_of_players_in() : 
    """ 
    Return 2 to 5 (if lower than 2, pixel matching was wrong)
    Included me
    """
    
    count = 0
    for Seat in range(1, config.TOTAL_SEATS+1):
        if c.last_player_cards_cache[Seat] == True :
            count += 1
    return count


def am_i_last_player_by_seat_order():
    """ 
    Return True or False
    At preflop last possible player is always big blind, At non preflop last possible player is always dealer
    """
    
    my_position = my_turn_by_seat_order()

    if my_position[1] - my_position[0] == 0 :
        return True
    else :
        return False

def am_i_last_player_by_seat_order_at_non_preflop_stage() :
    """
    Return True or False
    The rules may differs on the other websites. (for 2 players) 
    Last possible player is always dealer for this function.
    This function is usefull when deciding at pre_flop 
    """
    
    #Pre_Flop1 = Pre_Flop()

    Total = 0
    for i in range(1,6) :
        

        if c.small_blind_seat != c.dealer_seat : 
            Seat = Turn_Finder( c.small_blind_seat , i )
        elif c.small_blind_seat == c.dealer_seat : #2 players # The rules may differs on the other websites. (for 2 players)
            Seat = Turn_Finder( c.big_blind_seat , i )
            
        if Seat != c.my_seat_number :
            if c.last_player_cards_cache[Seat] == True :
                Total += 1
        elif Seat == c.my_seat_number :
            #if c.last_player_cards_cache[Seat] != True :  #not on main file anymore
                #set_just_do_check_fold_to_true("my_turn_by_seat_order()")
                #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) My Cards (seat %s) is not visible" %c.my_seat_number)
            #else :
                #Total += 1
                #my_position = Total
            Total += 1 #this line is copy & pasted here new
            my_position = Total #this line is copy & pasted here new
    if Total < 2 :
        pass #not on main file anymore
        #set_just_do_check_fold_to_true("my_turn_by_seat_order()") 
        #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) Total lower than 2 my seat %s" %c.my_seat_number)
    else :
        pass
        #return ( my_position , Total )
    #return ( my_position , Total ) #this line is copy & pasted here new
    if my_position == Total :
        return True
    else :
        return False

def am_i_first_player_by_seat_order():
    """ 
    Return True or False
    At preflop last possible player is always big blind, At non preflop last possible player is always dealer 
    """
    
    if my_turn_by_seat_order()[0] == 1 :
        return True
    else :
        return False

def my_turn_by_seat_order() : 
    """
    Return ( my_position , Total ) 
    my_position: (Min is 1. Max is 5)
    The rules may differs on the other websites. (for 2 players) 
    At preflop last possible player is always big blind, At non preflop last possible player is always dealer
    """
    
    #Pre_Flop1 = Pre_Flop()
    if c.preflop_stage == True and c.flop_stage == False :
        Pre_Flop1 = True
    else :
        Pre_Flop1 = False

    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( c.big_blind_seat + 1 , i )
        elif Pre_Flop1 == False and c.small_blind_seat != c.dealer_seat : 
            Seat = Turn_Finder( c.small_blind_seat , i )
        elif Pre_Flop1 == False and c.small_blind_seat == c.dealer_seat : #2 players # The rules may differs on the other websites. (for 2 players)
            Seat = Turn_Finder( c.big_blind_seat , i )
            
        if Seat != c.my_seat_number :
            if c.last_player_cards_cache[Seat] == True :
                Total += 1
        elif Seat == c.my_seat_number :
            #if c.last_player_cards_cache[Seat] != True :  #not on main file anymore
                #set_just_do_check_fold_to_true("my_turn_by_seat_order()")
                #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) My Cards (seat %s) is not visible" %c.my_seat_number)
            #else :
                #Total += 1
                #my_position = Total
            Total += 1 #this line is copy & pasted here new
            my_position = Total #this line is copy & pasted here new
    if Total < 2 :
        pass #not on main file anymore
        #set_just_do_check_fold_to_true("my_turn_by_seat_order()") 
        #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) Total lower than 2 my seat %s" %c.my_seat_number)
    else :
        pass
        #return ( my_position , Total )
    return ( my_position , Total ) #this line is copy & pasted here new

def my_turn_by_seat_order_at_non_preflop_stage() : 
    """
    Return ( my_position , Total ) 
    my_position: (Min is 1. Max is 5)
    The rules may differs on the other websites. (for 2 players) 
    Last possible player is always dealer for this function.
    This function is usefull when deciding at pre_flop 
    """
    
    #Pre_Flop1 = Pre_Flop()

    Total = 0
    for i in range(1,6) :
        

        if c.small_blind_seat != c.dealer_seat : 
            Seat = Turn_Finder( c.small_blind_seat , i )
        elif c.small_blind_seat == c.dealer_seat : #2 players # The rules may differs on the other websites. (for 2 players)
            Seat = Turn_Finder( c.big_blind_seat , i )
            
        if Seat != c.my_seat_number :
            if c.last_player_cards_cache[Seat] == True :
                Total += 1
        elif Seat == c.my_seat_number :
            #if c.last_player_cards_cache[Seat] != True :  #not on main file anymore
                #set_just_do_check_fold_to_true("my_turn_by_seat_order()")
                #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) My Cards (seat %s) is not visible" %c.my_seat_number)
            #else :
                #Total += 1
                #my_position = Total
            Total += 1 #this line is copy & pasted here new
            my_position = Total #this line is copy & pasted here new
    if Total < 2 :
        pass #not on main file anymore
        #set_just_do_check_fold_to_true("my_turn_by_seat_order()") 
        #Screenshot_Error("my_turn_by_seat_order() (This case can not happen) Total lower than 2 my seat %s" %c.my_seat_number)
    else :
        pass
        #return ( my_position , Total )
    return ( my_position , Total ) #this line is copy & pasted here new


def am_i_last_player_from_last_raiser() :
    """ 
    Return True or False
    Last raiser Except me. Last raiser can be at any stages. if no raiser sofar it will return False  
    Turn order is by last raiser sofar seat order.
    Example: Stage is River and only raise has occur at preflop; dealer at seat 5 had raised and my seat is 3 and seat 4 is empty ; it returns True
    """
    
    my_position = my_turn_from_last_raiser_sofar()
    if my_position == None :
        return False
    if my_position[1] - my_position[0] == 0 :
        return True
    else :
        return False 

def am_i_first_player_from_last_raiser() :
    """ 
    Return True or False
    Last raiser Except me. Last raiser can be at any stages. if no raiser sofar it will return False  
    Turn order is by last raiser sofar seat order.
    Example: Stage is River and only raise has occur at preflop; dealer at seat 5 had raised and my seat is 2 and seat 1 is empty ; it returns True
    """
    
    my_position = my_turn_from_last_raiser_sofar()
    if my_position == None :
        return False
    if my_position[0] == 2 :
        return True
    else :
        return False 

def am_i_after_last_raiser_by_seat_order() : 
    """
    Return True or False
    The rules may differs on the other websites. (for 2 players)
    In this function, even at preflop the last player is counted the dealer.
    It is counted as so far. If no raiser at all it will return True.
    """
    
    last_raiser_seat = last_raiser_seat_sofar() 

    if last_raiser_seat == None :
        return True

    if c.small_blind_seat != c.dealer_seat : #small bllind is the first player
        first_player = c.small_blind_seat
    elif c.small_blind_seat == c.dealer_seat : #big bllind is the first player #2 players # The rules may differs on the other websites. (for 2 players)
        first_player = c.big_blind_seat 

    for i in range(1,6):
        Seat = Turn_Finder( first_player , i )
        if Seat == c.my_seat_number :
            return False
        elif Seat == last_raiser_seat :
            return True
        else :
            continue

def my_turn_from_last_raiser_sofar(): 
    """
    Return ( my_position , Total ) 
    my_position: (Min is 2. Max is 5)
    Turn order is by last raiser sofar seat order.
    last raiser Except me.. return None if there is no other raisers so far 
    Last raiser can be at any stages 
    Example: Stage is River and only raise has occur at preflop; dealer at seat 5 had raised and my seat is 3 and only seat 4 is empty ; it returns (4,4)
    """
    
    Last_Red_Seat = last_raiser_seat_sofar()

    Total = 0
    for i in range(1,6):
        
        Seat = Turn_Finder( Last_Red_Seat , i )

        if Seat != c.my_seat_number :
            if c.last_player_cards_cache[Seat] == True :
                Total += 1
        elif Seat == c.my_seat_number :
            #if c.last_player_cards_cache[Seat] != True :   #not on main file anymore
                #set_just_do_check_fold_to_true("my_turn_from_last_raiser_cache()")
                #Screenshot_Error("my_turn_from_last_raiser_cache() (This case can not happen) My Cards (seat %s) is not visible" %c.my_seat_number)
            #else :
                #Total += 1
                #my_position = Total
            Total += 1 #this line is copy & pasted here new
            my_position = Total #this line is copy & pasted here new           
    if Total < 2 :
        pass #not on main file anymore
        #set_just_do_check_fold_to_true("my_turn_from_last_raiser_cache()")
        #Screenshot_Error("my_turn_from_last_raiser_cache() (This case can not happen1) Total lower than 2 my seat %s" %c.my_seat_number)
    else :
        pass
        #return ( my_position , Total )
    return ( my_position , Total ) #this line is copy & pasted here new


def did_i_checked() :
    """ 
    Return True or False
    It depends on my last action, so if stage round is 0 it will look at the former stage.
    if no action at Pre_Flop it returns True.
    calling Blinds at Pre_Flop will counted as checking and returns True.
    Among 1.did_i_checked() 2.did_i_called() 3.did_i_raised() one of them is always True and the other two is False.
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" ; Round = c.preflop_betting_round
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop" ; former_stage = "Pre_Flop" ; Round = c.flop_betting_round
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" ; former_stage = "Flop" ; Round = c.turn_betting_round
    elif c.river_stage == True :
        stage = "River" ; former_stage = "Turn" ; Round = c.river_betting_round   

    if stage == "Pre_Flop" and ( c.last_bets_cache[c.my_seat_number] == None or c.last_bets_cache[c.my_seat_number] <= c.BLIND_VALUE ) :
        return True
    elif stage == "Pre_Flop" :
        return False
    # other stages except Pre_Flop: 
    elif Round == 0 :
        if last_raise_at(former_stage) == 0 : return True
        else : return False 
    elif c.last_bets_cache[c.my_seat_number] == None :
        return True
    elif c.last_bets_cache[c.my_seat_number] != None :
        return False

def did_i_called() :
    """ 
    Return True or False
    calling Blinds at Pre_Flop will counted as checking and returns False.
    It depends on my last action, so if stage round is 0 it will look at the former stage.
    Among 1.did_i_checked() 2.did_i_called() 3.did_i_raised() one of them is always True and the other two is False.
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" ; Round = c.preflop_betting_round
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop" ; former_stage = "Pre_Flop" ; Round = c.flop_betting_round
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" ; former_stage = "Flop" ; Round = c.turn_betting_round
    elif c.river_stage == True :
        stage = "River" ; former_stage = "Turn" ; Round = c.river_betting_round  

    if stage == "Pre_Flop" and c.last_white_chips_cache[c.my_seat_number] == True and c.last_bets_cache[c.my_seat_number] > c.BLIND_VALUE :
        return True
    elif stage == "Pre_Flop" :
        return False
    # other stages except Pre_Flop:
    elif Round == 0 :
        try :
            Mine = c.my_last_raise_at[former_stage]
        except :
            Mine = 0  # means i have not raised    
        if Mine == last_raise_at(former_stage) :
            return False
        else :
            return True
    elif c.last_white_chips_cache[c.my_seat_number] == True :
        return True
    elif c.last_white_chips_cache[c.my_seat_number] == False :
        return False

def did_i_raised() :
    """ 
    Return True or False
    It depends on my last action, so if stage round is 0 it will look at the former stage.
    Among 1.did_i_checked() 2.did_i_called() 3.did_i_raised() one of them is always True and the other two is False.
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" ; Round = c.preflop_betting_round
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop" ; former_stage = "Pre_Flop" ; Round = c.flop_betting_round
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" ; former_stage = "Flop" ; Round = c.turn_betting_round
    elif c.river_stage == True :
        stage = "River" ; former_stage = "Turn" ; Round = c.river_betting_round  

    if stage == "Pre_Flop" and c.last_red_chips_cache[c.my_seat_number] == True :
        return True
    elif stage == "Pre_Flop" :
        return False
    # other stages except Pre_Flop: 
    elif Round == 0 : 
        try :
            Mine = c.my_last_raise_at[former_stage]
        except :
            Mine = 0  # means i have not raised    
        if Mine != 0 and Mine == last_raise_at(former_stage) :
            return True
        else :
            return False
    elif c.last_red_chips_cache[c.my_seat_number] == True :
        return True
    elif c.last_red_chips_cache[c.my_seat_number] == False :
        return False


def did_i_raise_sofar(): 
    """ Return True or False """

    return c.did_i_raised_at["Pre_Flop"] or c.did_i_raised_at["Flop"] or c.did_i_raised_at["Turn"] or c.did_i_raised_at["River"]

def did_i_raise_at(stage) : 
    """ 
    Return True or False 
    stage argument should be written in These string formats: "Pre_Flop" "Flop" "Turn" "River" otherwise it will error
    """
    
    return c.did_i_raised_at[stage]

def am_i_last_raiser_at(stage) : 
    """ 
    Return True or False
    stage argument should be written in These string formats: "Pre_Flop" "Flop" "Turn" "River" otherwise it will error
    if any stage is True or False the next stages are set to True or False too(even not reached stages), so It is counted as so far. 
    If no raising at all returns True
    If i've not raised at all but the others have raised, returns False
    """
    
    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage)
    for i in range( start , len(List) ) :
        stage = List[i]

        try :
            Mine = c.my_last_raise_at[stage]
        except :
            Mine = 0  # means i have not raised

        if last_raise_at(stage) == 0 and Mine == 0 and stage != "Pre_Flop" :
            continue # continue to former stage in the list
        elif last_raise_at(stage) <= Mine :
            return True
        elif last_raise_at(stage) > Mine :
            return False

def am_i_last_raiser() : 
    """ 
    Return True or False
    As same as am_i_last_raiser_at(stage) for current stage. It is counted as so far 
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    return am_i_last_raiser_at(stage)


def is_it_first_round() :
    """ Return True or False """
    
    if c.preflop_stage == True and c.flop_stage == False :
        Round = c.preflop_betting_round
    elif c.flop_stage == True and c.turn_stage == False :
        Round = c.flop_betting_round
    elif c.turn_stage == True and c.river_stage == False :
        Round = c.turn_betting_round
    elif c.river_stage == True :
        Round = c.river_betting_round  

    if Round == 0 :
        return True
    else :
        return False


"""
The intense of raisers Except me:
"""

def number_of_raisers_sofar() : #tested ok #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. #for testing i have put a shout(c.bets_cache) at the end of Read_Bets() function 
    """ 
    Return 0 to 4
    Except me 
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage) #starting back from current stage will work but i have find out no reason to do above lines instead of iritating all stages simply
    Raisers = [ c.my_seat_number ]

    count = 0
    for i in range( start , len(List) ) : #loop for stages

        stage = List[i]
        for Seat in range(1, config.TOTAL_SEATS+1): #loop for seats

            if Seat in Raisers : #Except me and avoid repetitive player
                continue 

            Round = 0
            while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
                try:
                    if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                        count += 1 
                        Raisers.append(Seat)
                        break
                except:
                    break
                Round += 1

    return count

def number_of_raisers_now() :
    """
    Return 0 to 4
    Except me 
    """  

    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    return number_of_raisers_at( stage )

def number_of_raisers_at( stage ) :
    """
    Return 0 to 4
    Except me 
    stage variable should be written in string format : "Pre_Flop" ; "Flop"  ; "Turn" ; "River" otherwise it will return 0.
    """
    
    Players_count = 0
    for Seat in range(1, config.TOTAL_SEATS+1): 
        if Seat == c.my_seat_number : #Except me
            continue 
        Round = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                    Players_count += 1 ; break
            except:
                break
            Round += 1

    return Players_count

def number_of_players_more_than_once_raised_at( stage ) :
    """
    Return 0 to 4
    Except me 
    stage variable should be written in string format : "Pre_Flop" ; "Flop"  ; "Turn" ; "River" otherwise it will return 0.
    """
    
    Players_count = 0
    for Seat in range(1, config.TOTAL_SEATS+1):
        if Seat == c.my_seat_number : #Except me
            continue 
        Round = 0 ; count = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                    count += 1 
            except:
                break
            if count >= 2 :
                Players_count += 1
                break
            Round += 1

    return Players_count


def any_double_raiser_now() :
    """
    Return True or False
    Except me
    returns True or False only. if a raiser has raised triple it returns True too.
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    for Seat in range(1, config.TOTAL_SEATS+1): 
        count = 0
        if Seat == c.my_seat_number : #Except me
            continue 
        Round = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                    count += 1 
            except:
                break
            Round += 1

            if count >= 2 : # double raise
                return True

    return False

def any_triple_raiser_now() :
    """
    Return True or False
    Except me
    returns True or False only. if a raiser has more raised than triple it returns True too.
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    for Seat in range(1, config.TOTAL_SEATS+1): 
        count = 0
        if Seat == c.my_seat_number : #Except me
            continue 
        Round = 0
        while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
            try:
                if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                    count += 1 
            except:
                break
            Round += 1

            if count >= 3 : # triple raise
                return True

    return False

def any_double_raiser_sofar() :
    """
    Return True or False
    Except me
    returns True or False only. if a raiser has raised triple it returns True too.
    """  

    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage) #starting back from current stage will work but i have find out no reason to do above lines instead of iritating all stages simply

    for i in range( start , len(List) ) : #loop for stages

        stage = List[i]
        
        for Seat in range(1, config.TOTAL_SEATS+1): #loop for seats
            count = 0
            if Seat == c.my_seat_number : #Except me
                continue 

            Round = 0
            while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
                try:
                    if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                        count += 1 
                except:
                    break
                Round += 1
                if count >= 2 : # double raise
                    return True

    return False

def any_triple_raiser_sofar() :
    """
    Return True or False
    Except me
    returns True or False only. if a raiser has more raised than triple it returns True too.
    """
    
    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop" 
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"  
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn" 
    elif c.river_stage == True :
        stage = "River" 

    List = ["River" , "Turn" , "Flop" , "Pre_Flop"]
    start = List.index(stage)#starting back from current stage will work but i have find out no reason to do above lines instead of iritating all stages simply

    for i in range( start , len(List) ) : #loop for stages

        stage = List[i]
        
        for Seat in range(1, config.TOTAL_SEATS+1): #loop for seats
            count = 0
            if Seat == c.my_seat_number : #Except me
                continue 

            Round = 0
            while True : #check if Rounds are started from 0 at all stages. otherwise this function will not work properly. 
                try:
                    if c.red_chips_cache["%s %s" %(stage,Round)][Seat] == True : 
                        count += 1 
                except:
                    break
                Round += 1
                if count >= 3 : # triple raise
                    return True

    return False


"""
Not direct Practical functions:
"""

def Turn_Finder(Seat_Starter , Xth) :
    """ Return The seat number;for instance;(4,1)returns seat 4! """
    Answer = (Seat_Starter - 1 + Xth ) % 5
    if Answer == 0 :
        return 5
    else :
        return Answer

def last_raiser_seat_sofar() :
    """ 
    Return 1,..,5 and None
    Except me (because after ocr, max of c.bets_cache at any stage and round is not me for sure), if no raising is found: returns None 
    """
    
    Seat = None
    for Stage in [ ("Pre_Flop",c.preflop_betting_round ) , ("Flop",c.flop_betting_round) , ("Turn",c.turn_betting_round) , ("River",c.river_betting_round) ] : 
        try :            
            List = c.bets_cache["%s %s" %Stage] # Error Line
            List = list( List.items() )
            second_indexes = []
            for i in List :
                if type(i[1]) == int : 
                    second_indexes.append( i[1] ) 
            for Seat_count , Item in List :
                if c.red_chips_cache["%s %s" %Stage][Seat_count] == True and Item == max( second_indexes ) : # c.red_chips_cache to avoid pre_flop blinds or calls as raises 
                    Seat = Seat_count
        except :
            pass    

    return Seat

def last_raisers_list_seat_now() :
    """ 
    Return a List
    Except me. c.my_seat_number = 1, raisers seat: 3 , 5. returns : [5,3]. if no raisers: [] 
    """
    
    last_raisers_list = []
    for i in range(1,5) :
        Seat = Turn_Finder( c.my_seat_number + 1 , i )
        if c.last_red_chips_cache[Seat] :
            last_raisers_list.append(Seat)

    last_raisers_list.reverse()
    return last_raisers_list

def next_playing_player_seat( forward_backward_number ) :
    """ 
    Return 1,...,5 and None
    forward_backward_number can be + or -
    if abs(forward_backward_number) > (4 or more than playing players) : return None 
    """
    
    if forward_backward_number > 0 :
        sign = +1
    elif forward_backward_number < 0 :
        sign = -1
    else :
        return None
    
    p = 0
    for i in range(1,5) :
        Seat = Turn_Finder( c.my_seat_number + 1 , sign * i )
        if c.last_player_cards_cache[Seat] == True :
            p += (sign * 1)
        if p == forward_backward_number :
            return Seat
    #set_just_do_check_fold_to_true("next_playing_player_seat()")
    #Screenshot_Error("next_playing_player at cache is None")

def Players_turn_by_seat_order( Player_Seat ) : # just for below function usage 
    """ 
    Return ( Player_position , Total )
    Player_position: (Min is 1. Max is 5)
    The rules may differs on the other websites. (for 2 players) 
    At preflop last possible player is always big blind, At non preflop last possible player is always dealer
    if Player_Seat Card is False it will assume Player_Seat Card is True 
    """
    
    #Pre_Flop1 = Pre_Flop() 
    if c.preflop_stage == True and c.flop_stage == False :
        Pre_Flop1 = True
    else :
        Pre_Flop1 = False

    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( c.big_blind_seat + 1 , i )
        elif Pre_Flop1 == False and c.small_blind_seat != c.dealer_seat :
            Seat = Turn_Finder( c.small_blind_seat , i )
        elif Pre_Flop1 == False and c.small_blind_seat == c.dealer_seat : #2 players # The rules may differs on the other websites. (for 2 players)
            Seat = Turn_Finder( c.big_blind_seat , i )
            
        if Seat != Player_Seat :
            if c.last_player_cards_cache[Seat] == True :
                Total += 1
        elif Seat == Player_Seat :
            #if c.last_player_cards_cache[Seat] != True :
                #set_just_do_check_fold_to_true("Players_turn_from_me_coins_cache()")
                #Screenshot_Error("Players_turn_from_me_coins_cache() (This case can not happen) Player Cards (seat %s) is not visible" %Player_Seat)
            #else :
                #Total += 1
                #Player_position = Total
            Total += 1 #this line is copy & pasted here new
            Player_position = Total #this line is copy & pasted here new
    if Total < 2 :
        pass #not on main file anymore
        #set_just_do_check_fold_to_true("Players_turn_from_me_coins_cache()")
        #Screenshot_Error("Players_turn_from_me_coins_cache() (This case can not happen) Total lower than 2 my seat %s" %Player_Seat)
    else :
        pass
        #return ( Player_position , Total )
    return ( Player_position , Total ) #this line is copy & pasted here new

def Players_turn_from_me_by_seat_order( Player_Seat ) : 
    """ 
    Return -4,...,+4 except 0
    if before me :-2, if after me: +4(+4 is max), no 0.if Player_Seat Card is False it will return something wrong like 0
    At preflop last possible player is always big blind, At non preflop last possible player is always dealer. 
    so at preflop and non preflop stages, Players_turn_from_me_by_seat_order differs.
    """
    
    Answer = Players_turn_by_seat_order( Player_Seat )[0] - my_turn_by_seat_order()[0]
    return Answer
    
