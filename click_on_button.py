# 1. Create button_coordinates function at screen_monitoring.button_coordinates sub package
# 2. Create button_pixel(game_position, button_name) function at screen_monitoring.pixle_matching sub package 
#    and remove functions like call_button_pixel(game_position)

# at main file:
import screen_monitoring.button_coordinates.button_coordinates as button_coordinates

def click_on_button(button_name): #new function
    global game_position, Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    load_variables()
    if pm.button_pixel(game_position, button_name) : #new function
        pyautogui.click( button_coordinates(game_position, button_name) ) #new function
        shout( paint.light_cyan.bold("%s is clicked" %button_name) )
    else :
        time0 = time.time()
        fix_game_disruption("Click on %s button"%button_name )
        time1 = time.time() - time0
        if pm.player_cards_pixel(game_position,  My_Seat_Number ) and pm.button_pixel(game_position, button_name) and time1 <= 10 :
            pyautogui.click( button_coordinates(game_position, button_name) ) #new function
            shout(paint.light_cyan.bold("Call_Button is clicked"))
        if button_name in ('call', 'check', 'fold', 'bet', 'raise') :
            set_check_mode_to_true("Click on %s button()"%button_name)
        else:
            raise_exception_the_problem("Click on %s button()"%button_name)

"""
for functions like:
def click_on_available_seat(seat):
def number_of_clicks_on_plus_button( number):
def number_of_click_on_minus_button(number):
and so on...
create separated functions
"""