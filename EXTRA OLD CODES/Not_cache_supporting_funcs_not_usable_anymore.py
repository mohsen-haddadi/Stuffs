def my_turn_from_coins() :
    global My_Seat_Number , Small_Blind_Seat , Big_Blind_Seat , Dealer_Seat , Check_Mod

    Pre_Flop1 = Pre_Flop()
    Total = 0
    for i in range(1,6) :
        
        if Pre_Flop1 == True :
            Seat = Turn_Finder( Big_Blind_Seat + 1 , i )
        elif Pre_Flop1 == False and Small_Blind_Seat != Dealer_Seat :
            Seat = Turn_Finder( Small_Blind_Seat , i )
        elif Pre_Flop1 == False and Small_Blind_Seat == Dealer_Seat :
            Seat = Turn_Finder( Big_Blind_Seat , i )
            
        if Seat != My_Seat_Number :
            if Cards(Seat) == True :
                Total += 1
        elif Seat == My_Seat_Number :
            if Cards(Seat) != True :
                Check_Mod_On("my_turn_from_coins()")
                Screenshot_Error("my_turn_from_coins() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Check_Mod_On("my_turn_from_coins()")
        Screenshot_Error("my_turn_from_coins() (This case can not happen) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )



def is_there_any_raiser():
    """ Except me """
    global My_Seat_Number
    
    for Seat in range(1,6):
        if Seat == My_Seat_Number :
            continue
        elif Red(Seat) :
            return True
    return False
           
def my_turn_from_last_raiser() :
    """ is_there_any_raiser() should be True, then we run this Function,
    otherwise Last_Red_Seat var can error not assigned """
    global My_Seat_Number , Check_Mod

    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Red(Seat) :
            Last_Red_Seat = Seat

    Total = 0
    for i in range(1,6):
        
        Seat = Turn_Finder( Last_Red_Seat , i )

        if Seat != My_Seat_Number :
            if Cards(Seat) == True :
                Total += 1
        elif Seat == My_Seat_Number :
            if Cards(Seat) != True :
                Check_Mod_On("my_turn_from_last_raiser()")
                Screenshot_Error("my_turn_from_last_raiser() (This case can not happen) My Cards (seat %s) is not visible" %My_Seat_Number)
            else :
                Total += 1
                my_position = Total
    if Total < 2 :
        Check_Mod_On("my_turn_from_last_raiser()")
        Screenshot_Error("my_turn_from_last_raiser() (This case can not happen1) Total lower than 2 my seat %s" %My_Seat_Number)
    else :
        return ( my_position , Total )



def next_playing_player_seat( My_Seat_Number , forward_backward_number ) :
    """ forward_backward_number can be + or -
    if abs(forward_backward_number) >= (5 or more than playing players) : return None """
    global Check_Mod

    if forward_backward_number > 0 :
        sign = +1
    elif forward_backward_number < 0 :
        sign = -1
    else :
        return None
    
    p = 0
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , sign * i )
        if Cards(Seat) == True :
            p += (sign * 1)
        if p == forward_backward_number :
            return Seat
    Check_Mod_On("next_playing_player_seat")
    Screenshot_Error("next_playing_player is None")


def last_raisers_list_seat( My_Seat_Number ) :
    """ Except me. My_Seat_Number = 1, raisers seat: 3 , 5. returns : [5,3]. if no raisers: [] """

    last_raisers_list = []
    for i in range(1,5) :
        Seat = Turn_Finder( My_Seat_Number + 1 , i )
        if Red(Seat) :
            last_raisers_list.append(Seat)

    last_raisers_list.reverse()
    return last_raisers_list

def number_of_raisers( My_Seat_Number ) :
    """ Except me """
    return len(last_raisers_list( My_Seat_Number ))
