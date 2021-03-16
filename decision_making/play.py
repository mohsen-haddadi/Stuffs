VERSION = 1

#OK
from decision_making.rules_and_info.table_information import *
from decision_making.rules_and_info.straight import *
from decision_making.rules_and_info.flush import *
from decision_making.rules_and_info.non_straight_and_flush import *
from decision_making.rules_and_info.suit_and_value import *
from decision_making.rules_and_info.starting_hands import *
#from rules_and_info.table_information import *
#from rules_and_info.straight import *
#from rules_and_info.flush import *
#from rules_and_info.non_straight_and_flush import *
#from rules_and_info.suit_and_value import *
#from rules_and_info.starting_hands import *
from iprint import shout
import config as c

"""
Me_str() or Me_Flush() can overlap lower than Me_full_house() 
(Except Me_str() and Me_2_pair() won't overlap) 
so for all functions lower than Me_full_house() like: 
1. play_hand5_individual_or_1_pair() and 2. Play_1_pair() .... , 
(Me_str() or Me_Flush()) are excluded.
"""


def bluff_table_flush_4_cards(): 

    if River_Deside() and Table_Flush_4_cards() \
    and not Me_str() and not Me_Flush() \
    and Me_Individual() and ( Table_Individual() or Table_1_pair() ) \
    and Table_str_1_cards_Number() !=2 \
    and last_raise_at("River") == 0 \
    and last_raise_at("Turn") == 0 \
    and last_raise_at("Flop") <= 4 * c.BLIND_VALUE \
    and last_raise_at("Pre_Flop") <= 4 * c.BLIND_VALUE :

        shout("Bluffing table flush 4 cards")
        scenario(1)
        return True
    else :
        scenario(2)
        return False


def to_play_hand5_individual_or_1_pair():
    
    if not hand5() or Any_raiser_sofar() or Pre_Flop_Deside() \
    or ( not Me_Individual() and not Me_1_pair() ) \
    or ( Me_str() or Me_Flush() ) :

        scenario(3)
        return False
    else:
        scenario(4)
        return True

def play_hand5_individual_or_1_pair(): # Check the logic
    """ 
    lower than or 1 pair, but overall full house or overall 4 of kind are possible 
    so if hand5() is True, Play_individual_cards() and Play_1_pair() should not run anyway.
    """
    def bluff_hand5_flop_table_2_cards(): # define it inside the function

        if Flop_Deside() and not Any_raiser_sofar() and hand5() \
        and ( Table_1_pair() or Table_3_of_kinds() ) and Me_Individual() :

            shout("Bluffing hand5 flop table 2 cards")
            scenario(5)
            return True
        else :
            scenario(6)
            return False

    # Preflop is transfered to play_pre_flop() function 

    #elif Pre_Flop_Deside() :
    #
    #    return ("raise", 3)

    if Flop_Deside() :

        if bluff_hand5_flop_table_2_cards() :

            scenario(7)
            return ("raise", 4)

        elif Me_Individual() or Table_1_pair() \
        or ( Me_1_pair() and Me_1_pair_Ranking()[0] > 1 ) :

            scenario(8)
            return ("check")

        elif Me_1_pair() and Me_1_pair_Ranking()[0] == 1 :

            scenario(9)
            return ("raise", 3)

    elif Turn_Deside() :

        if Me_Individual()\
        or ( Table_1_pair() and not did_i_raise_at("Flop") )\
        or ( Me_1_pair() and
             ( 
               Me_1_pair_Ranking()[0] > 2 
               or ( Me_1_pair_Ranking()[0] == 2 and Table_1_pair() ) 
             ) 
           )\
        or Table_str_1_cards_Number() == 2 or Table_Flush_4_cards() :

            scenario(10)
            return ("check")

        else :

            scenario(11)
            return ("raise", 3)

    elif River_Deside() :

        if bluff_table_flush_4_cards() :

            scenario(12)
            return ("raise", 2)

        elif am_i_last_player_by_seat_order() or Me_Individual() \
        or ( Table_1_pair() and not did_i_raise_at("Turn") )\
        or ( Me_1_pair() and Me_1_pair_Ranking()[0] != 1 
             and not did_i_raise_at("Turn") )\
        or Table_str_1_cards_Number() == 2 \
        or Table_Flush_4_cards() or Table_Flush_5_cards() :

            scenario(13)
            return ("check")

        else :

            scenario(14)
            return ("raise", 3)


def to_play_individual_cards():

    if not Me_Individual() or Any_raiser_sofar() or Pre_Flop_Deside()\
    or hand5() or ( Me_str() or Me_Flush() ) :

        scenario(15)
        return False
    else:
        scenario(16)
        return True

