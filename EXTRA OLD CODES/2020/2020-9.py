
while True :

    preflop_stage = False ; flop_stage = False ; turn_stage = False ; river_stage = False 
""
    if bot_status == True :

        shout("****** Running bot_status == True Section ******"
              , color = 'on_green')
        reset_just_do_check_fold_to_false() #

        reset_table_information() #

        if pm.my_seat_won_pixel(game_position,  my_seat_number ) == False :
            My_Bank = ocr_my_bank(game_position, my_seat_number )
            if My_Bank != None :
                if My_Bank >= 15 * BLIND_VALUE :
                    shout("My Bank is:%s" %My_Bank, color = 'light_green')
                elif My_Bank != 0 :
                    shout("My Bank is:%s" %My_Bank, color = 'light_green')
                    shout("Rebuying...")
                    pass # Later i'll build
        else :
            shout("My Bank can't be read")
            My_Bank = None
        
        Hand_End_Cheker1 = hand_is_ended()
        while Hand_End_Cheker1 :
            Hand_End_Cheker1 = hand_is_ended()

        if pm.active_player_pixel(game_position, my_seat_number) != True \
        or ( pm.active_player_pixel(game_position, my_seat_number) == True \
            and pm.notification_banner_pixel(game_position, my_seat_number) == True ):
            read_and_global_banks_and_names() 
        else :
            shout("Players Info is not Read", color = 'on_light_red')





        time02 = 0 ; fo = 0 
        time1 = time.time()
        Cards1 = False
        shout("Looking for cards in bot_status == True Section..."
              , color = 'light_magenta')
        while Cards1 == False and time02 < 5 * 60 : #being alone time
            Cards1 = pm.player_cards_pixel(game_position,  my_seat_number )
            time2 = time.time() - time1
            n60 = ( time2 - 120 ) // 60
            if not time2 < 2 * 60 and n60 >= fo :
                fix_game_disruption("1")
                fo += 1
                time02 = time.time() - time1                

        if not time02 < 5 * 60 : #being alone time
            raise Exception("0.1.No one join, time to exit. Or Game is locked, force to restart(will be build in future), bot_status == None")






        if Cards1 == True :
            if pm.pre_flop_pixel(game_position) == False or ( pm.pre_flop_pixel(game_position) == True and is_there_any_raiser() == True) :
                set_just_do_check_fold_to_true("this is Ok! Becuase i may start program from middle of the game")

            bot_status = False
            shout("Cards are founded", color = 'light_magenta')
            shout ("****** First hand Started ******", color = 'on_green')


    elif bot_status == None :
        raise Exception("5.This can not happen IN FUTURE becuase main menu automation is built\
                        ( fix_game_disruption --> Sit_In --> table is full --> exit -->\
                        bot_status = None --> main menu --> bot_status = True )")

""

#-------    

    if Hand_End_Cheker1 == False and pm.pre_flop_pixel(game_position) == False \
    and bot_status == False and just_do_check_fold != True :
        fix_game_disruption("2")
        set_just_do_check_fold_to_true("2")
        screenshot_error('6. pm.pre_flop_pixel() == False')
    elif Hand_End_Cheker1 == False and bot_status == False and just_do_check_fold != True :
        Pre_Flop1 = True #(2020: Pre_Flop1 has no usage)
        preflop_stage = True

    if Hand_End_Cheker1 == False and pm.player_cards_pixel(game_position,  my_seat_number ) == True and bot_status == False :  
        read_and_global_my_cards() #
        play_sound() #


    its_my_turn = False
    Gray1 = True ; fo = 0 
    time1 = time.time()
    shout("Looking for light...", color = 'light_magenta') 
    while Hand_End_Cheker1 == False and (its_my_turn == False or Gray1 == True) and flop_stage == False and bot_status == False and time.time() - time1 < 5 * 60 :
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
        raise Exception("5.1.Game is locked, force to restart, bot_status == None")

    if flop_stage == True :
        set_just_do_check_fold_to_true("1.5")
        screenshot_error("6.5 Pre Flop is Jumped, game must lagged")
        
         
    preflop_betting_round = 0 #(2018) shouldn't it be -1 ?! test it by printing for example player_cards_cache dic which prints rounds too
    if pm.active_player_pixel(game_position,  my_seat_number ) == True and Gray1 == False and hand_is_ended() == False and flop_stage == False and bot_status == False :
        preflop_betting_round += 1
        shout("light is founded", color = 'light_magenta')
        read_and_save_bets() #
        click_decision() # preflop
    elif hand_is_ended() == False and flop_stage == False and bot_status == False :
        fix_game_disruption("4 Entering This section is not possible")
        screenshot_error("6.6 Entering This section is not possible")
        #(2018) shouldn't preflop_betting_round += 1 line be here too ?!
        read_and_save_bets() #
        click_decision() # preflop



