#💊 : means edited
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
    if seat == 1:
        return pixelMatchesColor( game_position[0]+369, game_position[1]+329, (18,111,213), tolerance=10 ) #Small_seat_1
    if seat == 2:
        return pixelMatchesColor( game_position[0]+111, game_position[1]+332, (21,124,218), tolerance=10 ) #Small_seat_2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-145, game_position[1]+329, (16,105,211), tolerance=10 ) #Small_seat_3
    if seat == 4:
        return pixelMatchesColor( game_position[0]-173, game_position[1]+212, (22,112,212), tolerance=10 ) #Small_seat_4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+400, game_position[1]+212, (22,112,212), tolerance=10 ) #Small_seat_5

#2020
def big_blind_pixel(game_position, seat):
    # check if a seat is on big blind position by returning True or False
    if seat == 1:
        return pixelMatchesColor( game_position[0]+367, game_position[1]+329, (180,180,180), tolerance=10 ) #Big_seat_1
    if seat == 2:
        return pixelMatchesColor( game_position[0]+111, game_position[1]+332, (200,200,200), tolerance=10 ) #Big_seat_2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-145, game_position[1]+329, (185,185,185), tolerance=10 ) #Big_seat_3
    if seat == 4:
        return pixelMatchesColor( game_position[0]-174, game_position[1]+212, (185,185,185), tolerance=10 ) #Big_seat_4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+400, game_position[1]+212, (185,185,185), tolerance=10 ) #Big_seat_5

#2020
def dealer_pixel(game_position, seat): #💊
    # check if a seat is on dealer position by returning True or False
    if seat == 1:
        return pixelMatchesColor( game_position[0]+39, game_position[1]+202, (170, 129, 54), tolerance=10 ) #Dealer_seat_1
    if seat == 2:
        return pixelMatchesColor( game_position[0]-46, game_position[1]+174, (170, 129, 54), tolerance=10 ) #Dealer_seat_2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-89, game_position[1]+93, (170, 129, 54), tolerance=10 ) #Dealer_seat_3
    if seat == 4:
        return pixelMatchesColor( game_position[0]+157, game_position[1]+34, (170, 129, 54), tolerance=10 ) #Dealer_seat_4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+294, game_position[1]+91, (170, 129, 54), tolerance=10 ) #Dealer_seat_5
    if seat == 6:
        return pixelMatchesColor( game_position[0]+286, game_position[1]+157, (170, 129, 54), tolerance=10 ) #Dealer_seat_6 

def player_chips_pixel(game_position, seat): #💊
    # Checks if there is any call/bet/raising chips in front of a seat or not, by returning True or False
    if seat==1:
        return pixelMatchesColor( game_position[0]+74, game_position[1]+186, (0 ,0 ,0), tolerance=30 ) #Bet_coin_seat_1
    if seat==2:
        return pixelMatchesColor( game_position[0]+68, game_position[1]+125, (0 ,0 ,0), tolerance=30 ) #Bet_coin_seat_2
    if seat==3:
        return pixelMatchesColor( game_position[0]-16, game_position[1]+449, (0 ,0 ,0), tolerance=30 ) #Bet_coin_seat_3
    if seat==4:
        return pixelMatchesColor( game_position[0]+288, game_position[1]+22, (0 ,0 ,0), tolerance=30 ) #Bet_coin_seat_4
    if seat==5:
        return pixelMatchesColor( game_position[0]+235, game_position[1]+165, (0 ,0 ,0), tolerance=30 ) #Bet_coin_seat_5

def player_cards_pixel(game_position, seat): #💊
    # It checks if a player has cards in his hands or not, by returning True of False
    if seat == 1:
        return pixelMatchesColor( game_position[0]+75, game_position[1]+197, (255, 255, 255), tolerance=10 ) #Cards_seat_1
    if seat == 2:
        return pixelMatchesColor( game_position[0]-139, game_position[1]+136, (255, 255, 255), tolerance=10 ) #Cards_seat_2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-139, game_position[1]-1, (255, 255, 255), tolerance=10 ) #Cards_seat_3
    if seat == 4:
        return pixelMatchesColor( game_position[0]+75, game_position[1]-57, (255, 255, 255), tolerance=10 )#Cards_seat_4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+322, game_position[1]-1, (255, 255, 255), tolerance=10 ) #Cards_seat_5
    if seat == 6:
        return pixelMatchesColor( game_position[0]+322, game_position[1]+135, (255, 255, 255), tolerance=10 ) #Cards_seat_6