def play_individual_cards():

    def bluff_table_1_pair() :

        if not Pre_Flop_Deside() and Me_Individual() and Table_1_pair()\
        and not Any_raiser_sofar():

            shout("Bluffing table 1 pair")
            scenario(17)
            return True
        else :
            scenario(18)
            return False

    if Flop_Deside() or Turn_Deside() :

        if bluff_table_1_pair() and not did_i_raise_sofar() :
            scenario(19)
            return ("raise", 2)
        else :
            scenario(20)
            return ("check")

    elif River_Deside() :

        if bluff_table_flush_4_cards() :
            scenario(21)
            return ("raise", 2)
        if bluff_table_1_pair() and not did_i_raise_sofar() :
            scenario(22)
            return ("raise", 2)
        elif Table_4_of_kinds()\
             and max( n(c.my_1th_card) , n(c.my_2th_card) ) in (14,13):
            scenario(23)
            return ("raise", 1)
        else :
            scenario(24)
            return ("check")


def to_play_1_pair():

    if not Me_1_pair() or Pre_Flop_Deside() or Any_raiser_sofar() or hand5()\
    or ( Me_str() or Me_Flush() ):

        scenario(25)
        return False
    else:
        scenario(26)
        return True

def play_1_pair():
    """
    Only with Rank == 1 will be bet. if Kicker card was good bet 2*c.BLIND_VALUE if not bet 1*c.BLIND_VALUE
    Easily in case of danger like Table flush 4 or 5 cards ,or str 1 cards == 2  ;it will be checked 
    """
    if Flop_Deside() :

        if Table_1_pair() :

            scenario(27)
            return ("check")

        elif Me_1_pair_Ranking()[1] >= 10 and Me_1_pair_Ranking()[0] == 1 :

            scenario(28)
            return ("raise", 2)

        elif Me_1_pair_Ranking()[0] == 1 :

            scenario(29)
            return ("raise", 1)

        else :

            scenario(30)
            return ("check")

    elif Turn_Deside() :

        if Table_1_pair() or Table_Flush_4_cards() \
        or Table_str_1_cards_Number() == 2 :

            scenario(31)
            return ("check")

        elif Me_1_pair_Ranking()[1] >= 10 and Me_1_pair_Ranking()[0] == 1 :

            scenario(32)
            return ("raise", 2)

        elif Me_1_pair_Ranking()[0] == 1 :

            scenario(33)
            return ("raise", 1)

        else :

            scenario(34)
            return ("check")

    elif River_Deside() :

        if Table_1_pair() or Table_2_pair() or Me_1_pair_Ranking()[0] != 1\
        or Table_Flush_4_cards() or Table_Flush_5_cards()\
        or Table_str_1_cards_Number() == 2\
        or ( am_i_last_player_by_seat_order() and did_i_raise_sofar() ) :

            scenario(35)
            return ("check")

        elif Me_1_pair_Ranking()[1] >= 10 :

            scenario(36)
            return ("raise", 2)

        else :

            scenario(37)
            return ("raise", 1)


def to_play_2_pair():

    if not Me_2_pair() or Pre_Flop_Deside() or Any_raiser_sofar()\
    or ( Me_str() or Me_Flush() ):

        scenario(38)
        return False
    else:
        scenario(39)
        return True

def play_2_pair(): #OK

    if Flop_Deside() :

        scenario(40)
        return ("raise", 3)

    elif Turn_Deside() :

        if Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 \
        or ( Table_1_pair() 
             and ( not did_i_raise_sofar() or Me_2_pair_Ranking()[0] > 1 ) 
           ):

            scenario(41)
            return ("check")

        else :

            scenario(42)
            return ("raise", 3)

    elif River_Deside() :

        if Table_Flush_4_cards() or Table_Flush_5_cards()\
        or Table_str_1_cards_Number() == 2\
        or ( Table_1_pair() 
             and ( not did_i_raise_sofar() or Me_2_pair_Ranking()[0] > 1 
                   or am_i_last_player_by_seat_order() 
                 ) 
           ):

            scenario(43)
            return ("check")

        elif not Table_str_1_cards() and not Table_str_2_cards()\
        and not Table_Flush()\
        and not Table_1_pair() and not Table_3_of_kinds()\
        and Me_2_pair_Ranking() in [(1,2),(1,3),(1,4)] :

            scenario(44)
            return ("raise", 9)

        else :

            scenario(45)
            return ("raise", 3)


def to_play_3_of_kind():

    if not Me_3_of_kinds() or Pre_Flop_Deside() or Any_raiser_sofar()\
    or ( Me_str() or Me_Flush() ):

        scenario(46)
        return False
    else:
        scenario(47)
        return True

