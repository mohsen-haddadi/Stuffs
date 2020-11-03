import time, os

import pyautogui, win32api

#import resizewindow

def find_game_reference_point_for_cheet():

    print('searching for game region on screen...')
    image_path = os.path.abspath(os.path.dirname(__file__)) + '/cheet reference image.png'
    game_position = pyautogui.locateOnScreen(image_path)
    if game_position == None:
        raise Exception("can not find game region on screen")
    game_position = (int(game_position[0]),int(game_position[1]))
    print('game reference point is set to:(%s, %s)'%(game_position[0],game_position[1]))
    return game_position

#game_position = (500,500) # TEST
game_position = find_game_reference_point_for_cheet()
pyautogui.click(game_position)

print("Press 'Enter' to do pixel matching")
#https://www.quora.com/How-do-I-detect-mouse-events-left-click-with-Python
# Left button down = 0 or 1. Button up = -127 or -128 
#state_left = win32api.GetKeyState(0x01)
# enter key: 
state_left = win32api.GetKeyState(13) 

count = 0
while True: 
    #a = win32api.GetKeyState(0x01) 
    a = win32api.GetKeyState(13)
 
    if a != state_left:  # Button state changed 

        state_left = a 
        if a < 0:
            count += 1
            print('pixel grabing number %s:'%count)
            x, y = pyautogui.position()
            pixel_matrix = pyautogui.pixel(x, y)

            x_relative = x-game_position[0] 
            if x_relative >= 0:
                x_relative = '+'+str(x_relative)
            else:
                x_relative = str(x_relative)

            y_relative = y-game_position[1]
            if y_relative >= 0:
                y_relative = '+'+str(y_relative)
            else:
                y_relative = str(y_relative)

            print('pixelMatchesColor( game_position[0]%s, game_position[1]%s, %s, tolerance=10 )' 
                  %(x_relative, y_relative, pixel_matrix) )

    time.sleep(0.001)