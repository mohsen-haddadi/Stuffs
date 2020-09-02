import numpy, pyautogui
from pyautogui import pixelMatchesColor

def pre_flop_pixel(game_position): 
    # Check if the game is on pre flop by returning True or False
    return not flop_pixel(game_position)

def flop_pixel(game_position):
    # Check if the game is on flop by returning True or False
    flop = pixelMatchesColor( game_position[0]+136, game_position[1]+218, (237,237,237) ) #Flop
    return flop 

def turn_pixel(game_position):
    # Check if the game is on turn by returning True or False
    turn = pixelMatchesColor( game_position[0]+196, game_position[1]+218, (237,237,237) ) #Turn
    return turn 

def river_pixel(game_position):
    # Check if the game is on river by returning True or False
    river = pixelMatchesColor( game_position[0]+261, game_position[1]+218, (237,237,237) ) #River
    return river 
#2020
def small_blind_pixel(game_position, seat):
    # check if a seat is on small blind position by returning True or False
    small_blind_seat_1 = pixelMatchesColor( game_position[0]+369, game_position[1]+329, (18,111,213), tolerance=10 ) #Small_seat_1
    small_blind_seat_2 = pixelMatchesColor( game_position[0]+111, game_position[1]+332, (21,124,218), tolerance=10 ) #Small_seat_2
    small_blind_seat_3 = pixelMatchesColor( game_position[0]-145, game_position[1]+329, (16,105,211), tolerance=10 ) #Small_seat_3
    small_blind_seat_4 = pixelMatchesColor( game_position[0]-173, game_position[1]+212, (22,112,212), tolerance=10 ) #Small_seat_4
    small_blind_seat_5 = pixelMatchesColor( game_position[0]+400, game_position[1]+212, (22,112,212), tolerance=10 ) #Small_seat_5

    if seat == 1: return small_blind_seat_1
    if seat == 2: return small_blind_seat_2
    if seat == 3: return small_blind_seat_3
    if seat == 4: return small_blind_seat_4
    if seat == 5: return small_blind_seat_5
#2020
def big_blind_pixel(game_position, seat):
    # check if a seat is on big blind position by returning True or False
    big_blind_seat_1 = pixelMatchesColor( game_position[0]+367, game_position[1]+329, (180,180,180), tolerance=10 ) #Big_seat_1
    big_blind_seat_2 = pixelMatchesColor( game_position[0]+111, game_position[1]+332, (200,200,200), tolerance=10 ) #Big_seat_2
    big_blind_seat_3 = pixelMatchesColor( game_position[0]-145, game_position[1]+329, (185,185,185), tolerance=10 ) #Big_seat_3
    big_blind_seat_4 = pixelMatchesColor( game_position[0]-174, game_position[1]+212, (185,185,185), tolerance=10 ) #Big_seat_4
    big_blind_seat_5 = pixelMatchesColor( game_position[0]+400, game_position[1]+212, (185,185,185), tolerance=10 ) #Big_seat_5

    if seat == 1: return big_blind_seat_1
    if seat == 2: return big_blind_seat_2
    if seat == 3: return big_blind_seat_3
    if seat == 4: return big_blind_seat_4
    if seat == 5: return big_blind_seat_5
#2020
def dealer_pixel(game_position, seat):
    # check if a seat is on dealer position by returning True or False
    dealer_seat_1 = pixelMatchesColor( game_position[0]+397, game_position[1]+330, (255,155,0), tolerance=10 ) #Dealer_seat_1
    dealer_seat_2 = pixelMatchesColor( game_position[0]+144, game_position[1]+333, (254,193,0), tolerance=10 ) #Dealer_seat_2
    dealer_seat_3 = pixelMatchesColor( game_position[0]-116, game_position[1]+330, (255,154,0), tolerance=10 ) #Dealer_seat_3
    dealer_seat_4 = pixelMatchesColor( game_position[0]-202, game_position[1]+212, (255,160,0), tolerance=10 ) #Dealer_seat_4
    dealer_seat_5 = pixelMatchesColor( game_position[0]+429, game_position[1]+212, (255,160,0), tolerance=10 ) #Dealer_seat_5 

    if seat == 1: return dealer_seat_1
    if seat == 2: return dealer_seat_2
    if seat == 3: return dealer_seat_3
    if seat == 4: return dealer_seat_4
    if seat == 5: return dealer_seat_5