def play_3_of_kind(): #OK

    if Flop_Deside() :

        if did_i_raise_at("Pre_Flop") :
            scenario(48)
            return ("raise", 3)

        else :

            shout("Check and Raise Strategy")
            scenario(49)
            return ("check")

    elif Turn_Deside() :

        if Me_3_of_kinds_Ranking()[0] == 2 and not did_i_raise_at("Flop") :

            scenario(50)
            return ("check")

        elif Me_3_of_kinds_Ranking()[0] == 2 :

            shout("Anti Bluff bet")
            scenario(51)
            return ("raise", 3)

        elif Me_3_of_kinds_Ranking()[0] == 1\
        and not Me_3_of_kinds([c.board_card_1th ,
                               c.board_card_2th , 
                               c.board_card_3th])\
        and not did_i_raise_sofar():

            shout("Check and Raise Strategy")
            scenario(52)
            return ("check")

        elif Me_3_of_kinds_Ranking()[0] == 1 :

            scenario(53)
            return  ("raise", 3)
       

    elif River_Deside() :

        if ( Me_3_of_kinds_Ranking()[0] == 2 or Table_Flush_4_cards()
             or Table_str_1_cards_Number() == 2 
           )\
        and ( am_i_last_player_by_seat_order() 
              or ( not am_i_last_player_by_seat_order() 
                   and not did_i_raise_at("Turn") 
                 ) 
            ) :

            shout("Check Weak Me_3_of_kinds")
            scenario(54)
            return ("check")

        elif Me_3_of_kinds_Ranking()[0] == 2 or Table_Flush_4_cards()\
        or Table_str_1_cards_Number() == 2 :

            shout("Anti Bluff bet")
            scenario(55)
            return ("raise", 3)

        #Rank == 2 finished.
        elif Table_2_pair() and Me_3_of_kinds_Ranking()[0] == 1\
        and ( Table_Individual_Cards_List()[0] 
              < min( Table_2_same_Cards_List()[0] ,
                     Table_2_same_Cards_List()[1] 
                   ) 
            ) :

            shout("Best hand of full house")
            scenario(56)
            return ("raise", 6)

        else : 

            shout("Bet Normal Me_3_of_kinds hand")
            scenario(57)
            return ("raise", 3) #Table_full_house is possible too


def to_play_straight():

    if not Me_str() or Pre_Flop_Deside() or Any_raiser_sofar() or Me_Flush():

        scenario(58)
        return False
    else:
        scenario(59)
        return True

