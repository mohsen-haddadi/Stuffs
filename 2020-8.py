import time, os
from datetime import datetime
import pyautogui, pygame, win32gui, win32con
import screen_monitoring.find_game_position.find_game_position as find_game_position
import screen_monitoring.pixel_matching.pixel_matching as pm
import decision_making.decide
#importing same level directory modules
import config
from iprint import shout
from readability_then_read_cards import read_and_global_my_cards,\
read_and_global_flop_cards, read_and_global_turn_card,\
read_and_global_river_card
from readability_then_ocr import ocr_my_bank
from readability_then_click import fold, check, call, all_in,\
raising, check_fold
from set_variables import set_all_variables_to_none,\
determine_small_blind_seat, determine_big_blind_seat, determine_dealer_seat,\
reset_just_do_check_fold_to_false, read_and_global_banks_and_names,\
reset_table_information, red_chips, read_and_save_bets
from fix_game_disruption import fix_game_disruption,\
set_just_do_check_fold_to_true, screenshot_error

def create_file_directories():
    
    config.DATED_REPORT_FOLDER = datetime.now().strftime("%Y.%m.%d %A %H.%M.%S")
    config.REPORTS_DIRECTORY = "Reports/%s" %config.DATED_REPORT_FOLDER
    if not os.path.exists( config.REPORTS_DIRECTORY ):
        os.makedirs( config.REPORTS_DIRECTORY )

pygame.mixer.init() #Check later if i can move this line to first line of sound() function or not.
def sound(string_name) :
    try :
        pygame.mixer.music.load( os.path.join('Sounds' ,
                                              "%s.wav" %string_name ) )
        return pygame.mixer.music.play()
    except :
        pass

def play_sound() :
    global preflop_stage , flop_stage , turn_stage , river_stage  , my_1th_card , my_2th_card
    load_variables()

    if preflop_stage == True and flop_stage == False :
        if hand1() :
            sound("Michel")
            shout("Playing Music: 'Michel'", color = 'light_cyan')
        elif hand2() :
            sound("Alan Walker")
            shout("Playing Music: 'Alan Walker'", color = 'light_cyan')
        elif hand3() :
            sound("Alan Walker")
            shout("Playing Music: 'Alan Walker'", color = 'light_cyan')
        elif hand4() :
            sound("Pocket low pairs")
            shout("Playing Music: 'Pocket low pairs'", color = 'light_cyan')
        elif hand5() :
            sound("Bob Marley")
            shout("Playing Music: 'Bob Marley'", color = 'light_cyan')


"""
Using 'if' line at below is a MUST, bescause while importing main file from the other files,
2 diffrent DATED_REPORT_FOLDER with diffrent times will be created for each file and therefore shoutings from each file will be save in seperated files. 
So i should put DATED_REPORT_FOLDER variable in load_variables() and save_variables() too.
"""
if __name__ == '__main__':
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)

    config.set_all_variables_to_none()
    create_file_directories()
    #shout("Hello Kitty", color = 'rainbow')

# FUNCTIONS_Pixel-Maching ---------------------------------------------------------------------------------------------

def sb_b_d_buttons_are_founded():
    global game_position
    load_variables()

    small_blind_button_founded, big_blind_button_founded, dealer_button_founded = (False, False, False)
    for seat in [1,2,3,4,5]:
        if pm.small_blind_pixel(game_position, seat) == True:
            small_blind_button_founded = True
            break
    for seat in [1,2,3,4,5]:
        if pm.big_blind_pixel(game_position, seat) == True:
            big_blind_button_founded = True
            break
    for seat in [1,2,3,4,5]:
        if pm.dealer_pixel(game_position, seat) == True:
            dealer_button_founded = True
            break
    return small_blind_button_founded and big_blind_button_founded and dealer_button_founded

def declare_the_winners():
    global game_position
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.my_seat_won_pixel(game_position, seat) == True:
            shout("I won the game!", color = 'on_light_magenta')
        if pm.other_seat_won_pixel(game_position, seat) == True :
            shout("Seat %s won the game!" %seat)

def is_there_any_raiser():
    """ Except me """
    global my_seat_number
    
    for seat in range(1,6):
        if seat == my_seat_number :
            continue
        elif red_chips(seat) :
            return True
    return False

def hand_is_ended():
    global game_position
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.my_seat_won_pixel(game_position, seat):
            return True
        if pm.other_seat_won_pixel(game_position, seat):
            return True
    return False
            