# PreFlop: -------


    if bot_status == False :

        shout("Running PreFlop Section")
        time01 = time.time()
        time02 = time.time() - time01
        
        while Hand_End_Cheker1 == False and flop_stage == False and time02 < 5 * 60 and bot_status == False :

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
            raise Exception("8.I should work on main menu automation later!(game is locked maybe, force to exit or restart),bot_status == None mishavad")
            fix_game_disruption("6")


# Flop: -------


    if bot_status == False :

        shout("Running Flop Section")
        time01 = time.time()
        time02 = time.time() - time01
        flop_betting_round = -1
        while Hand_End_Cheker1 == False and turn_stage == False and time02 < 5 * 60 and bot_status == False :

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
            raise Exception("10.I should work on main menu automation later!(game is locked maybe, force to exit or restart),bot_status == None mishavad")
            fix_game_disruption("8")    



# Turn: -------

    
    if bot_status == False :

        shout("Running Turn Section")
        time01 = time.time()
        time02 = time.time() - time01
        turn_betting_round = -1
        while Hand_End_Cheker1 == False and river_stage == False and time02 < 5 * 60 and bot_status == False :

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
            raise Exception("12.I should work on main menu automation later!(game is locked maybe, force to exit or restart),bot_status == None mishavad")
            fix_game_disruption("10")            
            

# River: -------


    if bot_status == False :

        shout("Running River Section")
        time01 = time.time()
        time02 = time.time() - time01
        river_betting_round = -1
        while Hand_End_Cheker1 == False and time02 < 5 * 60 and bot_status == False :

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
            raise Exception("14.I should work on main menu automation later!(game is locked maybe, force to exit or restart),bot_status == None mishavad")
            fix_game_disruption("12")            
            


#-------
            
    if Hand_End_Cheker1 == True and bot_status == True :

        declare_the_winners()
        shout ("-------- Hand Ended --------", color = 'on_green')

    if Hand_End_Cheker1 == True and bot_status == False :

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
            raise Exception("15.Game is locked, force to restart, bot_status == None")
            


    if Hand_End_Cheker1 == False and bot_status == False :

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
            raise Exception("16.No one join, time to exit. Or Game is locked, force to restart, bot_status == None")

        elif bot_status == False :
            shout ("-------- New Hand Started --------", color = 'on_green')
            shout ("Coins are Founded")
            config.determine_small_blind_seat()
            config.determine_big_blind_seat()
            config.determine_dealer_seat()       


                    
            time02 = 0 ; fo = 0 
            time1 = time.time()
            Cards1 = False
            shout("Looking for cards...", color = 'light_magenta')
            while Hand_End_Cheker1 == False and Cards1 == False and bot_status == False and time02 < 1.5 * 60 :
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
                raise Exception("17.Game is locked, force to restart, bot_status == None")

            if Cards1 == True :
                shout("Cards are founded", color = 'light_magenta')

            elif not time02 < 1.5 * 60 :
                fix_game_disruption("15")

            if Hand_End_Cheker1 == True and Cards1 == False :
                fix_game_disruption("16. I am maybe out")
            



