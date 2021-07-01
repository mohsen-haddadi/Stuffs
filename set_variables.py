#OK
import config
from iprint import shout
import screen_monitoring.find_game_position.find_game_position as find_game_position
import screen_monitoring.pixel_matching.pixel_matching as pm
from readability.ocr import ocr_bet, ocr_other_players_bank, ocr_my_bank, ocr_other_names, ocr_my_name
from readability.fix_game_disruption import set_just_do_check_fold_to_true,\
reset_just_do_check_fold_to_false

#testing sub packages imports
test = False
if test == True:
    config.game_position = find_game_position.find_game_reference_point()
    #print(read_cards.read_flop_cards(game_position))
    #decision_making.rules_and_info.flush.load_variables()
    input("wait")


def set_all_variables_to_none():
    """By running the program every time, we'll make sure config 
    variables are cleaned off the last run"""
    config.game_position , config.DATED_REPORT_FOLDER , config.REPORTS_DIRECTORY,\
    config.preflop_stage , config.flop_stage , config.turn_stage , config.river_stage ,\
    config.preflop_betting_round , config.flop_betting_round ,\
    config.turn_betting_round , config.river_betting_round ,\
    config.board_card_1th , config.board_card_2th , config.board_card_3th ,\
    config.board_card_4th, config.board_card_5th , config.my_1th_card , config.my_2th_card ,\
    config.my_seat_number , config.MY_PROFILE_NAME ,\
    config.just_do_check_fold , config.bot_status , config.new_hand,\
    config.player_cards_cache , config.white_chips_cache , config.red_chips_cache , config.bets_cache ,\
    config.last_white_chips_cache , config.last_red_chips_cache ,\
    config.last_player_cards_cache , config.last_bets_cache, config.seats_not_folded,\
    config.did_i_raised_at  , config.my_last_raise_at ,\
    config.players_name , config.players_bank , config.last_players_bank, config.playing_seats,\
    config.BLIND_VALUE , config.TOTAL_SEATS ,\
    config.small_blind_seat , config.big_blind_seat , config.dealer_seat,\
    config.hand_number, config.game_number, config.scenario_list,\
    config.csv_path = (None,)*47

def turn_finder(starter_seat , xth) :
    """Returns the seat number; for instance; (4,1) returns seat 4!"""
    answer = (starter_seat - 1 + xth ) % c.TOTAL_SEATS
    if answer == 0 :
        return c.TOTAL_SEATS
    else :
        return answer

def determine_small_big_dealer_seats(): #💊

    for seat in range(1, config.TOTAL_SEATS+1):
        if pm.dealer_pixel(config.game_position, seat):
            shout("Dealer is on seat %s" %seat)
            config.dealer_seat = seat
            break

    config.small_blind_seat = None
    config.big_blind_seat = None

    for i in range(1, len(config.TOTAL_SEATS) + 1):
        seat = turn_finder( config.dealer_seat , i )
        if pm.player_chips_pixel(seat):
            # Modify this line if at other websites 
            # small and big blinds are equal.
            if ocr_bet(seat) / config.BLIND_VALUE < 1:
                config.small_blind_seat = seat
                    for i in range(1, len(config.TOTAL_SEATS) + 1):
                        seat = turn_finder( config.small_blind_seat , i )
                            if pm.player_chips_pixel(seat):
                                if ocr_bet(seat) / config.BLIND_VALUE == 1:
                                    config.big_blind_seat = seat
    if None in (config.small_blind_seat, config.big_blind_seat):
        set_just_do_check_fold_to_true('small or big blind seat have not been set')
    else:
        shout("Small blind is on seat %s" %config.small_blind_seat)
        shout("Big blind is on seat %s" %config.big_blind_seat)


def determine_playing_seats():
    """
    playing_seats dictionary is used for calculating 
    my seat positioning ranking. # NOT ANYMORE #💊
    Seated out players waiting for their first big blinds are not counted.
    """
    for seat in range(1, config.TOTAL_SEATS+1):
        if ( not pm.available_seat_pixel(config.game_position, seat)
             and pm.player_cards_pixel(config.game_position, seat) ):
            config.playing_seats[seat] = True
        else:
            config.playing_seats[seat] = False

    shout("TEST. playing_seats dictionary is: %s" %config.playing_seats 
          , color = 'on_light_red')
            