def play_straight():
    """
    If Me_str() is True, functions lower than Me_full_house() like: 
    1.play_hand5_individual_or_1_pair() and 2.Play_1_pair()... 
    should return False
    """
    if Flop_Deside() :

        shout("Low bet and Raise Strategy")
        scenario(60)
        return ("raise", 3)

    elif Turn_Deside() :

        if Table_Flush_4_cards()\
        or ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 2 )\
        or ( Me_str_2_cards() 
             and is_there_any_better_possible_1_card_straight_on_table() 
           ):

            shout("Check Weak Me_str hand")
            scenario(61)
            return ("check")

        elif not Table_Individual() or Table_Flush_3_cards() or\
        ( Me_str_2_cards() and Me_str_2_cards_Ranking() != 1 
          and not is_there_any_better_possible_1_card_straight_on_table() 
        )\
        or ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 
             and Table_str_2_cards() 
             and str_2_Cards_list([c.board_card_1th ,
                                   c.board_card_2th ,
                                   c.board_card_3th ,
                                   c.board_card_4th])[0][0]\
               > str_1_Cards_list([c.board_card_1th ,
                                   c.board_card_2th , 
                                   c.board_card_3th , 
                                   c.board_card_4th])[0] 
           ) : #Avoid Me_str_1_cards 10 to Ace

            shout("Bet Normal Me_str hand")
            if Max_raise_sofar() <= 3 * c.BLIND_VALUE :

                scenario(62)
                return ("raise", 3)

            else :

                scenario(63)
                return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

        elif Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_1_cards hand, 10 to Ace")
            if not did_i_raise_sofar() :

                scenario(64)
                return ("raise", 2) 

            else :

                shout("I can Bet more and better at the other sites")
                scenario(65)
                return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

        elif Me_str_2_cards() and Me_str_2_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_2_cards hand")
            if not did_i_raise_sofar() :

                scenario(66)
                return ("raise", 4) 

            elif Max_raise_sofar() <=  3 * c.BLIND_VALUE :

                scenario(67)
                return ("raise", 6) 

            else :

                scenario(68)
                return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)        

    elif River_Deside() :

        if Table_Flush_4_cards() or Table_Flush_5_cards() or Table_2_pair()\
        or Table_3_of_kinds()\
        or ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 2 )\
        or ( Me_str_2_cards() 
             and is_there_any_better_possible_1_card_straight_on_table() 
           ):

            shout("Check or Anti Bluff Bet Weak Me_str hand")

            if Max_raise_sofar() >=  6 * c.BLIND_VALUE\
            or am_i_last_player_by_seat_order() :

                scenario(69)
                return ("check")

            else :

                shout("Anti Bluff Bet")
                scenario(70)
                return ("raise", Max_raise_sofar() // c.BLIND_VALUE)    

        elif Table_Flush_3_cards() or Table_1_pair()\
        or ( Me_str_2_cards() and Me_str_2_cards_Ranking() != 1 
             and not is_there_any_better_possible_1_card_straight_on_table() 
           )\
        or ( Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 
             and Table_str_2_cards() 
             and str_2_Cards_list([c.board_card_1th ,
                                   c.board_card_2th , 
                                   c.board_card_3th , 
                                   c.board_card_4th , 
                                   c.board_card_5th])[0][0] \
               > str_1_Cards_list([c.board_card_1th , 
                                   c.board_card_2th , 
                                   c.board_card_3th , 
                                   c.board_card_4th ,
                                   c.board_card_5th])[0] 
           ): #Avoid Me_str_1_cards 10 to Ace

            shout("Normal Me_str hand")

            if not did_i_raise_at("Turn") :

                scenario(71)
                return ("raise", 3) 

            elif did_i_raise_at("Turn") and am_i_last_player_by_seat_order():

                shout("I can Bet it at the other sites")
                scenario(72)
                return ("check")

            elif did_i_raise_at("Turn")\
            and not am_i_last_player_by_seat_order():

                if Max_raise_sofar() <=  3 * c.BLIND_VALUE :
                    scenario(73)
                    return ("raise", 3) 
                else :
                    scenario(74)
                    return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

        elif Me_str_1_cards() and Me_str_1_cards_Ranking() == 1 :

            shout("Awesome Me_str_1_cards hand, 10 to Ace, Bet")
            if not did_i_raise_sofar() :

                scenario(75)
                return ("raise", 2) 

            else :

                shout("I can Bet more and better at the other sites")
                scenario(76)
                return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

        elif Me_str_2_cards() and Me_str_2_cards_Ranking() == 1 :

            shout("Bet Awesome Me_str_2_cards hand")
            if not did_i_raise_sofar() :
                scenario(77)
                return ("raise", 4) 
            elif am_i_last_player_by_seat_order() :
                if Max_raise_sofar() <= 3 * c.BLIND_VALUE :
                    scenario(78)
                    return ("raise", 6) 
                else :
                    scenario(79)
                    return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)    
            else :
                if Max_raise_sofar() <= 3 * c.BLIND_VALUE :
                    scenario(80)
                    return ("raise", 9) 
                else : 
                    scenario(81)
                    return ("raise", (4 * Max_raise_sofar()) // c.BLIND_VALUE)    


def to_play_flush():

    if not Me_Flush() or Pre_Flop_Deside() or Any_raiser_sofar():
        scenario(82)
        return False
    else:
        scenario(83)
        return True

def play_flush():
    """
    If Me_Flush() is True, functions lower than Me_full_house() like: 
    1.play_hand5_individual_or_1_pair() and 2.Play_1_pair()... 
    should return False
    """
    if Flop_Deside() :

        shout("Low bet and Raise Strategy")
        scenario(84)
        return ("raise", 3) 

    elif Turn_Deside() :

        if Me_Flush_by_4_table_cards() :

            if Me_Flush_Ranking() <= 4 :

                shout("Weak Me_Flush hand")
                scenario(85)
                return ("check")

            elif 2 <= Me_Flush_Ranking() <= 3 :

                shout("Good Me_Flush hand")

                if am_i_last_player_by_seat_order() :

                    shout("I can Bet with 2 <= Rank <= 3 at the other sites")
                    scenario(86)
                    return ("check")

                else :

                    scenario(87)
                    return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

            elif Me_Flush_Ranking() == 1 :

                shout("Awesome Me_Flush hand")

                if not did_i_raise_sofar() :

                    scenario(88)
                    return ("raise", 2) 

                elif did_i_raise_sofar() :

                    shout("Low bet and Raise Strategy")
                    scenario(89)
                    return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

        elif Me_Flush_by_3_table_cards() :

            shout("A Good or Awesome Me_Flush hand")

            if Max_raise_sofar() <= 2 * c.BLIND_VALUE :

                scenario(90)
                return ("raise", 3) 

            elif Max_raise_sofar() > 2 * c.BLIND_VALUE :

                scenario(91)
                return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)    

    elif River_Deside() :

        if Table_3_of_kinds() or Table_2_pair() :

            shout("Weak Me_Flush hand")
            scenario(92)
            return ("check")

        elif ( Me_Flush_by_4_table_cards() or Me_Flush_by_5_table_cards() ) :

            if Me_Flush_Ranking() != 1 :

                shout("Weak Me_Flush hand") 

                if did_i_raise_at("Turn")\
                and not am_i_last_player_by_seat_order():

                    shout("Anti Bluff bet")
                    scenario(93)
                    return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

                elif not did_i_raise_at("Turn")\
                or am_i_last_player_by_seat_order() :

                    shout("I can Bet with 2 <= Rank <= 3 at the other sites")
                    scenario(94)
                    return ("check")

            if Me_Flush_Ranking() == 1 :

                if Table_1_pair() :

                    shout("Good Me_Flush hand")

                    if not did_i_raise_sofar() :
                        scenario(95)
                        return ("raise", 2) 

                    elif did_i_raise_sofar() :
                        scenario(96)
                        return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

                elif not Table_1_pair() :

                    shout("Awesome Me_Flush hand")

                    if not did_i_raise_sofar() :
                        scenario(97)
                        return ("raise", 2) 

                    elif did_i_raise_sofar() :
                        scenario(98)
                        return ("raise"
                                ,(2 * Max_raise_sofar()) // c.BLIND_VALUE)    

        elif Me_Flush_by_3_table_cards() :

            if Table_1_pair() :

                shout("Good Me_Flush hand")

                if not did_i_raise_sofar() :
                    scenario(99)
                    return ("raise", 3) 

                elif did_i_raise_sofar() :
                    scenario(100)
                    return ("raise", Max_raise_sofar() // c.BLIND_VALUE)

            elif not Table_1_pair() :

                shout("A Good or Awesome Me_Flush hand")

                if Me_Flush_Ranking() != 1 :
                    scenario(101)
                    return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)    

                elif Me_Flush_Ranking() == 1 :
                    scenario(102)
                    return ("raise", (3 * Max_raise_sofar()) // c.BLIND_VALUE)    


def to_play_full_house():

    if not Me_full_house() or Pre_Flop_Deside() or Any_raiser_sofar():
        scenario(103)
        return False
    else:
        scenario(104)
        return True

def play_full_house():

    if Flop_Deside() :
        # whether I've had raised at pre flop or not i check and raise
        shout("check and raise strategy") 
        scenario(105)
        return ("check")

    elif Turn_Deside() :

        if not did_i_raise_sofar() or Max_raise_sofar() <= 1 :

            scenario(106)
            return ("raise", 4)
        else :
            scenario(107)
            return ("raise", (3 * Max_raise_sofar()) // c.BLIND_VALUE)

    elif River_Deside() :

        if Me_full_house_Ranking() == 4 :
            if am_i_last_player_by_seat_order() or not did_i_raise_at("Turn")\
            or Max_raise_sofar() >= 5 * c.BLIND_VALUE :

                scenario(108)
                return ("check")
            else :
                shout("Anti bluff raise")
                scenario(109)
                return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)

        elif not did_i_raise_sofar()\
        or Max_raise_sofar() <= 3 * c.BLIND_VALUE:

            scenario(110)
            return ("raise", 9)
        else :
            scenario(111)
            return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)


def to_play_4_of_kind():

    if not Me_4_of_kinds() or Pre_Flop_Deside() or Any_raiser_sofar():
        scenario(112)
        return False
    else:
        scenario(113)
        return True

def play_4_of_kind(): #OK

    if Flop_Deside() :

        if did_i_raise_sofar():
            shout("Low bet and raise strategy")
            scenario(114)
            return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)   
        else :
            shout("check and raise strategy")
            scenario(115)
            return ("check")

    elif Turn_Deside():

        if did_i_raise_sofar() :
            shout("Low bet and raise strategy")
            scenario(116)
            return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)
        else :
            shout("Low bet and raise strategy")
            scenario(117)
            return ("raise", 2)

    elif River_Deside() :

        if did_i_raise_sofar() :
            scenario(118)
            return ("raise", (3 * Max_raise_sofar()) // c.BLIND_VALUE)
        else :
            scenario(119)
            return ("raise", 4)


def to_play_pocket_pair(): # Later check if a case is missed or not at River.
    # hand4() or hand3() or hand2() or hand1()
    if not Me_pocket_pair() or Pre_Flop_Deside() or Any_raiser_sofar()\
    or Me_str() or Me_Flush():
        scenario(120)
        return False
    else :
        scenario(121)
        return True

def play_pocket_pair(): # Later check if a case is missed or not at River.
    # hand4() or hand3() or hand2() or hand1()
    if Flop_Deside():

        if Table_3_of_kinds():
            if hand4():
                scenario(122)
                return ("raise", 3)
            elif hand3():
                scenario(123)
                return ("raise", 3) # hand 3:7 DONE
            elif hand2():
                scenario(124)
                return ("raise", 4) # hand 2:7 DONE
            elif hand1():
                scenario(125)
                return ("raise", 5) # hand 1:7 DONE

        elif cards_ranking(c.my_1th_card) == 1:
            if hand4():
                scenario(126)
                return ("raise", 2)
            elif hand3():
                scenario(127)
                return ("raise", 3) # hand 3:8 DONE
            elif hand2():
                scenario(128)
                return ("raise", 4) # hand 2:8 DONE
            elif hand1():
                scenario(129)
                return ("raise", 5) # hand 1:8 DONE

        elif cards_ranking(c.my_1th_card) > 1:
            scenario(130)
            return ("check")

    elif Turn_Deside():

        if Table_3_of_kinds() and Me_pocket_pair_Ranking() == 1:

            if hand4():
                scenario(131)
                return ("raise", 3)
            elif hand3():
                scenario(132)
                return ("raise", 3) # hand 3:9 DONE
            elif hand2():
                scenario(133)
                return ("raise", 4) # hand 2:9 DONE
            elif hand1():
                scenario(134)
                return ("raise", 5) # hand 1:9 DONE

        # hand 1:9.1 DONE
        elif Table_4_of_kinds():
            if n(c.my_1th_card) == 14 or \
            ( n(c.my_1th_card) == 13 and n(c.board_card_1th) == 14 ):

            scenario(135)
            return ("raise", 5)

        elif Table_3_of_kinds() or Table_4_of_kinds() \
        or cards_ranking(c.my_1th_card) > 1:

            scenario(136)
            return ("check")

        elif cards_ranking(c.my_1th_card) == 1:

            if hand4():
                scenario(137)
                return ("raise", 2)

            elif hand3():
                scenario(138)
                return ("raise", 3) # hand 3:10 DONE

            elif hand2(): 
                # hand 2:10 DONE
                if am_i_last_player_by_seat_order():
                    scenario(139)
                    return ("raise", 6)
                else:
                    scenario(140)
                    return ("raise", 4)

            elif hand1():
                # hand 1:10 DONE
                if am_i_last_player_by_seat_order():
                    scenario(141)
                    return ("raise", 7)
                else:
                    scenario(142)
                    return ("raise", 5)

    elif River_Deside():
        # Later check if a case is missed or not.
        if Table_4_of_kinds():
            if n(c.my_1th_card) == 14 or \
            ( n(c.my_1th_card) == 13 and n(c.board_card_1th) == 14 ):

                scenario(143)
                return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)

            else:
                scenario(144)
                return ("check")

        elif Table_3_of_kinds() and (Me_pocket_pair_Ranking() == 1
                                   or am_i_last_player_by_seat_order() ):
            scenario(145)
            return ("check")

        elif not Table_3_of_kinds() and (cards_ranking() > 1
                                     or am_i_last_player_by_seat_order()):
            scenario(146)
            return ("check")

        elif Me_pocket_pair_Ranking() == 1\
        and not am_i_last_player_by_seat_order() and Table_3_of_kinds():

            if hand4():
                scenario(147)
                return ("raise", 3)
            elif hand3():
                scenario(148)
                return ("raise", 3) # hand 3:12 DONE
            elif hand2():
                scenario(149)
                return ("raise", 4) # hand 2:12 DONE
            elif hand1():
                scenario(150)
                return ("raise", 5) # hand 1:12 DONE

        elif Me_pocket_pair_Ranking() == 1\
        and not am_i_last_player_by_seat_order():

            if ( Table_Flush_4_cards() or Table_Flush_5_cards()
                 or Table_str_1_cards_Number() == 2):

                shout("Anti bluff raise")

                if hand4():
                    scenario(151)
                    return ("raise", 2)
                elif hand3():
                    scenario(152)
                    return ("raise", 3) # hand 3:13 DONE
                elif hand2():
                    scenario(153)
                    return ("raise", 4) # hand 2:13 DONE
                elif hand1():
                    scenario(154)
                    return ("raise", 5) # hand 1:13 DONE

            else:

                if hand4():
                    scenario(155)
                    return ("raise", 2)
                elif hand3():
                    scenario(156)
                    return ("raise", 3) # hand 3:14 DONE
                elif hand2():
                    scenario(157)
                    return ("raise", 4) # hand 2:14 DONE
                elif hand1():
                    scenario(158)
                    return ("raise", 5) # hand 1:14 DONE


