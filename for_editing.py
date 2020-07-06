def rebuy_if_bank_is_low(min_blinds = 15):
    my_bank = ocr_my_bank(game_position, my_seat_number)
    if my_bank == None :
        shout("My bank can't be read")
    elif my_bank != None :
        shout(paint.light_green.bold("My bank is:%s" %my_bank))
        if 0 < my_bank <= min_blinds * BLIND_VALUE:
            shout("Rebuying...")
            pass # Later i'll build

def wait_for_first_hand(waiting_minutes = 5):
    global waiting_for_first_hand

    shout(paint.light_magenta.bold("Looking for my cards pixel to start first hand..."))
    start_time = time.time() ; fixing_retry = 1

    while pm.player_cards_pixel(game_position,  my_seat_number) \
    and time.time() - start_time < 60 * waiting_minutes:
        if (time.time() - start_time) > (60 * waiting_minutes) / 3 \
        and fixing_retry <= 1:
            fixing_retry += 1
            fix_game_disruption()

    if time.time() - start_time >= 60 * waiting_minutes :
        waiting_for_first_hand = None
        raise Exception("No one join the table, force to restart \
                        (will be build in future)")
    # My cards pixel is founded:
    else:
        # I may have run again program from middle of the game
        if pm.pre_flop_pixel(game_position) == False or \
        ( pm.pre_flop_pixel(game_position) == True and is_there_any_raiser() == True):
            set_just_do_check_fold_to_true("program is started again\
                                            from middle of the game")




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




