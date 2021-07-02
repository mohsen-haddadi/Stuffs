#OK
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.ocr.ocr as ocr
import configs as c
from iprint import shout
from readability.fix_game_disruption import fix_game_disruption, set_just_do_check_fold_to_true, screenshot_error

def replace_letters_comma_space_m_k(ocr_string):
    string = ocr_string
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("M","*1000000")
    string = string.replace("K","*1000")
    return string

# If there is no script to ocr, ocr functions at ocr module
# will return empty string '', not None.
def ocr_my_bet():
    """
    my bet number on bet button
    If ocr fails this function will uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    
    ocr_string = ocr.ocr_my_bet_to_string(c.game_position)
    shout("my bet ocr string is: %s" %ocr_string)
    eval_string = replace_letters_comma_space_m_k(ocr_string)
    digit_string = eval_string.replace("*","")

    if digit_string.isdigit():
        return eval(eval_string)
    # else include digit_string like: '', 'c540!'
    else :
        fix_game_disruption("ocr_my_bet is not digit")
        ocr_string = ocr.ocr_my_bet_to_string(c.game_position)
        shout("my bet ocr string is: %s" %ocr_string)
        eval_string = replace_letters_comma_space_m_k(ocr_string)
        digit_string = eval_string.replace("*","")

        if digit_string.isdigit():
            return eval(eval_string)
        else:
            set_just_do_check_fold_to_true("ocr_bet is not digit")            
            screenshot_error("ocr_bet is not digit")
            return None  

def ocr_bet(seat, printing = True):
    """
    If ocr fails this function will uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
 
    ocr_string = ocr.ocr_bet_to_string(c.game_position, seat)
    if printing:
        shout("bet ocr string at seat %s is: %s" %(seat, ocr_string))
    eval_string = replace_letters_comma_space_m_k(ocr_string)
    digit_string = eval_string.replace("*","")

    if digit_string.isdigit():
        return eval(eval_string)
    # else include digit_string like: '', 'c540!'
    else :
        fix_game_disruption("ocr_bet is not digit at seat %s" %seat)
        ocr_string = ocr.ocr_bet_to_string(c.game_position, seat)
        if printing:
            shout("bet ocr string at seat %s is: %s" %(seat, ocr_string))
        eval_string = replace_letters_comma_space_m_k(ocr_string)
        digit_string = eval_string.replace("*","")

        if digit_string.isdigit():
            return eval(eval_string)
        else:
            set_just_do_check_fold_to_true("ocr_bet is not digit")            
            screenshot_error("ocr_bet is not digit at seat %s" %seat)
            return None            

def ocr_other_players_bank(seat):
    """
    If ocr fails this function will uses:
    (will use nothing)
    Will not uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    #global my_seat_number , MY_PROFILE_NAME , bot_status , just_do_check_fold

    ocr_string = ocr.ocr_other_players_bank_to_string(c.game_position, seat)
    shout("other players bank ocr string at seat %s is: %s" 
          %(seat, ocr_string))
    eval_string = replace_letters_comma_space_m_k(ocr_string)
    digit_string = eval_string.replace("*","")
    if digit_string.isdigit():
        return eval(eval_string)
    # else include digit_string like: '', 'c540!'
    else:
        shout("ocr_other_players_bank is not digit and set to None at seat %s"
              %seat )
        return None

def ocr_my_bank():
    """
    If ocr fails this function will uses:
    1. fix_game_disruption()
    Will not uses:
    1. set_just_do_check_fold_to_true()
    """
    #global my_seat_number , MY_PROFILE_NAME , bot_status , just_do_check_fold

    ocr_string = ocr.ocr_my_bank_to_string(c.game_position, c.my_seat_number)
    shout("my bank ocr string at seat %s is: %s"%(c.my_seat_number, ocr_string))
    eval_string = replace_letters_comma_space_m_k(ocr_string)
    digit_string = eval_string.replace("*","")

    if digit_string.isdigit():
        return eval(eval_string)
    # else include digit_string like: '', 'c540!'
    else :
        fix_game_disruption("ocr_my_bank is not digit at seat %s" 
                            %c.my_seat_number)
        ocr_string = ocr.ocr_my_bank_to_string(c.game_position, c.my_seat_number)
        shout("my bank ocr string at seat %s is: %s" 
              %(c.my_seat_number, ocr_string))
        eval_string = replace_letters_comma_space_m_k(ocr_string)
        digit_string = eval_string.replace("*","")

        if digit_string.isdigit():
            return eval(eval_string)
        else:           
            screenshot_error("ocr_my_bank is not digit at seat %s"
                             %c.my_seat_number)
            return None            

def ocr_other_names(seat): #💊
    """
    If ocr fails this function will uses:
    (will use nothing)
    Will not uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    string = ocr.ocr_other_names_to_string(c.game_position, seat)
    shout("other name ocr string at seat %s is: %s" %(seat, string) )
    if string == '': #💊
        return None
    else:
        return string

def ocr_my_name(): #💊
    """
    If ocr fails this function will uses:
    (will use nothing)
    Will not uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    string = ocr.ocr_my_name_to_string(c.game_position, c.my_seat_number)
    shout("my name ocr string at seat %s is: %s" %(c.my_seat_number, string))
    return string