def to_play_pocket_3_of_kinds():
    # hand4() or hand3() or hand2() or hand1()
    if not Me_pocket_3_of_kinds() or Pre_Flop_Deside() or Any_raiser_sofar()\
    or Me_str() or Me_Flush():
        scenario(159)
        return False
    else:
        scenario(160)
        return True

def play_pocket_3_of_kinds():
    # hand4() or hand3() or hand2() or hand1()
    if Flop_Deside():

        if hand4():
            scenario(161)
            return ("raise", 4)
        else:
            shout("Low bet and re raise strategy")
            if hand3():
                scenario(162)
                return ("raise", 4) # hand 3:6 DONE
            elif hand2():
                scenario(163)
                return ("raise", 4) # hand 2:6 DONE
            elif hand1():
                scenario(164)
                return ("raise", 4) # hand 1:6 DONE

    elif Turn_Deside():

        if ( Table_Flush_4_cards() or Table_str_1_cards_Number() == 2 ):

            if not did_i_raise_at("Flop")\
            or am_i_last_player_by_seat_order():

                scenario(165)
                return("check")

            elif did_i_raise_at("Flop"):

                shout("Anti bluff raise")
                scenario(166)
                return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE) 

        else:

            scenario(167)
            return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)

    elif River_Deside():

        if Table_4_of_kinds():
            scenario(168)
            return ("check")

        elif ( Table_Flush_4_cards() or Table_Flush_5_cards()
               or Table_str_1_cards_Number() == 2):

            if not did_i_raise_at("Turn") or (did_i_raise_at("Turn")
                                    and am_i_last_player_by_seat_order()):
                scenario(169)
                return ("check")

            elif (did_i_raise_at("Turn")
                  and not am_i_last_player_by_seat_order() ):

                if Max_raise_sofar() >= 8 * c.BLIND_VALUE :

                    scenario(170)
                    return("check")

                else:

                    shout("Anti bluff raise")
                    scenario(171)
                    return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)

        else:

            if ( Table_str_1_cards() or Table_str_2_cards_Number() >= 2
                 or Table_Flush() ):

                if Max_raise_sofar() >= 8 * c.BLIND_VALUE :

                    scenario(172)
                    return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)

                else:

                    scenario(173)
                    return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)

            else:

                scenario(174)
                return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)


