#OK
import configs as c 
from iprint import shout
import screen_monitoring.find_game_position.find_game_position as find_game_position
import screen_monitoring.pixel_matching.pixel_matching as pm
from readability.ocr import ocr_bet, ocr_other_players_bank, ocr_my_bank, ocr_other_names, ocr_my_name
from readability.fix_game_disruption import set_just_do_check_fold_to_true,\
reset_just_do_check_fold_to_false

#testing sub packages imports
test = False
if test == True:
    c.game_position = find_game_position.find_game_reference_point()
    #print(read_cards.read_flop_cards(game_position))
    #decision_making.rules_and_info.flush.load_variables()
    input("wait")


def set_all_variables_to_none():
    """By running the program every time, we'll make sure configs 
    variables are cleaned off the last run"""
    c.game_position , c.DATED_REPORT_FOLDER , c.REPORTS_DIRECTORY,\
    c.preflop_stage , c.flop_stage , c.turn_stage , c.river_stage ,\
    c.preflop_betting_round , c.flop_betting_round ,\
    c.turn_betting_round , c.river_betting_round ,\
    c.board_cards , c.my_hole_cards,\
    c.my_seat_number , c.MY_PROFILE_NAME ,\
    c.just_do_check_fold , c.bot_status , c.new_hand,\
    c.player_cards_cache , c.white_chips_cache , c.red_chips_cache , c.bets_cache ,\
    c.last_white_chips_cache , c.last_red_chips_cache ,\
    c.last_player_cards_cache , c.last_bets_cache, c.seats_not_folded,\
    c.did_i_raised_at  , c.my_last_raise_at ,\
    c.players_name , c.players_bank , c.last_players_bank, c.playing_seats,\
    c.BLIND_VALUE , c.TOTAL_SEATS ,\
    c.small_blind_seat , c.big_blind_seat , c.dealer_seat,\
    c.win_odds , c.next_win_odds_average , c.draw_odds ,\
    c.hand_number, c.game_number, c.scenario_list,\
    c.csv_path = (None,)*45

def turn_finder(starter_seat , xth) :
    """Returns the seat number; for instance; (4,1) returns seat 4!"""
    answer = (starter_seat - 1 + xth ) % c.TOTAL_SEATS
    if answer == 0 :
        return c.TOTAL_SEATS
    else :
        return answer

def determine_small_big_dealer_seats(): #💊 #NOT TESTED

    for seat in range(1, c.TOTAL_SEATS+1):
        if pm.dealer_pixel(c.game_position, seat):
            shout("Dealer is on seat %s" %seat)
            c.dealer_seat = seat
            break

    c.small_blind_seat = None
    c.big_blind_seat = None

    for i in range(1, c.TOTAL_SEATS + 1):
        seat = turn_finder( c.dealer_seat , i )
        if pm.player_chips_pixel(c.game_position, seat):
            # Modify this line if at other websites 
            # small and big blinds are equal.
            bet = ocr_bet(seat, printing = False)
            if bet == None: # to avoid devision Error
                continue
            if bet / c.BLIND_VALUE < 1:
                c.small_blind_seat = seat
                break
    if c.small_blind_seat != None:
        for i in range(1, c.TOTAL_SEATS + 1):
            seat = turn_finder( c.small_blind_seat , i )
            if pm.player_chips_pixel(c.game_position, seat):
                bet = ocr_bet(seat, printing = False)
                if bet == None: # to avoid devision Error
                    continue
                if bet / c.BLIND_VALUE == 1:
                    c.big_blind_seat = seat
                    break
    if None in (c.small_blind_seat, c.big_blind_seat):
        set_just_do_check_fold_to_true('small or big blind seat have not been set')
    else:
        shout("Small blind is on seat %s" %c.small_blind_seat)
        shout("Big blind is on seat %s" %c.big_blind_seat)


def determine_playing_seats():
    """
    playing_seats dictionary is used for calculating 
    my seat positioning ranking. # NOT ANYMORE #💊
    Seated out players waiting for their first big blinds are not counted.
    """
    for seat in range(1, c.TOTAL_SEATS+1):
        if pm.player_cards_pixel(c.game_position, seat): #💊
            c.playing_seats[seat] = True
        else:
            c.playing_seats[seat] = False

    shout("TEST. playing_seats dictionary is: %s" %c.playing_seats 
          , color = 'on_light_red')
            

### Read_Bets & dinctionaries & Reset var funcs: ****************************************************************************************************************************

