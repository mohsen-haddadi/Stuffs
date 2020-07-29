import time, os, socket, re, pickle
from PIL import Image
import pyautogui, cv2, numpy, pygame, win32gui, win32con, wmi
from datetime import datetime
from painter import paint
import screen_monitoring.find_game_position.find_game_position as find_game_position
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.ocr.ocr as ocr
import screen_monitoring.read_cards.read_cards as read_cards
import screen_monitoring.click_coordinates.click_coordinates as click_coordinates
import decision_making.decide

#testing sub packages imports
test = False
if test == True:
    game_position = find_game_position.find_game_reference_point()
    #print(read_cards.read_flop_cards(game_position))
    #decision_making.rules_and_info.flush.load_variables()
    input("wait")

def load_variables():
    """ variables order is important while loading """
    global game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat

    game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat = \
    pickle.load( open( "pickled variables.p", "rb" ) )


def save_variables() :
    """
    functions i used save_variables() at: 1.click_decision() 2.fix_game_disruption() (containting funcs are not used anywhere else, so variables will overlap) 
    3.Check_Mod_On() 4.getpo() 5.getpo_for_starting() 6.Create_file_directories()
    Pickling at click_decision() will support Pickling variables at funcs like Read pm.player_cards_pixel(game_position, ), Determind small blind(), and.... because click_decision() is run after them.

    Where ever i use save_variables() at the end of a function i should Implement load_variables() at the first line of that function.
    To Pickle real updated variables.
    Becuase by running main file functions from the other files, the variables will update for that file but will not update for mian file. 
    like just_do_check_fold variable in fix_game_disruption() run from Buttons which is run from decide file.
    click_decision() should not use load_variables() because it's running at main file and it is a gate way. some varibiales may have changed in main while True.

    At gate way lines to the other files use save_variables() before and load_variables() after them. 
    The only gate way line is currently in click_decision() function now. By seperating read cards files, I can expand gate ways to lines like read pm.player_cards_pixel(game_position, ) 

    delete variables.p or set all variables to None at the beggining. (Done)
    By running main file if i have not assigned varibales from before, it will error. 
    By implementing load_variables() I can delete all global lines from supporting and... funcitons. 
    But I keep them to see the varibales I've used for that functions. 
    """
    global game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat

    pickle.dump( [game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat], \
    open( "pickled variables.p", "wb" ) )



def set_all_variables_to_none():
    global game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat

    game_position , DATED_REPORT_FOLDER , REPORTS_DIRECTORY,\
    preflop_stage , flop_stage , turn_stage , river_stage ,\
    preflop_betting_round , flop_betting_round ,\
    turn_betting_round , river_betting_round ,\
    board_card_1th , board_card_2th , board_card_3th ,\
    board_card_4th, board_card_5th , my_1th_card , my_2th_card ,\
    my_seat_number , MY_PROFILE_NAME ,\
    just_do_check_fold , waiting_for_first_hand ,\
    player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    last_white_chips_cache , last_red_chips_cache ,\
    last_player_cards_cache , last_bets_cache,\
    did_i_raised_at  , my_last_raise_at , players_name , players_bank ,\
    BLIND_VALUE , small_blind_seat , big_blind_seat , dealer_seat = (None,)*38
    save_variables()

def create_file_directories():
    global DATED_REPORT_FOLDER , REPORTS_DIRECTORY
    load_variables()
    
    DATED_REPORT_FOLDER = datetime.now().strftime("%Y.%m.%d %A %H.%M.%S")
    REPORTS_DIRECTORY = "Reports/%s" %DATED_REPORT_FOLDER
    if not os.path.exists( REPORTS_DIRECTORY ):
        os.makedirs( REPORTS_DIRECTORY )
    save_variables()

