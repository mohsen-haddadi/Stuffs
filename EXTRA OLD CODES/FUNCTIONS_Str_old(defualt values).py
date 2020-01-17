from FUNCTIONS_Str_Flush_Pairs import *

def Table_str_1_cards( List=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th

    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen table_str_1_cards")

    if len(str_1_Cards_list( table_cards_list )) == 0 :
        return False
    else :
        return True

def Table_str_2_cards( List=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th

    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen table_str_2_cards")

    if len(str_2_Cards_list( table_cards_list )) == 0 :
        return False
    else :
        return True

def Table_str_1_cards_Number( List=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th

    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen table_str_1_cards_Number")

    return len(str_1_Cards_list( table_cards_list )) 

def Table_str_2_cards_Number( List=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th

    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen table_str_2_cards_Number")

    return len(str_2_Cards_list( table_cards_list )) 


def Str_1_cards( List=None , My_1th_Card_var=None , My_2th_Card_var=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ,\
           My_1th_Card , My_2th_Card

    if My_1th_Card_var != None and My_2th_Card_var != None :
        My_1th_Card = My_1th_Card_var
        My_2th_Card = My_2th_Card_var
    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen str_1_cards")

    for i in str_1_Cards_list( table_cards_list ) :
        if n(My_1th_Card) == i or n(My_2th_Card) == i :
            return True
        if n(My_1th_Card) == 14 :
            if 1 == i or n(My_2th_Card) == i :
                return True
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) == i or 1 == i :
                return True   
     
    return False

def Str_2_cards( List=None , My_1th_Card_var=None , My_2th_Card_var=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ,\
           My_1th_Card , My_2th_Card

    if My_1th_Card_var != None and My_2th_Card_var != None :
        My_1th_Card = My_1th_Card_var
        My_2th_Card = My_2th_Card_var
    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen str_2_cards")

    if n(My_1th_Card) == n(My_2th_Card):
        return False
    for i in str_2_Cards_list( table_cards_list ) :
        if n(My_1th_Card) in i and n(My_2th_Card) in i :
            return True
        if n(My_1th_Card) == 14 :
            if 1 in i and n(My_2th_Card) in i :
                return True
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) in i and 1 in i :
                return True   
    return False


def Str_1_cards_Ranking( List=None , My_1th_Card_var=None , My_2th_Card_var=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ,\
           My_1th_Card , My_2th_Card

    if My_1th_Card_var != None and My_2th_Card_var != None :
        My_1th_Card = My_1th_Card_var
        My_2th_Card = My_2th_Card_var
    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen str_1_cards_Ranking")

    rank = 0
    for i in str_1_Cards_list( table_cards_list ) :
        rank += 1
        if n(My_1th_Card) == i or n(My_2th_Card) == i :
            return rank
        if n(My_1th_Card) == 14 :
            if 1 == i or n(My_2th_Card) == i :
                return rank
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) == i or 1 == i :
                return rank    

      
def Str_2_cards_Ranking( List=None , My_1th_Card_var=None , My_2th_Card_var=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ,\
           My_1th_Card , My_2th_Card

    if My_1th_Card_var != None and My_2th_Card_var != None :
        My_1th_Card = My_1th_Card_var
        My_2th_Card = My_2th_Card_var
    if List != None :
        table_cards_list = List
    elif Pre_Flop1_Deside :
        return None
    elif Flop1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th ]
    elif Turn1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th ]
    elif River1_Deside :
        table_cards_list = [ Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ]
    else :
        print("This can not happen str_2_cards_Ranking")

    if n(My_1th_Card) == n(My_2th_Card):
        return None
    rank = 0
    for i in str_2_Cards_list( table_cards_list ) :
        rank += 1
        if n(My_1th_Card) in i and n(My_2th_Card) in i :
            return rank
        if n(My_1th_Card) == 14 :
            if 1 in i and n(My_2th_Card) in i :
                return rank
        if n(My_2th_Card) == 14 :
            if n(My_1th_Card) in i and 1 in i :
                return rank


def Str( List=None , My_1th_Card_var=None , My_2th_Card_var=None ):
    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th ,\
           My_1th_Card , My_2th_Card

    if My_1th_Card_var != None and My_2th_Card_var != None :
        My_1th_Card = My_1th_Card_var
        My_2th_Card = My_2th_Card_var

    if Str_2_cards( List ) == True or Str_1_cards( List ) == True :
        return True
    else:
        return False


def Is_above_str_1_card( List=None , My_1th_Card_var=None , My_2th_Card_var=None ):

    global Pre_Flop1_Deside , Flop1_Deside , Turn1_Deside , River1_Deside ,\
           Card_1th , Card_2th , Card_3th , Card_4th , Card_5th,\
           My_1th_Card , My_2th_Card

    if My_1th_Card_var != None and My_2th_Card_var != None :
        My_1th_Card = My_1th_Card_var
        My_2th_Card = My_2th_Card_var

    if Table_str_1_cards( List ) == False :
        return False
    elif Str_2_cards( List ) == False :
        return True
    elif max(My_1th_Card,My_2th_Card) <= str_1_Cards_list( List )[0] :
        return True
    else :
        return False







    
    
