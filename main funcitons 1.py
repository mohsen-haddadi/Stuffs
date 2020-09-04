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

    shout("Looking for my cards pixel to start first hand..."
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
        raise Exception("No one join the table, force to restart "\
                        "(will be build in future)")
    # My cards pixel is founded:
    else:
        waiting_for_first_hand = False
        # I may have had run again program from middle of the game
        if (not pm.pre_flop_pixel(game_position)  
            or (pm.pre_flop_pixel(game_position) 
                and is_there_any_raiser() )) :
            set_just_do_check_fold_to_true("program is started again "\
                                           "from middle of the game")
            




while True:

    if waiting_for_first_hand == True :
        reset_just_do_check_fold_to_false() 
        reset_table_information() 
        rebuy_if_bank_is_low(min_blinds = 15)
        # Wait till this loop to end to read_and_global_banks_and_names()
        while hand_is_ended():
            pass
        read_and_global_banks_and_names()
        # Looks for my cards pixel to start first hand
        wait_for_first_hand(waiting_minutes = 5)

    elif waiting_for_first_hand == None :
        raise Exception("5.This can not happen IN FUTURE becuase main "\
                        "menu automation is built " \
                        "( fix_game_disruption --> Sit_In --> "\
                        "table is full --> exit --> "\
                        "waiting_for_first_hand = None --> main menu "\
                        "--> waiting_for_first_hand = True )")

    # Now i'm in the game, waiting_for_first_hand == False
    #
    # At the end run while hand_is_ended(): pass 
    # to make sure Hand_End_Cheker1 is False
    while not waiting_for_first_hand != False :
        # reset new hand at reset_table_information() to False
        if new_hand: 
            declare_the_winners()

            # If time is past, do sth else
            # Inside it reset_just_do_check_fold_to_false()
            # and reset_table_information()
            # while hand_is_ended(): pass ;new_hand = False
            wait_celebration_ends() 
        # If time is past or there is no other player , do sth else
        wait_for_sb_b_d_buttons()
        # If there is no other player or i'm not in 
        # or time is past, do sth else
        wait_for_my_hand_to_be_dealt()

        # use this statment after functions which use fix_game_disruption()
        if waiting_for_first_hand != False: break
        # global new_hand = hand_is_ended() inside functions
        if new_hand: continue 
        determine_dealer_seat()
        determine_big_blind_seat()
        determine_small_blind_seat()    

        read_and_global_my_cards() 

        if waiting_for_first_hand != False: break
        play_sound()



        shout("Looking for my turn to come at preflop_stage..."
              , color = 'light_magenta') 
        # If time is past, or not pm.pre_flop_pixel 
        # or hand_is_ended(), do sth else
        wait_for_my_turn() # set _stage = True
        if waiting_for_first_hand != False: break
        if new_hand: continue
        read_and_save_bets()
        if waiting_for_first_hand != False: break
        click_decision() # preflop

        shout("Looking for my turn to come at flop_stage..."
              , color = 'light_magenta') 
        # If time is past, or not pm.flop_pixel 
        # or hand_is_ended(), do sth else
        wait_for_my_turn() # set _stage = True
        if waiting_for_first_hand != False: break
        if new_hand: continue
        read_and_save_bets()
        if waiting_for_first_hand != False: break
        click_decision() # preflop

        shout("Looking for my turn to come at turn_stage..."
              , color = 'light_magenta')  
        # If time is past, or not pm.turn_pixel 
        # or hand_is_ended(), do sth else
        wait_for_my_turn() # set _stage = True
        if waiting_for_first_hand != False: break
        if new_hand: continue
        read_and_save_bets()
        if waiting_for_first_hand != False: break
        click_decision() # preflop

        shout("Looking for my turn to come at river_stage..."
              , color = 'light_magenta')  
        # If time is past, or not pm.river_pixel 
        # or hand_is_ended(), do sth else
        wait_for_my_turn() # set _stage = True
        if waiting_for_first_hand != False: break
        if new_hand: continue
        read_and_save_bets()
        if waiting_for_first_hand != False: break
        click_decision() # preflop