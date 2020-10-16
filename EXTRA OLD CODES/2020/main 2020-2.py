def hand_is_ended():
    """
    This is an important function, because it determines
    when new hand will start.
    For cheet: 
    1.Yellow around winning cards 
    2.If everyone fold the somebodies raise, only one player have cards.
    """
    for seat in [1,2,3,4,5]:
        if pm.my_seat_won_pixel(game_position, seat):
            return True
        if pm.other_seat_won_pixel(game_position, seat):
            return True
    return False

def rebuy_if_bank_is_low(min_blinds = 15):
    global BLIND_VALUE
    my_bank = ocr_my_bank()
    if my_bank == None :
        shout("My bank can't be read")
    elif my_bank != None :
        shout(paint.light_green.bold("My bank is:%s" %my_bank))
        if 0 < my_bank <= min_blinds * BLIND_VALUE:
            shout("Rebuying...")
            pass # Later i'll build

def wait_for_first_hand(waiting_minutes = 5):
    global waiting_for_first_hand

    shout("Looking for cards in 'WAITING_FOR_FIRST_HAND' Section..."
          , color = 'light_magenta')
    start_time = time.time()
    fixing_retry = 1
    while (not pm.player_cards_pixel(game_position,  my_seat_number) 
           and time.time()-start_time < 60*waiting_minutes) :

        if ( (time.time()-start_time) > (60*waiting_minutes)/3 
            and fixing_retry <= 1) :
            fixing_retry += 1
            fix_game_disruption()

    if time.time() - start_time >= 60 * waiting_minutes :
        waiting_for_first_hand = None
        shout("No one join the table, call operator ")
    # My cards pixel is founded:
    else:
        shout("My cards are founded", color = 'light_magenta')
        waiting_for_first_hand = False
        # I may have had run again program from middle of the game
        # If I've resume the game, set waiting_for_first_hand = True
        if (not pm.pre_flop_pixel(game_position)  
            or (pm.pre_flop_pixel(game_position) 
                and is_there_any_raiser() )) :
            set_just_do_check_fold_to_true("program is started again "\
                                           "from middle of the game")
            
def stages_are_sequenced():
    if (pm.river_pixel() and
        False in (config.preflop_stage, config.flop_stage, config.river_stage)):
        return False
    if pm.turn_pixel() and False in (config.preflop_stage, config.flop_stage):
        return False
    if pm.flop_pixel() and config.preflop_stage == False:
        return False
    return True

def shifted_to_next_stage():
    if config.preflop_stage and not config.flop_stage and pm.flop_pixel():
        return True
    if config.flop_stage and not config.turn_stage and pm.turn_pixel():
        return True
    if config.turn_stage and not config.river_stage and pm.river_pixel():
        return True
    return False

def read_board_cards_and_update_stage():
    if config.preflop_stage and not config.flop_stage and pm.flop_pixel():
        config.flop_stage = True
        read_and_global_flop_cards()
        if waiting_for_first_hand == False:
            shout("Waiting for my turn at flop_stage...", 'light_magenta') 
    if config.flop_stage and not config.turn_stage and pm.turn_pixel():
        config.turn_stage = True
        read_and_global_turn_card()
        if waiting_for_first_hand == False:
            shout("Waiting for my turn at turn_stage...", 'light_magenta') 
    if config.turn_stage and not config.river_stage and pm.river_pixel():
        config.river_stage = True
        read_and_global_river_card()
        if waiting_for_first_hand == False:
            shout("Waiting for my turn at river_stage...", 'light_magenta') 

def its_my_turn():
    if pm.active_player_pixel(config.game_position, config.my_seat_number):
        shout("It is my turn now", color = 'light_magenta')
        return True
    return False

def update_betting_rounds():
    if config.preflop_stage and not config.flop_stage:
        config.preflop_betting_round += 1
        shout('TESTING. preflop_betting_round is:%s'
              %config.preflop_betting_round, color = 'on_light_red')
    if config.flop_stage and not config.turn_stage:
        config.flop_betting_round += 1
        shout('TESTING. flop_betting_round is:%s'
              %config.flop_betting_round, color = 'on_light_red')
    if config.turn_stage and not config.river_stage:
        config.turn_betting_round += 1
        shout('TESTING. turn_betting_round is:%s'
              %config.turn_betting_round, color = 'on_light_red')
    if config.river_stage:
        config.river_betting_round += 1
        shout('TESTING. river_betting_round is:%s'
              %config.river_betting_round, color = 'on_light_red')


