import time, os
import pyautogui 

def DEVEOLOPING_find_game_reference_point(game_region = 1):
    # In a large screen monitor, you can run several games at the same time.
    global game_position
    # Just an example:
    GAME_REGIONS_COORDINATES = {1:(0,0,1000,700), 2:(1000,700,1700,1400)}

    print( 'searching for game region (%s) on screen...' %game_region )
    game_position = pyautogui.locateOnScreen( 'reference image.png', 
                    region = GAME_REGIONS_COORDINATES[game_region] )
    if game_position == None:
        raise Exception("can not find game region on screen")
    else:
        print('game reference point is set') 

def find_game_reference_point():
    #global game_position

    print('searching for game region on screen...')
    image_path = os.path.abspath(os.path.dirname(__file__)) + '/reference image.png'
    game_position = pyautogui.locateOnScreen(image_path)
    if game_position == None:
        print('can not find game region, using alternative reference image after 10 sec...')
        time.sleep(10)
        image_path = os.path.abspath(os.path.dirname(__file__)) + '/alternative reference image.png'
        alternative_game_position = pyautogui.locateOnScreen(image_path)
        if alternative_game_position == None:
            raise Exception("can not find game region on screen")
        else:
            game_position = ( alternative_game_position[0]+328 , alternative_game_position[1]-245 )

    game_position = (int(game_position[0]),int(game_position[1]))
    print('game reference point is set to:(%s, %s)'%(game_position[0],game_position[1]))
    return game_position
