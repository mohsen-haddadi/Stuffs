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
    reference_images = ['reference image', 'reference image 2', 'reference image 3', 'reference image 4', 'reference image 5']
    for reference_image in reference_images:
        image_path = os.path.abspath(os.path.dirname(__file__)) + '/reference image.png'

        game_position = pyautogui.locateOnScreen(image_path)
        if game_position == None:
            print('can not find game region, using next reference image after 10 sec...')
            time.sleep(10)
            continue
        else:
            game_position = (int(game_position[0]),int(game_position[1]))
            print('game reference point is set to:(%s, %s)'%(game_position[0],game_position[1]))
            return game_position

    raise Exception("can not find game region on screen")