def to_play_pocket_full_house():
    # hand4() or hand3() or hand2() or hand1()
    if not Me_pocket_full_house() or Pre_Flop_Deside() or Any_raiser_sofar():
        scenario(175)
        return False
    else:
        scenario(176)
        return True

def play_pocket_full_house():
    # hand4() or hand3() or hand2() or hand1()
    if Flop_Deside():

        if Me_pocket_full_house_Ranking() == 2:

            if hand4():
                scenario(177)
                return ("raise", 4)
            else:
                shout("Low bet and re raise strategy")
                if hand3():
                    scenario(178)
                    return ("raise", 4) # hand 3:6 DONE
                elif hand2():
                    scenario(179)
                    return ("raise", 4) # hand 2:6 DONE
                elif hand1():
                    scenario(180)
                    return ("raise", 4) # hand 1:6 DONE

        if Me_pocket_full_house_Ranking() == 1:
            shout("Check and raise strategy")
            scenario(181)
            return ("check")

    elif Turn_Deside():

        if Me_pocket_full_house_Ranking() in (3, 4):
            shout("Check weak pocket full house")
            scenario(182)
            return ("check")

        else:
            scenario(183)
            return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)

    elif River_Deside():

        if Me_pocket_full_house_Ranking() in (3, 4):

            if am_i_last_player_by_seat_order()\
            or Max_raise_sofar() > 4 * c.BLIND_VALUE :

                scenario(184)
                return("check")

            else:

                shout("Anti bluff raise")
                scenario(185)
                return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)

        elif Me_pocket_full_house_Ranking() == 2:

            if Max_raise_sofar() >= 8 * c.BLIND_VALUE :

                scenario(186)
                return ("raise", (Max_raise_sofar()) // c.BLIND_VALUE)

            else:

                scenario(187)
                return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)

        elif Me_pocket_full_house_Ranking() == 1:

            scenario(188)
            return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)


