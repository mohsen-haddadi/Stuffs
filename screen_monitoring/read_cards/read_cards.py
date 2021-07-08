#💊 : means edited
import time, os
import numpy as np , cv2
import pyautogui
if __name__ == '__main__':
    import match_card
else:
    import screen_monitoring.read_cards.match_card as match_card

"""
1. Set these constants the same between create_source_cards_images.py and read_cards.py:
my_1th_card_region, my_2th_card_region, and table_card_region

2. Functions they are used: 
create_source_cards_images.crop_raw_card_image() 
and read_card.download_my_card() read_card.download_table_card()
"""

def download_my_card(game_position, my_seat , xth_card):
    """
    Use specific top left corner pixel of a card to set card region. 
    """
    my_1th_card_region = { 1:(game_position[0]+73, game_position[1]+195, 34, 28) } #💊
    my_2th_card_region = { 1:(game_position[0]+111, game_position[1]+195, 34, 28) } #💊

    if xth_card == 1:
        pyautogui.screenshot("image.png" , my_1th_card_region[my_seat] )
    elif xth_card == 2:
        pyautogui.screenshot("image.png" , my_2th_card_region[my_seat] )
    query_image = cv2.imread("image.png")
    if isinstance(query_image, type(None)):
        raise Exception("Unable to read image.png. screenshot has not saved image.png")
    os.remove("image.png")
    return query_image

def download_table_card(game_position, xth_card):
    """
    Use specific top left corner pixel of a card to set card region. 
    Set top left corner of table card regions to the same height. 
    """
    table_card_region = { 1:(game_position[0]+3, game_position[1]+64, 34, 28) , #💊
                          2:(game_position[0]+42, game_position[1]+64, 34, 28) , #💊
                          3:(game_position[0]+82, game_position[1]+64, 34, 28) , #💊
                          4:(game_position[0]+121, game_position[1]+64, 34, 28) , #💊
                          5:(game_position[0]+161, game_position[1]+64, 34, 28) } #💊

    pyautogui.screenshot("image.png" , table_card_region[xth_card] )
    query_image = cv2.imread("image.png")
    if isinstance(query_image, type(None)):
        raise Exception("Unable to read image.png. screenshot has not saved image.png")
    os.remove("image.png")
    return query_image

def read_my_cards(game_position, my_seat):
    """
    Example: returns ['8s' , 'Ac'] #💊
    my_1th_card, my_2th_card = board_cards
    """
    board_cards = []
    for xth_card in [1,2]:    
        query_image = download_my_card(game_position, my_seat , xth_card)
        value_image, suit_image = match_card.pre_process_query_image(query_image, False)
        #cv2.imwrite('%s screenshot value_image.png' %xth_card, value_image)
        #cv2.imwrite('%s screenshot suit_image.png' %xth_card, suit_image)
        result = match_card.match_floating_card(value_image, suit_image, False)
        if 'Unknown' in result[:2]: #💊
            board_cards.append('Unknown') #💊
        else: #💊
            board_cards.append(f'{result[0]}{result[1]}') #💊
    return board_cards

def read_flop_cards(game_position):
    """
    Example: returns ['Unknown', 'Qc', 'Tc'] #💊
    table_1th_card, table_2th_card, table_3th_card = flop_cards
    """
    flop_cards = []
    for xth_card in [1,2,3]:    
        query_image = download_table_card(game_position, xth_card)
        value_image, suit_image = match_card.pre_process_query_image(query_image, True)
        result = match_card.match_floating_card(value_image, suit_image, True)
        if 'Unknown' in result[:2]: #💊
            flop_cards.append('Unknown') #💊
        else: #💊
            flop_cards.append(f'{result[0]}{result[1]}') #💊
    return flop_cards

def read_turn_card(game_position):
    """
    Example: returns '4s' #💊 
    table_4th_card = turn_card
    """
    query_image = download_table_card(game_position, 4)
    value_image, suit_image = match_card.pre_process_query_image(query_image, True)
    turn_card = match_card.match_floating_card(value_image, suit_image, True)
    if 'Unknown' in turn_card[:2]: #💊
        turn_card = 'Unknown' #💊
    else: #💊
        turn_card = f'{turn_card[0]}{turn_card[1]}' #💊
    return turn_card

def read_river_card(game_position):
    """
    Example: returns '4s' #💊
    table_5th_card = river_card
    """
    query_image = download_table_card(game_position, 5)
    value_image, suit_image = match_card.pre_process_query_image(query_image, True)
    river_card = match_card.match_floating_card(value_image, suit_image, True)
    if 'Unknown' in river_card[:2]: #💊
        river_card = 'Unknown' #💊
    else: #💊
        river_card = f'{river_card[0]}{river_card[1]}' #💊
    return river_card