### Read_Bets & dinctionaries & Reset var funcs: ****************************************************************************************************************************

def white_chips(seat):
    # It checks if there is a white colored chips in front of a seat,
    # by returning True or False, to find out if a player has call or not
    #global game_position
        config.last_bets_cache[Seat] \
        = config.bets_cache["%s %s" %(stage, betting_round)][Seat]

    


    if not pm.player_chips_pixel(config.game_position, seat):
        return False
    for i in range(1, config.TOTAL_SEATS+1):
        if c.preflop_stage and not c.flop_stage:
            if

        

def red_chips(seat):
    """It checks if there is a red colored chips in front of a seat,
    by returning True or False, to find out if a player has bet/raised or not.
    (In accordance to Google: 'A bet is the first wager of a round.')
    """
    #global game_position

    if pm.player_chips_pixel(config.game_position, seat):
        return pm.are_chips_white_or_red_pixel(config.game_position, seat)
    else :
        return False

def read_and_save_banks_and_names() :
    #global game_position, players_name , players_bank , my_seat_number

    # First ocr my bank and name, so if we get a problem it will use
    # fix_game_disruption() function inside ocr_my_bank() and ocr_my_name()
    # because ocr_other_players_bank() and ocr_other_names() don't have 
    # fix_game_disruption()
    for seat in range(1, config.TOTAL_SEATS+1):
        if config.my_seat_number == seat:
            config.players_bank[config.my_seat_number] = ocr_my_bank()
            config.players_name[config.my_seat_number] = ocr_my_name()
        elif pm.other_player_seated_pixel(config.game_position, seat) == True:
            config.players_bank[seat] = ocr_other_players_bank(seat)
            config.players_name[seat] = ocr_other_names(seat)
            if red_chips(seat) :
                config.players_bank[seat] = None
    shout("TEST. Players Bank dictionary is: %s" %config.players_bank 
          , color = 'on_light_red')
    shout("TEST. Players Name dictionary is: %s" %config.players_name 
          , color = 'on_light_red')

def read_banks():
    for seat in range(1, config.TOTAL_SEATS+1):
        if config.my_seat_number == seat:
            config.last_players_bank[config.my_seat_number] = ocr_my_bank()
        elif pm.other_player_seated_pixel(config.game_position, seat) == True:
            config.last_players_bank[seat] = ocr_other_players_bank(seat)

def reset_table_information() : 
    """
    IT'S DONE: preflop_betting_round ,...,river_betting_round & preflop_stage 
    ,...,river_stage dar loope while True baresi va be in func
    baraye reset shodan enteghal dade shavand 
    """
    #global players_name , players_bank ,\
    #       player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    #       last_player_cards_cache , last_white_chips_cache , last_red_chips_cache , last_bets_cache,\
    #       did_i_raised_at , my_last_raise_at , preflop_betting_round , flop_betting_round , turn_betting_round , river_betting_round

    shout("Reseting table information")
    reset_just_do_check_fold_to_false()
    config.scenario_list = []
    config.playing_seats = {}
    config.players_name = {}
    config.players_bank = {}
    config.last_players_bank = {}
    for Seat in range(1, config.TOTAL_SEATS+1):
        config.players_name[Seat] = None
        config.players_bank[Seat] = None
        config.last_players_bank[Seat] = None
    config.player_cards_cache = {}
    config.white_chips_cache = {} 
    config.red_chips_cache = {}
    config.bets_cache = {}
    config.last_player_cards_cache = {}  
    config.last_white_chips_cache = {}   
    config.last_red_chips_cache = {}   
    config.last_bets_cache = {}

    # Make sure while starting the code did_i_raised_at is defined 
    # by reset_table_information() before first deciding; 
    # otherwise did_i_raise_sofar() at supporting funcs file will error
    config.did_i_raised_at = {"Pre_Flop": False , "Flop": False ,
                       "Turn": False , "River": False } 
    config.my_last_raise_at = {}
    # (2018) Later make sure if all rounds are starting from 0 in 
    # main While True loop (Round_... = 0 should be implemented in 
    # read_and_save_bets() for all stages so for example 
    # bets_cache dictionary surely will "have Round_... 0"). 
    # For testing i have put a shout(bets_cache) at the end of 
    # read_and_save_bets() function 
    config.preflop_betting_round = -1
    config.flop_betting_round = -1
    config.turn_betting_round = -1
    config.river_betting_round = -1
    # if a stage is True, previous stages are also True
    config.preflop_stage = False 
    config.flop_stage = False 
    config.turn_stage = False 
    config.river_stage = False 

