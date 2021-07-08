#OK
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.read_cards.read_cards as read_cards
import configs as c
from iprint import shout
from readability.fix_game_disruption import fix_game_disruption, set_just_do_check_fold_to_true, screenshot_error


def read_and_save_my_cards(): #💊
    """Example: c.my_hole_cards == ['Unknown', '3h'] """

    c.my_hole_cards = read_cards.read_my_cards(c.game_position, c.my_seat_number)
    if 'Unknown' in  c.my_hole_cards: 

        fix_game_disruption("my cards are read Unknown")
        c.my_hole_cards =\
        read_cards.read_my_cards(c.game_position, c.my_seat_number)

        if 'Unknown' in c.my_hole_cards or pm.flop_pixel(c.game_position):

            screenshot_error('my hole cards are read Unknown')
            set_just_do_check_fold_to_true("my hole cards are read Unknown again")

    shout(f"My hole cards are: {c.my_hole_cards[0]}, {c.my_hole_cards[1]}", color = 'green')

def read_and_save_flop_cards(): #💊  
    """Example: flop_cards == ['As','Unknown', '3h'] """

    flop_cards = read_cards.read_flop_cards(c.game_position)

    if 'Unknown' in flop_cards:
        fix_game_disruption("One or all flop cards are read 'Unknown'")
        flop_cards = read_cards.read_flop_cards(c.game_position)

        if ('Unknown' in flop_cards
            or not pm.flop_pixel(c.game_position) 
            or pm.turn_pixel(c.game_position) ):

            set_just_do_check_fold_to_true("One or all flop cards are read 'Unknown' again")

    c.board_cards.extend(flop_cards)
    shout(f"Flop cards are: {c.board_cards[0]}, {c.board_cards[1]}, {c.board_cards[2]}"
          , color = 'green')

def read_and_save_turn_card(): #💊 

    board_card_4th = read_cards.read_turn_card(c.game_position)
    
    if 'Unknown' == board_card_4th: 

        fix_game_disruption("Turn card is read 'Unknown'")
        board_card_4th = read_cards.read_turn_card(c.game_position)

        if ( 'Unknown' == board_card_4th  
            or not pm.turn_pixel(c.game_position)
            or pm.river_pixel(c.game_position) ) :

            set_just_do_check_fold_to_true("Turn card is read 'Unknown' again")

    if len(c.board_cards) == 3:
        c.board_cards.append(board_card_4th)
        shout(f"Turn card is: {c.board_cards[3]}", color = 'green')
    else:
        set_just_do_check_fold_to_true('flop cards have been not saved already')

def read_and_save_river_card(): #💊 
    
    board_card_5th = read_cards.read_river_card(c.game_position)
    
    if 'Unknown' == board_card_5th: 

        fix_game_disruption("River card is read 'Unknown'")
        board_card_5th = read_cards.read_river_card(c.game_position)

        if ('Unknown' == board_card_5th 
            or not pm.river_pixel(c.game_position) ):

            set_just_do_check_fold_to_true("River card is read 'Unknown' again")

    if len(c.board_cards) == 4:
        c.board_cards.append(board_card_5th)
        shout(f"River card is: {c.board_cards[4]}", color = 'green')
    else:
        set_just_do_check_fold_to_true('flop or turn cards have been not saved already')