def click_decision():

    decision = decision_making.decide.decide()
    if decision[0] == "check" :
        check()
    elif decision[0] == "call" :
        call()
    elif decision[0] == "fold" :
        fold()
    elif decision[0] == "raise" :
        raising(decision[1] * BLIND_VALUE)
    elif decision[0] == "all_in" :
        all_in()
    elif decision[0] == "check_fold" :
        check_fold()
    elif decision[0] == "not defined" :
        screenshot_error("decide function deficiency")
        check_fold()
    elif decision == None:
        screenshot_error("A play function returned None")
        check_fold()
    else :
        screenshot_error("returned string is not in standard format")
        check_fold()
    time.sleep(1)


if __name__ == '__main__':

    # first line values: ----------------------
    MY_PROFILE_NAME = "XXX"
    if input("Is My Name: %s ?(Enter:yes/any keyword:no)"%MY_PROFILE_NAME) != "" :
        MY_PROFILE_NAME = input("Enter Profile Name: ")
    my_seat_number = int( input("My seat number? ") )
    waiting_for_first_hand = True # will be omitted (None,True,False)
    just_do_check_fold = False
    BLIND_VALUE = 100000000
    players_name = {}
    players_bank = {}
    white_chips_cache = {} ; red_chips_cache = {} ; player_cards_cache = {} ; bets_cache = {} 
    # check later if reseting dictionaries in reset_table_info function works fine, do not repeat them here
    # first line values Ended -----------------


    game_position = find_game_position.find_game_reference_point()


while True :

    preflop_stage = False ; flop_stage = False ; turn_stage = False ; river_stage = False 

#    if waiting_for_first_hand == True :
#
#        shout("****** Running waiting_for_first_hand == True Section ******"
#              , color = 'on_green')
#        reset_just_do_check_fold_to_false() #
#
#        reset_table_information() #
#
#        if pm.my_seat_won_pixel(game_position,  my_seat_number ) == False :
#            My_Bank = ocr_my_bank(game_position, my_seat_number )
#            if My_Bank != None :
#                if My_Bank >= 15 * BLIND_VALUE :
#                    shout("My Bank is:%s" %My_Bank, color = 'light_green')
#                elif My_Bank != 0 :
#                    shout("My Bank is:%s" %My_Bank, color = 'light_green')
#                    shout("Rebuying...")
#                    pass # Later i'll build
#        else :
#            shout("My Bank can't be read")
#            My_Bank = None
#        
#        Hand_End_Cheker1 = hand_is_ended()
#        while Hand_End_Cheker1 :
#            Hand_End_Cheker1 = hand_is_ended()
#
#        if pm.active_player_pixel(game_position, my_seat_number) != True \
#        or ( pm.active_player_pixel(game_position, my_seat_number) == True \
#            and pm.notification_banner_pixel(game_position, my_seat_number) == True ):
#            read_and_global_banks_and_names() 
#        else :
#            shout("Players Info is not Read", color = 'on_light_red')
#
#
#
#
#
#        time02 = 0 ; fo = 0 
#        time1 = time.time()
#        Cards1 = False
#        shout("Looking for cards in waiting_for_first_hand == True Section..."
#              , color = 'light_magenta')
#        while Cards1 == False and time02 < 5 * 60 : #being alone time
#            Cards1 = pm.player_cards_pixel(game_position,  my_seat_number )
#            time2 = time.time() - time1
#            n60 = ( time2 - 120 ) // 60
#            if not time2 < 2 * 60 and n60 >= fo :
#                fix_game_disruption("1")
#                fo += 1
#                time02 = time.time() - time1                
#
#        if not time02 < 5 * 60 : #being alone time
#            raise Exception("0.1.No one join, time to exit. Or Game is locked, force to restart(will be build in future), waiting_for_first_hand == None")
#
#
#
#
#
#
#        if Cards1 == True :
#            if pm.pre_flop_pixel(game_position) == False or ( pm.pre_flop_pixel(game_position) == True and is_there_any_raiser() == True) :
#                set_just_do_check_fold_to_true("this is Ok! Becuase i may start program from middle of the game")
#
#            waiting_for_first_hand = False
#            shout("Cards are founded", color = 'light_magenta')
#            shout ("****** First hand Started ******", color = 'on_green')
#
#
#    elif waiting_for_first_hand == None :
#        raise Exception("5.This can not happen IN FUTURE becuase main menu automation is built\
#                        ( fix_game_disruption --> Sit_In --> table is full --> exit -->\
#                        waiting_for_first_hand = None --> main menu --> waiting_for_first_hand = True )")
#