def white_chips(seat): #💊
    """It checks if there is a white colored chips in front of a seat,
    by returning True or False, to find out if a player has call or not.
    It is not accurate for multi round raises.
    Note: last_bets_cache is needed before using this function,
    therefore read_and_save_bets() should have been implemented before using this function.
    """
    # last_bets_cache = {1: .5,2: 1,3: 2,4: None,5: 2,6: 6} and my_seat_number = 3
    # after this loop bets will be: bets == [2, 0, 2, 6, 0.5, 1]
    bets = []
    for i in range(1, c.TOTAL_SEATS + 1):
        seat_after_me = turn_finder(c.my_seat_number , i)
        if c.last_bets_cache[seat_after_me] != None:
            bets.append(c.last_bets_cache[seat_after_me])
        else:
            bets.append(0)
    #print(f'bets is: {bets}')
    # my_seat_number = 3 and seat = 2, this loop returns seat == 5
    for i in range(1, c.TOTAL_SEATS + 1):
        if turn_finder(c.my_seat_number, i) == seat:
            seat = i - 1
            break
    #print(f'seat is: {seat}')
    #print(f'bet at seat {seat} is: {bets[seat]}')
    # if it is my seat
    if seat == 0:
        if c.preflop_stage == True and c.flop_stage == False :
            stage = "Pre_Flop"
        elif c.flop_stage == True and c.turn_stage == False :
            stage = "Flop"
        elif c.turn_stage == True and c.river_stage == False :
            stage = "Turn"
        elif c.river_stage == True :
            stage = "River"
        try :
            _ = c.my_last_raise_at[stage] # means i have raised 
            return False
        except : # means i have not raised 
            if bets[seat] == 0:
                return False
            else:
                return True
    # if it is not my seat
    elif c.preflop_stage and not c.flop_stage:
        if 0 < bets[seat] <= c.BLIND_VALUE or 0 < bets[seat] <= max(bets[:seat]):
            return True
        else:
            return False
    else:
        if 0 < bets[seat] <= max(bets[:seat]):
            return True
        else:
            return False

def red_chips(seat): #💊
    """It checks if there is a red colored chips in front of a seat,
    by returning True or False, to find out if a player has bet/raised or not.
    (In accordance to Google: 'A bet is the first wager of a round.')
    Note: last_bets_cache is needed before using this function,
    therefore read_and_save_bets() should have been implemented before using this function.
    """
    # last_bets_cache = {1: .5,2: 1,3: 2,4: None,5: 2,6: 6} and my_seat_number = 3
    # after this loop bets will be: bets == [2, 0, 2, 6, 0.5, 1]
    bets = []
    for i in range(1, c.TOTAL_SEATS + 1):
        seat_after_me = turn_finder(c.my_seat_number , i)
        if c.last_bets_cache[seat_after_me] != None:
            bets.append(c.last_bets_cache[seat_after_me])
        else:
            bets.append(0)
    # my_seat_number = 3 and seat = 2, this loop returns 5
    for i in range(1, c.TOTAL_SEATS + 1):
        if turn_finder(c.my_seat_number, i) == seat:
            seat = i - 1
            break
    # if it is my seat
    if seat == 0:
        if c.preflop_stage == True and c.flop_stage == False :
            stage = "Pre_Flop"
        elif c.flop_stage == True and c.turn_stage == False :
            stage = "Flop"
        elif c.turn_stage == True and c.river_stage == False :
            stage = "Turn"
        elif c.river_stage == True :
            stage = "River"
        try :
            _ = c.my_last_raise_at[stage] # means i have raised 
            return True
        except : # means i have not raised
            return False
    # if it is not my seat
    elif c.preflop_stage and not c.flop_stage:
        if bets[seat] > c.BLIND_VALUE and bets[seat] > max(bets[:seat]):
            return True
        else:
            return False
    else:
        if bets[seat] > max(bets[:seat]):
            return True
        else:
            return False

def read_and_save_banks_and_names(): #💊
    #global game_position, players_name , players_bank , my_seat_number

    # First ocr my bank and name, so if we get a problem it will use
    # fix_game_disruption() function inside ocr_my_bank() and ocr_my_name()
    # because ocr_other_players_bank() and ocr_other_names() don't have 
    # fix_game_disruption()
    for seat in range(1, c.TOTAL_SEATS+1):
        if c.my_seat_number == seat:
            c.players_bank[c.my_seat_number] = ocr_my_bank()
            c.players_name[c.my_seat_number] = ocr_my_name()
        elif pm.other_player_seated_pixel(c.game_position, seat) == True:
            c.players_bank[seat] = ocr_other_players_bank(seat)
            c.players_name[seat] = ocr_other_names(seat)
            if pm.player_chips_pixel(c.game_position, seat): #💊
                bet = ocr_bet(seat, printing = False) #💊
                if bet != None and c.players_bank[seat] != None: #💊
                    c.players_bank[seat] = c.players_bank[seat] + bet #💊
    shout("TEST. Players Bank dictionary is: %s" %c.players_bank 
          , color = 'on_light_red')
    shout("TEST. Players Name dictionary is: %s" %c.players_name 
          , color = 'on_light_red')

