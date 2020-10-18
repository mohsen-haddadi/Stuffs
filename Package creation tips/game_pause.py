import keyboard , time
""" source: https://stackoverflow.com/questions/24072790/detect-key-press-in-python """
   
def game_is_puased():

    if keyboard.is_pressed("end"): 
        print("game is paused")
        #config.bot_status = 'WAITING_FOR_FIRST_HAND'
        # DON'T use set_just_do_check_fold_to_true() here.
        # we use it at wait_for_my_first_hand() function, this function will 
        # checks if the hand is just started or not and won't waste 
        # just started hands by doing just check_fold.
        return True
    return False

print("hold 'End' button to pause the game")

while True: #main loop
    print("main loop")
    while True: #loops such as pixel matching for my turn or starting new hand
        if game_is_puased():
            input("press Enter to start again...") 
            #fix_game_disruption('game is unpaused')
            break 
        time.sleep(2) #program excecution(pixel matching)
        print("in sub loop")        
