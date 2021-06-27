
def click_coordinates(game_position, name):
    if name == 'fold':
        coordinate = ( game_position[0]+51, game_position[1]+581 )
    elif name == 'check':
        coordinate = ( game_position[0]+246, game_position[1]+578 )
    elif name == 'call':
        coordinate = ( game_position[0]+261, game_position[1]+575 )
    elif name == 'bet':
        coordinate = ( game_position[0]+461, game_position[1]+576 )
    elif name == 'raise':
        coordinate = ( game_position[0]+461, game_position[1]+576 )
    elif name == 'plus':
        coordinate = ( game_position[0]+246, game_position[1]+648 )
    elif name == 'minus':
        coordinate = ( game_position[0]-9, game_position[1]+648 )
    elif name == 'half_pot':
        pass # add coordiantes later
    elif name == 'pot':
        pass # add coordiantes later
    elif name == 'all_in':
        coordinate = ( game_position[0]+531, game_position[1]+648 )


    elif name == 'available_seat_1':
        coordinate = ( game_position[0]+362, game_position[1]+408 )
    elif name == 'available_seat_2':
        coordinate = ( game_position[0]+107, game_position[1]+411 )
    elif name == 'available_seat_3':
        coordinate = ( game_position[0]-148, game_position[1]+408 )
    elif name == 'available_seat_4':
        coordinate = ( game_position[0]-178, game_position[1]+103 )
    elif name == 'available_seat_5':
        coordinate = ( game_position[0]+392, game_position[1]+103 )

    elif name == 'exit':
        coordinate = ( game_position[0]+378, game_position[1]+21 )
    elif name == 'menu':
        coordinate = ( game_position[0]-399, game_position[1]-66 )
    elif name == 'buy_in':
        coordinate = ( game_position[0]+71, game_position[1]+448 )
    elif name == 'max_buy_in':
        coordinate = (game_position[0]+264, game_position[1]+236)
    elif name == 'min_buy_in':
        coordinate = (game_position[0]-46, game_position[1]+244)
    elif name == 're_buy':
        coordinate = ( game_position[0]+91, game_position[1]+430 )
    elif name == 'i_am_back':
        coordinate = ( game_position[0]+137, game_position[1]+608 )

    elif name == 'exit_probable_advertisement':
        coordinate = (0, 720)
    elif name == 'close_update_window':
        coordinate = (1570, 10) 
        
    return coordinate