def read_banks():
    for seat in range(1, c.TOTAL_SEATS+1):
        if c.my_seat_number == seat:
            c.last_players_bank[c.my_seat_number] = ocr_my_bank()
        elif pm.other_player_seated_pixel(c.game_position, seat) == True:
            c.last_players_bank[seat] = ocr_other_players_bank(seat)

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
    c.scenario_list = []
    c.playing_seats = {}
    c.players_name = {}
    c.players_bank = {}
    c.last_players_bank = {}
    for Seat in range(1, c.TOTAL_SEATS+1):
        c.players_name[Seat] = None
        c.players_bank[Seat] = None
        c.last_players_bank[Seat] = None
    c.player_cards_cache = {}
    c.white_chips_cache = {} 
    c.red_chips_cache = {}
    c.bets_cache = {}
    c.last_player_cards_cache = {}  
    c.last_white_chips_cache = {}   
    c.last_red_chips_cache = {}   
    c.last_bets_cache = {}

    # Make sure while starting the code did_i_raised_at is defined 
    # by reset_table_information() before first deciding; 
    # otherwise did_i_raise_sofar() at supporting funcs file will error
    c.did_i_raised_at = {"Pre_Flop": False , "Flop": False ,
                       "Turn": False , "River": False } 
    c.my_last_raise_at = {}
    # (2018) Later make sure if all rounds are starting from 0 in 
    # main While True loop (Round_... = 0 should be implemented in 
    # read_and_save_bets() for all stages so for example 
    # bets_cache dictionary surely will "have Round_... 0"). 
    # For testing i have put a shout(bets_cache) at the end of 
    # read_and_save_bets() function 
    c.preflop_betting_round = -1
    c.flop_betting_round = -1
    c.turn_betting_round = -1
    c.river_betting_round = -1
    # if a stage is True, previous stages are also True
    c.preflop_stage = False 
    c.flop_stage = False 
    c.turn_stage = False 
    c.river_stage = False 
    c.board_cards = []
    c.my_hole_cards = []
    c.win_odds = None
    c.next_win_odds_average = None
    c.draw_odds = None

def read_and_save_bets() :
    #global game_position, player_cards_cache , white_chips_cache , red_chips_cache , bets_cache ,\
    #       last_white_chips_cache , last_red_chips_cache , last_player_cards_cache , last_bets_cache,\
    #       preflop_betting_round , flop_betting_round , turn_betting_round , river_betting_round ,\
    #       preflop_stage , flop_stage , turn_stage , river_stage
    shout('read_and_save_bets...')

    if c.preflop_stage == True and c.flop_stage == False :
        stage = "Pre_Flop"
        betting_round = c.preflop_betting_round
    elif c.flop_stage == True and c.turn_stage == False :
        stage = "Flop"
        betting_round = c.flop_betting_round        
    elif c.turn_stage == True and c.river_stage == False :
        stage = "Turn"
        betting_round = c.turn_betting_round
    elif c.river_stage == True :
        stage = "River"
        betting_round = c.river_betting_round

    c.player_cards_cache["%s %s" %(stage, betting_round)] = {}
    c.white_chips_cache["%s %s" %(stage, betting_round)] = {}
    c.red_chips_cache["%s %s" %(stage, betting_round)] = {}
    c.bets_cache["%s %s" %(stage, betting_round)] = {}
    c.last_player_cards_cache = {}
    c.last_white_chips_cache = {}
    c.last_red_chips_cache = {}
    c.last_bets_cache = {}
    
    for Seat in range(1, c.TOTAL_SEATS+1):

        c.player_cards_cache["%s %s" %(stage, betting_round)][Seat] \
        = pm.player_cards_pixel(c.game_position, Seat)

        if pm.player_chips_pixel(c.game_position, Seat): #💊
            c.bets_cache["%s %s" %(stage, betting_round)][Seat] = ocr_bet(Seat)
        else :
            c.bets_cache["%s %s" %(stage, betting_round)][Seat] = None

        c.last_bets_cache[Seat] \
        = c.bets_cache["%s %s" %(stage, betting_round)][Seat]

    for Seat in range(1, c.TOTAL_SEATS+1):
        c.white_chips_cache["%s %s" %(stage, betting_round)][Seat] \
        = white_chips(Seat)
        c.red_chips_cache["%s %s" %(stage, betting_round)][Seat] \
        = red_chips(Seat) #💊
        c.last_player_cards_cache[Seat] \
        = c.player_cards_cache["%s %s" %(stage, betting_round)][Seat]
        c.last_white_chips_cache[Seat] \
        = c.white_chips_cache["%s %s" %(stage, betting_round)][Seat]
        c.last_red_chips_cache[Seat] \
        = c.red_chips_cache["%s %s" %(stage, betting_round)][Seat]

        if c.last_white_chips_cache[Seat] == True : 
            shout("Seat%s Call: $%s" %(Seat, c.last_bets_cache[Seat]), 
                  color = 'light_green') #💊
        elif c.last_red_chips_cache[Seat] == True :
            shout("Seat%s Raise: $%s" %(Seat, c.last_bets_cache[Seat]), 
                  color = 'light_green') #💊

    # (2018) Delete this later. just for testing if rounds are 
    # started from 0, esp at preflop stage        
    shout("shouting from read_and_save_bets(), bets_cache is: %s"%c.bets_cache) 