def other_player_seated_pixel(game_position, seat): #💊
    # It checks at ordinary situations if there is a player on the seat or not
    if seat == 1:
        return pixelMatchesColor( game_position[0]+153, game_position[1]+247, (245, 245, 245), tolerance=20 ) #Others_In_seat_1
    if seat == 2:
        return pixelMatchesColor( game_position[0]-60, game_position[1]+182, (245, 245, 245), tolerance=20 ) #Others_In_seat_2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-60, game_position[1]+50, (245, 245, 245), tolerance=20 ) #Others_In_seat_3
    if seat == 4:
        return pixelMatchesColor( game_position[0]+152, game_position[1]-4, (245, 245, 245), tolerance=20 )#Others_In_seat_4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+400, game_position[1]+49, (245, 245, 245), tolerance=20 ) #Others_In_seat_5
    if seat == 6:
        return pixelMatchesColor( game_position[0]+400, game_position[1]+183, (245, 245, 245), tolerance=20 ) #Others_In_seat_6

def i_am_seated_pixel(game_position, seat):# remove it
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

def active_player_pixel(game_position, seat): #💊
    # It checks whose player turn is, 
    # using the lighting pixel on a seat, by returning True or False 
    if seat==1:
        return pixelMatchesColor( game_position[0]+64, game_position[1]+255, (166, 31, 103), tolerance=10 ) #Light_Turn_seat_1
    if seat==2:
        return pixelMatchesColor( game_position[0]-151, game_position[1]+194, (166, 31, 103), tolerance=10 ) #Light_Turn_seat_2
    if seat==3:
        return pixelMatchesColor( game_position[0]-151, game_position[1]+58, (166, 31, 103), tolerance=10 ) #Light_Turn_seat_3
    if seat==4:
        return pixelMatchesColor( game_position[0]+64, game_position[1]+2, (166, 31, 103), tolerance=10 ) #Light_Turn_seat_4
    if seat==5:
        return pixelMatchesColor( game_position[0]+312, game_position[1]+58, (166, 31, 103), tolerance=10 ) #Light_Turn_seat_5
    if seat==6:
        return pixelMatchesColor( game_position[0]+310, game_position[1]+194, (166, 31, 103), tolerance=10 ) #Light_Turn_seat_6
