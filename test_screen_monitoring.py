import time
import cv2, pyautogui, win32gui, win32con
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

def find_game_reference_point_for_testing():
    #global game_position

    print('searching for game region on screen...')

    image_path ='screen_monitoring/find_game_position/reference image.png'
    game_position = pyautogui.locateOnScreen(str(image_path))
    if game_position == None:
        raise Exception("can not find game region on screen")
    else:
        print('game reference point is set')
        return game_position

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


# Globaling game_position
game_position = find_game_reference_point_for_testing()
test_read_cards(my_seat = 1, show_image = False)
test_click_coordinates()

