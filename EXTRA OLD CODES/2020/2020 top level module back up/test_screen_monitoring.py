import time
import cv2, pyautogui, win32gui, win32con
import numpy as np
import screen_monitoring.find_game_position.find_game_position as find_game_position
import screen_monitoring.pixel_matching.pixel_matching as pm
import screen_monitoring.ocr.ocr as ocr
import screen_monitoring.read_cards.read_cards as read_cards
import screen_monitoring.read_cards.match_card as match_card
import screen_monitoring.click_coordinates.click_coordinates as click_coordinates

"""
Test all modules from screen_monitoring sub package
First open the game or the image of the game on the screen to start testing.
"""

def find_game_reference_point_for_this_module():
    #global game_position

    print('searching for game region on screen...')

    image_path ='screen_monitoring/find_game_position/reference image.png'
    game_position = pyautogui.locateOnScreen(str(image_path))
    if game_position == None:
        raise Exception("can not find game region on screen")
    else:
        print('game reference point is set')
        return int(game_position[0]), int(game_position[1])


def test_find_game_position():
    game_position = find_game_position.find_game_reference_point()
    print('game_position is: (%s, %s)' %game_position)

def test_read_cards(my_seat = 1, show_image = False):
    """
    Before start testing, put a poker game table on top of your monitor screen. 
    It tests card reading functionality, and shows the screen shot cards from
    screen to make sure that pre_process_query_image() function works fine
    and coordinates like: TABLE_CARD_VALUE_COORDINATE,...
    ,table_card_region are set correctly.
    """

    def show_my_pre_process_card_images(game_position, my_seat):
        for xth_card in [1,2]:    
            query_image =\
            read_cards.download_my_card(game_position, my_seat, xth_card)
            value_image, suit_image =\
            match_card.pre_process_query_image(query_image, False)
            print('My %sth card value image' %xth_card)
            cv2.imshow('My %sth card value image' %xth_card, value_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print('My %sth card suit image' %xth_card)
            cv2.imshow('My %sth card suit image' %xth_card, suit_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            #cv2.imwrite('My %sth card screenshot value_image.png' 
            #            %xth_card, value_image)
            #cv2.imwrite('My %sth card screenshot suit_image.png'
            #            %xth_card, suit_image)

    def show_table_pre_process_card_images(game_position):
        for xth_card in [1,2,3,4,5]:    
            query_image = read_cards.download_table_card(game_position
                                                         , xth_card)
            value_image, suit_image =\
            match_card.pre_process_query_image(query_image, True)
            print('Table %sth card value image' %xth_card)
            cv2.imshow('Table %sth card value image' %xth_card, value_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print('Table %sth card suit image' %xth_card)
            cv2.imshow('Table %sth card suit image' %xth_card, suit_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            #cv2.imwrite('Table %sth card screenshot value_image.png' 
            #            %xth_card, value_image)
            #cv2.imwrite('Table %sth card screenshot suit_image.png'
            #            %xth_card, suit_image)

    my_1th_card, my_2th_card =\
    read_cards.read_my_cards(game_position, my_seat)
    table_1th_card, table_2th_card, table_3th_card =\
    read_cards.read_flop_cards(game_position)
    table_4th_card = read_cards.read_turn_card(game_position)
    table_5th_card = read_cards.read_river_card(game_position)

    print('my cards are:%s , %s'%(my_1th_card, my_2th_card))
    print('table cards are:%s, %s, %s, %s, %s'
    %(table_1th_card, table_2th_card, table_3th_card,
      table_4th_card, table_5th_card))
    if show_image == True:
        show_my_pre_process_card_images(game_position, my_seat)
        show_table_pre_process_card_images(game_position)

def test_ocr(show_images = False):
    global my_bank
    # 1. Run this function to test if screen shot images are on correct 
    #    position and if ocr works fine or not.
    # 2. To rebuild this module for new websites, you can manipulate 
    #    pre_process_ocr_image() function to get better ocr results.

    def show_bets_images(game_position, seat):  
        pil_image = ocr.download_bet_image(game_position, seat)
        image = ocr.pre_process_ocr_image(pil_image)
        cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('bet on seat %s:%s'%(seat, bet), cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #cv2.imwrite('bet on seat %s.png' %seat, image)

    def show_other_players_bank_images(game_position, seat):  
        pil_image = ocr.download_other_players_bank_image(game_position, seat)
        image = ocr.pre_process_ocr_image(pil_image)
        cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('other_players_bank on seat %s:%s'
                   %(seat, other_players_bank), cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #cv2.imwrite('other_players_bank on seat %s.png' %seat, image)

    def show_my_bank_images(game_position, seat):  
        pil_image = ocr.download_my_bank_image(game_position, seat)
        image = ocr.pre_process_ocr_image(pil_image)
        cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('my_bank on seat %s:%s'%(seat, my_bank), cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #cv2.imwrite('my_bank on seat %s.png' %seat, image)

    def show_other_names_images(game_position, seat):  
        pil_image = ocr.download_other_names_image(game_position, seat)
        image = ocr.pre_process_ocr_image(pil_image)
        cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('other_names on seat %s:%s'%(seat, other_names), cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #cv2.imwrite('others_name on seat %s.png' %seat, image)

    def show_my_name_images(game_position, seat):  
        pil_image = ocr.download_my_name_image(game_position, seat)
        image = ocr.pre_process_ocr_image(pil_image)
        cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('my_name on seat %s:%s'%(seat, my_name), cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #cv2.imwrite('my_name on seat %s.png' %seat, image)

    t0 = time.time()

    for seat in [1,2,3,4,5]:
        bet = ocr.ocr_bet_to_string(game_position, seat) 
        print('bet on seat %s:%s'%(seat, bet) )
        if show_images == True :
            show_bets_images(game_position, seat)
    for seat in [1,2,3,4,5]:
        other_players_bank = ocr.ocr_other_players_bank_to_string(game_position,
                                                              seat) 
        print('other_players_bank on seat %s:%s'%(seat, other_players_bank) )
        if show_images == True :
            show_other_players_bank_images(game_position, seat)
    for seat in [1,2,3,4,5]:
        my_bank = ocr.ocr_my_bank_to_string(game_position, seat) 
        print('my_bank on seat %s:%s'%(seat, my_bank) )
        if show_images == True :
            show_my_bank_images(game_position, seat)
    for seat in [1,2,3,4,5]:
        other_names = ocr.ocr_other_names_to_string(game_position, seat) 
        print('other_names on seat %s:%s'%(seat, other_names) )
        if show_images == True :
            show_other_names_images(game_position, seat)
    for seat in [1,2,3,4,5]:
        my_name = ocr.ocr_my_name_to_string(game_position, seat) 
        print('my_name on seat %s:%s'%(seat, my_name) )
        if show_images == True :
            show_my_name_images(game_position, seat)

    t = time.time() - t0
    print('total time consumption: %s' %t)
    print('average time consumption for each ocr: %s' %(t/25) )

def test_click_coordinates():

    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,1153,222,440,593,0)

    def click(name):
        x, y = click_coordinates.click_coordinates(game_position, name)
        pyautogui.click(x, y)
    # This list may differ for other websites
    ALL_CLICK_NAMES = [
    'fold', 'check', 'call', 'bet', 'raise', 'plus', 'minus', 'all_in', 
    'available_seat_1', 'available_seat_2', 'available_seat_3',
    'available_seat_4', 'available_seat_5',
    'exit', 'exit_yes', 'menu', 'rebuy_menu', 'leave_next_hand_ok', 
    'buy_in', 'buy_in_plus', 'buy_in_minus', 're_buy', 're_buy_plus',
    're_buy_minus', 'i_am_back',
    'exit_probable_advertisement', 'close_update_window',
    ]
    for name in ALL_CLICK_NAMES:
        print('clicking on %s in 3 seconds...'%name)
        time.sleep(3)
        click(name)

def test_pixel_matching():

    # This list may differ for other websites
    ALL_CLICK_NAMES = [
    'fold', 'check', 'call', 'bet', 'raise', 'plus', 'minus', 'all_in', 
    #'available_seat_1', 'available_seat_2', 'available_seat_3',
    #'available_seat_4', 'available_seat_5',
    'exit', 'exit_yes', 'menu', 'rebuy_menu', 'leave_next_hand_ok', 
    'buy_in', 'buy_in_plus', 'buy_in_minus', 're_buy', 're_buy_plus',
    're_buy_minus', 'i_am_back',
    #'exit_probable_advertisement', 'close_update_window',
    ]

    print('\n***testing pixel matching for buttons:***')

    for button_name in ALL_CLICK_NAMES:
        print('%s button pixel is: %s'
              %(button_name, pm.button_pixel(game_position, button_name) ) )
    for seat in [1,2,3,4,5]:
        print('available_seat_%s button pixel is: %s'
              %(seat, pm.available_seat_pixel(game_position, seat) ) )

    print('\n***testing pixel matching for non buttons:***')

    print('pre_flop_pixel is: %s' %pm.pre_flop_pixel(game_position) )
    print('flop_pixel is: %s' %pm.flop_pixel(game_position) )  
    print('turn_pixel is: %s' %pm.turn_pixel(game_position) )  
    print('river_pixel is: %s' %pm.river_pixel(game_position) )    
    for seat in [1,2,3,4,5]:
        print('small_blind_pixel at seat %s is: %s'
              %(seat, pm.small_blind_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('big_blind_pixel at seat %s is: %s'
              %(seat, pm.big_blind_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('dealer_pixel at seat %s is: %s'
              %(seat, pm.dealer_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('player_chips_pixel at seat %s is: %s'
              %(seat, pm.player_chips_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('player_cards_pixel at seat %s is: %s'
              %(seat, pm.player_cards_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('other_player_seated_pixel at seat %s is: %s'
              %(seat, pm.other_player_seated_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('i_am_seated_pixel at seat %s is: %s'
              %(seat, pm.i_am_seated_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('active_player_pixel at seat %s is: %s'
              %(seat, pm.active_player_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('my_seat_won_pixel at seat %s is: %s'
              %(seat, pm.my_seat_won_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('other_seat_won_pixel at seat %s is: %s'
              %(seat, pm.other_seat_won_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('notification_banner_pixel at seat %s is: %s'
              %(seat, pm.notification_banner_pixel(game_position, seat) ) )
    for seat in [1,2,3,4,5]:
        print('are_chips_white_or_red_pixel at seat %s is: %s'
              %(seat, pm.are_chips_white_or_red_pixel(game_position, seat) ) )

if __name__ == '__main__':
    # Globaling the game_position
    game_position = find_game_reference_point_for_this_module()

    test_find_game_position()
    #test_read_cards(my_seat = 1, show_image = False)
    test_ocr(show_images = False)
    #test_pixel_matching()
    #test_click_coordinates()