def read_and_save_bets() :
    #global game_position, player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    #       last_white_chips_cache , last_red_chips_cache , last_player_cards_cache , last_bets_cache,\
    #       preflop_betting_round , flop_betting_round , turn_betting_round , river_betting_round ,\
    #       preflop_stage , flop_stage , turn_stage , river_stage


    if config.preflop_stage == True and config.flop_stage == False :
        stage = "Pre_Flop"
        betting_round = config.preflop_betting_round
    elif config.flop_stage == True and config.turn_stage == False :
        stage = "Flop"
        betting_round = config.flop_betting_round        
    elif config.turn_stage == True and config.river_stage == False :
        stage = "Turn"
        betting_round = config.turn_betting_round
    elif config.river_stage == True :
        stage = "River"
        betting_round = config.river_betting_round

    config.player_cards_cache["%s %s" %(stage, betting_round)] = {}
    config.white_chips_cache["%s %s" %(stage, betting_round)] = {}
    config.red_chips_cache["%s %s" %(stage, betting_round)] = {}
    config.bets_cache["%s %s" %(stage, betting_round)] = {}
    config.last_player_cards_cache = {}
    config.last_white_chips_cache = {}
    config.last_red_chips_cache = {}
    config.last_bets_cache = {}
    
    for Seat in range(1, config.TOTAL_SEATS+1):

        config.player_cards_cache["%s %s" %(stage, betting_round)][Seat] \
        = pm.player_cards_pixel(config.game_position, Seat)

        if pm.player_chips_pixel(config.game_position, seat): #💊
            config.bets_cache["%s %s" %(stage, betting_round)][Seat] = ocr_bet(Seat)

            if config.last_white_chips_cache[Seat] == True : 
                shout("Seat%s Call: $%s" 
                      %(Seat, 
                        config.bets_cache["%s %s" %(stage, betting_round)][Seat])
                      , color = 'light_green')

            elif config.last_red_chips_cache[Seat] == True :
                shout("Seat%s Raise: $%s" 
                      %(Seat, 
                        config.bets_cache["%s %s" %(stage, betting_round)][Seat])
                      , color = 'light_green')
        else :
            config.bets_cache["%s %s" %(stage, betting_round)][Seat] = None

        config.last_bets_cache[Seat] \
        = config.bets_cache["%s %s" %(stage, betting_round)][Seat]

    for Seat in range(1, config.TOTAL_SEATS+1):
        config.white_chips_cache["%s %s" %(stage, betting_round)][Seat] \
        = white_chips(Seat)
        config.red_chips_cache["%s %s" %(stage, betting_round)][Seat] \
        = red_chips(Seat) #💊
        config.last_player_cards_cache[Seat] \
        = config.player_cards_cache["%s %s" %(stage, betting_round)][Seat]
        config.last_white_chips_cache[Seat] \
        = config.white_chips_cache["%s %s" %(stage, betting_round)][Seat]
        config.last_red_chips_cache[Seat] \
        = config.red_chips_cache["%s %s" %(stage, betting_round)][Seat]

    # (2018) Delete this later. just for testing if rounds are 
    # started from 0, esp at preflop stage        
    shout("shouting from read_and_save_bets(), bets_cache is: %s"%config.bets_cache) 