#-------    

    if Hand_End_Cheker1 == False and pm.pre_flop_pixel(game_position) == False \
    and waiting_for_first_hand == False and just_do_check_fold != True :
        fix_game_disruption("2")
        set_just_do_check_fold_to_true("2")
        screenshot_error('6. pm.pre_flop_pixel() == False')
    elif Hand_End_Cheker1 == False and waiting_for_first_hand == False and just_do_check_fold != True :
        Pre_Flop1 = True #(2020: Pre_Flop1 has no usage)
        preflop_stage = True

    if Hand_End_Cheker1 == False and pm.player_cards_pixel(game_position,  my_seat_number ) == True and waiting_for_first_hand == False :  
        read_and_global_my_cards() #
        play_sound() #


    its_my_turn = False
    Gray1 = True ; fo = 0 
    time1 = time.time()
    shout("Looking for light...", color = 'light_magenta') 
    while Hand_End_Cheker1 == False and (its_my_turn == False or Gray1 == True) and flop_stage == False and waiting_for_first_hand == False and time.time() - time1 < 5 * 60 :
        if pm.button_pixel(game_position, 'i_am_back') :
            fix_game_disruption("2.5 I am back Button is True")
        Hand_End_Cheker1 = hand_is_ended()
        its_my_turn = pm.active_player_pixel(game_position,  my_seat_number )
        Gray1 = pm.notification_banner_pixel(game_position,  my_seat_number )
        flop_stage = pm.flop_pixel(game_position)
        n20 = (time.time() - time1 - 60 ) // 20
        if time.time() - time1 > 1 * 60 and n20 >= fo :
            fix_game_disruption("3")
            fo += 1
            
    if not time.time() - time1 < 5 * 60 :
        raise Exception("5.1.Game is locked, force to restart, waiting_for_first_hand == None")

    if flop_stage == True :
        set_just_do_check_fold_to_true("1.5")
        screenshot_error("6.5 Pre Flop is Jumped, game must lagged")
        
         
    preflop_betting_round = 0 #(2018) shouldn't it be -1 ?! test it by printing for example player_cards_cache dic which prints rounds too
    if pm.active_player_pixel(game_position,  my_seat_number ) == True and Gray1 == False and hand_is_ended() == False and flop_stage == False and waiting_for_first_hand == False :
        preflop_betting_round += 1
        shout("light is founded", color = 'light_magenta')
        read_and_save_bets() #
        click_decision() # preflop
    elif hand_is_ended() == False and flop_stage == False and waiting_for_first_hand == False :
        fix_game_disruption("4 Entering This section is not possible")
        screenshot_error("6.6 Entering This section is not possible")
        #(2018) shouldn't preflop_betting_round += 1 line be here too ?!
        read_and_save_bets() #
        click_decision() # preflop