def shout(string, color = None) :
    global DATED_REPORT_FOLDER
    load_variables()

    if color == None:
        pass 
    elif color == 'light_cyan':
        string = paint.light_cyan.bold(string)
    elif color == 'green':
        string = paint.green.bold(string)
    elif color == 'light_green':
        string = paint.light_green.bold(string)
    elif color == 'yellow':
        string = paint.yellow.bold(string)
    elif color == 'light_magenta':
        string = paint.light_magenta.bold(string)

    elif color == 'rainbow':
        string = paint.rainbow.bold(string)

    elif color == 'on_green':
        string = paint.on_green.bold(string)
    elif color == 'on_light_blue':
        string = paint.on_light_blue.bold(string)
    elif color == 'on_yellow':
        string = paint.on_yellow.bold(string)
    elif color == 'on_light_magenta':
        string = paint.on_light_magenta.bold(string)
    elif color == 'on_light_red':
        string = paint.on_light_red.bold(string)

    text_file_name = os.path.join("Reports/%s" %DATED_REPORT_FOLDER,
                                  DATED_REPORT_FOLDER)
    date_and_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
    date_and_time = date_and_time[:-4]

    if 'PROMPT' in os.environ :
        print("%s: %s" %(date_and_time, string))
        # Clear the paint effects on string to make string raw and readable
        string = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', string) 
    else :
        # Clear the paint effects on string to make string raw and readable
        string = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', string)
        print("%s: %s" %(date_and_time, string))

    text_file = open("%s.txt" %text_file_name , "a")
    text_file.write("%s: %s" %(date_and_time, string))
    text_file.write( "\n" )
    text_file.close()

    # Test colors in Command Prompt:
    #shout('light_cyan', 'light_cyan') ; shout('green', 'green')
    #shout('light_green', 'light_green'); shout('yellow', 'yellow') 
    #shout('light_magenta', 'light_magenta'); shout('rainbow', 'rainbow')
    #shout('on_green', 'on_green'); shout('on_light_blue', 'on_light_blue')
    #shout('on_yellow', 'on_yellow') 
    #shout('on_light_magenta', 'on_light_magenta')
    #shout('on_light_red', 'on_light_red')



pygame.mixer.init() #Check later if i can move this line to first line of sound() function or not.
def sound(string_name) :
    try :
        pygame.mixer.music.load( os.path.join('Sounds' ,
                                              , "%s.wav" %string_name ) )
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

    set_all_variables_to_none()
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

def white_chips(seat):
    # It checks if there is a white colored chips in front of a seat,
    # by returning True or False, to find out if a player has call or not
    global game_position
    load_variables()

    if pm.player_chips_pixel(game_position, seat):
        return not pm.are_chips_white_or_red_pixel(game_position, seat)
    else :
        return False

def red_chips(seat):
    # It checks if there is a red colored chips in front of a seat,
    # by returning True or False, to find out if a player has bet/raised or not.
    # (In accordance to Google: 'A bet is the first wager of a round.')
    global game_position
    load_variables()

    if pm.player_chips_pixel(game_position, seat):
        return pm.are_chips_white_or_red_pixel(game_position, seat)
    else :
        return False

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

# 2017 :------------------------------

###
def determine_small_blind_seat():
    global game_position, small_blind_seat
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.small_blind_pixel(game_position, seat):
            small_blind_seat = seat
            shout("Seat %s is at Small Blind Seat" %seat)
            break

### 
def determine_big_blind_seat():
    global game_position, big_blind_seat
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.big_blind_pixel(game_position, seat):
            big_blind_seat = seat
            shout("Seat %s is at Big Blind Seat" %seat)
            break

###
def determine_dealer_seat():
    global game_position, dealer_seat
    load_variables()

    for seat in [1,2,3,4,5]:
        if pm.dealer_pixel(game_position, seat):
            dealer_seat = seat
            shout("Seat %s is at Dealer Seat" %seat)
            break


# FUNCTIONS_Pixel-Maching Ended ---------------------------------------------------------------------------------------



# def_Buttons_new: ---------------------------------------------------------------------------------------------------------------
def click(name):
    x, y = click_coordinates.click_coordinates(game_position, name)
    pyautogui.click(x, y)
    if name in ('available_seat_1', 'available_seat_2', 'available_seat_3',
                'available_seat_4', 'available_seat_5', 'exit_probable_advertisement',
                'close_update_window'):
        shout("%s is clicked" %name, color = 'light_cyan')
    else:
        shout("%s button is clicked" %name, color = 'light_cyan')

def hold_click(name ,seconds = 10):
    x, y = click_coordinates.click_coordinates(game_position, name)
    pyautogui.mouseDown(x=x, y=y)
    time.sleep(seconds)
    pyautogui.mouseUp()
    shout("%s button is hold for %s seconds" %(name, seconds), color = 'light_cyan')