#2020
def my_seat_won_pixel(game_position, seat):
    # looking for a sign of winning on my seat to check if I have won the game by returning True or False    
    if seat == 1:
        return pixelMatchesColor( game_position[0]+442, game_position[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-1
    if seat == 2:
        return pixelMatchesColor( game_position[0]+187, game_position[1]+422, (248,123,10), tolerance=5 ) #Win-Finish-Me-seat-2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-68, game_position[1]+415, (248,125,9), tolerance=5 ) #Win-Finish-Me-seat-3
    if seat == 4:
        return pixelMatchesColor( game_position[0]-98, game_position[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+472, game_position[1]+95, (250,130,6), tolerance=5 ) #Win-Finish-Me-seat-5

#2020
def other_seat_won_pixel(game_position, seat):
    # looking for a sign on other's seat to check if they have won the game by returning True or False
    if seat == 1:
        return pixelMatchesColor( game_position[0]+419, game_position[1]+412, (249,126,8), tolerance=5 ) #Win-Finish-Others-seat-1
    if seat == 2:
        return pixelMatchesColor( game_position[0]+164, game_position[1]+411, (249,127,8), tolerance=5 ) #Win-Finish-Others-seat-2
    if seat == 3:
        return pixelMatchesColor( game_position[0]-91, game_position[1]+419, (248,123,9), tolerance=5 ) #Win-Finish-Others-seat-3
    if seat == 4:
        return pixelMatchesColor( game_position[0]-121, game_position[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-4
    if seat == 5:
        return pixelMatchesColor( game_position[0]+449, game_position[1]+112, (248,124,9), tolerance=5 ) #Win-Finish-Others-seat-5

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
    """
    If the color of the sign behind chips is 
    red it returns True (bet(not bet on preflop)/raise), 
    if the color is white it returns False (call)
    """
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

def available_seat_pixel(game_position, seat): #💊
    # It checks if the seat is free to be seated or not, by returning True or False
    if seat == 1 :
        return pixelMatchesColor( game_position[0]+107, game_position[1]+238, (26, 112, 81), tolerance=10 )
    if seat == 2 :
        return pixelMatchesColor( game_position[0]-98, game_position[1]+176, (26, 112, 81), tolerance=10 )
    if seat == 3 :
        return pixelMatchesColor( game_position[0]-98, game_position[1]+34, (26, 112, 81), tolerance=10 )
    if seat == 4 :
        return pixelMatchesColor( game_position[0]+108, game_position[1]-29, (26, 112, 81), tolerance=10 )
    if seat == 5 :
        return pixelMatchesColor( game_position[0]+314, game_position[1]+34, (26, 112, 81), tolerance=10 )
    if seat == 6 :
        return pixelMatchesColor( game_position[0]+316, game_position[1]+178, (26, 112, 81), tolerance=10 )


def button_pixel(game_position, button_name):
    #It checks if button is existed and it's on its position or not.
    if button_name == 'fold': #💊
        x1 = pixelMatchesColor( game_position[0]+187, game_position[1]+468, (222, 224, 229), tolerance=25 )
        x2 = pixelMatchesColor( game_position[0]+156, game_position[1]+480, (255, 255, 255), tolerance=2 )
        return (x1 or x2)
    elif button_name == 'check': #💊
        return pixelMatchesColor( game_position[0]+303, game_position[1]+471, (41, 41, 41), tolerance=50 )      
    elif button_name == 'call': #💊
        return pixelMatchesColor( game_position[0]+297, game_position[1]+466, (0, 0, 0), tolerance=30 )  
    elif button_name == 'bet': #💊
        return pixelMatchesColor( game_position[0]+416, game_position[1]+466, (0, 0, 0), tolerance=5 )  
    elif button_name == 'raise': #💊
        return pixelMatchesColor( game_position[0]+430, game_position[1]+466, (0, 0, 0), tolerance=5 )  
    elif  button_name == 'half_pot': #💊 
        return pixelMatchesColor( game_position[0]+332, game_position[1]+375, (255, 255, 255), tolerance=10 )
    elif  button_name == 'pot': #💊 
        return pixelMatchesColor( game_position[0]+379, game_position[1]+378, (255, 255, 255), tolerance=10 )
    elif button_name == 'all_in': #💊
        return pixelMatchesColor( game_position[0]+431, game_position[1]+375, (255, 255, 255), tolerance=10 )

    elif button_name == 'exit': #💊
        x1 = pixelMatchesColor( game_position[0]+173, game_position[1]-263, (65, 65, 65), tolerance=10 )
        x2 = pixelMatchesColor( game_position[0]+173, game_position[1]-263, (0, 0, 0), tolerance=10 )
        return (x1 or x2)
    elif button_name == 'menu': #💊 
        return pixelMatchesColor( game_position[0]-136, game_position[1]-257, (255, 255, 255), tolerance=10 )
    elif button_name == 'buy_in': #💊 
        x1 = pixelMatchesColor( game_position[0]-40, game_position[1]+317, (26, 112, 81), tolerance=10 ) #Buy_In_Button
        x2 = pixelMatchesColor( game_position[0]-40, game_position[1]+317, (34, 145, 105), tolerance=10 ) #Buy_In_Button_Light
        return (x1 or x2)
    elif button_name == 'max_buy_in': #💊 
        return pixelMatchesColor( game_position[0]+214, game_position[1]+141, (255, 255, 255), tolerance=2 ) #max_buy_in_button
    elif button_name == 'min_buy_in': #💊 
        return pixelMatchesColor( game_position[0]+124, game_position[1]+141, (255, 255, 255), tolerance=2 ) #min_buy_in_button
    elif button_name == 're_buy': #💊
        return pixelMatchesColor( game_position[0]+358, game_position[1]-208, (26, 112, 81), tolerance=10 )
    elif button_name == 'i_am_back': #💊 
        x1 = pixelMatchesColor( game_position[0]+168, game_position[1]+473, (190, 195, 204), tolerance=40 )
        x2 = pixelMatchesColor( game_position[0]+156, game_position[1]+480, (255, 255, 255), tolerance=2 )
        return (x1 or x2)