# PreFlop: -------


    if waiting_for_first_hand == False :

        shout("Running PreFlop Section")
        time01 = time.time()
        time02 = time.time() - time01
        
        while Hand_End_Cheker1 == False and flop_stage == False and time02 < 5 * 60 and waiting_for_first_hand == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            its_my_turn = False ; Flop1 = False ; fo = 0
            shout("Looking for Next sign...", color = 'light_magenta')
            while Hand_End_Cheker1 == False and its_my_turn == False and Flop1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    game_position = find_game_position.find_game_reference_point()
                    fo = 1
                if pm.button_pixel(game_position, 'i_am_back') :
                    fix_game_disruption("4.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  my_seat_number )
                Flop1 = pm.flop_pixel(game_position)
                time2 = time.time() - time1
                    
            if not time2 < 1 * 60 :
                fix_game_disruption("5")

            if Hand_End_Cheker1 == False :

                if its_my_turn == True and Flop1 == False :
                    preflop_betting_round += 1
                    shout("light is founded", color = 'light_magenta')
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # preflop
                    elif just_do_check_fold != True :
                        set_just_do_check_fold_to_true("3")
                        screenshot_error("7.Red should be True here, check later why this happens")
                        read_and_save_bets() #
                        click_decision() # preflop
                        
                if Flop1 == True :
                    flop_stage = True
                    shout("Reading Flop Cards...", color = 'light_magenta')
                    read_and_global_flop_cards() #

        if not time02 < 5 * 60 :
            raise Exception("8.I should work on main menu automation later!(game is locked maybe, force to exit or restart),waiting_for_first_hand == None mishavad")
            fix_game_disruption("6")


# Flop: -------


    if waiting_for_first_hand == False :

        shout("Running Flop Section")
        time01 = time.time()
        time02 = time.time() - time01
        flop_betting_round = -1
        while Hand_End_Cheker1 == False and turn_stage == False and time02 < 5 * 60 and waiting_for_first_hand == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            its_my_turn = False ; Turn1 = False ; fo = 0
            shout("Looking for Next sign...", color = 'light_magenta')
            while Hand_End_Cheker1 == False and its_my_turn == False and Turn1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    game_position = find_game_position.find_game_reference_point()
                    fo = 1
                if pm.button_pixel(game_position, 'i_am_back') :
                    fix_game_disruption("6.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  my_seat_number )
                Turn1 = pm.turn_pixel(game_position)
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                fix_game_disruption("7")
                
            if Hand_End_Cheker1 == False :

                if its_my_turn == True and Turn1 == False :
                    flop_betting_round += 1
                    shout("light is founded", color = 'light_magenta')
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # Flop
                    elif flop_betting_round > 0 :
                        set_just_do_check_fold_to_true("4")
                        screenshot_error("9.Red should be True here")
                        read_and_save_bets() #
                        click_decision() # Flop
                    else :
                        read_and_save_bets() #
                        click_decision() # Flop
                        
                if Turn1 == True :            
                    turn_stage = True
                    shout("Reading Turn Card", color = 'light_magenta')
                    read_and_global_turn_card() #        
            
        if not time02 < 5 * 60 :
            raise Exception("10.I should work on main menu automation later!(game is locked maybe, force to exit or restart),waiting_for_first_hand == None mishavad")
            fix_game_disruption("8")    



# Turn: -------

    
    if waiting_for_first_hand == False :

        shout("Running Turn Section")
        time01 = time.time()
        time02 = time.time() - time01
        turn_betting_round = -1
        while Hand_End_Cheker1 == False and river_stage == False and time02 < 5 * 60 and waiting_for_first_hand == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            its_my_turn = False ; River1 = False ; fo = 0
            shout("Looking for Next sign...", color = 'light_magenta')
            while Hand_End_Cheker1 == False and its_my_turn == False and River1 == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    game_position = find_game_position.find_game_reference_point()
                    fo = 1
                if pm.button_pixel(game_position, 'i_am_back') :
                    fix_game_disruption("8.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  my_seat_number )
                River1 = pm.river_pixel(game_position)
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                fix_game_disruption("9")
                
            if Hand_End_Cheker1 == False :

                if its_my_turn == True and River1 == False :
                    turn_betting_round += 1
                    shout("light is founded", color = 'light_magenta')
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # Turn
                    elif turn_betting_round > 0 :
                        set_just_do_check_fold_to_true("5")
                        screenshot_error("11.Red should be True here")
                        read_and_save_bets() #
                        click_decision() # Turn
                    else :
                        read_and_save_bets() #
                        click_decision() # Turn
                        
                if River1 == True :            
                    river_stage = True
                    shout("Reading River Card", color = 'light_magenta')
                    read_and_global_river_card() #        
            
        if not time02 < 5 * 60 :
            raise Exception("12.I should work on main menu automation later!(game is locked maybe, force to exit or restart),waiting_for_first_hand == None mishavad")
            fix_game_disruption("10")            
            

# River: -------


    if waiting_for_first_hand == False :

        shout("Running River Section")
        time01 = time.time()
        time02 = time.time() - time01
        river_betting_round = -1
        while Hand_End_Cheker1 == False and time02 < 5 * 60 and waiting_for_first_hand == False :

            time02 = time.time() - time01
                
            time1 = time.time()
            time2 = time.time() - time1
            its_my_turn = False ; fo = 0
            shout("Looking for Next sign...", color = 'light_magenta')
            while Hand_End_Cheker1 == False and its_my_turn == False and time2 < 1 * 60 :
                if time.time() - time1 > 30 and fo == 0 :
                    shout("Looking for game on screen after 30s of idle...")
                    game_position = find_game_position.find_game_reference_point()
                    fo = 1
                if pm.button_pixel(game_position, 'i_am_back') :
                    fix_game_disruption("10.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                its_my_turn = pm.active_player_pixel(game_position,  my_seat_number )
                time2 = time.time() - time1

            if not time2 < 1 * 60 :
                fix_game_disruption("11")
                
            if Hand_End_Cheker1 == False :

                if its_my_turn == True and pm.river_pixel(game_position) == True :
                    river_betting_round += 1
                    shout("light is founded", color = 'light_magenta')
                    if is_there_any_raiser() == True :
                        read_and_save_bets() #
                        click_decision() # River
                    elif river_betting_round > 0 :
                        set_just_do_check_fold_to_true("6")
                        screenshot_error("13.Red should be True here")
                        read_and_save_bets() #
                        click_decision() # River
                    else :
                        read_and_save_bets() #
                        click_decision() # River


                               
            
        if not time02 < 5 * 60 :
            raise Exception("14.I should work on main menu automation later!(game is locked maybe, force to exit or restart),waiting_for_first_hand == None mishavad")
            fix_game_disruption("12")            
            


#-------
            
    if Hand_End_Cheker1 == True and waiting_for_first_hand == True :

        declare_the_winners()
        shout ("-------- Hand Ended --------", color = 'on_green')

    if Hand_End_Cheker1 == True and waiting_for_first_hand == False :

        declare_the_winners()
        shout ("-------- Hand Ended --------", color = 'on_green')
        
        reset_just_do_check_fold_to_false() #

        reset_table_information() #

        if pm.my_seat_won_pixel(game_position,  my_seat_number ) == False : 
            My_Bank = ocr_my_bank()
            if My_Bank != None :
                if My_Bank >= 15 * BLIND_VALUE : 
                    shout("My Bank is:%s" %My_Bank, color = 'light_green')
                elif My_Bank != 0 :
                    shout("My Bank is:%s" %My_Bank, color = 'light_green')
                    shout("Rebuying...")
                    pass # Later i'll build
        else :
            My_Bank = None
        
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Hand_End_Cheker1 == True and time02 < 1.5 * 60 :
            Hand_End_Cheker1 = hand_is_ended()
            time2 = time.time() - time1
            if not time2 < 2 * 60 :
                if fo == 0 :
                    fix_game_disruption("13")
                    fo = 1
                time02 = time.time() - time1                

        if not time02 < 1.5 * 60 :
            raise Exception("15.Game is locked, force to restart, waiting_for_first_hand == None")
            


    if Hand_End_Cheker1 == False and waiting_for_first_hand == False :

        if pm.active_player_pixel(game_position, my_seat_number) != True or ( pm.active_player_pixel(game_position, my_seat_number) == True and pm.notification_banner_pixel(game_position, my_seat_number) == True ) :
            read_and_global_banks_and_names() #
        else :
            shout("Players Info is not Read", color = 'on_light_red')

        Coins_Appeared = False
        time02 = 0 ; fo = 0 
        time1 = time.time()
        while Coins_Appeared == False and time02 < 5 * 60 : #being alone time
            Coins_Appeared = sb_b_d_buttons_are_founded()
            time2 = time.time() - time1
            if not time2 < 8 and fo == 0 :
                game_position = find_game_position.find_game_reference_point()
                fo = 1
            if not time2 < 2 * 60 :
                if fo == 1 :
                    fix_game_disruption("14")
                    fo = 2
                time02 = time.time() - time1                

        if not time02 < 5 * 60 : #being alone time
            raise Exception("16.No one join, time to exit. Or Game is locked, force to restart, waiting_for_first_hand == None")

        elif waiting_for_first_hand == False :
            shout ("-------- New Hand Started --------", color = 'on_green')
            shout ("Coins are Founded")
            config.determine_small_blind_seat()
            config.determine_big_blind_seat()
            config.determine_dealer_seat()       


                    
            time02 = 0 ; fo = 0 
            time1 = time.time()
            Cards1 = False
            shout("Looking for cards...", color = 'light_magenta')
            while Hand_End_Cheker1 == False and Cards1 == False and waiting_for_first_hand == False and time02 < 1.5 * 60 :
                if pm.button_pixel(game_position, 'i_am_back') :
                    fix_game_disruption("14.5 I am back Button is True")
                Hand_End_Cheker1 = hand_is_ended()
                Cards1 = pm.player_cards_pixel(game_position,  my_seat_number )
                time2 = time.time() - time1
                if not time2 < 2 * 60 :
                    if fo == 0 :
                        fix_game_disruption("15")
                        fo = 1
                    time02 = time.time() - time1                

            if not time02 < 1.5 * 60 :
                raise Exception("17.Game is locked, force to restart, waiting_for_first_hand == None")

            if Cards1 == True :
                shout("Cards are founded", color = 'light_magenta')

            elif not time02 < 1.5 * 60 :
                fix_game_disruption("15")

            if Hand_End_Cheker1 == True and Cards1 == False :
                fix_game_disruption("16. I am maybe out")
            