def click_on_button(button_name): 
    # for call, check, fold, bet, raise,
    # exit, menu, rebuy_menu,
    # exit_yes, leave_next_hand_ok, buy_in, and re_buy buttons.
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand 
    load_variables()

    if pm.button_pixel(game_position, button_name) : 
        click(button_name) 
        if button_name == 'exit':
            waiting_for_first_hand = None

    else :

        if button_name in ('call', 'check', 'fold', 'bet', 'raise') :

            time0 = time.time()
            fix_game_disruption("button %s is not visible" %button_name )
            time1 = time.time() - time0
            if waiting_for_first_hand == True:
                return None
            elif just_do_check_fold == True:
                if pm.button_pixel(game_position, 'check') :
                    click('check')
                elif pm.button_pixel(game_position, 'fold') :
                    click('fold') 
                else:
                    screenshot_error("check and fold buttons are not visible")  
            elif pm.player_cards_pixel(game_position,  my_seat_number ) \
            and pm.button_pixel(game_position, button_name) and time1 <= 10 :
                click(button_name) #new function
            else :
                set_just_do_check_fold_to_true("There is problem on clicking on button %s" %button_name)

        elif button_name in ('exit', 'menu', 'rebuy_menu'):

            fix_game_disruption("button %s is not visible" %button_name )
            if pm.button_pixel(game_position, button_name):
                click(button_name)
                if button_name == 'exit':
                    waiting_for_first_hand = None
            else:
                raise_exception_the_problem("button %s is not visible" %button_name)

        elif button_name in ('exit_yes', 'leave_next_hand_ok', 'buy_in', 're_buy'):

            raise_exception_the_problem("button %s is not visible" %button_name)

def number_of_clicks_on_button(button_name, number): # Number of clicks 
    # for plus and minus buttons
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    load_variables()

    number = int(number)
    if pm.button_pixel(game_position, button_name) :
        for i in range (number):
            click(button_name)
    else :
        time0 = time.time()
        fix_game_disruption("button %s is not visible" %button_name)
        time1 = time.time() - time0
        if waiting_for_first_hand == True:
            return None
        elif just_do_check_fold == True:
            if pm.button_pixel(game_position, 'check') :
                click('check')
            elif pm.button_pixel(game_position, 'fold') :
                click('fold') 
            else:
                screenshot_error("check and fold buttons are not visible") 
        if pm.player_cards_pixel(game_position,  my_seat_number ) \
        and pm.button_pixel(game_position, button_name) and time1 <= 10 :
            for i in range (number):
                click(button_name)
        else :
            set_just_do_check_fold_to_true("There is problem on clicking on button %s" %button_name)

def hold_click_on_button(button_name, seconds = 10): 
    # for buy_in_plus and buy_in_minus and re_buy_plus and re_buy_minus buttons
    # It holds left click for 10s
    global game_position
    load_variables()
    if pm.button_pixel(game_position, button_name) :
        hold_click(button_name ,seconds = seconds)

    else :
        time.sleep(2)
        if pm.button_pixel(game_position, button_name) :
            hold_click(button_name ,seconds = seconds)
        else :
            raise_exception_the_problem("button %s is not visible" %button_name) 

def find_and_click_on_reconnect_button():
    global game_position
    load_variables()

    shout('looking for reconnect button')
    x1=pyautogui.locateCenterOnScreen('screen_monitoring/game_position/reconnect button.png')
    if x1 != None :
        pyautogui.click(x1)
        shout('reconnect button founded and clicked', color = 'yellow')
        time.sleep(5)
        if pm.button_pixel(game_position, 'i_am_back') == True :
            click('i_am_back')
        return x1
    
    x2=pyautogui.locateCenterOnScreen('screen_monitoring/game_position/reconnect button.png')
    if x2 != None :
        pyautogui.click(x2)
        shout('reconnect button founded and clicked', color = 'yellow')
        time.sleep(5)
        if pm.button_pixel(game_position, 'i_am_back') == True :
            click('i_am_back')
        return x1

    else :
        return None

# 2017: -----------------------------

def fold():
    global game_position , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    return click_on_button('fold')

def check():
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    return click_on_button('check')

def call():
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    return click_on_button('call')

def all_in_old( Minus_Blinds = 0 ): #not completed on did_i_raised_at and my_last_raise_at. i won't use this fuction anymore
    """ if 0 : all_in everything """
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand

    if pm.button_pixel(game_position, 'all_in') == False and pm.button_pixel(game_position, 'call') == True \
    and pm.button_pixel(game_position, 'bet') == False and pm.button_pixel(game_position, 'raise') == False :
        return click_on_button('call')
    
    if Minus_Blinds == 0 :
        click_on_button('all_in')
        if pm.button_pixel(game_position, 'bet') == True :
            return click_on_button('bet')
        else :
            return click_on_button('raise')
    else :
        click_on_button('all_in')
        number_of_clicks_on_button('minus', Minus_Blinds)
        if pm.button_pixel(game_position, 'bet') == True :
            return click_on_button('bet')
        else :
            return click_on_button('raise')