def player_chips_pixel(game_position, seat): #New define function for celeb
    # Checks if there is any call/bet/raising chips in front of a seat or not, by returning True or False
    if seat==1:
        return pixelMatchesColor( game_position[0]+298, game_position[1]+317, (240,16,0), tolerance=10 ) #Bet_coin_seat_1
    if seat==2:
        return pixelMatchesColor( game_position[0]+79, game_position[1]+320, (237,16,0), tolerance=10 ) #Bet_coin_seat_2
    if seat==3:
        return pixelMatchesColor( game_position[0]-138, game_position[1]+317, (241,17,0), tolerance=10 ) #Bet_coin_seat_3
    if seat==4:
        return pixelMatchesColor( game_position[0]-143, game_position[1]+231, (241,17,0), tolerance=10 ) #Bet_coin_seat_4
    if seat==5:
        return pixelMatchesColor( game_position[0]+302, game_position[1]+231, (241,17,0), tolerance=10 ) #Bet_coin_seat_5

def player_cards_pixel(game_position, seat):
    # It checks if a player has cards in his hands or not, by returning True of False
    if seat==1:
        c1 = pixelMatchesColor( game_position[0]+330, game_position[1]+331, (154,7,13), tolerance=5 ) #Cards_seat_1
        c2 = pixelMatchesColor( game_position[0]+328, game_position[1]+333, (154,7,13), tolerance=5 ) 
        return c1 or c2
    if seat==2:
        c1 = pixelMatchesColor( game_position[0]+74, game_position[1]+332, (154,7,13), tolerance=5 ) #Cards_seat_2
        c2 = pixelMatchesColor( game_position[0]+72, game_position[1]+334, (154,7,13), tolerance=5 ) 
        return c1 or c2
    if seat==3:
        c1 = pixelMatchesColor( game_position[0]-181, game_position[1]+331, (154,7,13), tolerance=5 ) #Cards_seat_3
        c2 = pixelMatchesColor( game_position[0]-183, game_position[1]+333, (154,7,13), tolerance=5 ) 
        return c1 or c2
    if seat==4:
        c1 = pixelMatchesColor( game_position[0]-140, game_position[1]+212, (154,7,13), tolerance=5 ) #Cards_seat_4
        c2 = pixelMatchesColor( game_position[0]-142, game_position[1]+193, (154,7,13), tolerance=20 )
        return c1 or c2
    if seat==5:
        c1 = pixelMatchesColor( game_position[0]+359, game_position[1]+212, (154,7,13), tolerance=5 ) #Cards_seat_5 
        c2 = pixelMatchesColor( game_position[0]+357, game_position[1]+193, (154,7,13), tolerance=20 ) 
        return c1 or c2

def other_player_seated_pixel(game_position, seat): # celeb
    # It checks at ordinary situations if there is a player on the seat or not

    if seat == 1:
        return pixelMatchesColor( game_position[0]+321, game_position[1]+403, (4,6,7), tolerance=2 ) #Others_In_seat_1
    if seat == 2:
        return pixelMatchesColor( game_position[0]+161, game_position[1]+398, (5,7,8), tolerance=2 ) #Others_In_seat_2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-94, game_position[1]+403, (4,6,7), tolerance=2 ) #Others_In_seat_3
    if seat == 4:
        return pixelMatchesColor( game_position[0]-124, game_position[1]+163, (4,6,7), tolerance=2 ) #Others_In_seat_4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+431, game_position[1]+183, (4,5,6), tolerance=2 ) #Others_In_seat_5

