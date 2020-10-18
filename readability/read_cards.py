#OK
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.read_cards.read_cards as read_cards
import config
from iprint import shout
from readability.fix_game_disruption import fix_game_disruption, set_just_do_check_fold_to_true


def read_and_save_my_cards():
    #global game_position, my_1th_card , my_2th_card  , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    config.my_1th_card, config.my_2th_card =\
    read_cards.read_my_cards(config.game_position, config.my_seat_number)

    if ('Unknown' in config.my_1th_card 
        or 'Unknown' in config.my_2th_card ):

        fix_game_disruption("my cards are read Unknown")
        config.my_1th_card, config.my_2th_card =\
        read_cards.read_my_cards(config.game_position, config.my_seat_number)

        if ('Unknown' in config.my_1th_card 
            or 'Unknown' in config.my_2th_card
            or pm.flop_pixel(config.game_position) ):

            set_just_do_check_fold_to_true("my cards are read Unknown again")

    shout("My cards are: %s %s, %s %s"
          %(my_1th_card[0][0], my_1th_card[0][1],
            my_2th_card[1][0], my_2th_card[1][1])
          , color = 'green')

def read_and_save_flop_cards(): 
    #global game_position, board_card_1th , board_card_2th , board_card_3th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    config.board_card_1th, config.board_card_2th, config.board_card_3th =\
    read_cards.read_flop_cards(config.game_position)

    if ( 'Unknown' in config.board_card_1th 
        or 'Unknown' in config.board_card_2th
        or 'Unknown' in config.board_card_3th ):

        fix_game_disruption("Flop cards are read 'Unknown'")
        config.board_card_1th, config.board_card_2th, config.board_card_3th =\
        read_cards.read_flop_cards(config.game_position)

        if ('Unknown' in config.board_card_1th 
            or 'Unknown' in config.board_card_2th
            or 'Unknown' in config.board_card_3th 
            or not pm.flop_pixel(config.game_position) 
            or pm.turn_pixel(config.game_position) ):

            set_just_do_check_fold_to_true("Flop cards are read 'Unknown' again")

    shout("Flop cards are: %s %s, %s %s, %s %s" 
          %(config.board_card_1th[0][0], config.board_card_1th[0][1], 
            config.board_card_2th[1][0], config.board_card_2th[1][1],
            config.board_card_3th[1][0], config.board_card_3th[1][1])
          , color = 'green')

def read_and_save_turn_card(): 
    #global game_position, board_card_4th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status

    config.board_card_4th = read_cards.read_turn_card(config.game_position)
    
    if 'Unknown' in config.board_card_4th:

        fix_game_disruption("Turn card is read 'Unknown'")
        config.board_card_4th = read_cards.read_turn_card(config.game_position)

        if ( 'Unknown' in config.board_card_4th 
            or not pm.turn_pixel(config.game_position)
            or pm.river_pixel(config.game_position) ) :

            set_just_do_check_fold_to_true("Turn card is read 'Unknown' again")

    shout("Turn card is: %s %s" %(config.board_card_4th[0], config.board_card_4th[1])
          , color = 'green')

def read_and_save_river_card(): 
    #global game_position, board_card_5th , just_do_check_fold , my_seat_number , MY_PROFILE_NAME , bot_status
    
    config.board_card_5th = read_cards.read_river_card(config.game_position)
    
    if 'Unknown' in config.board_card_5th:

        fix_game_disruption("River card is read 'Unknown'")
        config.board_card_5th = read_cards.read_river_card(config.game_position)

        if ('Unknown' in config.board_card_5th 
            or not pm.river_pixel(config.game_position) ):

            set_just_do_check_fold_to_true("River card is read 'Unknown' again")

    shout("River card is: %s %s" %(config.board_card_5th[0], config.board_card_5th[1])
          , color = 'green')

