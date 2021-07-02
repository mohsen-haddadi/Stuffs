#OK
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.read_cards.read_cards as read_cards
import configs as c
from iprint import shout
from readability.fix_game_disruption import fix_game_disruption, set_just_do_check_fold_to_true


def read_and_save_my_cards():
    #global game_position, my_1th_card , my_2th_card  , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    c.my_1th_card, c.my_2th_card =\
    read_cards.read_my_cards(c.game_position, c.my_seat_number)

    if ('Unknown' in c.my_1th_card 
        or 'Unknown' in c.my_2th_card ):

        fix_game_disruption("my cards are read Unknown")
        c.my_1th_card, c.my_2th_card =\
        read_cards.read_my_cards(c.game_position, c.my_seat_number)

        if ('Unknown' in c.my_1th_card 
            or 'Unknown' in c.my_2th_card
            or pm.flop_pixel(c.game_position) ):

            set_just_do_check_fold_to_true("my cards are read Unknown again")

    shout("My cards are: %s, %s"
          %(c.my_1th_card, c.my_2th_card)
          , color = 'green')

def read_and_save_flop_cards(): 
    #global game_position, board_card_1th , board_card_2th , board_card_3th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    c.board_card_1th, c.board_card_2th, c.board_card_3th =\
    read_cards.read_flop_cards(c.game_position)

    if ( 'Unknown' in c.board_card_1th 
        or 'Unknown' in c.board_card_2th
        or 'Unknown' in c.board_card_3th ):

        fix_game_disruption("Flop cards are read 'Unknown'")
        c.board_card_1th, c.board_card_2th, c.board_card_3th =\
        read_cards.read_flop_cards(c.game_position)

        if ('Unknown' in c.board_card_1th 
            or 'Unknown' in c.board_card_2th
            or 'Unknown' in c.board_card_3th 
            or not pm.flop_pixel(c.game_position) 
            or pm.turn_pixel(c.game_position) ):

            set_just_do_check_fold_to_true("Flop cards are read 'Unknown' again")

    shout("Flop cards are: %s, %s, %s" 
          %(c.board_card_1th, c.board_card_2th, c.board_card_3th)
          , color = 'green')

def read_and_save_turn_card(): 
    #global game_position, board_card_4th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    c.board_card_4th = read_cards.read_turn_card(c.game_position)
    
    if 'Unknown' in c.board_card_4th:

        fix_game_disruption("Turn card is read 'Unknown'")
        c.board_card_4th = read_cards.read_turn_card(c.game_position)

        if ( 'Unknown' in c.board_card_4th 
            or not pm.turn_pixel(c.game_position)
            or pm.river_pixel(c.game_position) ) :

            set_just_do_check_fold_to_true("Turn card is read 'Unknown' again")

    shout("Turn card is: %s" %(c.board_card_4th[0])
          , color = 'green')

def read_and_save_river_card(): 
    #global game_position, board_card_5th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status
    
    c.board_card_5th = read_cards.read_river_card(c.game_position)
    
    if 'Unknown' in c.board_card_5th:

        fix_game_disruption("River card is read 'Unknown'")
        c.board_card_5th = read_cards.read_river_card(c.game_position)

        if ('Unknown' in c.board_card_5th 
            or not pm.river_pixel(c.game_position) ):

            set_just_do_check_fold_to_true("River card is read 'Unknown' again")

    shout("River card is: %s" %(c.board_card_5th[0])
          , color = 'green')

