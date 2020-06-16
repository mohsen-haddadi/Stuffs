import time
import pyautogui 


def DEVEOLOPING_find_game_reference_point(game_region = 1):
    # In a large screen monitor, you can run several games at the same time.
    global GAME_POSITION
    # Just an example:
    GAME_REGIONS_COORDINATES = {1:(0,0,1000,700), 2:(1000,700,1700,1400)}

    print( 'searching for game region (%s) on screen...' %game_region )
    GAME_POSITION = pyautogui.locateOnScreen( 'reference image.png', 
                    region = GAME_REGIONS_COORDINATES[game_region] )
    if GAME_POSITION == None:
        raise Exception("can not find game region on screen")
    else:
        print('game reference point is set') 

def find_game_reference_point():
    global GAME_POSITION

    print('searching for game region on screen...')
    GAME_POSITION = pyautogui.locateOnScreen('reference image.png')
    if GAME_POSITION == None:
        raise Exception("can not find game region on screen")
    else:
        print('game reference point is set')

def test():
    find_game_reference_point()


if __name__ == '__main__':
    test()