waiting_for_first_hand = True
while True:

    reset_just_do_check_fold_to_false() 
    reset_table_information() 

    if waiting_for_first_hand == True:
        shout("* bot_status == 'WAITING_FOR_FIRST_HAND' *",color = 'on_green')
        rebuy_if_bank_is_low(min_blinds = 15)
        read_and_global_banks_and_names()
        # Looks for my cards pixel to start first hand
        # Inside it shout looking for my cards TO START FIRST HAND 
        # and shout my cards founded with light_magenta
        # They will be shouted again at wait_for_my_hand_to_be_dealt() unfortunately
        # It changes waiting_for_first_hand to: 1.False if my cards founded.
        # 2.None if time is passed.
        wait_for_first_hand(waiting_minutes = 5)
        # It set global new_hand to False, to pass the 'if new_hand:' inside
        # waiting_for_first_hand == False section.
        # I may have resume from middle of the game, so it better to use
        # this function instead of using 'new_hand = False' line
        wait_celebration_ends(waiting_seconds = 10) #not defined yet
        
    elif waiting_for_first_hand == None:
        shout("* bot_status == 'ON_MAIN_MENU' *", color = 'on_green')
        raise Exception("5.This can not happen IN FUTURE because main "\
                        "menu automation is built " \
                        "( fix_game_disruption --> Sit_In --> "\
                        "table is full --> exit --> "\
                        "waiting_for_first_hand = None --> main menu "\
                        "--> waiting_for_first_hand = True )")






def wait_celebration_ends(waiting_seconds = 10):
    global new_hand

    t1 = time.time()
    while True:
        new_hand = hand_is_ended()
        if not new_hand:
            break
        if time.time() - t1 > waiting_seconds:
            fix_game_disruption('game is stuck')
            break
    # sleep time so buttons and cards are dealt properly
    time.sleep(1)
        

def sb_b_d_buttons_are_founded():
    """For cheet there is no small or big blind buttons"""
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

def wait_for_sb_b_d_buttons(waiting_seconds = 5):

    t1 = time.time()
    while True:
        if sb_b_d_buttons_are_founded():
            break
        if time.time() - t1 > waiting_seconds:
            fix_game_disruption('buttons are not founded')
            break

def wait_for_my_new_hand_to_be_dealt(waiting_minutes = 10): #not completed

    t1 = time.time()
    while True:
        if pm.player_cards_pixel(game_position,  my_seat_number):
            shout()
            break






    # Now I'm in the game
    elif waiting_for_first_hand == False:
        if new_hand: 
            declare_the_winners()
            # Inside it: if time is past, do sth else 
            # while hand_is_ended(): pass ;new_hand = False
            wait_celebration_ends(waiting_seconds = 10) #not defined yet
        shout("* bot_status == 'I_AM_PLAYING' *")
        # Inside it if cards are founded set config.preflop_stage = True
        # shout looking for my cards and my cards founded with light_magenta
        # If there is no other player or i'm not in 
        # or i'm in but there is no other players for a long time
        # or time is past, do sth else
        shout("Looking for cards in 'I_AM_PLAYING' Section...", 'light_magenta')
        wait_for_my_new_hand_to_be_dealt(waiting_minutes = 10) #not defined yet
        if waiting_for_first_hand != False or new_hand: continue
        shout("My cards are founded", color = 'light_magenta')
        shout ("-------- New Hand Started --------", color = 'on_green')
        # If time is past, do sth else
        wait_for_sb_b_d_buttons(waiting_seconds = 5) 
        # use this statment after functions which use fix_game_disruption()
        if waiting_for_first_hand != False: continue
        # global new_hand = hand_is_ended() inside waiting functions
        if new_hand: continue 
        determine_dealer_seat()
        determine_big_blind_seat()
        determine_small_blind_seat() # Reduce 3 functions to 1 and then change function name
        read_and_global_my_cards() # Change function name to a better one
        rebuy_if_bank_is_low(min_blinds = 15)
        read_and_global_banks_and_names()
        if waiting_for_first_hand != False: continue
        play_sound_for_good_starting_hands()

        shout("Waiting for my turn at preflop_stage...", 'light_magenta') 
        t1 = time.time()
        # Playing a whole hand in this loop
        while True:
            if its_my_turn():
                update_betting_rounds()
                read_and_save_bets()
                if waiting_for_first_hand == False:
                    click_decision() # Transfer the function to this module
            if shifted_to_next_stage(): 
                read_board_cards_and_update_stage()
                if not stages_are_sequenced():
                    set_just_do_check_fold_to_true('stages are not sequenced')
                    screenshot_error('stages are not sequenced')
            if t1 - time.time() > 5 * 60:
                fix_game_disruption('This hand last more than 5 minutes')
            new_hand = hand_is_ended()
            if new_hand:
                shout ("-------- Hand ended --------", color = 'on_green')
                break
            if waiting_for_first_hand != False:
                break

    else:
        # change None, True, False to 'ON_MAIN_MENU', 'I_AM_PLAYING', WAITING_FOR_FIRST_HAND
        raise Exception('waiting_for_first_hand is only None or False or True')