def all_in():
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand

    if pm.button_pixel(game_position, 'all_in') == False and pm.button_pixel(game_position, 'call') == True \
    and pm.button_pixel(game_position, 'bet') == False and pm.button_pixel(game_position, 'raise') == False :
        return click('call')
    
    click_on_button('all_in')
    if pm.button_pixel(game_position, 'bet') == True :
        return click('bet')
    else :
        return click_on_button('raise')

def raising( Blinds ):
    """ 
    Act for both raising and betting 
    Blinds is the amount of money like in ocr; not the number of blinds
    if Blinds == BLIND_VALUE (or less): won't click on plus button
    """
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand,\
    preflop_stage , flop_stage , turn_stage , river_stage , did_i_raised_at , my_last_raise_at , BLIND_VALUE
    load_variables()

    if preflop_stage == True and flop_stage == False :
        stage = "Pre_Flop" 
    elif flop_stage == True and turn_stage == False :
        stage = "Flop"  
    elif turn_stage == True and river_stage == False :
        stage = "Turn" 
    elif river_stage == True :
        stage = "River" 

    did_i_raised_at[stage] = True

    Bets = [last_bets_cache[Seat] for Seat in range(1,6) if last_red_chips_cache[Seat] and last_bets_cache[Seat] != None ]     

    if preflop_stage and not flop_stage :
        Bets.append(BLIND_VALUE)
    else :
        Bets.append(0) #That's why raising() algorithm can be use and act for betting too.

    Bets.sort(reverse = True )

    Raise_base = max(Bets)

    Bets_difference = [ Bets[i] - Bets[i+1] for i in range(len(Bets)-1) ]

    if Bets_difference == [] :
        Raise_add = BLIND_VALUE
    elif max(Bets_difference) <= BLIND_VALUE :
        Raise_add = BLIND_VALUE
    else :
        Raise_add = max(Bets_difference)

    if Blinds > Raise_base + Raise_add :
        my_last_raise_at[stage] = Blinds
    else :
        my_last_raise_at[stage] = Raise_base + Raise_add

    number_of_clicks_on_button('plus', ( Blinds - (Raise_base + Raise_add) ) // BLIND_VALUE)
    #Till here as same as raising()

    if pm.button_pixel(game_position, 'raise') :
        click('raise')
    elif pm.button_pixel(game_position, 'bet') :
        click('bet')
    else :

        fix_game_disruption("RAISE() Button, No Raise nor Bet Button founded")
        if pm.button_pixel(game_position, 'raise') :
            click('raise')
        elif pm.button_pixel(game_position, 'bet') :
            click('bet')
        else :
            set_just_do_check_fold_to_true("No raise nor bet button founded")

def check_fold():
    global game_position, just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    if pm.button_pixel(game_position, 'check') :
        click('check')
    elif pm.button_pixel(game_position, 'fold') :
        click('fold') 
    else :

        fix_game_disruption("check_fold()")
        if waiting_for_first_hand != False:
            return None
        elif pm.button_pixel(game_position, 'check') :
            click('check')
        elif pm.button_pixel(game_position, 'fold') :
            click('fold') 
        else:
            set_just_do_check_fold_to_true("check_fold()(It's already True)") 
            screenshot_error("check and fold buttons are not visible")      


# def_Buttons_new Ended ----------------------------------------------------------------------------------------------------------





# Read Cards: --------------------------------------------------------------------------------------------------------------------

def read_and_global_my_cards():
    global game_position, my_1th_card , my_2th_card  , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    load_variables()

    my_1th_card, my_2th_card =\
    read_cards.read_my_cards(game_position, my_seat_number)

    if ('Unknown' in my_1th_card 
        or 'Unknown' in my_2th_card ):

        fix_game_disruption("my cards are read Unknown")
        my_1th_card, my_2th_card =\
        read_cards.read_my_cards(game_position, my_seat_number)

        if ('Unknown' in my_1th_card 
            or 'Unknown' in my_2th_card
            or pm.flop_pixel(game_position) ):

            set_just_do_check_fold_to_true("my cards are read Unknown again")

    shout("My cards are: %s %s, %s %s"
          %(my_1th_card[0][0], my_1th_card[0][1],
            my_2th_card[1][0], my_2th_card[1][1])
          , color = 'green')

def read_and_global_flop_cards(): 
    global game_position, board_card_1th , board_card_2th , board_card_3th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand

    board_card_1th, board_card_2th, board_card_3th =\
    read_cards.read_flop_cards(game_position)

    if ( 'Unknown' in board_card_1th 
        or 'Unknown' in board_card_2th
        or 'Unknown' in board_card_3th ):

        fix_game_disruption("Flop cards are read 'Unknown'")
        board_card_1th, board_card_2th, board_card_3th =\
        read_cards.read_flop_cards(game_position)

        if ('Unknown' in board_card_1th 
            or 'Unknown' in board_card_2th
            or 'Unknown' in board_card_3th 
            or not pm.flop_pixel(game_position) 
            or pm.turn_pixel(game_position) ):

            set_just_do_check_fold_to_true("Flop cards are read 'Unknown' again")

    shout("Flop cards are: %s %s, %s %s, %s %s" 
          %(board_card_1th[0][0], board_card_1th[0][1], 
            board_card_2th[1][0], board_card_2th[1][1],
            board_card_3th[1][0], board_card_3th[1][1])
          , color = 'green')

def read_and_global_turn_card(): 
    global game_position, board_card_4th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand

    board_card_4th = read_cards.read_turn_card(game_position)
    
    if 'Unknown' in board_card_4th:

        fix_game_disruption("Turn card is read 'Unknown'")
        board_card_4th = read_cards.read_turn_card(game_position)

        if ( 'Unknown' in board_card_4th 
            or not pm.turn_pixel(game_position)
            or pm.river_pixel(game_position) ) :

            set_just_do_check_fold_to_true("Turn card is read 'Unknown' again")

    shout("Turn card is: %s %s" %(board_card_4th[0], board_card_4th[1])
          , color = 'green')

def read_and_global_river_card(): 
    global game_position, board_card_5th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand
    
    board_card_5th = read_cards.read_river_card(game_position)
    
    if 'Unknown' in board_card_5th:

        fix_game_disruption("River card is read 'Unknown'")
        board_card_5th = read_cards.read_river_card(game_position)

        if ('Unknown' in board_card_5th 
            or not pm.river_pixel(game_position) ):

            set_just_do_check_fold_to_true("River card is read 'Unknown' again")

    shout("River card is: %s %s" %(board_card_5th[0], board_card_5th[1])
          , color = 'green')

# Read Cards Ended ---------------------------------------------------------------------------------------------------------------

# OCR Bet Number Positions new 2016: ---------------------------------------------------------------------------------------------
def replace_letters_comma_space_m_k(ocr_string):
    string = ocr_string
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace("M","*1000000")
    string = string.replace("K","*1000")
    return string

# If there is no script to ocr, ocr functions at ocr module
# will return empty string '', not None.
def ocr_bet(seat):
    """
    If ocr fails this function will uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    global my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand , just_do_check_fold , last_white_chips_cache , last_red_chips_cache
    load_variables()
 
    ocr_string = ocr.ocr_bet_to_string(game_position, seat)
    shout("bet ocr string at seat %s is: %s" %(seat, ocr_string))
    eval_string = replace_letters_comma_space_m_k(ocr_string)
    digit_string = eval_string.replace("*","")

    if digit_string.isdigit():
        return eval(eval_string)
    # else include digit_string like: '', 'c540!'
    else :
        fix_game_disruption("ocr_bet is not digit at seat %s" %seat)
        ocr_string = ocr.ocr_bet_to_string(game_position, seat)
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
    global my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand , just_do_check_fold
    load_variables()

    ocr_string = ocr.ocr_other_players_bank_to_string(game_position, seat)
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
    global my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand , just_do_check_fold
    load_variables()

    ocr_string = ocr.ocr_my_bank_to_string(game_position, my_seat_number)
    shout("my bank ocr string at seat %s is: %s"%(my_seat_number, ocr_string))
    eval_string = replace_letters_comma_space_m_k(ocr_string)
    digit_string = eval_string.replace("*","")

    if digit_string.isdigit():
        return eval(eval_string)
    # else include digit_string like: '', 'c540!'
    else :
        fix_game_disruption("ocr_my_bank is not digit at seat %s" 
                            %my_seat_number)
        ocr_string = ocr.ocr_my_bank_to_string(game_position, my_seat_number)
        shout("my bank ocr string at seat %s is: %s" 
              %(my_seat_number, ocr_string))
        eval_string = replace_letters_comma_space_m_k(ocr_string)
        digit_string = eval_string.replace("*","")

        if digit_string.isdigit():
            return eval(eval_string)
        else:           
            screenshot_error("ocr_my_bank is not digit at seat %s"
                             %my_seat_number)
            return None            

def ocr_other_names(seat):
    """
    If ocr fails this function will uses:
    (will use nothing)
    Will not uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    name_is_hidden_1 = pm.other_seat_won_pixel(game_position, seat)
    name_is_hidden_2 = pm.notification_banner_pixel(game_position, seat)
    if name_is_hidden_1 or name_is_hidden_2 :
        return None
    else :
        string = ocr.ocr_other_names_to_string(game_position, seat)
        shout("other name ocr string at seat %s is: %s" %(seat, string) )
        return string

def ocr_my_name():
    """
    If ocr fails this function will uses:
    (will use nothing)
    Will not uses:
    1. fix_game_disruption()
    2. set_just_do_check_fold_to_true()
    """
    if pm.my_seat_won_pixel(game_position, my_seat_number):
        return True
    if pm.notification_banner_pixel(game_position, my_seat_number):
        return None
    string = ocr.ocr_my_name_to_string(game_position, my_seat_number)
    shout("my name ocr string at seat %s is: %s" %(my_seat_number, string))
    return string

# OCR Others Name Positions 2016 Ended -------------------------------------------------------------------------------------------







# fix_game_disruption: -------------------------------------------------------------------------------------------------------------------

#def ocr(x,y,h,w):

#def ocr_my_name(Seat_Num):
#
#def pm.i_am_seated_pixel(game_position, Number):
#
#def pm.available_seat_pixel(game_position, Number):

#def click_on_available_seat(seat):

#def click_on_exit_button(): 

def sit_in(chips): # "Min buy in" or "Max buy in"
    global game_position, my_seat_number , waiting_for_first_hand
    load_variables()

    shout("Searching for a seat to sit in", color = 'yellow')
    my_seat_number = None
    for i in range(1 ,6 ):
        if pm.available_seat_pixel(game_position,i) == True :
            click('available_seat_%s' %i)
            my_seat_number = i
            waiting_for_first_hand = True
            shout("Sit_In() --> waiting_for_first_hand is True."
                  , color = 'yellow')
            break
    if my_seat_number == None :
        click_on_button('exit')
        
        raise Exception("Sit_In(chips):This can not happen IN FUTURE becuase main menu automation is built")
    else :
        x1 = time.time()
        time1 = 0
        Buy_In = None 
        while ( (time1 < 5) and Buy_In !=True ):
            Buy_In = pm.button_pixel(game_position, 'buy_in')
            x2 = time.time()
            time1 = x2-x1
        if Buy_In != True :
            fix_game_disruption("Sit_In(chips):Buy_In != True")
        if (chips == "Min buy in" and my_seat_number != None) :
            hold_click_on_button('buy_in_minus', seconds = 10)
        if (chips == "Max buy in" and my_seat_number != None):
            hold_click_on_button('buy_in_plus', seconds = 10)
        if my_seat_number != None :
            click_on_button('buy_in')
            screenshot_error("Rebuyed")
#
#def pm.i_am_back_button_pixel(game_position):

#def click_on_i_am_back_button(): # we can use click('i_am_back') directly

#def click_on_reconnect_button():

def is_internet_disconnected():
  REMOTE_SERVER = "www.google.com"
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    shout('internet is connected')
    return False
  except:
     pass
  return True

def check_i_am_in_or_out():
    global game_position, my_seat_number , MY_PROFILE_NAME , just_do_check_fold
    load_variables()

    if pm.button_pixel(game_position, 'i_am_back') == True :
        click('i_am_back')
    if ocr_my_name() == MY_PROFILE_NAME or ocr_my_name() == True :
        shout("I am In", color = 'yellow')
        return ("In")

    for i in range(1,6):
        if pm.i_am_seated_pixel(game_position, i) :
            if is_internet_disconnected() == False and find_and_click_on_reconnect_button() == None :
                if my_seat_number == i :
                    shout("I am In not by OCR")
                    return ("In")
                else :
                    my_seat_number = i
                    shout('I AM IN,BUT MY SEAT IS MANUALLY CHANGED TO: %s' %my_seat_number)
                    set_just_do_check_fold_to_true("My seat is manually changed!")
                    return ("In")
                
    shout("I am Out", color = 'yellow')
    return ("Out")

def fix_game_disruption(String = None): #if find_game_reference_point() == None or ...
    global game_position , my_seat_number , MY_PROFILE_NAME , waiting_for_first_hand , just_do_check_fold
    load_variables()

    shout( 7*"-" , color = 'yellow')
    if String == None :
        shout("fix_game_disruption() is running....", color = 'yellow')
    elif type(String) == str :
        shout("fix_game_disruption() <-- %s is running...." %String
              , color = 'yellow')

    if is_internet_disconnected() :
        shout('Internet is Disconnected, waiting to reconect...')
        while is_internet_disconnected() :
            continue
        shout('Internet is Connected Back!')
        time.sleep(15)
        if find_and_click_on_reconnect_button() == None :
            screenshot_error('No reconnect button founded')

    click('exit_probable_advertisement') # click to Exit probable Advertisement
    shout("Position (0,720) is clicked", color = 'yellow')
    pyautogui.press('esc')
    
    game_position = pyautogui.locateOnScreen(
                    'screen_monitoring/find_game_position/reference image.png')
    if game_position == None:
        alternative_game_position = pyautogui.locateOnScreen(
                    'screen_monitoring/find_game_position/alternative reference image.png')   
        game_position = ( alternative_game_position[0]+328 , alternative_game_position[1]-245 ) 
    if game_position != None :
        game_position = (int(game_position[0]),int(game_position[1]))
    else:
        for process in wmi.WMI().Win32_Process ():
            if process.Name == 'SystemSettings.exe' :
                shout("SystemSettings Update is on desktop")
                shout("closing Windows Update program")
                screenshot_error('right before closing windows update program')
                click('close_update_window')
                break        

    if game_position == None :
        game_position = find_game_position.find_game_reference_point()
    if game_position != None :
        shout("Game region refounded after fix_game_disruption()"
              , color = 'yellow')
    
    if pm.button_pixel(game_position, 'i_am_back') == True :
        click('i_am_back')
        if pm.player_cards_pixel(game_position,  my_seat_number ) == True :
            just_do_check_fold = True
            shout("After fix_game_disruption() --> just_do_check_fold is True."
                  , color = 'yellow')
        else :
            waiting_for_first_hand = True
            shout("After fix_game_disruption() --> waiting_for_first_hand is True."
                  , color = 'on_yellow')

    if check_i_am_in_or_out() == "Out":
        sit_in("Min buy in")

    shout( 7*"-" , color = 'yellow')
    save_variables()

#if (buttoms are still not visible after vital signs).... : #My pixel matching were wrong somewhere
#    t = time.time()
#    pyautogui.screenshot( 'Error %s.png' %t )
#    raise Exception('what was the probelm on %s?' %t ) 
        
def screenshot_error(type_of_error): #type_of_error in string
    global REPORTS_DIRECTORY
    load_variables()
    t = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
    t = t[:-4]
    shout("Screenshot Error: %s" %type_of_error, color = 'on_light_blue')
    pyautogui.screenshot( '%s/Error %s %s.png' %(REPORTS_DIRECTORY, t, type_of_error) )

def raise_exception_the_problem(string):
    screenshot_error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')

# fix_game_disruption Ended --------------------------------------------------------------------------------------------------------------



### Read_Bets & dinctionaries & Reset var funcs: ****************************************************************************************************************************


def read_and_global_banks_and_names() :
    global game_position, players_name , players_bank , my_seat_number
    load_variables()

    # First ocr my bank and name, so if we get a problem it will use
    # fix_game_disruption() function inside ocr_my_bank() and ocr_my_name()
    # because ocr_other_players_bank() and ocr_other_names() don't have 
    # fix_game_disruption()
    players_bank[my_seat_number] = ocr_my_bank()
    players_name[my_seat_number] = ocr_my_name()
    for seat in range(1,6):
        if my_seat_number == seat:
            continue
        elif pm.other_player_seated_pixel(game_position, seat) == True :
            players_bank[seat] = ocr_other_players_bank(seat)
            players_name[seat] = ocr_other_names(seat)
            if red_chips(seat) :
                players_bank[seat] = None
    shout("Players Bank dictionary is: %s" %players_bank 
          , color = 'on_light_red')
    shout("Players Name dictionary is: %s" %players_name 
          , color = 'on_light_red')

def reset_table_information() : 
    """ preflop_betting_round ,...,river_betting_round & preflop_stage 
        ,...,river_stage dar loope while True baresi va be in func
        baraye reset shodan enteghal dade shavand """
    global players_name , players_bank ,\
           player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
           last_player_cards_cache , last_white_chips_cache , last_red_chips_cache , last_bets_cache,\
           did_i_raised_at , my_last_raise_at , preflop_betting_round , flop_betting_round , turn_betting_round , river_betting_round
    load_variables()

    shout("Reseting table information")
    for Seat in range(1,6):
        players_name[Seat] = None
        players_bank[Seat] = None
    player_cards_cache = {}
    white_chips_cache = {} 
    red_chips_cache = {}
    bets_cache = {}
    last_player_cards_cache = {}  
    last_white_chips_cache = {}   
    last_red_chips_cache = {}   
    last_bets_cache = {}

    # Make sure while starting the code did_i_raised_at is defined 
    # by reset_table_information() before first deciding; 
    # otherwise did_i_raise_sofar() at supporting funcs file will error
    did_i_raised_at = {"Pre_Flop": False , "Flop": False ,
                       "Turn": False , "River": False } 

    # (2018) Later make sure if all rounds are starting from 0 in 
    # main While True loop (Round_... = 0 should be implemented in 
    # read_and_save_bets() for all stages so for example 
    # bets_cache dictionary surely will "have Round_... 0"). 
    # For testing i have put a shout(bets_cache) at the end of 
    # read_and_save_bets() function 
    preflop_betting_round = 0 
    flop_betting_round = 0  
    turn_betting_round = 0  
    river_betting_round = 0
    
def set_just_do_check_fold_to_true(string = None) :
    global just_do_check_fold
    load_variables()

    just_do_check_fold = True
    if string == None :
        shout("just_do_check_fold is On", color = 'on_yellow')
    elif type(string) == str :
        shout("just_do_check_fold is On: %s" %string, color = 'on_yellow')
    save_variables()

def reset_just_do_check_fold_to_false() :
    global just_do_check_fold
    load_variables()

    if just_do_check_fold == True :
        shout("just_do_check_fold is reset to False")
        just_do_check_fold = False
    save_variables()

def read_and_save_bets() :
    global game_position, player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
           last_white_chips_cache , last_red_chips_cache , last_player_cards_cache , last_bets_cache,\
           preflop_betting_round , flop_betting_round , turn_betting_round , river_betting_round ,\
           preflop_stage , flop_stage , turn_stage , river_stage
    load_variables()

    if preflop_stage == True and flop_stage == False :
        stage = "Pre_Flop"
        betting_round = preflop_betting_round
    elif flop_stage == True and turn_stage == False :
        stage = "Flop"
        betting_round = flop_betting_round        
    elif turn_stage == True and river_stage == False :
        stage = "Turn"
        betting_round = turn_betting_round
    elif river_stage == True :
        stage = "River"
        betting_round = river_betting_round

    player_cards_cache["%s %s" %(stage, betting_round)] = {}
    white_chips_cache["%s %s" %(stage, betting_round)] = {}
    red_chips_cache["%s %s" %(stage, betting_round)] = {}
    bets_cache["%s %s" %(stage, betting_round)] = {}
    last_player_cards_cache = {}
    last_white_chips_cache = {}
    last_red_chips_cache = {}
    last_bets_cache = {}
    
    for Seat in range(1,6) :

        player_cards_cache["%s %s" %(stage, betting_round)][Seat] \
        = pm.player_cards_pixel(game_position, Seat)
        white_chips_cache["%s %s" %(stage, betting_round)][Seat] \
        = white_chips(Seat)
        red_chips_cache["%s %s" %(stage, betting_round)][Seat] \
        = red_chips(Seat)
        last_player_cards_cache[Seat] \
        = player_cards_cache["%s %s" %(stage, betting_round)][Seat]
        last_white_chips_cache[Seat] \
        = white_chips_cache["%s %s" %(stage, betting_round)][Seat]
        last_red_chips_cache[Seat] \
        = red_chips_cache["%s %s" %(stage, betting_round)][Seat]

        # Can replace with:
        # if pm.player_chips_pixel(game_position, seat):
        if (last_white_chips_cache[Seat] == True 
            or last_red_chips_cache[Seat] == True):

            bets_cache["%s %s" %(stage, betting_round)][Seat] = ocr_bet(Seat)

            if last_white_chips_cache[Seat] == True : 
                shout("Seat%s Call: $%s" 
                      %(Seat, 
                        bets_cache["%s %s" %(stage, betting_round)][Seat])
                      , color = 'light_green')

            elif last_red_chips_cache[Seat] == True :
                shout("Seat%s Raise: $%s" 
                      %(Seat, 
                        bets_cache["%s %s" %(stage, betting_round)][Seat])
                      , color = 'light_green')
        else :

            bets_cache["%s %s" %(stage, betting_round)][Seat] = None
        last_bets_cache[Seat] \
        = bets_cache["%s %s" %(stage, betting_round)][Seat]

    # (2018) Delete this later. just for testing if rounds are 
    # started from 0, esp at preflop stage        
    shout("shouting from read_and_save_bets(), bets_cache is: %s"%bets_cache) 
    save_variables()


### Read_Bets & dinctionaries & Reset var funcs Ended ***********************************************************************************************************************
            

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
    paint.enabled = True # for cmd use
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
            determine_small_blind_seat()
            determine_big_blind_seat()
            determine_dealer_seat()       


                    
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
            