def i_am_seated_pixel(game_position, seat):
    # It checks at ordinary situations if I am on the seat or not

    if seat == 1 :
        x = pixelMatchesColor( game_position[0]+426, game_position[1]+381, (8,9,11) ) #me_in_1
        return (x)
    if seat == 2 :
        x = pixelMatchesColor( game_position[0]+177, game_position[1]+382, (10,12,14) ) #me_in_2
        return (x)
    if seat == 3 :
        x = pixelMatchesColor( game_position[0]-75, game_position[1]+379, (8,10,12) ) #me_in_3
        return (x)
    if seat == 4 :
        x = pixelMatchesColor( game_position[0]-106, game_position[1]+161, (9,11,13) ) #me_in_4
        return (x)
    if seat == 5 :
        x = pixelMatchesColor( game_position[0]+458, game_position[1]+181, (7,8,10) ) #me_in_5
        return (x)

def active_player_pixel(game_position, seat): # celeb
    # It checks whose player turn is, 
    # using the lighting pixel on a seat, by returning True or False 
    if seat==1:
        return pixelMatchesColor( game_position[0]+346, game_position[1]+328, (34,41,48), tolerance=5 ) #Light_Turn_seat_1
    if seat==2:
        return pixelMatchesColor( game_position[0]+96, game_position[1]+330, (47,59,69), tolerance=5 ) #Light_Turn_seat_2
    if seat==3:
        return pixelMatchesColor( game_position[0]-116, game_position[1]+328, (34,41,48), tolerance=5 ) #Light_Turn_seat_3
    if seat==4:
        return pixelMatchesColor( game_position[0]-161, game_position[1]+219, (33,41,47), tolerance=5 ) #Light_Turn_seat_4
    if seat==5:
        return pixelMatchesColor( game_position[0]+383, game_position[1]+217, (31,40,45), tolerance=5 ) #Light_Turn_seat_5