def to_play_pocket_4_of_kinds():
    # hand4() or hand3() or hand2() or hand1()
    if not Me_pocket_4_of_kinds() or Pre_Flop_Deside() or Any_raiser_sofar():
        scenario(189)
        return False
    else:
        scenario(190)
        return True

def play_pocket_4_of_kinds():
    # hand4() or hand3() or hand2() or hand1()
    if Flop_Deside():

        shout("Check and raise strategy")
        scenario(191)
        return ("check")

    elif Turn_Deside():

        scenario(192)
        return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)

    elif River_Deside():

        scenario(193)
        return ("raise", (2 * Max_raise_sofar()) // c.BLIND_VALUE)


def to_play_pre_flop():

    if not Pre_Flop_Deside() or Any_raiser_sofar():
        scenario(194)
        return False
    else:
        scenario(195)
        return True

def play_pre_flop(): # handbook and script are same

    if hand4():
        scenario(196)
        return ("raise", 2)

    elif hand3():
        scenario(197)
        return ("raise", 3) # hand 3:2 DONE

    elif hand2():
        scenario(198)
        return ("raise", 4) # hand 2:2 DONE

    elif hand1():
        scenario(199)
        return ("raise", 5)        

    elif hand5():
        scenario(200)
        return ("raise", 3)

    elif c.small_blind_seat == c.my_seat_number :
        if hand7():
            scenario(201)
            return ("fold")
        else:
            scenario(202)
            return ("call")

    elif c.big_blind_seat == c.my_seat_number :
        scenario(203)
        return ("check")

    else :
        if hand6():
            scenario(204)
            return ("call")
        else:
            scenario(205)
            return ("fold")


def to_play_pre_flop_raised(): # handbook and script are same

    if not Pre_Flop_Deside() or not Any_raiser_sofar():
        scenario(206)
        return False
    else:
        scenario(207)
        return True

def play_pre_flop_raised(): # handbook and script are same

    if hand4():

        if not did_i_raise_at("Pre_Flop") \
        and last_raise_at("Pre_Flop") <= 5 * c.BLIND_VALUE :

            scenario(208)
            return ("call") 
        elif did_i_raise_at("Pre_Flop") \
        and last_raise_at("Pre_Flop") <= 6 * c.BLIND_VALUE :

            scenario(209)
            return ("call")

        else:
            scenario(210)
            return ("fold")

    elif hand3():

        # hand 3:3 DONE
        if not did_i_raise_at("Pre_Flop") \
        and last_raise_at("Pre_Flop") <= 6 * c.BLIND_VALUE :

            scenario(211)
            return ("call") 
        # hand 3:4 3:5 DONE
        elif did_i_raise_at("Pre_Flop") \
        and (  (number_of_raisers_at("Pre_Flop") == 1
                and last_raise_at("Pre_Flop") <= 7.5 * c.BLIND_VALUE )
             or
               (number_of_raisers_at("Pre_Flop") > 1
                and last_raise_at("Pre_Flop") <= 9.5 * c.BLIND_VALUE )
            ):

            scenario(212)
            return ("call")

        else:
            scenario(213)
            return ("fold")

    elif hand2():
        # hand 2:2.1 DONE
        if last_raise_at("Pre_Flop") <= 3 * c.BLIND_VALUE :
            scenario(214)
            return ("raise", 5)
        # hand 2:3 DONE
        elif not did_i_raise_at("Pre_Flop") \
        and (  (number_of_raisers_at("Pre_Flop") == 1
                and last_raise_at("Pre_Flop") <= 7 * c.BLIND_VALUE )
             or
               (number_of_raisers_at("Pre_Flop") > 1
                and last_raise_at("Pre_Flop") <= 9.5 * c.BLIND_VALUE )
            ):

            scenario(215)
            return ("call") 
        # hand 2:4 2:5 DONE
        elif did_i_raise_at("Pre_Flop") \
        and (  (number_of_raisers_at("Pre_Flop") == 1
                and last_raise_at("Pre_Flop") <= 9.5 * c.BLIND_VALUE )
             or
               (number_of_raisers_at("Pre_Flop") > 1
                and last_raise_at("Pre_Flop") <= 10.5 * c.BLIND_VALUE )
            ):

            scenario(216)
            return ("call")

        else:
            scenario(217)
            return ("fold")

    elif hand1():
        # Some functions are not defined, 
        # so I skip this if statment for now.

        #if (did_player_all_in_at_seat() == True or
        #    did_player_semi_all_in_at_seat() == True)\
        #and number_of_players_in() >= 3 \
        #and is_there_a_player_between_me_and_last_raiser() \
        #and Max_raise_sofar() >= 5 * c.BLIND_VALUE :
        #
        #    return ("call")
        #else:
        #    return ("raise", (2.5 * Max_raise_sofar()) // c.BLIND_VALUE)

        scenario(218)
        return ("raise", (2.5 * Max_raise_sofar()) // c.BLIND_VALUE)

    # 'AKs', 'AQs', 'AJs', 'AKo'
    elif holdem_starting_hand_ranking() in (8, 10, 11, 12)\
    and Max_raise_sofar() <= 4 * c.BLIND_VALUE:

        scenario(219)
        return ("call")

    elif hand5():

        if ( not did_i_raise_at("Pre_Flop") 
             and Max_raise_sofar() > 3.5 * c.BLIND_VALUE 
           )\
        or ( did_i_raise_at("Pre_Flop")
             and Max_raise_sofar() >= 5 * c.BLIND_VALUE
           ):

            scenario(220)
            return ("fold")
        else:
            scenario(221)
            return ("call")

    elif c.small_blind_seat == c.my_seat_number and hand9()\
    and Max_raise_sofar() < 2.5 * c.BLIND_VALUE:

        shout("Anti Bluff call. Defending pre flop blind")
        scenario(222)
        return ("call")

    elif c.big_blind_seat == c.my_seat_number and hand8()\
    and Max_raise_sofar() < 2.5 * c.BLIND_VALUE:

        shout("Anti Bluff call. Defending pre flop blind")
        scenario(223)
        return("call")

    else:
        scenario(224)
        return("fold")




#def play_flop_raised(): # write it in paper and then define it here
#
#def play_turn_raised(): # write it in paper and then define it here
#
#def play_river_raised(): # write it in paper and then define it here
#
#
#def overall_full_house(): # define it 1.here or 2.at supporting function(need to import FUNCTIONS_Pair file) or 3.define at FUNCTIONS_Pair file. NUMBER 3 IS THE BEST ANSWER
#
#def overall_4_of_kind(): # define it 1.here or 2.at supporting function(need to import FUNCTIONS_Pair file) or 3.define at FUNCTIONS_Pair file. NUMBER 3 IS THE BEST ANSWER
#it seemes there is no need to define functions overall_full_house() and overall_4_of_kind() at all (2019)
