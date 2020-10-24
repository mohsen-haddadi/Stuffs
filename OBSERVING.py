def wait_hand_ends_when_observing(waiting_minutes = 5):
    shout('waiting till current hand ends...')
    t1 = time.time()
    fixing_retry = 1
    while True:
        config.new_hand = hand_is_ended()
        if config.new_hand:
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
            break
        if (time.time()-t1) > ((60*waiting_minutes)/4) and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()
        if time.time() - t1 > 60 * waiting_minutes :
            config.bot_status = 'ON_MAIN_MENU'
            shout("No hand ending after %s minutes, "\
            	  "call operator to go to main menu" %waiting_minutes)
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 


def wait_new_hand_starts_when_observing(waiting_minutes = 30):
    shout('waiting new hand starts by looking for dealer button...')
    t1 = time.time()
    fixing_retry = 1
    while True:
        if sb_b_d_buttons_are_founded():
            break
        if (time.time()-t1) > ((60*waiting_minutes)/4) and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()
        if time.time() - t1 > 60 * waiting_minutes :
            config.bot_status = 'ON_MAIN_MENU'
            shout("No one join the table after %s minutes, "\
                  "call operator to go to main menu" %waiting_minutes)
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def am_i_in_or_not():

    for i in range(1,6):
        if pm.i_am_seated_pixel(config.game_position, i) :
            config.my_seat_number = i
            return True
    config.my_seat_number = None
    return False



def bot_is_observing():
    wait_hand_ends_when_observing(waiting_minutes = 30)
    while True:
        if config.bot_status != 'OBSERVING': 
            break
        shout("* bot_status == 'OBSERVING' *",color = 'on_green')
        reset_table_information()
        wait_new_hand_starts_when_observing(waiting_minutes = 30)
        shout ("-------- New Hand Started --------", color = 'on_green')
        if config.bot_status != 'OBSERVING':
            break
        # use this statement after waiting functions 
        # which uses config.new_hand = hand_is_ended()
        if config.new_hand: 
            continue
        determine_small_big_dealer_seats()
        if am_i_in_or_not():
            if pm.player_cards_pixel(config.game_position
                                     , config.my_seat_number):
                read_and_save_my_cards()
                play_sound_for_good_starting_hands()
        read_and_save_banks_and_names()

        # Playing a whole hand in this loop
        observing_a_hand()
        if config.bot_status != 'OBSERVING':
            break
        if config.new_hand: 
            continue
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            break 

def observing_a_hand():
    """Use wait_hand_ends_when_observing() before all breaks, 
    except one which ended without any problem.
    """
    t1 = time.time()
    while True:
        if shifted_to_next_stage(): 
            read_board_cards()
            if not stages_are_sequenced():
                shout("Stages are not sequenced",color = 'on_light_red')
                screenshot_error('stages are not sequenced')
                wait_hand_ends_when_observing(waiting_minutes = 30)
                break # new line
        if its_my_turn(): #if some has bet
            update_betting_rounds()
            read_and_save_bets()
            if config.bot_status == 'I_AM_PLAYING':
                click_decision() #🌏🌱♣♠♦♥🌱🌏
        if t1 - time.time() > 5 * 60:
            config.bot_status = 'WAITING_FOR_FIRST_HAND'
            fix_game_disruption('This hand last more than 5 minutes')
            wait_hand_ends_when_observing(waiting_minutes = 30)
            break # new line
        config.new_hand = hand_is_ended()
        if config.new_hand:
            declare_the_winners()
            wait_celebration_ends(waiting_seconds = 10)
            # Hand is ended without any problem. Save statistical data here.
            shout('I should save statistical data here later.', 'rainbow')
            shout ("-------- Hand ended --------", color = 'on_green')
            break
        if config.bot_status != 'OBSERVING': # will not be used
            break
        if game_is_paused():
            fix_game_disruption('game is unpaused')
            if config.bot_status == 'OBSERVING':
                wait_hand_ends_when_observing(waiting_minutes = 30)
            break 