#2020
def my_seat_won_pixel(game_position, seat):
    # looking for a sign of winning on my seat to check if I have won the game by returning True or False    
    i_won_on_seat_1 = pixelMatchesColor( game_position[0]+442, game_position[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-1
    i_won_on_seat_2 = pixelMatchesColor( game_position[0]+187, game_position[1]+422, (248,123,10), tolerance=5 ) #Win-Finish-Me-seat-2
    i_won_on_seat_3 = pixelMatchesColor( game_position[0]-68, game_position[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-3
    i_won_on_seat_4 = pixelMatchesColor( game_position[0]-98, game_position[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-4
    i_won_on_seat_5 = pixelMatchesColor( game_position[0]+472, game_position[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-5

    if seat == 1: return i_won_on_seat_1
    if seat == 2: return i_won_on_seat_2
    if seat == 3: return i_won_on_seat_3
    if seat == 4: return i_won_on_seat_4
    if seat == 5: return i_won_on_seat_5
#2020
def other_seat_won_pixel(game_position, seat):
    # looking for a sign on other's seat to check if they have won the game by returning True or False
    others_won_on_seat_1 = pixelMatchesColor( game_position[0]+419, game_position[1]+412, (249,126,8), tolerance=5 ) #Win-Finish-Others-seat-1
    others_won_on_seat_2 = pixelMatchesColor( game_position[0]+164, game_position[1]+411, (249,127,8), tolerance=5 ) #Win-Finish-Others-seat-2
    others_won_on_seat_3 = pixelMatchesColor( game_position[0]-91, game_position[1]+419, (248,123,9), tolerance=5 ) #Win-Finish-Others-seat-3
    others_won_on_seat_4 = pixelMatchesColor( game_position[0]-121, game_position[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-4
    others_won_on_seat_5 = pixelMatchesColor( game_position[0]+449, game_position[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-5

    if seat == 1: return others_won_on_seat_1
    if seat == 2: return others_won_on_seat_2
    if seat == 3: return others_won_on_seat_3
    if seat == 4: return others_won_on_seat_4
    if seat == 5: return others_won_on_seat_5

def notification_banner_pixel(game_position, seat): # celeb
    # It checks if a notification banner which contains messages like:
    # 'FOLD, CHECK, BET, RAISE, CALL, ALL_IN' has covered player name or not,
    # by returning True of False.
    if seat == 1 :
        x1 = pixelMatchesColor( game_position[0]+291, game_position[1]+348, (62,72,86), tolerance=5 ) #Gray_Sign_Me_seat_1
        x2 = pixelMatchesColor( game_position[0]+315, game_position[1]+351, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_1
        return (x1 or x2)
    if seat == 2 :
        x1 = pixelMatchesColor( game_position[0]+36, game_position[1]+351, (61,70,85), tolerance=5 ) #Gray_Sign_Me_seat_2
        x2 = pixelMatchesColor( game_position[0]+60, game_position[1]+353, (61,71,86), tolerance=5 ) #Gray_Sign_Other_seat_2
        return (x1 or x2)
    if seat == 3 :
        x1 = pixelMatchesColor( game_position[0]-219, game_position[1]+348, (62,72,86), tolerance=5 ) #Gray_Sign_Me_seat_3
        x2 = pixelMatchesColor( game_position[0]-195, game_position[1]+351, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_3
        return (x1 or x2)
    if seat == 4 :
        x1 = pixelMatchesColor( game_position[0]-249, game_position[1]+43, (62,72,87), tolerance=5 ) #Gray_Sign_Me_seat_4
        x2 = pixelMatchesColor( game_position[0]-225, game_position[1]+46, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_4
        return (x1 or x2)
    if seat == 5 :
        x1 = pixelMatchesColor( game_position[0]+321, game_position[1]+43, (62,72,87), tolerance=5 ) #Gray_Sign_Me_seat_5
        x2 = pixelMatchesColor( game_position[0]+345, game_position[1]+46, (61,70,85), tolerance=5 ) #Gray_Sign_Other_seat_5
        return (x1 or x2)
 
def are_chips_white_or_red_pixel(game_position, seat): #celeb
    # If the color of the sign behind chips is
    # red it returns True (bet/raise), if the color is white it returns False (call)

    def avg_color(x,y,h,w) :
        image = pyautogui.screenshot(region=(x, y , h, w) )
        image.convert('RGB')
        open_cv_image = numpy.array(image)

        avg_color_per_row = numpy.average(open_cv_image, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        return avg_color

    if seat == 1 :
        x = avg_color(game_position[0]+313,game_position[1]+310,15,15) #Bet_White_or_Red_seat1
        if x[2] < 20 :
            return True
        else :
            return False
    if seat == 2 :
        x = avg_color(game_position[0]+95,game_position[1]+312,15,15) #Bet_White_or_Red_seat2
        if x[2] < 20 :
            return True
        else :
            return False
    if seat == 3 :
        x = avg_color(game_position[0]-123,game_position[1]+310,15,15) #Bet_White_or_Red_seat3
        if x[2] < 20 :
            return True
        else :
            return False
    if seat == 4 :
        x = avg_color(game_position[0]-128,game_position[1]+223,15,15) #Bet_White_or_Red_seat4
        if x[2] < 20 :
            return True
        else :
            return False
    if seat == 5 :
        x = avg_color(game_position[0]+318,game_position[1]+223,15,15) #Bet_White_or_Red_seat5
        if x[2] < 20 :
            return True
        else :
            return False


# pixel matchings to click on buttons:

def available_seat_pixel(game_position, seat):
    # It checks if the seat is free to be seated or not, by returning True or False
    if seat == 1 :
        x1 = pixelMatchesColor( game_position[0]+362, game_position[1]+408, (1,79,164) ) #Seat1
        x2 = pixelMatchesColor( game_position[0]+362, game_position[1]+408, (21,102,189) ) #Seat1_Light
        return (x1 or x2)
    if seat == 2 :
        x1 = pixelMatchesColor( game_position[0]+107, game_position[1]+411, (1,78,163) ) #Seat2
        x2 = pixelMatchesColor( game_position[0]+107, game_position[1]+411, (21,101,188) ) #Seat2_Light
        return (x1 or x2)
    if seat == 3 :
        x1 = pixelMatchesColor( game_position[0]-148, game_position[1]+408, (1,79,164) ) #Seat3
        x2 = pixelMatchesColor( game_position[0]-148, game_position[1]+408, (21,102,189) ) #Seat3_Light
        return (x1 or x2)
    if seat == 4 :
        x1 = pixelMatchesColor( game_position[0]-178, game_position[1]+103, (1,79,164) ) #Seat4
        x2 = pixelMatchesColor( game_position[0]-178, game_position[1]+103, (21,102,189) ) #Seat4_Light
        return (x1 or x2)
    if seat == 5 :
        x1 = pixelMatchesColor( game_position[0]+392, game_position[1]+103, (1,79,164) ) #Seat5
        x2 = pixelMatchesColor( game_position[0]+392, game_position[1]+103, (21,102,189) ) #Seat5_Light
        return (x1 or x2)


def button_pixel(game_position, button_name):
    #It checks if button is existed and it's on its position or not.
    if button_name == 'fold':
        x1 = pixelMatchesColor( game_position[0]+51, game_position[1]+581, (190,22,28) ) #Fold
        x2 = pixelMatchesColor( game_position[0]+51, game_position[1]+581, (220,27,33) ) #Fold_Light
        return (x1 or x2)
    elif button_name == 'check':
        x1 = pixelMatchesColor( game_position[0]+246, game_position[1]+578, (1,83,170) ) #Check_up
        x2 = pixelMatchesColor( game_position[0]+246, game_position[1]+584, (254,254,254) ) #Check_down
        x3 = pixelMatchesColor( game_position[0]+246, game_position[1]+578, (1,95,194) ) #Check_up_Light
        x4 = pixelMatchesColor( game_position[0]+246, game_position[1]+584, (254,254,254) ) #Check_down_Light
        return ( (x1 and x2) or (x3 and x4) )        
    elif button_name == 'call':
        x1 = pixelMatchesColor( game_position[0]+261, game_position[1]+575, (0,84,172) ) #Call_up
        x2 = pixelMatchesColor( game_position[0]+260, game_position[1]+579, (249,249,249) ) #Call_down
        x3 = pixelMatchesColor( game_position[0]+261, game_position[1]+575, (0,97,198) ) #Call_up_Light
        x4 = pixelMatchesColor( game_position[0]+260, game_position[1]+579, (249,249,249) ) #Call_down_Light
        return ( (x1 and x2) or (x3 and x4) )
    elif button_name == 'bet':
        x1 = pixelMatchesColor( game_position[0]+461, game_position[1]+576, (24,115,0), tolerance=15 ) #Bet_up
        x2 = pixelMatchesColor( game_position[0]+463, game_position[1]+579, (242,242,242), tolerance=15 ) #Bet_down
        x3 = pixelMatchesColor( game_position[0]+461, game_position[1]+576, (28,135,0), tolerance=15 ) #Bet_up_Light
        x4 = pixelMatchesColor( game_position[0]+463, game_position[1]+579, (242,242,242), tolerance=15 ) #Bet_down_Light
        return ( (x1 and x2) or (x3 and x4) )
    elif button_name == 'raise':
        x1 = pixelMatchesColor( game_position[0]+461, game_position[1]+576, (25,117,0), tolerance=15 ) #Raise_up
        x2 = pixelMatchesColor( game_position[0]+448, game_position[1]+579, (239,239,239), tolerance=15 ) #Raise_down
        x3 = pixelMatchesColor( game_position[0]+461, game_position[1]+576, (29,137,0), tolerance=15 ) #Raise_up_Light
        x4 = pixelMatchesColor( game_position[0]+448, game_position[1]+579, (239,239,239), tolerance=15 ) #Raise_down_Light
        return ( (x1 and x2) or (x3 and x4) )
    elif button_name == 'plus':
        x1 = pixelMatchesColor( game_position[0]+246, game_position[1]+648, (58,68,83) ) #Plus_Button
        x2 = pixelMatchesColor( game_position[0]+246, game_position[1]+648, (77,88,105) ) #Plus_Button_Light
        return (x1 or x2)
    elif button_name == 'minus':
        x1 = pixelMatchesColor( game_position[0]-9, game_position[1]+648, (58,68,83) ) #Minus_Button
        x2 = pixelMatchesColor( game_position[0]-9, game_position[1]+648, (77,88,105) ) #Minus_Button_Light
        return (x1 or x2)
    elif button_name == 'all_in':
        x1 = pixelMatchesColor( game_position[0]+531, game_position[1]+648, (207,90,6) ) #All_In_Button
        x2 = pixelMatchesColor( game_position[0]+531, game_position[1]+648, (235,98,0) ) #All_In_Button_Light
        return (x1 or x2)



    elif button_name == 'exit':
        x1 = pixelMatchesColor( game_position[0]+378, game_position[1]+21, (130,135,146) ) #Exit_Button
        x2 = pixelMatchesColor( game_position[0]+378, game_position[1]+21, (156,160,168) ) #Exit_Button_Light
        return (x1 or x2)
    elif button_name == 'exit_yes':
        x1 = pixelMatchesColor( game_position[0]+47, game_position[1]+355, (168,11,16) ) #Exit_Yes_Button
        x2 = pixelMatchesColor( game_position[0]+47, game_position[1]+355, (177,13,19) ) #Exit_Yes_Button_Light
        return (x1 or x2)
    elif button_name == 'menu':
        x1 = pixelMatchesColor( game_position[0]-399, game_position[1]-66, (38,44,47), tolerance=5 ) #Menu_Button
        x2 = pixelMatchesColor( game_position[0]-399, game_position[1]-66, (78,83,97), tolerance=5 ) #Menu_Button_Light
        return (x1 or x2)
    elif button_name == 'rebuy_menu':
        x1 = pixelMatchesColor( game_position[0]+513, game_position[1]+14, (203,0,6) ) #Rebuy_Menu_Button
        return (x1)
    elif button_name == 'leave_next_hand_ok':
        x1 = pixelMatchesColor( game_position[0]+108, game_position[1]+342, (0,83,171) ) #Leave_Next_Hand_OK_Button
        x2 = pixelMatchesColor( game_position[0]+108, game_position[1]+342, (0,95,193) ) #Leave_Next_Hand_OK_Button_Light
        return (x1 or x2)
    elif button_name == 'buy_in':
        x1 = pixelMatchesColor( game_position[0]+71, game_position[1]+448, (26,123,0) ) #Buy_In_Button
        x2 = pixelMatchesColor( game_position[0]+71, game_position[1]+448, (32,149,0) ) #Buy_In_Button_Light
        return (x1 or x2)
    elif button_name == 'buy_in_plus':
        x1 = pixelMatchesColor( game_position[0]+264, game_position[1]+236, (58,68,83) ) #Buy_In_Plus_Button
        x2 = pixelMatchesColor( game_position[0]+264, game_position[1]+236, (77,88,105) ) #Buy_In_Plus_Button_Light
        return (x1 or x2)
    elif button_name == 'buy_in_minus':
        x1 = pixelMatchesColor( game_position[0]-46, game_position[1]+244, (54,62,76) ) #Buy_In_Minus_Button
        x2 = pixelMatchesColor( game_position[0]-46, game_position[1]+244, (70,80,96) ) #Buy_In_Minus_Button_Light
        return (x1 or x2)
    elif button_name == 're_buy':
        x1 = pixelMatchesColor( game_position[0]+91, game_position[1]+430, (26,124,0) ) #Re_Buy_Button
        x2 = pixelMatchesColor( game_position[0]+91, game_position[1]+430, (32,150,0) ) #Re_Buy_Button_Light
        return (x1 or x2)
    elif button_name == 're_buy_plus':
        x1 = pixelMatchesColor( game_position[0]+264, game_position[1]+254, (58,68,83) ) #Re_Buy_Plus_Button
        x2 = pixelMatchesColor( game_position[0]+264, game_position[1]+254, (77,88,105) ) #Re_Buy_Plus_Button_Light
        return (x1 or x2)
    elif button_name == 're_buy_minus':
        x1 = pixelMatchesColor( game_position[0]-46, game_position[1]+261, (54,62,76) ) #Re_Buy_Minus_Button
        x2 = pixelMatchesColor( game_position[0]-46, game_position[1]+261, (70,80,96) ) #Re_Buy_Minus_Button_Light
        return (x1 or x2)
    elif button_name == 'i_am_back':
        x1 = pixelMatchesColor( game_position[0]+137, game_position[1]+608, (1,80,165) ) #I_am_back_Button
        x2 = pixelMatchesColor( game_position[0]+137, game_position[1]+608, (1,91,188) ) #I_am_back_Button_Light
        return (x1 or x2)


